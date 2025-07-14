# ABCEx (in development)

{% hint style="info" %}
To discuss terms and integration, please contact the [service representative](https://t.me/ABCEX_management).

**Disclaimer:** When connecting your website to any service, please independently assess the potential risks involved in the partnership.
{% endhint %}

{% hint style="success" %}
[General guide to configuring trading action parameters](https://premium.gitbook.io/main/osnovnye-nastroiki/modul-torgovye-deistviya/sozdanie-torgovogo-deistviya/parametry-torgovykh-deistvii)
{% endhint %}

Go to the "**Trading Actions**" section ➔ "**Add Action**," enter a name for the new trading action in the "**Title**" field, select ABCEx from the "**Module**" dropdown menu, leave the status as "**Active Action**," and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (48).png" alt="" width="422"><figcaption></figcaption></figure>

Enter the API key provided by the exchange representative (leave the "**Domain**" field empty) and save your changes.

<figure><img src="../../../.gitbook/assets/image (45).png" alt=""><figcaption></figcaption></figure>

Within the module, you can create one of two actions — "**Sell**" or "**Buy**."

{% hint style="info" %}
The "**Sell**" action is suitable when you want to convert the amount received from the client’s currency request into the stablecoin USDT (or another currency you find appropriate).

The "**Buy**" action is suitable when you prefer not to keep a reserve of the payout currency in your exchange accounts and plan to purchase the currency for payout only when a client places a buy order with your exchanger. In this case, you should use the [ABCEx auto-payout module](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/abcex) to pay out the currency immediately after purchase.
{% endhint %}

Example: **Exchange direction BTC - USDT**.  
If you want to <mark style="color:red;">**sell**</mark> the equivalent of the amount received from the client on the ABCEx exchange (for example, sell BTC after receiving USDT) — select the "**Amount to give**" field in the trade settings for the action "**Sell**" (currencies should be set to "**Auto**" or in the "**Currency code**" field (the currency to sell), select BTC).  
The exchange will execute a <mark style="color:red;">**sale**</mark> of BTC from your balance and a <mark style="color:green;">**purchase**</mark> of USDT at the market rate.

If you want to <mark style="color:green;">**buy**</mark> the equivalent of the amount sent to the client on the exchange (for example, buy BTC by paying USDT) — select the "**Amount to give**" field in the trade settings for the action "**Buy**" (currencies should be set to "**Auto**" or in the "**Currency code**" field (the currency to sell), select BTC).  
The exchange will execute a <mark style="color:green;">**purchase**</mark> of BTC from your balance and a <mark style="color:red;">**sale**</mark> of USDT at the market rate.

---

**Examples of trading actions:**

Example 1:  
Action "<mark style="color:red;">**Sell**</mark>", exchange direction **USDT TRC20 to BTC**, in the trade settings the currencies for buying ("**Currency code**") — **USDT** and selling ("**Trading currency code**") — **RUB**, amount from the order "**Amount to give**".  
The client creates an order to receive 0.0012 BTC (~100 USDT) and pays for it. At this moment (if the trade status is set to "**After merchant confirmation pending status**"), the exchange will execute a <mark style="color:red;">**sale**</mark> of **USDT** for **RUB** for the order amount (provided there is sufficient balance to complete the action).

Example 2:  
Action "<mark style="color:red;">**Sell**</mark>", exchange direction **USDT TRC20 to BTC**, in the trade settings currencies are set to "**Auto**" for both buying and selling, amount "**Amount to give**".  
The client creates an order to receive 0.0012 BTC (~100 USDT) and pays for it. At this moment, the exchange will execute a <mark style="color:green;">**purchase**</mark> of **BTC** using **USDT** for the order amount.

Example 3:  
The action "**Sell**" with the exchange direction from **BTC** to **USDT TRC20**, where the trading directions (TD) have "**Auto**" selected for both buying and selling currencies, and the amount is set as "**You receive**."  
The client creates an order to receive 100 USDT and pays for it. At that moment, the exchange will execute a **purchase** of **BTC** using USDT for the order amount.

Example 4:  
The action "**Sell**" with the exchange direction from **USDT TRC20** to **RUB**, where the trading directions have "**Auto**" selected for both buying and selling currencies, and the amount is set as "**You receive**."  
The client creates an order to receive 8,500 RUB (approximately 100 USDT) and pays for it. At that moment, the exchange will execute a **purchase** of **USDT** using RUB for the order amount.

---

**Note:**  
It is possible to create actions for stepwise exchanges from one currency to another through intermediate currencies. Most often, when there is no direct trading pair **currency 1** ➔ **currency 2** on the exchange, the exchange is done via the stablecoin USDT (TRC20) (**currency 1** ➔ **USDT** ➔ **currency 2**), but you can also use alternative routes.

To set up a stepwise exchange, you need to:

* Create two trading actions: **Sell** (**currency 1** ➔ **USDT**) and **Buy** (**USDT** ➔ **currency 2**)  
* Select the same exchange directions and trigger statuses in the "**Addition Settings**" block within the trading action settings  
* Set the execution order: 1 for the **Sell** action, 2 for the **Buy** action

---

For the trading action to execute correctly, it is also important to select a currency pair that is traded on the ABCEx exchange in the "**Currency Code**" and "**Trading Currency Code**" fields. If you select "**Auto**," the currencies will be chosen automatically (see examples above).

Currently, the available pairs are **USDT/RUB** and **BTC/USDT** (and their reverses).

![Image](../../../.gitbook/assets/image%20(2121).png)

---

**Warning:**  
If you select currencies that do not form a trading pair, the trading action will definitely fail with an error upon execution.