Title: Can I predict the winning lottery numbers
Date: 2019-12-29
Category: data-science
Tags: statistics,ml
Authors: Haridas N

This was one of the questions asked by a colleague of mine who is new to the data
analytics and Machine learning space. I had to tell him that this isn’t possible
because data itself is not suitable to do any sort of valuable predictions.
It usually takes some time to get this intuition. Those who have statistics
background can quickly catch-up, others have to put up extra effort to solidify
these concepts.

So, back to the question, can we build a model to predict lottery numbers?
The short answer is NO, and the long answer is NO :). Now you have to ask why!

### Why this post?
This question may be a very trivial one for seasoned ML practitioners, but
sometimes experienced one also misses the key basic concepts when it comes to
how to deal with data and what data is good for a particular problem.
This is my attempt to answer the questions that I had!

### Looking into the winning chances
Let’s take one lottery series for this experiment, this lottery number has 2
alphabet and 6 numbers, eg; AG389435. In this case how many unique lottery
tickets can be printed?


$$
 \begin{array}{l}
 Total\ number\ of\ lotteries\ for\ number\ sequence\ of\ form\
 \mathbf{AB123456}\\
 \\
 =\ 26^{2} \ *\ 10\ ^{6} \ \\
 =\ 676\ Million\\
 \\
 =\ Chance\ of\ winning\ for\ a\ person\ =\ \frac{1}{676\ Million} \ =\
 \mathbf{1.47*10^{-9}}\\
 \\
 Here\ we\ are\ assuming\ equal\ chance\ for\ all\ to\ win,\ and\ the\ lottery\
 system\ will\\
 ensure\ this\ constraint.\\
 \\
 So\ winning\ probability/chance\ is\ \mathbf{0.000000147} \ \ or\ 1\ in\ 676\
 Million
 \end{array}
$$

To put this number into context, let's take another study done to identify the
cancer risk due to smoking [[link]] [2]. According to their study, they estimate 1 in 10
men and 1 in 8 women in India can expect to develop cancer of any form, in their
lifespan after the age of 35 years. This means getting cancer is a way higher chance
than winning a lottery.


### Why am I saying lottery data isn't usable for any prediction

Because the lottery prediction is done using some random number generator (RNG),
this means RNG ensures that every lottery purchased gets an equal probability of
winning, usually the odds of winning are above 1 in Million. And there won't be
any relation between historical predicted number and the future numbers, because
they are close to independent. So you can't find any relation from the
historical winning numbers.

If we are using some faulty RNG machine or RNG system with lesser entropy then
the results may be skewed, so we can see patterns in number prediction.
So how few individuals broke the lottery system legally, below listed are the
two instances people worked hard to increase their chances of winning, here also
they aren't predicting the actual winning numbers, instead of increasing the chance
of winning probability of each lottery.

1. [Michle Memorized live game patterns, video](https://www.youtube.com/watch?v=8rJw4BgPs4w)

    <p>
        <iframe width="200" height="100" src="https://www.youtube.com/embed/8rJw4BgPs4w"
        frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope;
        picture-in-picture" allowfullscreen></iframe>
    </p>

    This story may come as a Hollywood movie soon.



2. Or you have to run a lottery syndicate to increase the chance of winning by pooling the tickets from multiple contributors. Here is an interesting guy who did this thing across the world. It's purely playing against the odds by purchasing more tickets.

    <p>
       <iframe width="560" height="315"
       src="https://www.youtube.com/embed/eOX7acjkGv0" frameborder="0"
       allow="accelerometer; autoplay; encrypted-media; gyroscope;
       picture-in-picture" allowfullscreen></iframe>
   </p>



### Does an ML model won’t predict the winning numbers at all?

If you run enough times, your model may predict the right answers sometimes, so why
are you saying ML models can’t predict correctly at all? We call a model doing
good when it produces predictions better than a simple guess. If your model
prediction accuracy is close to any other simple guesswork, then why do you
need this ML model after all.

The predictions are really based on known patterns. The patterns are coming out
of data ( data may be image, sound, simple numbers anything).


### When can we do ML

We can do any sort of data analysis or prediction using statistical methods only
when the data has some repeating patterns or correlation or some inherent
orders.

eg; When you see a different type of cat, you can identify it as a cat, how’s that
working, when you look at it objectively there is some underlying order in
their pixels and behaviors, and our brain maps those patterns of light signals
to the cat. And you can apply this same analogy ( similar technique ) to our ML
models here, models learn to identify cat/dog by capturing these common
patterns present in the data or image or video. If the data doesn’t bring these
patterns, how can any system or our brain identify a particular object?


### Similarities with Language Models

The number of sequences in the lottery number can be treated as a finite sequence.
The random numbers from RNG usually pick random numbers from this finite
sequence. Let's connect this to the Language models in NLP. NLP language models
predict the next word from whatever it has seen till now. If we take all the
words in the English dictionary, it comes around 171,476 words. If we arrange these
words in a particular order it forms a valid sentence, ie; we can't put all
combinations of words to form a valid sentence. This means there is a fixed
order of word sequence, this is what the NLP models learn internally via word
co-occurrence and other methods.

Now come back and see how the sequence predicted by RNG for the lottery has some
pattern ?, it shouldn't. So we can't find any sort of significant statistical
correlation between two lottery numbers.


### How clickstreams are helping for the recommendation

This is another way of pulling out data that has some meaning or patterns
present in it. When you browse over any e-commerce site, for a given query your
mouse movement leaves out some meaning about those items. They are related items
!. So if you pull out the clickstream done by a user for a session we can find
the related items and using that data we can do recommendations for a given
query.

You can read more about this from this paper from [Airbnb](https://astro.temple.edu/~tua95067/kdd2018.pdf)

I will be posting one more article to show how those individuals increased their
chances of winning.


[2]: https://www.ncbi.nlm.nih.gov/pubmed/21545200
