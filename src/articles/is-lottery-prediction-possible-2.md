Title: Expected Value of Lottery Ticket
Date: 2020-02-27
Category: data-science
Tags: statistics, probability
Authors: Haridas N



In my previous post, I have explained how the lottery number system works, and
forecasting a winning number isn't possible with confidence greater than the
random chance. This randomness of the data doesn't help us do any kinda
analytic. The only thing that can be done is to verify the lottery prediction
doesn't have any skewness towards a particular set of numbers.

Considering randomness involved in the lottery system, still few people found
a way to win the lottery with a higher confidence level or they are sure that they
can make a profit out of the lottery. I showed a few such instances in my previous
blog entry. In this blog let's dive into one such case more deeply and see how
and what helped them exploit the lottery system.

In short, they exploited the issues in Game Settings and make use of the Law of
Large Numbers to maximize their profit.


### The game setting


I'm taking a game named WINFALL played in the 2004 period in Michigan. Michigan
State scrapped the previous game with this one to lure people to buy more
lottery tickets. WINFALL offered better prize money for lower matching numbers
and an option of distributing all prize money if the jackpot hits 5Million or
above and nobody won the jackpot for the subsequent draw.

The game setting is:-

1. Players can select 6 numbers randomly from 1 to 49.
2. One lottery means this selected 6 numbers and costs $1
3. The lottery draw happens weekly twice, Wednesday and Saturday.
4. The Michigan lottery randomly picks 6 numbers as jackpot numbers on a particular
    drawing day.
5. Anybody who has these exact 6 numbers gets the full jackpot money.
6. Those who have fewer matches like, 3 matching numbers get 5 dollars, 4 matches
    get 100 dollars and 5 matches get 2500 dollars.
7. When the jackpot crosses 5Million, and nobody gets the jackpot then the full jackpot is
distributed to all the lower matching lotteries. This means those lower matching numbers get 10x more money. 3 number matches get 50 dollars, 4 number matches get 1000 dollars and 5 number matches get 25000 dollars.


The fact was most of the time nobody gets Jackpot, those cases lower matching
numbers get corresponding prize money. Obviously when the jackpot crosses
5Million there will be high demand for tickets because each 3 or higher match
gets 10x more prizes unless nobody gets the jackpot on that draw.

At this stage, it looks like a standard lottery game played in those times. What
you think about the weakness of this game and how people exploited it to win
guaranteed profit out of this lottery game. The usual idea was the "lottery is
a tax on poor people" and any person who knows the chance of winning won't go
near the lottery games, including me :).

But what was the reason math geeks Selbee's and other MIT students see an
opportunity here ?. They found a way to increase their chance of winning. See
below to know how they cracked it.


### Your winning chances

Let's see first what are the visible chances here to win a jackpot or other
prizes. The game we are discussing is 6/49, which means pick 6 numbers from 1-49
numbers. We need to know what is the chance of getting a jackpot or what's the
chance of getting 3, 4, or 5 matching numbers when a lottery draw happens.


#### Urn Model

To easily model this, think of we have 49 balls which are labeled 1-49 in an Urn.
Each lottery purchase means picking 6 balls from this Urn with replacement. Also,
think of the six numbers which are going to be picked for the jackpot are colored in
BLUE and all other balls are RED in color.

So when you buy a lottery ticket, what are the chances of getting blue balls
? Getting 3 or more blue balls means a corresponding prize waiting for you.

$$
\begin{array}{l}
Odds\ of\ getting\ no\ blue\ ball\ at\ all\ \ \ \ \ \ \ \ =\ \frac{^{6} C_{0}{}{}{} \times ^{43} C_{6}}{^{49} C_{6}} \ =\frac{6096454}{13983816} \ =\ 0.435\\
\\
Odds\ of\ getting\ 1\ blue\ ball\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ =\frac{^{6} C_{1}{}{}{} \times ^{43} C_{5}}{^{49} C_{6}} =\ \frac{5775588}{13983816} \ =\ 0.41\\
\\
Odds\ of\ getting\ 2\ blue\ ball\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ =\frac{^{6} C_{2}{}{}{} \times ^{43} C_{4}}{^{49} C_{6}} =\ \frac{1851150}{13983816} \ =0.13\\
\\
Odds\ of\ getting\ 3\ blue\ ball\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ =\frac{^{6} C_{3}{}{}{} \times ^{43} C_{3}}{^{49} C_{6}} \ =\ 0.017\ \\
\\
Odds\ of\ getting\ 4\ blue\ ball\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ =\frac{^{6} C_{4}{}{}{} \times ^{43} C_{2}}{^{49} C_{6}} \ =0.00096\\
\\
Odds\ of\ getting\ 5\ blue\ ball\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ =\frac{^{6} C_{5}{}{}{} \times ^{43} C_{1}}{^{49} C_{6}} \ =\ 1.844\ *\ 10^{-5}\\
\\
Odds\ of\ getting\ 6\ blue\ ball\ or\ Jackpot\ \ \ =\frac{^{6} C_{6}{}{}{} \times ^{43} C_{0}}{^{49} C_{6}} \ =\ 7.15\ *\ 10^{-8} \ \
\end{array}
$$

