Is callback really a bad thing ? It isn't.
==========================================

:date: 05-1-2017
:category: blog
:tags: node,callback,promise


TL;DR version

    Make use of the node.js team recommendation for callbacks,

    1. Fix the callback signature, like callback(err, obj),
    2. Callback should be the last argument in a function,
    3. Change the data structure or make use of promise, and similar methods to 
       reduce the nested nature of callbacks.
    4. Don't bring baggages from other languages, be like JS ninja when coding in
       JS ;)


Full version,

My early part of career I used to code in vanila-javascript, Jquery,
Jquery-plugins,  Sproutcore etc. Those time I wasn't faced with these callback
issues mainly because I wasn't involved with much complicated JS centric codes
and frameworks really helped out to abstract out the complications.
So it's mainly writing simple functions, closures and DOM tricks.

But lately after coding in node.js for few months, it's very clear that
callbacks are there most part of the codebase. To understand the callbacks and
why it exists is the key, after that it naturally comes for you when writing
codes.

Key concepts of Node.js / JS engines are

    1. Event loop,
    2. Call Stack ( Macro and Micro )
    3. Non-blocking IO (Network, memory, Disk, IPC)
    4. Transparent worker threads / web workers

If you dig more down you can see that the language is build on top of the core
OS kernal features like non-blocking IO and related libs (libuv).
And lately the big players are invested a lot of time to create more optimized
compilers, which helped the boom of node.js at backend side.

Due to this inherent nature of non-blocking IO and event loop, most of the code that you write
going to be executed nonsequential, so we need to attach a callback function
which will take care the operation when it finished and ready with
result or error.

We have full freedom to define the callback function for each requirements, but
its recommended to keep the common signature across project / language
/ community to avoid lot of confusions.

Here I"m making use of the redis library to showcase the callback chain.
Similarly any DB / IO related libraries follows this method in
nodejs standard library.

.. code-block:: java

    /*
    Brief doc about the what function does.

    @arg key: 
    @arg callback(err, result): The More information about the signature of the
                                callback is much appreciated one.
    */
    'use strict';
    var Redis = require("ioredis");
    var redis = new Redis();

    function initializeRedis(callback) {
        var pipeline = redis.pipeline();
        pipeline.set("weightKey", 80);
        pipeline.set("heightKey", 1.8);

        pipeline.exec(function(err, results) {
            if (err) {
                callback(err, null);
            } else {
                callback(null, true);
            }

        });

    };

    function calculateBmi(weightKey, heightKey, callback) {
        redis.get("weightKey", function(err, weight) {
            if (!err) {
                redis.get("heightKey", function(err, height) {
                    if(err) {
                        callback(err, null);
                    }else {
                        // Units: Weight in KG, and height in Meters.
                        let bmi = weight / (height * height)
                        callback(null, bmi);
                    }
                })
            }else {
                callback(err, null);
            }
        });
    }

    initializeRedis(function (err, done) {
        if(err) {
            console.log("Redis initalization failed");
            process.exit()
        } else {
            //Actual call to the method.
            calculateBmi("weightKey", "heightKey", function(err, bmi) {
                if (err) {
                    console.log("Error on calculation: " + err);
                } else {
                    console.log("Your BMI: " + bmi);
                }
                process.exit()
            });
        }
    });

Above code you can see that how the use of callbacks comes in, and how we set
the signature of the callback to propagate the error back to the caller. The
redis db call is IO involved, so it will be scheduled asynchronously, that's the
reason we are attaching the `callback` with its arguments. The things go out of
our control if we have more nested redis calls. That's where our code go crazy
and we call it as callback hell and all.

Sticking to the standard callback structure, still it's cluttered with nested
callbacks. But clarity of how the code execution happening is very clear, and
I feel keeping verbosity is fine to avoid readability issue and better
maintenance. Other normal coding standards like keeping the reusable components
separate as much as possible so that we won't repeat ourself in different part of our
codebase.

