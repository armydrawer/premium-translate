# Module: "Trading Actions"

The module description and pricing information are available via [this link](https://premiumexchanger.com/tradeapi/).

{% embed url="https://youtu.be/V9OtYr5m19U" %}

{% hint style="warning" %}
When trading on an exchange, discrepancies may occur due to cryptocurrency price fluctuations during the execution of a trade. To mitigate this, it’s essential to maintain a small reserve for each cryptocurrency to cover the difference between the price at the time of placing the order and the price at the time of execution.

To avoid such discrepancies, follow these steps:

1. Set up a small reserve for each cryptocurrency you trade. For example, the reserve could be 0.003 BTC.
2. Regularly monitor the reserve size and replenish it as needed.

**Example:**

Let’s say you want to buy 1 BTC. At the time of placing the order, the price of Bitcoin is $50,000. However, by the time the trade is executed, the price may have changed to $50,009. In this case, the discrepancy is $9. If you have a reserve of 0.003 BTC, this difference will be covered.

**Important:**

The size of the reserve required to cover discrepancies depends on the trade size and the cryptocurrency’s volatility.
{% endhint %}

The purpose of the trading module is to fully automate the process of executing orders and recording current exchange rates, whether cryptocurrencies are present in your portfolio or not.

There are two main types of trading actions:

1. <mark style="color:red;">**Selling**</mark> cryptocurrency via an order.
2. <mark style="color:green;">**Buying**</mark> cryptocurrency via an order.

Each of these actions can be divided into two scenarios:

1. <mark style="color:red;">**Selling**</mark> cryptocurrency via an order when it is <mark style="color:green;">**available**</mark> in your portfolio.
2. <mark style="color:green;">**Buying**</mark> cryptocurrency via an order when the currency used for the purchase is <mark style="color:green;">**available**</mark> in your portfolio.

and

1. <mark style="color:red;">**Selling**</mark> cryptocurrency via an order when it is <mark style="color:red;">**not available**</mark> in your portfolio.
2. <mark style="color:green;">**Buying**</mark> cryptocurrency via an order when the currency used for the purchase is <mark style="color:red;">**not available**</mark> in your portfolio.

This categorization allows for a more detailed description of various trading scenarios.

---

## Selling Cryptocurrency

When selling or buying cryptocurrency via an order, and the required currency is <mark style="color:green;">available</mark> in your portfolio, the process is simpler and more efficient. In this case, the automated trading system operates as follows:

1. The client creates an order and receives a payment address from the merchant.
2. The client makes the payment (you can also configure [rate recalculation](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/valyuty-i-napravleniya/sozdanie-novogo-napravleniya-obmena#vkladka-pereschet-zayavok) at the time of payment, which is crucial for locking in the rate and ensuring a stable profit margin for the order). The system then automatically sells the cryptocurrency on the exchange from your portfolio.
3. After the cryptocurrency is sold, the client receives the corresponding amount, and the system records the current rate at the time of payment.
4. The system then transfers the funds to the exchange and continues the process.

{% hint style="info" %}
In practice, this works as follows:

Suppose you have 1 BTC in your portfolio on an exchange account. For receiving cryptocurrency, you use, for example, a block.io wallet (any merchant wallet can be used for receiving cryptocurrency).

A client creates an order to purchase 0.1 BTC and makes the payment. At the time of payment, the system instantly sells 0.1 BTC on the exchange, for example, for USDT.

As a result, you have 0.1 BTC in your block.io account, 0.9 BTC in your exchange account, and USDT from the sale of 0.1 BTC.

Once the entire BTC amount is transferred to your block.io account, you can move all the BTC to your exchange account in one transaction, reducing transfer fees.
{% endhint %}

This method minimizes risks and ensures a more stable profit margin for the order, as the rate is locked in at the time of payment. Additionally, optimizing fund transfers between the exchange and wallets reduces fees and increases trading efficiency.

But what if you <mark style="color:red;">don’t have</mark> Bitcoin in your portfolio and only have USDT? In this case, a margin account on the exchange comes to the rescue. The steps described above remain the same. However, since you don’t have BTC in your portfolio, the system will borrow the required amount of BTC from the exchange and sell it, using your USDT account as collateral for the loan (note: any currency can be used as collateral).

For those familiar with stock, commodity, or forex trading, this type of sale is known as a "short sale" or "shorting." It involves selling an asset you don’t own.

Let’s break it down step by step using the example above:

1. The client creates an order and receives a payment address from the merchant.
2. The client pays for 0.1 BTC (you can also configure [rate recalculation](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/valyuty-i-napravleniya/sozdanie-novogo-napravleniya-obmena#vkladka-pereschet-zayavok) at the time of payment, which is crucial for locking in the rate and ensuring a stable profit margin for the order).
3. Once the client pays, the system automatically borrows and sells 0.1 BTC on the exchange, using your USDT account as collateral.
4. The cryptocurrency is received, for example, in a block.io wallet (any merchant wallet can be used for receiving cryptocurrency).
5. As a result, you have 0.1 BTC in your block.io account, a <mark style="color:red;">debt</mark> of 0.1 BTC to the exchange, and USDT from the sale of 0.1 BTC.

{% hint style="info" %}
If you have multiple orders and your <mark style="color:red;">debt</mark> to the exchange is 1 BTC, while your block.io account holds 1 BTC, you can transfer 1 BTC from block.io to the exchange account to repay the debt. This allows you to lock in the rate without risking price changes, even if you don’t have cryptocurrency in your portfolio.
{% endhint %}

---

## Buying Cryptocurrency

The process of buying cryptocurrency when it is <mark style="color:green;">available</mark> in your portfolio works as follows. For example, let’s consider an exchange of rubles from Sberbank for 0.1 BTC:

1. The client creates an order, and you provide them with a payment card.
2. The client pays the required amount.
3. You manually set the order status to "Paid" (you can also configure [rate recalculation](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/valyuty-i-napravleniya/sozdanie-novogo-napravleniya-obmena#vkladka-pereschet-zayavok) at the time of payment, which is crucial for locking in the rate and ensuring a stable profit margin for the order).

{% hint style="info" %}
For example, you have 1 BTC in your block.io wallet. When you set the order status to "Paid," the exchange instantly buys 0.1 BTC. Then, you click the "Transfer" button, and 0.1 BTC is sent from your block.io wallet. As a result, you have 0.9 BTC in your block.io wallet and 0.1 BTC in your exchange account.

When multiple orders accumulate, and the entire amount of Bitcoin from your block.io wallet is transferred to the exchange account, you can transfer the total Bitcoin amount back to block.io.
{% endhint %}

If you <mark style="color:red;">don’t have</mark> Bitcoin in your portfolio but only USDT, and you want to automatically fulfill orders, the margin account comes to the rescue again. To prepare for this:

1. Transfer the required amount of USDT to your exchange account, enough to buy 1 BTC, for example.
2. Take out a loan of 1 BTC on the exchange.
3. Transfer 1 BTC from the exchange to your block.io wallet. As a result, you’ll have 1 BTC in your block.io wallet and a <mark style="color:red;">debt</mark> of 1 BTC on the exchange.

Now, clients can create exchange orders, and you can fulfill them by sending Bitcoin from your block.io wallet. For example, let’s consider an exchange of rubles from Sberbank for 0.1 BTC:

1. The client submits a request, and you provide them with a payment card.  
2. The client pays the required amount.  
3. You manually set the request status to "Paid" (you can also configure [recalculation based on the exchange rate](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/valyuty-i-napravleniya/sozdanie-novogo-napravleniya-obmena#vkladka-pereschet-zayavok) at the time of payment, which is crucial for locking in the rate and ensuring a stable profit margin for the transaction).  

{% hint style="info" %}  
When you set the request status to "Paid," an amount of 0.1 BTC is instantly purchased on the exchange, and the <mark style="color:red;">debt</mark> of 0.1 BTC is settled. Then, you click the "Transfer" button, and 0.1 BTC is sent from your block.io wallet. As a result, you are left with 0.9 BTC in your block.io wallet, and the <mark style="color:red;">debt</mark> to the exchange is now 0.9 BTC.  

When you accumulate multiple requests and fully settle the debt to the exchange, you receive the USDT sold for Sberbank rubles and have no remaining debt to the exchange. The sale is conducted at the rate you set, regardless of Bitcoin price fluctuations on the exchange.  
{% endhint %}  

It’s also worth noting that all the actions described above—buying and selling—can be combined depending on your needs. You can carry out cryptocurrency-to-cryptocurrency exchanges even if you don’t actually have the cryptocurrency in your possession. For example, you can exchange XMR for BTC.  

Additionally, you can create more complex trading operations involving cryptocurrency-to-cryptocurrency exchanges, including trading pairs that don’t exist on the exchange, such as XMR to XRP and vice versa.  

The examples provided use a merchant and auto-payouts via the block.io wallet. It’s important to note that you can use any merchant and/or configure automatic payouts as you see fit. Trading actions are tied exclusively to the request statuses, so it doesn’t matter which merchant or auto-payout system you choose to use.  