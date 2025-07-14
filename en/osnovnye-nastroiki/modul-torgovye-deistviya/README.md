# Trading Actions Module

A description of the module and pricing information are available [here](https://premiumexchanger.com/tradeapi/).

{% embed url="https://youtu.be/V9OtYr5m19U" %}

{% hint style="warning" %}
When executing trades on an exchange, discrepancies can occur because cryptocurrency prices may change during the transaction process. To avoid such discrepancies, it’s necessary to maintain a small reserve for each cryptocurrency. This reserve will cover the difference between the price at the time the order is placed and the price at the time the trade is executed.

To prevent discrepancies when making trades on the exchange, follow these steps:

1. Set aside a small reserve for each cryptocurrency you trade. For example, a reserve of 0.003 BTC.
2. Regularly monitor the reserve amount and replenish it as needed.

**Example:**

Suppose you want to buy 1 BTC. At the time you place the order, the Bitcoin price is $50,000. However, by the time the trade executes, the price might have changed to $50,009. In this case, the discrepancy is $9. If you have a reserve of 0.003 BTC in your balance, this difference will be covered.

**Important:**

The size of the reserve needed to cover discrepancies depends on the trade volume and the volatility of the cryptocurrency.
{% endhint %}

The purpose of the trading module is to fully automate the process of executing orders and recording current prices, whether or not your portfolio contains various cryptocurrencies.

There are two main types of trading actions:

1. <mark style="color:red;">**Selling**</mark> cryptocurrency by order.
2. <mark style="color:green;">**Buying**</mark> cryptocurrency by order.

Each of these actions can be further divided into two options:

Here is a natural, fluent English translation of the provided text:

---

1. **Selling** cryptocurrency by request when it is **available** in the portfolio.  
2. **Buying** cryptocurrency by request when the currency used for the purchase is **available** in the portfolio.

and

1. **Selling** cryptocurrency by request when it is **not available** in the portfolio.  
2. **Buying** cryptocurrency by request when the currency used for the purchase is **not available** in the portfolio.

This distinction allows for a more detailed description of different trading scenarios.

## Selling Cryptocurrency

When selling or buying cryptocurrency by request, if the required currency is **available** in the portfolio, the process is simpler and more efficient. In this case, the automated trading system works as follows:

1. The client creates a request and receives a payment address from the merchant.  
2. The client pays the request (it is also possible to enable [recalculation based on the exchange rate](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/valyuty-i-napravleniya/sozdanie-novogo-napravleniya-obmena#vkladka-pereschet-zayavok) at the moment of payment, which is important for locking in the rate and ensuring a stable profit margin on the request), and the system automatically executes the sale of the cryptocurrency available in your portfolio on the exchange.  
3. After the cryptocurrency is sold, the client receives the corresponding amount, and the system records the current exchange rate at the time of the client’s payment.  
4. The system then transfers the funds to the exchange and continues the process.

{% hint style="info" %}  
In practice, it looks like this:

Suppose you have 1 BTC in your portfolio on the exchange account. To receive cryptocurrency, you use, for example, a block.io wallet (any merchant can be used to accept cryptocurrency).

A client creates a request to buy cryptocurrency worth 0.1 BTC and makes the payment. At the moment of payment, the system instantly sells 0.1 BTC on the exchange, for example, for USDT.

As a result, you have 0.1 BTC in your block.io account, 0.9 BTC remaining in your exchange account, and USDT received from selling 0.1 BTC.  
{% endhint %}

---

If you want, I can also help with a polished translation of the second part (selling/buying when the currency is not available) or any other sections.

As soon as the full amount of BTC is transferred to your block.io account, you can move all the BTC to your exchange account in a single transfer, which helps reduce transaction fees.

This method minimizes risks and ensures a more stable profit percentage on the order since the exchange rate is locked in at the time of payment. Additionally, optimizing fund transfers between the exchange and wallets lowers fees and improves trading efficiency.

But what if you don’t have any bitcoins in your portfolio and, for example, only hold USDT? In this case, a margin account on the exchange comes to your aid. The process works similarly to what was described above. However, since you don’t have BTC in your portfolio, the system will borrow the required amount of BTC on the exchange and sell it, using your USDT balance as collateral for the loan (note: any currency can be used as collateral).

For those who trade or invest on stock, commodity, or currency exchanges, this kind of sale is called a “short sale” or “shorting.” It means selling an asset you don’t actually own.

Let’s break down the steps using the example provided:

1. The client creates an order and receives a payment address from the merchant.
2. The client pays 0.1 BTC (you can also set up [rate recalculation](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/valyuty-i-napravleniya/sozdanie-novogo-napravleniya-obmena#vkladka-pereschet-zayavok) at the time the client pays the order, which is important for locking in the rate and ensuring a stable profit percentage on the order).
3. As soon as the client pays, the system automatically borrows and sells 0.1 BTC on the exchange, using your USDT account as collateral for the loan.
4. The cryptocurrency, for example, is received in the block.io wallet (cryptocurrency reception can be set up through any merchant).
5. As a result of this operation, you have 0.1 BTC in your block.io account, a 0.1 BTC debt to the exchange, and USDT obtained from selling the 0.1 BTC.

{% hint style="info" %}
If you have multiple orders and your **debt** to the exchange is 1 BTC, but you have 1 BTC in your block.io wallet, you can transfer 1 BTC from block.io to your exchange account to repay the debt. This way, you lock in the exchange rate without the risk of it changing, even if you don’t hold any cryptocurrency in your portfolio.
{% endhint %}

## Buying Cryptocurrency

Here’s how the process of buying cryptocurrency works **when you already have it in your portfolio**. Let’s say you’re exchanging rubles from Sberbank for 0.1 BTC:

1. The client creates an order, and you provide them with a card for payment.
2. The client pays the required amount.
3. You manually mark the order status as "Paid" (you can also set up [automatic recalculation based on the exchange rate](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/valyuty-i-napravleniya/sozdanie-novogo-napravleniya-obmena#vkladka-pereschet-zayavok) at the time the client pays, which is important for locking in the rate and ensuring a stable profit margin on the order).

{% hint style="info" %}
Suppose you have 1 BTC in your block.io wallet. When you mark the order as "Paid" on the exchange, 0.1 BTC is instantly purchased. Then, you click the "Transfer" button, and 0.1 BTC is sent from your block.io wallet. As a result, you’ll have 0.9 BTC left in your block.io wallet and 0.1 BTC credited to your exchange account.

When you accumulate many orders and the entire BTC balance from your block.io wallet is transferred to your exchange account, you can transfer the full BTC amount back from the exchange to your block.io wallet.
{% endhint %}

If you **don’t have** any BTC in your portfolio but only USDT, and you want to pay out orders automatically, a margin account comes to the rescue again. Here’s what you need to do in advance:

1. Transfer the required amount of USDT to your exchange account—enough to buy 1 BTC, for example.
2. Take out a loan of 1 BTC on the exchange account.
3. Send 1 BTC from the exchange to your block.io wallet. As a result, you’ll have 1 BTC in your block.io wallet balance and a **debt** of 1 BTC on your exchange account.

Here is a natural, fluent English translation of the provided text:

---

Then, clients can create exchange requests, and you pay out bitcoins from your block.io wallet. For example, suppose you have an exchange from rubles via Sberbank to 0.1 BTC:

1. The client creates a request, and you provide them with a payment card.
2. The client pays the required amount.
3. You manually set the request status to "Paid" (you can also configure [recalculation based on the exchange rate](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/valyuty-i-napravleniya/sozdanie-novogo-napravleniya-obmena#vkladka-pereschet-zayavok) at the time the client pays, which is important for locking in the rate and ensuring a stable profit margin on the request).

{% hint style="info" %}
When you set the request status to "Paid," the exchange instantly purchases 0.1 BTC, and the <mark style="color:red;">debt</mark> of 0.1 BTC is settled. Then, you click the "Transfer" button, and 0.1 BTC is paid out from your block.io wallet. As a result, you have 0.9 BTC left in your block.io wallet, and the <mark style="color:red;">debt</mark> to the exchange is 0.9 BTC.

When you accumulate many requests and the entire debt to the exchange is settled, you receive the sold USDT for Sberbank rubles and have zero debt to the exchange. The sale is carried out at the rate you set, regardless of any changes in Bitcoin’s price on the exchange.
{% endhint %}

It’s also important to note that all the above buying and selling actions can be combined depending on your needs. You can perform cryptocurrency-to-cryptocurrency exchanges even if you don’t actually hold the coins. For example, exchanging XMR for BTC.

Additionally, it’s possible to create more complex trading operations involving cryptocurrency-to-cryptocurrency exchange directions, including trading pairs that don’t exist on the exchange, such as XMR to XRP and vice versa.

---

Let me know if you want it adjusted for a specific audience or style!

The examples used a merchant and automatic payouts via the block.io wallet. It’s important to note that you can use any merchant and/or configure automatic payouts as you see fit. Trading actions are tied solely to the status of the requests, regardless of which merchant or payout system you choose.