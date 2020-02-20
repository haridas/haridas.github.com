Title: Can I predict the winning lottery numbers 2
Date: 2020-02-13
Category: data-science
Tags: statistics,ml
Authors: Haridas N


NOTE: test the writing using google document.

Areas to cover:- 

1. Introduction about the lottery system
2. Game settings
3. Match behind the loop hole
4. How the lottery system fixed these issues
5. How we an relate this issue with other lottery systems like the one in
   Kerala.

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

But what was the reason math geeks Selbies and other MIT students see an
opportunity here ?. They found a way to increase their chance of winning. See
below to know how they cracked it.


### What was the loop hole in the above listed rules ?

Selbis are retired
elder couple, they came across this lottery game once they were in a stationary
store. Selbi was able to see a loop hole in the game in that short time, or put
it other way he saw higher likelihood of making profit out of this game at
particular time period. He went back and done few more statistical analysis to
validate his theory. All was coming in his favour.


\begin{array}{l}
 In\ the\ above\ contraints,\ what\ are\ the\ odds\ of\ getting\ 3\ match\\
 \\
 Here\ use\ the\ Urn\ model\ to\ pick\ the\ right\ numbers\ from\ the\
 available\\
 49\ numbers.\\
 \\
 Odds\ of\ hitting\ no\ match\ at\ all\ =\ \frac{^{6} C_{0}{}{}{} \times ^{43}
 C_{6}}{^{49} C_{6}} \ =\frac{6096454}{13,983,816} \ =\ 0.435\\
 \\
 Odds\ of\ getting\ 1\ matching\ numbers=\frac{^{6} C_{1}{}{}{} \times ^{43}
 C_{5}}{^{49} C_{6}} =\ \frac{6,600,672}{13,983,816} \ =\ 0.472\\
 \\
 Odds\ of\ getting\ 2\ matching\ numbers=\frac{^{6} C_{2}{}{}{} \times ^{43}
 C_{4}}{^{49} C_{6}} =\ \frac{2,115,600}{13,983,816} \ =0.1512\\
 \\
 Odds\ of\ getting\ 3\ matching\ numbers=\frac{^{6} C_{3}{}{}{} \times ^{43}
 C_{3}}{^{49} C_{6}} =\ 0.017\ \ \eqsim \frac{1}{54}\\
 \\
 Odds\ of\ getting\ 4\ matching\ numbers\ =\frac{^{6} C_{4}{}{}{} \times ^{43}
 C_{4}}{^{49} C_{6}} \ =0.00096\\
 \\
 Odds\ of\ getting\ 5\ matching\ numbers\ =\frac{^{6} C_{5}{}{}{} \times ^{43}
 C_{5}}{^{49} C_{6}} \ =\ 1.844\ *\ 10^{-5}\\
 \\
 Odds\ of\ getting\ 6\ matching\ numbers\ =\frac{^{6} C_{6}{}{}{} \times ^{43}
 C_{0}}{^{49} C_{6}} \ =\ 7.15\ *\ 10^{-8}\\
 \\
 \\
 \\
 If\ I\ purchase\ 4000\ lottery\ of\ 6\ number,\ how\ much\ we\ can\ expect\
 from\ it\ ?\\
 \\
 2200\ *\ 0.017\ *\ \$50\ =1870\\
 \\
 2200\ *\ 0.00096\ *\ \$1000\ =\ 2112\\
 \\
 2200\ *\ 1.844\ *\ 10^{-5} \ *\ \$\ 25000\ =\ 1014.2\\
 \end{array}

NOTE: Expectation value - Value of a random variable, sample enough number of
times will converge to expectation value or Mean.

```python
# Price money when we have n red balls ? 
price_money = {0: 0, 1: 0, 2: 0, 3: 5, 4: 100, 5: 2500, 6: 2000000 }

# When jackpot hits 5Millon or above.
#price_money = {0: 0, 1: 0, 2: 0, 3: 50, 4: 1000, 5: 25000, 6: 2000000 }

# Probability of getting n read ball ?
expected_win_price = 0

matches = []
prices = []
for i in range(0, 7):
    w_prob = (comb(43, 6-i) * comb(6, i)) / comb(49, 6)
    #total+= w_prob
    print(f"Probability of getting {i} red ball = {w_prob}")
    expected_win_price += w_prob * price_money[i]
    matches.append((i, w_prob))
    prices.append((price_money[i], w_prob))
    
print(f"Expected winning price of a single lottery is : {expected_win_price}" )

```

On Normal Drawing day the chances are listed below, 

