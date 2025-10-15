# Heleket

{% hint style="info" %}
If you need to update a module on the server, please refer to the [instructions](https://premium.gitbook.io/main/en/en/basic-settings/faq/updating-script-files-on-the-server/how-to-update-files-on-the-server#merchant-and-auto-payout-modules).
{% endhint %}

{% hint style="danger" %}
Starting June 23, 2025, an additional fee of 1 TRX will be charged for the first payment to each new static address (the "**Address**" field in the merchant module settings) on the USDT TRC20 network.

This change does not affect static addresses in other currencies and networks (such as USDT BEP20 and others) or temporary addresses (the "**Invoice**" field).

<img src="../../../.gitbook/assets/image%20(14)_eng.png" alt="" data-size="original">
{% endhint %}

## Merchant Account Settings

Register or log in to the [Heleket](https://dash.heleket.com/signup) system.

{% hint style="warning" %}
To connect to the service and receive a special rate for the exchange service, please contact a [Heleket service representative](https://t.me/business_Heleket) on Telegram and mention that you were referred by Premium Exchanger.

**Disclaimer**: When connecting your website to any service, please assess the potential risks of collaboration on your own.
{% endhint %}

Go to the "**Merchants**" section.

<figure><img src="../../../.gitbook/assets/image (2082)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

Click the "**Create merchant**" button.

<figure><img src="../../../.gitbook/assets/image (2075)_eng.png" alt=""><figcaption></figcaption></figure>

In the window that opens, enter the name of your project and click "**Create merchant**."

<figure><img src="../../../.gitbook/assets/image (2074)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

After successfully adding the merchant, proceed to configure it.

<figure><img src="../../../.gitbook/assets/image (2076)_eng.png" alt="" width="375"><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (2077)_eng.png" alt=""><figcaption></figcaption></figure>

Send a request to gain API access for your website.

<figure><img src="../../../.gitbook.assets/image%20(2078)_eng.png" alt=""><figcaption></figcaption></figure>

In the "**Merchant ID**" field, you will find your merchant ID; save it in a text file.

<figure><img src="../../../.gitbook/assets/image (2081)_eng.png" alt="" width="414"><figcaption></figcaption></figure>

Enter your domain and website name.

<figure><img src="../../../.gitbook/assets/image (2079)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

Verify ownership of the domain using one of the three methods (the quickest option is to place an HTML file in the root folder of your website).

<figure><img src="../../../.gitbook/assets/image (2080)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

Wait for the moderation of your project to be completed.

On the "**API Integration**" tab in the merchant settings, you will see the merchant ID as well as the keys for receiving and sending funds.

<figure><img src="../../../.gitbook/assets/image (2083)_eng.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (2087)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

If necessary, regenerate the key and save all data in a text file.

## Module Settings

In the admin panel, go to "**Merchants**" -> "**Merchants**," click the "**Add**" button, and select Heleket.

<figure><img src="../../../.gitbook/assets/image (2071)_eng.png" alt="" width="443"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (1140)_eng.png" alt="" width="460"><figcaption></figcaption></figure>

**Merchant ID** — **Merchant ID** from your Heleket account

**Api key** — **Payment API key** generated in your Heleket account

## Special Fields

<figure><img src="../../../.gitbook/assets/image (1441)_eng.png" alt="" width="329"><figcaption></figcaption></figure>

**Type** — the type of wallet that will be issued in the request (a new wallet for each request)\
• **Invoice** — a temporary wallet address created for a specific transaction, which has a limited lifespan after being issued in the request (receiving funds to this wallet is **time-limited** — 12 hours from the moment of issuance in the request)\
&#xNAN;_&#x46;or this type of wallet, a cron job must be created on the server._\
• **Address** — a permanent wallet address linked to your account with the merchant, with no lifespan limitation (receiving funds to this wallet is **not time-limited**)\
&#xNAN;_&#x50;ayment status is checked via callback; a cron job is not required for this type of wallet._

{% hint style="warning" %}
When using invoices, we recommend mentioning this in the request text so that the client does not send funds to the wallet after the invoice has expired.
{% endhint %}

**Currency Code** — specify the code of the currency being accepted according to the merchant's requirements.

**Network** — specify the network of the accepted currency according to the merchant's requirements.

{% hint style="info" %}
**Useful Links:**

Merchant fees (information available only to authorized users) — [dash.heleket.com/ru/business/merchant/{your\_merchant\_id}/commissions](https://dash.heleket.com/ru/business/merchant/ccc8c2c5-0966-40ed-b35d-40554d0d0791/commissions)\
![](../../../.gitbook/assets/image%20\(15\)_eng.png)

List of available currencies and networks — [doc.heleket.com/ru/other/reference](https://doc.heleket.com/ru/other/reference)
{% endhint %}

{% hint style="warning" %}
You can convert the currency received from the client into USDT at the market rate — to do this, enable the option for suitable currencies in the merchant settings:

![](<../../../.gitbook/assets/image (2085)_eng.png>)\\

List of currencies for which auto-conversion can be enabled:

<img src="../../../.gitbook/assets/image (2086)_eng.png" alt="" data-size="original">
{% endhint %}

## Continuing Configuration

Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/main/en/en/basic-settings/merchants-and-auto-payments/merchants/general-merchant-settings).
