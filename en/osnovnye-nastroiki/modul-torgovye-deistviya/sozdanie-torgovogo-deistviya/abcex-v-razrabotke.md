# ABCEx (Under Development)

{% hint style="info" %}
To discuss terms and set up a connection, please contact a [service representative](https://t.me/ABCEX_management).

**Disclaimer**: When connecting your website to any service, please independently assess the potential risks of collaboration.
{% endhint %}

{% hint style="success" %}
[General Guide for Configuring Trade Action Parameters](https://premium.gitbook.io/main/osnovnye-nastroiki/modul-torgovye-deistviya/sozdanie-torgovogo-deistviya/parametry-torgovykh-deistvii)
{% endhint %}

Go to the "**Trade Actions**" section ➔ "**Add Action**," enter a name for the trade action in the "**Title**" field, select ABCEx from the dropdown menu in the "**Module**" field, leave the status as "**Active Action**," and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (48)_eng.png" alt="" width="422"><figcaption></figcaption></figure>

Enter the API key provided by the exchange representative (leave the "**Domain**" field empty) and save the changes.

<figure><img src="../../../.gitbook/assets/image (45)_eng.png" alt=""><figcaption></figcaption></figure>

In the module, you can create one of two actions — "**Sell**" or "**Buy**."

{% hint style="info" %}
The "<mark style="color:red;">**Sell**</mark>" action is suitable when you want to convert the amount received from a client into a stablecoin like USDT (or another currency of your choice).

The "<mark style="color:green;">**Buy**</mark>" action is suitable when you do not want to maintain a reserve of the payout currency in your exchange account and plan to purchase the currency for payout only when a client submits a request to buy that currency from your exchange. In this case, you need to use the [ABCEx auto-payout module](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/abcex) to process the payout immediately after the purchase.

Example: **Exchange Direction BTC - USDT**.\
If you want to <mark style="color:red;">**sell**</mark> the equivalent of the amount received from the client on the ABCEx exchange (e.g., BTC, receiving USDT), select the "**Give**" amount in the trade action settings for the "**Sell**" action (currencies should be set to "**Auto**" to "**Auto**" or specify BTC in the "**Currency Code**" field).\
The exchange will execute a <mark style="color:red;">**sell**</mark> order for BTC from your balance and a <mark style="color:green;">**buy**</mark> order for USDT at the market rate.

If you want to <mark style="color:green;">**buy**</mark> the equivalent of the amount sent to the client on the exchange (e.g., BTC, paying with USDT), select the "**Give**" amount in the trade action settings for the "**Buy**" action (currencies should be set to "**Auto**" to "**Auto**" or specify BTC in the "**Currency Code**" field).\
The exchange will execute a <mark style="color:green;">**buy**</mark> order for BTC from your balance and a <mark style="color:red;">**sell**</mark> order for USDT at the market rate.
{% endhint %}

<div><figure><img src="../../../.gitbook/assets/image (50)_eng.png" alt="" width="486"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/image (610)_eng.png" alt="" width="472"><figcaption></figcaption></figure></div>

{% hint style="success" %}
Examples of Trade Actions:

Example 1:\
Action "<mark style="color:red;">**Sell**</mark>", exchange direction **USDT TRC20 to BTC**, with currencies selected in the trade action as "**Currency Code**" for buying — **USDT** and selling — **RUB**, amount from the request "**Give**".\
The client creates a request to receive 0.0012 BTC (~100 USDT) and pays for it. At this point (if the trade action is set to execute after the "**Awaiting Merchant Confirmation**" status), the exchange will execute a <mark style="color:red;">**sell**</mark> order for **USDT** to **RUB** for the request amount (provided there is sufficient balance to complete the action).\
![](<../../../.gitbook/assets/image (46)_eng.png>)

\
Example 2:\
Action "<mark style="color:red;">**Sell**</mark>", exchange direction **USDT TRC20 to BTC**, with currencies set to "**Auto**" for both buying and selling, amount "**Give**".\
The client creates a request to receive 0.0012 BTC (~100 USDT) and pays for it. At this point, the exchange will execute a <mark style="color:green;">**buy**</mark> order for **BTC** using **USDT** for the request amount.\
![](<../../../.gitbook/assets/image (47)_eng.png>)

\
Example 3:\
Action "<mark style="color:red;">**Sell**</mark>", exchange direction **BTC** to **USDT TRC20**, with currencies set to "**Auto**" for both buying and selling, amount "**Receive**".\
The client creates a request to receive 100 USDT and pays for it. At this point, the exchange will execute a <mark style="color:green;">**buy**</mark> order for **BTC** using **USDT** for the request amount.\
\
Example 4:\
Action "<mark style="color:red;">**Sell**</mark>", exchange direction **USDT TRC20** to **RUB**, with currencies set to "**Auto**" for both buying and selling, amount "**Receive**".\
The client creates a request to receive 8500 RUB (~100 USDT) and pays for it. At this point, the exchange will execute a <mark style="color:green;">**buy**</mark> order for **USDT** using **RUB** for the request amount.
{% endhint %}

{% hint style="warning" %}
Please note that you can create actions for step-by-step exchanges of one currency into another through intermediate currencies. Most often, when there is no direct pair **Currency 1** ➔ **Currency 2** on the exchange, the exchange is performed via the stablecoin USDT (TRC20) (**Currency 1** ➔ **USDT** ➔ **Currency 2**), but you can also use alternative options.

For step-by-step exchanges, you need to:

* Create 2 trade actions: **Sell** (**Currency 1** ➔ **USDT**) and **Buy** (**USDT** ➔ **Currency 2**)
* Select the same exchange directions and execution statuses in the "**Addition Settings**" block of the trade action settings
* Set the execution order: 1 — for the **Sell** action, 2 — for the **Buy** action
{% endhint %}

To ensure the trade action executes correctly, it is also important to select a currency pair that is traded on the ABCEx exchange in the "**Currency Code**" and "**Trading Currency Code**" fields. If you select "**Auto**," the currencies will be selected automatically (see examples above).

Currently available pairs are **USDT/RUB** and **BTC/USDT** (and their reverse pairs).

<figure><img src="../../../.gitbook/assets/image (2121)_eng.png" alt="" width="339"><figcaption></figcaption></figure>

{% hint style="danger" %}
If you select currencies that do not form a pair, the trade action will fail with an error during execution.
{% endhint %}