```text
Probability of getting 0 red ball = 0.4359649755116915
Probability of getting 1 red ball = 0.4130194504847604
Probability of getting 2 red ball = 0.13237802900152576
Probability of getting 3 red ball = 0.017650403866870102
Probability of getting 4 red ball = 0.000968619724401408
Probability of getting 5 red ball = 1.8449899512407772e-05
Probability of getting 6 red ball = 7.151123842018516e-08
Expected winning price of a single lottery is : 0.37426121739588103
```

On the 5Millon Jackpot day, the chance of winning are, 

```text
Probability of getting 0 red ball = 0.4359649755116915
Probability of getting 1 red ball = 0.4130194504847604
Probability of getting 2 red ball = 0.13237802900152576
Probability of getting 3 red ball = 0.017650403866870102
Probability of getting 4 red ball = 0.000968619724401408
Probability of getting 5 red ball = 1.8449899512407772e-05
Probability of getting 6 red ball = 7.151123842018516e-08
Expected winning price of a single lottery is : 2.455409882395478

```

Checkout how the expected value changed. This was the key insight those people 
seens on the game to exploit. **But it's not that simple, higher expected value
doesn't guarentee a profit of $2.45 for every $1 lottery ticket,
that intuition only for those who have stitstics background gets it**.

Expected value really means, by the Law of Large Number if we sample a random variable
enough number of times the random variable will converge to the expected value. Here how many sample
to take isn't fixed, only thing is how much close we are able to converge to the
expected value. In another way they have to purchase enough number of ticket to
ensure that their overall profit is close to the expected value projection.

$
\begin{array}{l}
 \Longrightarrow \ Probable\ winning\ price\ money\ using\ the\ odds\ of\
 winning\ the\ lottery.\\
 \\
 I\ bought\ 2200\ lottery,\ which\ costs\ \$1\ each.\ Roll-down\ week\ the\
 price\ money\ \\
 hits\ 10x\ higher\ for\ all\ the\ 3,\ 4,\ 5\ matches.\ If\ the\ jackpot\ hits\
 then\ the\ rolldown,\\
 won't\ be\ given.\\
 \\
 \Longrightarrow \ 2200\ *\ \left( 0.017\ *\ 50\ +\ 0.00096\ *\ 1000\ +\ 1.88\
 *\ 10^{-5} \ *\ 25000\ \right)\\
 Here\ we\ are\ for\ the\ 1\ and\ 2\ matches\ we\ won't\ get\ any\ money,\ we\
 aren't\ using\ 0,\ to\ multiply\\
 and\ descard\ those\ parts,\ as\ it's\ really\ \\
 \Longrightarrow \ 2200\ *\ 2.28\\
 \\
 Profit\ =\ 3645\ -\ 2200\ =1445\ \Longrightarrow \ \sim 40\%\ profit\ :)\\
 \\
 This\ means\ 1\ ticket\ returns\ more\ than\ \$1\ !\\
 \\
 \mathbf{If\ you\ buy\ one\ ticket,\ what\ is\ the\ likelihood\ of\ number\
 match}\\
 \\
 \Longrightarrow \ 0.472\ *\ 1\ +\ 0.1512\ *\ 2\ +\ 0.017\ *\ 3\ +\ 0.00096\ *\
 4\ +\ 1.88\ *\ 10^{-5} \ *\ 5\ +7.15\ *\ 10^{-8} \ *\ 6\\
 \Longrightarrow 0.7783\\
 \\
 \mathbf{In\ Normal\ scnario\ ( no\ roll\ down\ day\ ) \ the\ every\ doller\
 spend\ doesn't\ give\ statistical\ return}\\
 \mathbf{of\ doller\ plus,\ see\ below\ }\\
 \\
 For\ a\ single\ ticket\ what's\ the\ chance\ of\ winning\ ?\\
 \\
 \Longrightarrow \ \left( 0.017\ *\ 5\ +\ 0.00096\ *\ 100\ +\ 1.88\ *\ 10^{-5}
 \ *\ 2500\right)\\
 \Longrightarrow \ 0.228\ *\ \$1\\
 \\
 This\ means\ you\ get\ statistically\ 22\ cents\ if\ you\ spend\ 1\$\ on\ the\
 normal\ drawing\ days.\\
 \\
 The\ odds\ of\ return\ increased\ 10x\ times\ on\ the\ roll\ down\ days,\
 hence\ the\ lottery\ cartel\ tap\ that\\
 opportunity\ to\ make\ more\ money\ from\ the\ lottery.
 \end{array}
 $


#References

1. https://www.michigan.gov/documents/BSL-L-AR2003_133757_7.pdf
