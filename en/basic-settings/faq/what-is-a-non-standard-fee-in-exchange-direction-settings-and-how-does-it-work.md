# What is a Non-Standard Fee in Exchange Direction Settings and How Does It Work?

## Standard Fee

Here’s an example of how a merchant using the WebMoney payment system with a standard fee operates:

* The user sends 1,000 RUB.
* On the payment system’s website, the user pays 1,000 RUB plus the payment system’s fee of 8 RUB. In total, the user pays 1,008 RUB.
* The exchange service receives 1,000 RUB in its account.

## Non-Standard Fee

Now, let’s look at an example of how a merchant using the Yandex.Money payment system with a non-standard fee operates:

* The user sends 1,000 RUB.
* On the payment system’s website, the user pays exactly 1,000 RUB. The payment system’s fee of 5 RUB is included in this amount. So, the user pays 1,000 RUB in total.
* The exchange service receives 995 RUB in its account. The payment system’s fee of 5 RUB is deducted from the amount received, meaning the exchange service gets 995 RUB instead of the full 1,000 RUB sent by the user.

If the exchange service wants to receive exactly 1,000 RUB in its account, the user would need to pay 1,005 RUB. In this case, the payment amount of 1,005 RUB minus the payment system’s fee of 5 RUB would result in 1,000 RUB being credited to the exchange service’s account.

Non-standard fees can be used with Yandex.Money, Privat24, LiqPay, and some other payment systems.