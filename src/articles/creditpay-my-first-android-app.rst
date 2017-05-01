Creditpay My First app in playstore !
=====================================

:date: 20-04-2017
:category: blog
:tags: android,firebase


Yes, this is my first app in google play store. I created it my own needs.
It's simple app which helps to recommend a credit card for use on a particular day.

Right now the UX is very simple, but included the following features,

1. Multi device cloud sync using firebase database.
2. O-Auth support
3. Easy way to add new card with Card Name, Billing day (eg: 04, if the billing
   date is 04/April), and Grace Period ( How many days you get between bill
   generation date to actual bill payment date, generally this is 20 days).
4. Modify the card details.
5. Can be used offline.


Currently the card suggestion is based on the grace period details that we enter
when we add new card. It checks; for each card, how many days are there before
the card bill is generated.

For example, assume today is 6'th of a month, then we have to pick the card
which gives best score based on the following calculation.

    For a card;

    Billing day = 05'th of a month

    Grace period = 20 days

    Score of a card is: (#days between 6'th of this to 5'th of coming month)
    + (grace period of the card)

    ie; score = 30 + 20 = 50 (This will vary slightly due to varying number days
    of each month), and note that this is best score of a card based on the
    above given values.

Another example:- 

Assume today date is 21'st, we want to pick a card, for that card, the score is
= (05 (next month) - 21) + 20 = 14 + 20 = 34 days.

In ideal case we can maximize this if we made the purchase on 05'nd of the month
using this card. The app is just doing this and displaying the card after
sorting it out based on the score of each card.

.. image:: /images/creditpay.png
        :alt: yard-login-page
        :width: 50%
        :height: 550px
        :align: left

Roadmap:

 1. UX improvements.
 2. Display the card with more images and details.
 3. Methods to improve the offline usage.

If you guys interested, give a try and let me know your feedbacks.

Cheers!
