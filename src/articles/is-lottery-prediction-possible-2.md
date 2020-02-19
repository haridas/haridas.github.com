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

I'm taking the game played in 2007 period in USA state, ... Selbis are retired
elder couple, they came across this lottery game once they were in a stationary
store. Selbi was able to see a loop hole in the game in that short time, or put
it other way he saw higher likelihood of making profit out of this game at
particular time period. He went back and done few more statistical analysis to
validate his theory. All was coming in his favour.


## Rules of this Lottery game

He started by purchasing spending $2000 

Let's take the lottery game discussed on this video, 
All the lottery games, the odds of winning is purely based on probability of
getting first or other smaller prices, 
Based on lottery scheme it varies, if you are able to match 3 numbers out of 6, you get $5 or 4 o

Here the lottery game is structured as below, 


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

