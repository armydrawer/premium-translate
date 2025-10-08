# Binance

{% hint style="danger" %}
<mark style="color:red;">Before setting up auto payouts, please read the</mark> [<mark style="color:blue;">risk warning!</mark>](https://premium.gitbook.io/main/en/basic-settings/merchants-and-auto-payments/auto-payments/risk-warning)
{% endhint %}

{% hint style="info" %}
If you need to update the module on the server, please refer to the [instructions](https://premium.gitbook.io/main/en/en/basic-settings/faq/updating-script-files-on-the-server/how-to-update-files-on-the-server#merchant-and-auto-payout-modules).
{% endhint %}

## Merchant Account Settings

Register or log in to the [Binance](https://www.binance.com/) platform.

Go to the "**Account**" section and then to "**API Management**."

<figure><img src="../../../.gitbook/assets/image (1451)_eng.png" alt="" width="462"><figcaption></figcaption></figure>

Click on the "**Create API**" button and select the key type "**System Generated**."

<figure><img src="../../../.gitbook/assets/image (1452)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (1454)_eng.png" alt="" width="371"><figcaption></figcaption></figure>

Enter a name for the key and click "**Next**."

<figure><img src="../../../.gitbook/assets/image (1455)_eng.png" alt="" width="419"><figcaption></figcaption></figure>

Confirm the key generation using two-factor authentication.

<figure><img src="../../../.gitbook/assets/image (1457)_eng.png" alt="" width="337"><figcaption></figcaption></figure>

After confirming the key generation, you will be taken to the key page. Save the **API Key** and **Secret Key** in a text file.

<figure><img src="../../../.gitbook/assets/image (1458)_eng.png" alt=""><figcaption></figcaption></figure>

Click on the "**Edit Restrictions**" button to modify the key's operational methods in the "**API Restrictions**" section.

Enter your server's IP address in the "**IP Access Restrictions**" section and click "**Confirm**" to activate the editing of items in the "**API Restrictions**" section.

To enable auto payouts, activate the following options:

* Enable spot and margin trading
* Allow withdrawals
* Enable margin borrowing, repayment, and transfer (if you plan to use loans for currency payouts)

## **Module Settings**

In the admin panel, create a new merchant in the "**Auto Payouts**" -> "**Add Auto Payout**" section.

Select Binance from the dropdown list in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (1460)_eng.png" alt="" width="502"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (1461)_eng.png" alt="" width="440"><figcaption></figcaption></figure>

**API Key** — the public key generated in your Binance account (field "**API Key**")

**Secret Key** — the private key generated in your Binance account (field "**Secret Key**")

## Special Fields

<figure><img src="../../../.gitbook/assets/image (1462)_eng.png" alt=""><figcaption></figcaption></figure>

* **Network** — specify the network for the payout currency according to [Binance requirements](https://www.binance.com/en/network)

<figure><img src="../../../.gitbook/assets/image (1463)_eng.png" alt=""><figcaption></figcaption></figure>

* **Purchase the missing amount of crypto for payout** — options for auto-purchasing currency for payouts:\
  • **No** — do not purchase currency for payout, pay directly from the wallet (the wallet must have sufficient reserves of the payout currency)\
  • **Yes** — auto-purchase currency for payout only when there are insufficient reserves of the payout currency\
  • **Purchase and do not withdraw** — auto-purchase the payout currency to restore the reserve level after paying directly from the wallet\
  • **Buy the full amount** — auto-purchase the total amount of currency from the payout request

{% hint style="warning" %}
For the above option to work, the options "**Determine trade operation code**" and "**Trade operation code (if Manual)**" must be enabled.
{% endhint %}

* **Trading fee on the exchange (%)** — specify the percentage fee for the currency payout
* **Order type:**\
  • **Market** — the order will be executed immediately at the market price on the exchange.\
  • **Limit** — the order will be placed on the exchange at your price and executed according to the "**Order execution time (if Limit)**" parameter.
* **Order execution time (if Limit)** — this option is used only when the order type "**Limit**" is selected:\
  &#xNAN;**• GTC (Good-Til-Canceled)** — the order will remain valid until it is executed or canceled.\
  &#xNAN;**• IOC (Immediate or Cancel)** — the order is filled completely or partially, and the remaining part of the order is canceled.\
  &#xNAN;**• FOK (Fill or Kill)** — the order must be filled in its entirety; otherwise, the entire order will be canceled.
* **Determine trade operation code** — \
  &#xNAN;**• Manually** — select this option if you want to specify the currency to be used for purchasing the payout currency; this option works only when a currency code is provided in the "**Trade operation code (if Manual)**" option.\
  &#xNAN;**• Automatically** — automatically select the currency from the wallet for purchasing the payout currency (determined by the reserve balances in the wallet).
* **Trade operation code (if Manual)** — select the currency code from the dropdown list that will be used for purchasing the payout currency (usually USDT is used); this option is only applicable when "**Manually**" is selected for "**Determine trade operation code**."

## Continuing the Setup

Next, proceed to configure the merchant by following the [general setup instructions](https://premium.gitbook.io/main/en/basic-settings/merchants-and-auto-payments/auto-payments/obshie-nastroiki-merchantov-avtovyplat).