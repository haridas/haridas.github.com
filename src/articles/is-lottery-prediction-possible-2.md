Title: Can I predict the winning lottery numbers 2
Date: 2020-02-13
Category: data-science
Tags: statistics,ml
Authors: Haridas N


NOTE: test the writing using google document.

In my previous post I have explained how the lottery number system works and
forecasting a winning number isn't possible with confidence grater than the
random chance. This randomness of the data doesn't help us do any kinda
analytic. Only thing can be done is to verify the lottery prediction doesn't 
have any skewness towards particular set of numbers.

Considering all these properties of the lottery system, still few people found
a way to win the lottery with higher confidence level or they are sure that they
can make profit out of the lottery. I showed few such instances in previous blog
entry. In this blog let's disect how they are able to find a loop hole in the
lottery system.


Let's take the lottery game discussed on this video, 
All the lottery games, the odds of winning is purely based on probability of
getting, usually lottery games there will be price money for those tickets which
matched partially to the winning ticket. Based on lottery scheme it varies, if
you are able to match 3 numbers out of 6, you get $5 or 4 o

They understood the internall statistical significance for winning a price based
on particular game rules. What every I have mentioned about the previous post
for regarding the data quality still valid.


In this post lets see what are the techniques they have employed to find
weakness in the lotteries to win more prices money than what they spend in most
of the cases. Usually it's otherway around that you will fail most of the cases.

This has been possible because of the special game settings and its weakness, In
this blog I'm trying to go through the process of how they are able to find
a successful way of making profit out of lottery business.


In short these groups are known as "lottery syndicates"

Here the lottery game is structured as below, 

The type of lottery played in India and USA are different, mostely the USA has
online style lottery. In early 1990 all the lottery drwaing work being done
manually.


$
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
$


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

