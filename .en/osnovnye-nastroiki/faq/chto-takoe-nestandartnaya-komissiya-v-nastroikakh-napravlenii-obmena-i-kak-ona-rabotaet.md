# What is a Non-Standard Fee in Exchange Direction Settings and How Does It Work?

## Standard Fee

Here’s an example of how a merchant using the Webmoney payment system with a standard fee operates:

* The user sends 1000 RUB.
* On the payment system’s website, the user pays 1000 RUB plus the payment system’s fee of 8 RUB. In total, the user pays 1008 RUB.
* The exchange service receives 1000 RUB in their account.

## Non-Standard Fee

Here’s an example of how a merchant using the Yandex.Money payment system with a non-standard fee operates:

* The user sends 1000 RUB.
* On the payment system’s website, the user pays exactly 1000 RUB. The payment system’s fee of 5 RUB is included in this amount. So, the user pays 1000 RUB in total.
* The exchange service receives 995 RUB. The 5 RUB fee was deducted from the payment recipient, so the exchange service gets 995 RUB instead of the full 1000 RUB sent.

If you want the exchange service to receive exactly 1000 RUB, the user would need to pay, say, 1005 RUB. Then, after deducting the 5 RUB payment system fee, the exchange service would receive the full 1000 RUB.

Non-standard fees can be used with Yandex.Money, Privat24, Liqpay, and some other merchants.