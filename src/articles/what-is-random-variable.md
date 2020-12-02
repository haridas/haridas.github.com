Title: What's Random Variable
Date: 2020-11-30  00:00
Category: data-science
Tags: statistics
Authors: Haridas N

This is one of the basic ideas that are commonly not understood properly, we learn
this from the high school level. Currently, most of the exploration is going
back to basics and wondering why they are defined like that. I can see that most of the
definitions have mathematical backgrounds and general theorems or axioms
present, that I'm trying to understand more now. Here I want to see what’s
the intuition behind the Random Variables.

> **From Wikipedia:**
>
> A Random variable / Random Quantity/ Stochastic Variable is
> described as a variable whose value depends on outcomes of a random phenomenon.

The definition of Random variable in Formal Mathematical term is defined using
Measure Theory, It seems measure theory based intuitions are easier to connect
rather than statements which define the random variable. Usually, we remember
things if we can associate them with some real-world entities or actions, which
is more intuitively we can recollect when we want to restate or understand other
similar concepts. I’m trying to wrap around this basic idea using measure
theory.

## Measure Theory

Very generically we can say, Measure can be explained using the Set Theory from
the Wikipedia article is very apt here.

> **Measure on a Set is a systematic way to
> assign a real number to each suitable subset of a set.**

**Measurable Events:** We can group those set of events that can be measured or quantified by using some units that we are familiar with.

![MeasureTheory](../images/RandomVariable-Measure_theory.png)

Here `Set A` can be anything ( eg; all people in the world, space in physics, number of atoms in the universe ), that we are trying to understand. Power Set of `Set A` includes all elements in `Set A` as well as all combination of items in `Set A` including `null` item.

Assigning a real number to all these subset of A is called **Measuring**. We can do any type of measuring activity that is possible on the `Set A` or the measuring that's important to us. For example, to understand the heights of all humans in the gloab, we do Measure their height, here the measuring is finding height of each and every person and map that to a real line with some unit.

### σ-algebra ( Sigma Algebra )

An `Algebra` on a Set is a collection of subsets closed under Union and Intersections.

An Omega-Algebra on a Set is a collection of subsets closed under countable unions and Intersections.

What's mean by **closed** is that, if we take any two items from the given set and we do the specified operation (union or intersection), the result also available in the same Set.

The `Countable` union means,

This very imporatant that, all the subsets are not measurable, as it's won't follow the contraints of σ-algebra, Hence σ-algebra is a special contaraint applied on a Set to define the Measure and Measure space.

![CountableAddictivity](../images/Countable_additivity_of_a_measure.svg.png)

<p> [Source: Wikipedia] </p>

Note: Here $\mu$ is a **Measure**.

### Different Types of Measures

Based on some constraints applied on how we can do the measuring or what to measure we can group the Measuring to different types or special types of measures that are common for particular domain,

1. **Borel Measure**: Allocate real number to the space.
2. **Lebesgue Measure**: Standard way to measure the n-dimentional eculidean space. This measure is more general one and used to formalise the probability space also. As in that case the measure assign values in the range of [0, 1].
3. **Counting Measure**: Counts the number of items in a subset of `Set A`
4. etc.

### Measure Space

Measure space is defined using a triplet - $(X, A, \mu)$, Here

1. $X$ is the Set
2. $A$ $\sigma$-algebra defined on the Set
3. $\mu$ is the measure

The Set that we are trying to measure can be called as the **Measure Space**, there are different types of measure space,

1. **Eculidian space** - Try to measure the Length, Area, Volume, hyper volume etc. Or more common 3-D space.
2. **Probability Space** - In this case the Measure of entire Set is 1. And `null` set gets value zero -- We can say this space is an abstract space, with some special properties attached to it. This is being done by proper normalisation or knowing about all subsets in the measure space.
3. etc.

## Random Variable

Now we all already covered what's Random variable multiple times above, lets restate it here,

> **A random variable is not a variable but a function that maps from space to the
> real number domain.**
> So we can see that Random Variable is a measure done on a specified Measure Space.

So it's clear that we can pick, any measurable function as a random variable. Few constraints applied there are

1. Wheather that measurable function is usable to us.
2. We can do the measure on the given Space.

Q: So what's **Random** in Random Variable ?

A: Only thing here random being important is, at measure time we shouldn't biase on any specific type of subsets for measuring. So the **process** of measuring has randomness, hence we call this as random variable. One thing is in formal definitions this isn't really meant like this. Random in Random Variable was stick to it because it was used like that before and we simply sticking to it.

Let's take one example experiment, where we consider all humans as our **Measure Space**

### Measure height of all humans

Suppose if we do this experiment,

![HeightMeasure](../images/RandomVariable-Height-Random–Variable.png)

Is it really possible to measure this ?

Ans: No,

## Probability of a Random Variable

The formal definition of a Probability of a random variable also derived from the Measure Theory,

- Probability is involves same mapping to real number without normalisation
- Or To real number without any units of measure involved, instead trying to understand how likeliy the given type of measure compared to all other known items in the sample space.

> **Random Variable**
>
> Hello This isn't the case
> working with the same case.

## Probability Distributions

Once we know the probability of a Random Variable, next concept comes around it is, probability distribution. This is nothing but set of common patterns that we observe when try to measure different Measure spaces. We grouped them and named it, as we are observing such patterns from different Measure Spaces. This patterns are evolved and helping us to do abstract representations.

There are two key principle around this,

1. Central Limit Theory
2. Law of Large Numbers

These two are the phenomenons that we see on how the data/space behaves.

That's all for this entry, will cover some other key principle areas in next blog.

Thanks for reading. If you see any mistakes or have suggestions, please comment or contact me via twitter `@haridas_n`

## References

1. https://nrich.maths.org/13852
2. https://en.wikipedia.org/wiki/Probability_space
3. https://en.wikipedia.org/wiki/Probability_theory
4. https://en.wikipedia.org/wiki/Random_variable
5. https://en.wikipedia.org/wiki/Lebesgue_integration
