Title: Can I predict the winning lottery numbers 2
Date: 2020-02-13
Category: data-science
Tags: statistics,ml
Authors: Haridas N


NOTE: test the writing using google document.

In my previous post I have explained how the lottery number system works and
forecasting a winning number isn't possible with confidence grater than the
random chance. This randomness of the data doesn't help us do any kinda
analytic. Only thing that can be done is to verify the lottery prediction doesn't 
have any skewness towards particular set of numbers.

Considering randomness involved in the lottery system, still few people found
a way to win the lottery with higher confidence level or they are sure that they
can make profit out of the lottery. I showed few such instances in previous blog
entry. In this blog let's dive into one such case more deeply and see how and
what helped them exploit the lottery system.

In short they exploited the issues in game setting and took advantage of law of
large number to maximize their profit.


### The game setting

I'm taking a game named WINFALL played in 2004 period in Michigan. Michigan
lottery scraped the previous game with this one to lure the customers. 
WINFALL offered better prize money for lower matching numbers and an 
option of distributing all prize money if the jackpot hits 5Million or above and
nobody won the jackpot for the subsequent draw.

The game setting is:- 

1. Player can select 6 numbers randomly from 1 to 49.
2. One lottery means this selected 6 numbers and costs $1
3. The lottery draw happen weekly twice, Wednesday and Saturday.
4. Michigan lottery randomly pick 6 numbers as jackpot number on a particular
   drawing day.
5. Anybody has this exact 6 numbers, then the get the full jackpot money.
6. If nobody won the jackpot, then those who have fewer matches like, 
   3 matching number gets $5, 4 matches gets $100 and 5 matches gets $2500.
7. When the jackpot crosses 5Million, and nobody gets the jackpot then the full
   jackpot is distributed to all the lower matching lotteries. This means those
   lower matching numbers get 10x more money. 3 number match gets $50,
   4 number match gets $1000 and 5 number match gets $25000.

The fact was most of the time nobody gets Jackpot, those cases lower matching
numbers gets corresponding prize money. Obviously when the jackpot crosses
5Million there will be high demand for tickets, because each 3 or higher match
gets 10x more prize unless no jackpot on that draw.

At this stage it looks like a standard lottery game played in those times. What
you think about the weakness of this game and how people exploited it to win
guaranteed profit out of this lottery game. The usual idea was the "lottery is
a tax on poor people" and any person who knows the chance of winning won't go
near the lottery games, including me :).

But what was the reason math geeks Selbee's and other MIT students see an
opportunity here ?. They found a way to increase their chance of winning. See
below to know how they cracked it.


### Your winning chances

Let's see first what are the visible chances here to win a jackpot or 
other prizes. The game we are discussing is 6/49, means pick 6 numbers from 1-49 
numbers. We need to know what is the chance of getting jackpot or what's
the chance of getting 3, 4 or 5 matching numbers when a lottery draw happens.

#### Urn Model 

To easily model this, think of we have 49 balls which are labeled 1-49 in a Urn.
Each lottery purchase means picking 6 balls from this Urn with replacement.
Also think of the six numbers which are going to be picked for jackpot are 
colored in BLUE and all other balls are RED in color.

So when you buy a lottery, what are the chances of getting blue balls ? Getting
3 or more blue ball means corresponding prize waiting for you.


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

With above chances if we buy a ticket on a normal drawing period, how much return
you can expect ?

Matches and winning prize, 

|Number of Match|Prize money($)|
|-------------------|------------|
|3 | 5|
|4 | 100|
|5 | 2500|
|6 | 2000000|

Based on above table and the chances of winning, calculate the expected prize money
for a ticket.


0.43 * 0 + 0.41 * 0 + 0.13 * 0 + 0.017 * 5 + 0.00096 * 100 + 0.000018 * 2500 + 0.000000071 * 2000000 ~= 0.4

That means you get close to 40 cents for a dollar, that means if you play enough
number of times with this prize money you loose 60 cents per dollar.

Till this it's a well known fact that lottery games are kinda a "tax on poor", always
state make money out of it for sure. In the above case state make approximately 60 cent
for every ticket they sell. 


## The loop hole !

When the game jackpot size reaches 5Million, then the game rules has slight changes,
and they ensuring the next draw will ensure the entire money will be rolled down
to all other lower matching lotteries unless there is jackpot winner.

The new prize money range, 

|Number of Match|Prize money($)|
|-------------------|------------|
|3 | 50|
|4 | 1000|
|5 | 25000|
|6 | 5000000|


With this scenario what you think how much you make when you buy a ticket ? Let's
recalculate above expected winning prize.

Expected return = (0.43 * 0 + 0.41 * 0 + 0.13 * 0 + 0.017 * 50 + 
	0.00096 * 1000 + 0.000018 * 25000 + 0.000000071 * 5000000) ~= 2.615

