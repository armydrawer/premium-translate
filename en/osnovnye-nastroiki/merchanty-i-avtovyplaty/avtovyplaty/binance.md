# Binance

{% hint style="danger" %}
<mark style="color:red;">Before setting up auto payouts, be sure to read</mark> [<mark style="color:blue;">the risk warning</mark>](https://premiumexchanger.com/wiki/preduprezhdenie-auto/)<mark style="color:blue;">!</mark>
{% endhint %}

{% hint style="info" %}
If you need to update the module on your server, please follow this [instruction](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-avtovyplat).
{% endhint %}

## Settings in the Merchant Dashboard

Register or log in to the [Binance](https://www.binance.com/) platform.

Go to "**Account**" -> "**API Management**".

<figure><img src="../../../.gitbook/assets/image (1451).png" alt="" width="462"><figcaption></figcaption></figure>

Click the "**Create API**" button and select the key type "**System Generated**".

<figure><img src="../../../.gitbook/assets/image (1452).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (1454).png" alt="" width="371"><figcaption></figcaption></figure>

Enter a name for your API key and click "**Next**".

<figure><img src="../../../.gitbook/assets/image (1455).png" alt="" width="419"><figcaption></figcaption></figure>

Confirm the creation of the keys using two-factor authentication.

<figure><img src="../../../.gitbook/assets/image (1457).png" alt="" width="337"><figcaption></figcaption></figure>

After confirming, you will be taken to the API key page. Save your **API Key** and **Secret Key** to a text file.

<figure><img src="../../../.gitbook/assets/image (1458).png" alt=""><figcaption></figcaption></figure>

Click "**Edit Restrictions**" to open the API key permissions under the "**API Restrictions**" section.

Enter your server’s IP address in the "**IP Access Restrictions**" section and click "**Confirm**" to enable editing of the options under "**API Restrictions**".

To enable auto payouts, activate the following options:

* Enable Spot and Margin Trading
* Enable Withdrawals
* Enable Margin Borrowing, Repayment, and Transfer (if you plan to use loans for currency payouts)

## **Module Settings**

In the admin panel, create a new merchant under "**Auto Payouts**" -> "**Add Auto Payout**".

Select Binance from the dropdown menu in the "**Module**" field, enter a name for the module, and click "**Save**".

<figure><img src="../../../.gitbook/assets/image (1460).png" alt="" width="502"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (1461).png" alt="" width="440"><figcaption></figcaption></figure>

**API Key** — the public key generated in your Binance account dashboard (field "**API Key**").

**Secret Key** — the private key generated in your Binance account dashboard (field "**Secret Key**").

## Special Fields

<figure><img src="../../../.gitbook/assets/image (1462).png" alt=""><figcaption></figcaption></figure>

* **Network** — specify the payout currency network according to [Binance requirements](https://www.binance.com/en/network).

<figure><img src="../../../.gitbook/assets/image (1463).png" alt=""><figcaption></figcaption></figure>

* **Auto-purchase missing crypto balance for payout** — options for automatically buying payout currency:  
  • **No** — do not buy payout currency; pay out directly from the wallet (the wallet must have a sufficient balance of the payout currency)  
  • **Yes** — auto-purchase payout currency only if the wallet balance is insufficient  
  • **Buy to replenish, no payout** — auto-purchase payout currency to restore the reserve level after paying out directly from the wallet  
  • **Buy full amount** — auto-purchase the entire payout amount from the order

{% hint style="warning" %}
To use the above option, the settings "**Detect trade operation code**" and "**Trade operation code (if Manual)**" must be enabled.
{% endhint %}

Here is a natural, fluent English translation of the provided text:

---

* **Trading Fee on the Exchange (%)** — enter the percentage fee charged for currency payout  
* **Order Type:**  
  • **Market** — the order will be executed immediately at the current market price on the exchange.  
  • **Limit** — the order will be placed on the exchange at your specified price and executed according to the "**Order Execution Time (if Limit)**" setting.  
* **Order Execution Time (if Limit)** — this option applies only when the order type is set to "**Limit**":  
  • **GTC (Good-Til-Canceled)** — the order remains active until it is either fully executed or canceled.  
  • **IOC (Immediate or Cancel)** — the order is filled either fully or partially, and any unfilled portion is canceled immediately.  
  • **FOK (Fill or Kill)** — the order must be filled entirely at once; otherwise, it is completely canceled.  
* **Determine Trading Operation Code** —  
  • **Manual** — select this if you want to specify the currency used to purchase the payout currency yourself. This option is only available if a currency code is provided in the "**Trading Operation Code (if Manual)**" field.  
  • **Automatic** — the currency is selected automatically from your wallet balance to purchase the payout currency (based on available reserves in the wallet).  
* **Trading Operation Code (if Manual)** — choose the currency code from the dropdown list that will be used to purchase the payout currency (usually USDT). This option is only available if "**Manual**" is selected for "**Determine Trading Operation Code**".

## Continuing Setup

Next, proceed with configuring the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-merchantov-avtovyplat).

---

If you need it adapted for a specific audience or style, just let me know!