With the above changes if we buy a ticket on a normal drawing period, how much
return can you expect?

Matches and winning prize,


|Number of Match|Prize money($)|
|-------------------|------------|
|3 | 5|
|4 | 100|
|5 | 2500|
|6 | 2000000|

Based on the above table and the chances of winning, calculate the expected
prize money for a ticket.

\begin{array}{l}
Expected\ Return\ is\ =\ (\\
\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ 0.43\ *\ 0\ +\ 0.41\ *\ 0\ +\ 0.13\ *\ 0\ +\
0.017\ *\ 5\ +\\
\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ 0.00096\ *\ 100\ +\ 0.000018\ *\ 2500\ +\\
\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ 0.000000071\ *\ 2000000\\
) \ \ \sim =\mathbf{\ 0.4}
\end{array}


That means you get close to 40 cents for a dollar, which means if you play enough
number of times with this prize money you lose 60 cents per dollar. Otherwise
60% lose.

It's a well-known fact that lottery games are kinda a "tax on the poor",
always state makes money out of it for sure. In the above case, The State makes
approximately 60 cents for every ticket they sell.


## The loophole!

As we saw in the Game Setting section when the jackpot size reaches 5Million,
the next draw will ensure the entire money will be rolled down to all other
lower matching lotteries unless there is a jackpot winner.

The new prize money range, when the Jackpot crosses 5 Million and nobody wins the
jackpot on the following draw.


|Number of Match|Prize money($)|
|-------------------|------------|
|3 | 50|
|4 | 1000|
|5 | 25000|
|6 | 5000000|


With this scenario how much do you make when you buy a ticket? Let's
recalculate the new expected value of a ticket again.

\begin{array}{l}
New\ Expected\ Return\ is\ =\ (\\
\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ 0.43\ *\ 0\ +\ 0.41\ *\ 0\ +\ 0.13\ *\ 0\ +\
0.017\ *\ 50\ +\\
\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ 0.00096\ *\ 1000\ +\ 0.000018\ *\ 25000\ +\\
\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ 0.000000071\ *\ 5000000\\
) \ \ \sim =\ \mathbf{2.615}
\end{array}


Now for every dollar, you make close to $2.6, ie; You can expect close to 260%
profit. That means if you buy tickets when the jackpot reaches 5Million you get
a very good return from it.

WAIT, this case, if you buy ONLY one ticket will it  ensure a return of 2.6
dollar? NO !. Why so, that’s where the real meaning of Expected Value comes in.
To get close to the Expected Value, you have to sample enough times otherwise
buy enough tickets. So the overall return of all your tickets comes close to the
expected value of 2.6 dollars per ticket.

So what these people have done is they purchased a large number of tickets with
the help of their friends and partners. Even a few formed companies (Or lottery
syndicate) that give shares if some pool in their cash. That's how players like
Selbee's pooled enough money to purchase a lot of lotteries so that the overall
return will be close to the expected value mentioned above. The summary is to play
in bulk and get far better ROI.

There are more different strategies used to maximize the return or ensure how
fast we can converge to the expected value. I have attached a few references,
please read to get more background about it.


## Let's Implement it

```python
# prize money when we have n blue balls ?
prize_money = {0: 0, 1: 0, 2: 0, 3: 5, 4: 100, 5: 2500, 6: 2000000 }

# When jackpot hits 5Millon or above.
#prize_money = {0: 0, 1: 0, 2: 0, 3: 50, 4: 1000, 5: 25000, 6: 5000000 }

# Probability of getting n blue ball ?
expected_win_prize = 0

matches = []
prizes = []
for i in range(0, 7):
    w_prob = (comb(43, 6-i) * comb(6, i)) / comb(49, 6)
    #total+= w_prob
    print(f"Probability of getting {i} blue ball = {w_prob}")
    expected_win_prize += w_prob * prize_money[i]
    matches.append((i, w_prob))
    prizes.append((prize_money[i], w_prob))

print(f"Expected winning prize of a single lottery is : {expected_win_prize}" )

```

On Normal Drawing day the chances are listed below,

```text
# prize money when we have n blue balls ?
prize_money = {0: 0, 1: 0, 2: 0, 3: 5, 4: 100, 5: 2500, 6: 2000000 }

Probability of getting 0 blue ball = 0.4359649755116915
Probability of getting 1 blue ball = 0.4130194504847604
Probability of getting 2 blue ball = 0.13237802900152576
Probability of getting 3 blue ball = 0.017650403866870102
Probability of getting 4 blue ball = 0.000968619724401408
Probability of getting 5 blue ball = 1.8449899512407772e-05
Probability of getting 6 blue ball = 7.151123842018516e-08

The expected winning prize of a single lottery is: 0.37426121739588103
```

