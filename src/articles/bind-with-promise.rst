Bind With Promise
=================

:date: 21-12-2017
:category: blog
:tags: nodejs,promise,bind


`bind` function in js is an interesting function that does behave like a wrapper function,
which make the function bound with wrapper function. This wrapper function helps to
do call the target function with in custom contexts with arguments.
Bind act similar to the decorators in python, as in decorator also there is wrapper
function which intercept the target function. But here the `bind` is kinda black box
we  can't get custom behavior from it, nevertheless the standard nature of what
bind provide is what needed in the `javascript` async execution environment.

Javascript is known to be called as Lisp like functional behavior exposed via C like
syntax. The functions in js can run in any context, that context decides the `this`
argument, here the `bind` give the power to dynamically change the execution
context of a function.

I came across with bind more when working with the promise, where we chain the
operations using multiple functions. 


Let me show the use of bind with an example.

`request_handler.js`

.. code-block:: js

	'use strict';
	
	class Authenticator {
	    constructor(config) {
	        this.config = config;
	    }
	
	    authenticate(header) {
	        // Does some logic based on the authentication.
	        // throw Exception if auth fails.
	        return new Promise(function(resolve, reject) {
	            resolve(true);
	        });
	    }
	}
	
	class HandleRequest {
	    constructor() {
	    }
	
	    handle(req, header, result) {
			console.log('this object: ' + this + " result: " + result);
	        return new Promise(function(resolve, reject) {
	            resolve({'body': 'hello world', 'content-type': 'application/json'});
	        });
	    }
	}
	
	
	var auth = new Authenticator({'type': 'basic'});
	var handler = new HandleRequest();
	
	//console.log(auth, handler);
	
	var req = {'method': 'POST', 'body': ''}
	var headers = {'Authorization': 'Basic dweDasdfesdDDa=='}
	
	auth.authenticate(headers)
	    .then(handler.handle.bind(handler, req, headers))
	    .then(function(result) {
	        console.log("request successful..");
	        return 200;
	    })
	    .catch(function(error) {
	        // Some exception in the chain. Return 500 status.
	        console.log("request failed..");
	        return 500;
	    });

Just execute the code and see the result.

.. code-block:: bash

	$ node request_handler.js
	this object: [object Object] result: true
	request successful..

The example shows simple http request handling with authentication. We chained
the request process using promise for easiness. If you noticed here the request
handlers are all return standard promise objects, the final orchestration code
will chain it together with error handling.

.. code-block:: js

	.then(handler.handle.bind(handler, req, headers))

Bind function pass the arguments to target function in order they are bound to it.
 `.bind` func syntax,

.. code-block:: js

	fun.bind(thisArg[, arg1[, arg2[, ...]]])

As you know that `.then` method tasks a callback with single argument. When the
previous promise is resolved, the result will be passed that single callback argument.
With this in mind if you check the method `handler.handle`, this function takes
two arguments and also works with its on `this` context. Here is where the `bind`
help us to partially fill the required arguments before hand and then use that
partially function with `.then` clause.


If you check the function arguments, we already expecting the `result`
argument. And the `this` object inside the `handle` function now resolved to
the actual `HandleRequest` object that we created.

.. code-block:: js

	    handle(req, header, result) {
			console.log('this object: ' + typeof(this) + " result: " + result);
		...


We can bind `this` object as `null` if we want, so that the function work without
any external context with it.

.. code-block:: js

	.then(handler.handle.bind(null, req, headers))


If you want to see this behavior without promise chain, check bellow example for 
pure use of bind.

.. code-block:: javascript

    var wrappedHandler = handler.handle.bind(handler, req, headers);
	wrappedHandler(true).then(console.log);

This is actually happening inside the promise. Here the `wrappedHandler` function is called as Bound function.


Take away
---------

1. `bind` can be used to partially fill the arguments ( Term for this in functional programming is 'currying')
2. Can inject custom `this` context rather than the default global `this` or from current runtime context.
3. Really helpful with the `Promise` based programming and other cases via `currying`.


Reference 
---------

1. https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_objects/Function/bind