Now for every dollar you make close to $2.6. That means if you bugy tickets when the
jackpot reaches 5Million you get very good return from it.

Wait, this case, if you buy ONLY one ticket ensures return of 2.6 dollar ? NO. But
if you buy enough number of tickets OR assume if you play enough number of times
with this settings you total return will be come closer to the 2.16 dollar for
every dollar you spend.

So what these people have done is they purchase large number of tickets with the help of
their friends and partners. Even few formed company (Or lottery syndicate)
that give shares if some pool in their cash. That's how players like Selbee's
pooled enough money to purchase lot of lotteries so that the overall return will
be close to the expected value mentioned above. The summary is play in bulk and get
far better ROI.

There are more different strategies used to maximize the return or ensure how fast we
can converge to the expected value. I attached few references, please read to get
more background about it.


## Let's Implement it

NOTE: The precision will be better here, so the expectation value, and probabilities
values will be slightly higher.

```python
# prize money when we have n blue balls ? 
prize_money = {0: 0, 1: 0, 2: 0, 3: 5, 4: 100, 5: 2500, 6: 2000000 }

# When jackpot hits 5Millon or above.
#prize_money = {0: 0, 1: 0, 2: 0, 3: 50, 4: 1000, 5: 25000, 6: 2000000 }

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
Probability of getting 0 blue ball = 0.4359649755116915
Probability of getting 1 blue ball = 0.4130194504847604
Probability of getting 2 blue ball = 0.13237802900152576
Probability of getting 3 blue ball = 0.017650403866870102
Probability of getting 4 blue ball = 0.000968619724401408
Probability of getting 5 blue ball = 1.8449899512407772e-05
Probability of getting 6 blue ball = 7.151123842018516e-08

Expected winning prize of a single lottery is : 0.37426121739588103
```

On the 5Millon Jackpot day, the chance of winning for a given ticket.

```text
Probability of getting 0 blue ball = 0.4359649755116915
Probability of getting 1 blue ball = 0.4130194504847604
Probability of getting 2 blue ball = 0.13237802900152576
Probability of getting 3 blue ball = 0.017650403866870102
Probability of getting 4 blue ball = 0.000968619724401408
Probability of getting 5 blue ball = 1.8449899512407772e-05
Probability of getting 6 blue ball = 7.151123842018516e-08

Expected winning prize of a single lottery is : 2.455409882395478
```
Checkout how the expected value changed. This was the key insight those people 
seen on the game to exploit. **But it's not that simple, higher expected value
doesn't guarentee a profit of $2.45 for every $1 lottery ticket,
that intuition only for those who have stitstics background gets it**.

Expected value really means, by the Law of Large Number if we sample a random variable
enough number of times the values of random variable will converge to its expected value.
Here how many sample to take take from this random variable isn't fixed,
only thing is how much close we are able to converge to the expected value.
In another way they have to purchase enough number of ticket to ensure that their
overall profit is close to the expected value projection.

In the lottery scenario, you the Random Variable is "how many matching numbers do you have" 
,that indirectly tells the prize.

## How Michigan lottery fixed this problem

The problem was with strictly following the rules of the game, they didn't take it
seriously when bluk purchase of lottery happens across multiple stores. This game
has the inherent nature like the demand can drive the volume of sale, which is
exploited here to make the chances better for players like Selbee's and others.

Main things to control are, 

1. Restricting bulk selling.
2. Closely monitoring sudden spike in selling volumes.

After the news came out they stopped this game and added more restrictions on the
bulk purchases.

But some of other states in USA had similar lottery games and people like Selbee's 
exploited that chance.


## Kerala Lottery

Kerala is one of the state in India, where the Government running the lottery since 1967. Till
very recently lot of private lotteries were present in the market. Currently
Government is fully managing the system, no private parties can run a lottery.

From a quick look, above mentioned like mass lottery purchase isn't possible, as
here the lotteries are printed form, and state only prints fixed number of tickets
based on the previous selling trends. Also there are special serial numbers
for each districts in Kerala. Only possible issues are duplicate tickets and other
similar fraudulent activities, which are easily identifiable.


#References

0. http://www.casinocitytimes.com/news/article/michigan-lottery-launches-new-winfall-game-130262

1. https://www.mass.gov/files/documents/2016/08/vv/lottery-cash-winfall-letter-july-2012.pdf

2. http://www.jofamericanscience.org/journals/am-sci/0201/06-lihao-0106.pdf

2. https://en.wikipedia.org/wiki/Lottery\_mathematics

3. https://www.youtube.com/watch?v=U7f8j3mVMbc

4. https://highline.huffingtonpost.com/articles/en/lotto-winners/

5. http://www.keralalotery.in/p/kerala-lottery.html

6. A chapter in this book discuss about chance in lottery, must read for math nerds - "How Not to be Wrong"