On the 5Millon Jackpot day, the chance of winning for a given ticket.

```text
#prize_money = {0: 0, 1: 0, 2: 0, 3: 50, 4: 1000, 5: 25000, 6: 5000000 }

Probability of getting 0 blue ball = 0.4359649755116915
Probability of getting 1 blue ball = 0.4130194504847604
Probability of getting 2 blue ball = 0.13237802900152576
Probability of getting 3 blue ball = 0.017650403866870102
Probability of getting 4 blue ball = 0.000968619724401408
Probability of getting 5 blue ball = 1.8449899512407772e-05
Probability of getting 6 blue ball = 7.151123842018516e-08

The expected winning price of a single lottery is: 2.669943597656033
```

Check out how the expected value changed. This was the key insight those people
saw in the game and exploited. **It's not that straight forward, higher expected
value doesn't guarantee a profit of $2.45 for every $1 lottery ticket, that
intuition comes only for those who have a statistics background.**

Expected value really means, by the [Law of Large Number](
https://en.wikipedia.org/wiki/Law_of_large_numbers) if we sample a random variable
enough number of times the values of the random variable will converge to
its expected value or sample mean. Here how do we know how many samples to take
from this random variable? , That is only possible if we know the full distribution
properties of this random variable. In most cases that's not possible due to
infinite possibilities, we have to stop the sampling somewhere with an
acceptable error.

Instead of addressing it full proof, going with a large number of tickets or
samples from the random variable is enough to make a profit out of this game,
that's what these players did. They did some tweaking to maximize their returns
from their finite resources or purchasing power.

Here the random variable is a categorical variable with 7 values ( How many
lottery numbers matched against the jackpot number ).


## How Michigan lottery fixed this problem

The problem was with strictly following the rules of the game, they didn't take
it seriously when the bulk purchase of lottery happens across multiple stores. This game has an inherent nature like the demand can drive the volume of sale, which
is exploited here to make the chances better for players like Selbee's and
others.

The main things to control are,

1. Restricting bulk selling.
2. Closely monitoring sudden spike in selling volumes.

After the news came out they stopped this game and added more restrictions on
the bulk purchases.

But some other States in the USA had similar lottery games and people like
Selbee's exploited that chance also, But all of it eventually closed down after
sighting these issues.

In either case, the State doesn’t lose any money. Usually, the State uses the
profit from lottery games to do more social development.


## Kerala Lottery

Kerala is one of the States in India, where the Government has been running the
lottery since 1967. Till very recently a lot of private lotteries were present
in the market. Currently, the Government is fully controlling the system, no
private parties can run a lottery.

From a quick look, above mentioned like mass lottery purchase isn't possible
with Kerala Lottery, as here the lotteries are in printed form, and the state only
prints a fixed number of tickets based on the previous selling trends. Also, there
are special serial numbers for each District in Kerala. The only possible issues are
duplicate tickets and other similar fraudulent activities, which are easily
identifiable.

Currently, I'm picking up the probabilistic programming using pyro and edward,
soon I will model this problem in probabilistic programming to validate the same
by simulating the lottery game Coming soon.


NOTE: The entry was taken from its original [source](https://labs.imaginea.com/expected-value-of-lottery-ticket/) and cross-posted here.

#References

0. [http://www.casinocitytimes.com/news/article/michigan-lottery-launches-new-winfall-game-130262](http://www.casinocitytimes.com/news/article/michigan-lottery-launches-new-winfall-game-130262)
1. [https://www.mass.gov/files/documents/2016/08/vv/lottery-cash-winfall-letter-july-2012.pdf](
https://www.mass.gov/files/documents/2016/08/vv/lottery-cash-winfall-letter-july-2012.pdf)
2. [http://www.jofamericanscience.org/journals/am-sci/0201/06-lihao-0106.pdf](
http://www.jofamericanscience.org/journals/am-sci/0201/06-lihao-0106.pdf)
2. [https://en.wikipedia.org/wiki/Lottery_mathematics](
https://en.wikipedia.org/wiki/Lottery_mathematics)
3. [https://www.youtube.com/watch?v=U7f8j3mVMbc](
https://www.youtube.com/watch?v=U7f8j3mVMbc)
4. [https://highline.huffingtonpost.com/articles/en/lotto-winners/](
https://highline.huffingtonpost.com/articles/en/lotto-winners/)
5. [http://www.keralalotery.in/p/kerala-lottery.html](
    http://www.keralalotery.in/p/kerala-lottery.html)
6. [Book - How Not to be
   Wrong](https://www.amazon.in/How-Not-Be-Wrong-Mathematical/dp/0143127535)