You can make use of the Database API options like `pipeline`, `multi key`
retrieval, or picking better DB data structure which reduces the number of IO
interaction ( Which means we are reducing the #callbacks )

Eg: here we can avoid two calls if we keep the information of a person in
a redis HASH set.

This will greatly reduce the nested structure.

.. code-block:: js

    redis.hmget("userHashKey", "heightKey", "weightKey",
        function(err, results) {
           if (err) {
               callback(err, null);
           } else {
               let height = results[0];
               let weight = results[1];
               // Do your work now..
           }
    }
    
Think of the case if we can't modify the data structure, and still want to
simplify the syntax, make use of Promise or similar methods.


Promises
--------

Promise a method to reduce the verbosity of the callback, mainly recommended by
the community, so it's good to leverage the promise features in our code to
make the code less verbose and less number of if/else blocks. But one thing is the
libraries that we are using, or the modules we are writing should expose
promisified objects or classes, so you can interact with libs as per the promise
coding pattern. Currently promise libraries like `bluebird` provide options to
promisify an object which doesn't support promise behavior.

Technically It's kinda method as the word litterly means, gives some promise
object which will be met in future. Here we don't need to pass callback when we
creating the object rather, we create the object first, and then we attach the
required handlers, so that when the object actually returns result / error there
will be some handler ( callback ) available to deal with it. In the case of
promise the way that handler attachment is done is shown bellow, nothing
complecated, just need to get familear with it.

Any object with `then` method can be called promise if that objects follows the
specification given in `Promise/A+`. Promise wraps the async operation and gives
the response object even though the response is not yet ready, it eventually be ready.
Promise objecs can also be called as **thenable** objects, and it can be
chainable.

.. code-block:: javascript

    promise2 = promise1.then(onFulfilled, onRejected);
    // Where onFulfilled and onRejected are callback with single argument
    // onFullfiled gets result.
    // onRejected gets reason for failure.


Rewriting the above example looks as follows:- 

.. code-block:: java

     /*
     * Create your own promise object, that behave like thenable object
     * and can be used other parts of the codebase
     */
    var getValuePromise = function() {
            return new Promise(function(onFulfilled, onRejected) {
                var redisPromise = redis.pipeline()
                    .get("heightKey")
                    .get("weightKey")
                    .exec();

                redisPromise.then(function(results) {
                    // Both height and weight are packed in `results` object.
                    if (results[0][0] || results[1][0]) {
                        // If the redis operation have some error, call the
                        // Promise reject.
                        onRejected(val);
                    } else {
                        // Successful promise.
                        let val = {
                            'height': results[0][1],
                            'weight': results[1][1]
                        }
                        onFulfilled(val);
                    }
                })
            });
    }

    var getYourBmi = function() {
        return getValuePromise().then(function(val) {
            //console.log("Bmi calculation: " + val.height)
            return val.weight / (val.height * val.height );
        });
    }


    getYourBmi().then(function(result) {
        console.log("Your Bmi: " + result );
        process.exit()
    }).catch(function(error) {
        console.log("Calculation failed with error: " + error);
        process.exit()
    }


NOTE: Here the promise examples are based on the bluebird promise
implementation. Any objects or user defined objects can be converted to the
promisified version, by making use of the `Promise` object.

I'm surprised to see the specification of the `Promise/A+`,  it is very small and
concise text document. It clearly says what a promise implementation should
follow. After programming in Node.js with standard node.js callbacks
I'm convinced that use of Promise really make the code better and clean.

Main benefits are:-

    1. Less nesting levels or less number of callbacks. ie; Don't need to pass
       callback to each and every methods to properly handle the results from
       it.
    2. We can design the data flow and transformation as a pipeline.
    3. Error propagation and handling similar to that of sync code base.
    4. Chain the promise with multiple transformation or filters etc.
    5. Thenable objects are won't throw, it nicely pack the error and can be
       intercepted via `.catch` method of the promise object.


What happens Promise when a promise object is ready with its result before 
a 'then' handler is attached to handle it ?

    This won't happen because Promise/A+ insists so :). As the specification
    guarantee that,this scenario shouldn't happen, the implementation has to 
    ensure this by making the actual code block execution after emptying the 
    current call stack.


Generators
----------

As you guess this is co-routine implementation in Node.js and included in the
ES6 specification. If you familiar with python you should know the generators.
The concept is same. But with node.js, there is one more things, ie; its inherent
asynchronous execution, so combining async with generator give much better way to
represent complex flows in easy syntax. See few examples bellow. My current
projects we didn't used it, looking forward to try out in future projects.

Main features of generators are:-

1. Lazy loading
2. Memory efficient due to the lazy loading behavior, best fit to iterate
   through chunks of big files or streams.
3. Plays well with Asynchronous codes, this is win-win situation for both.


Here is the simple example of how to define a generator and how to consume it.

.. code-block:: java

    //Generator functions are defined using "function*" syntax.
    function* getList() {
        yield 'a';
        yield 'b';
    }

    for (let x of getList()) {
        console.log(x)
    }
    // Prints
    a
    b


    // Another way to retrieve the generator values are making use of 'next'
    // method.
    var gen = getList();

    console.log(gen.next())
    console.log(gen.next())
    console.log(gen.next())

    // Prints 
    { value: 'a', done: false }
    { value: 'b', done: false }
    { value: undefined, done: true} // Indicates generator finished.


Lets implement our above example using generator and promise.  
we are using *'co' library* which is just wrapper around generator which
internally loop through the generator till it finishes, so that we are getting the
sequential behavior.

.. code-block:: java

    // Here is the generator magic.
    // The async calls will be executed synchronously. Ie; it will block till
    // the call to async call finishes.

    var bmi = co(function*() {

        // First async call

        var setRedis = yield redis.pipeline()
                                  .set("heightKey", 1.8)
                                  .set("weightKey", 80)
                                  .exec();

        // Blocks here till the redis write operation finishes.


        // Second async call
        var res = yield getYourBmi()
        console.log("Your Bmi: " + res);

    }).catch(function(err) {
        // Errors are wrapped out ensure no callback way of handling the errors
        // from bottom up fashion.
        console.error(err.stack);

    });


You can see how cleanly generators helps to handle the async codes in sequential way.
There are lot of other ways you can make use of this feature in your code,
please check out the co library's github page for more examples.


References
----------

1. http://2ality.com/2015/03/es6-generators.html
2. https://www.promisejs.org/
3. https://blog.risingstack.com/node-js-at-scale-understanding-node-js-event-loop/
4. https://promisesaplus.com/
5. https://github.com/tj/co
