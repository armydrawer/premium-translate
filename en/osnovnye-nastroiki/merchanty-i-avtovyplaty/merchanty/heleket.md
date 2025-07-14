# Heleket

{% hint style="info" %}
If you need to update the module on your server, please follow the [instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-merchantov).
{% endhint %}

{% hint style="danger" %}
Starting June 23, 2025, an additional fee of 1 TRX will be charged on the first payment made to each new static address (the "**Address**" field in the merchant module settings) on the USDT TRC20 network.

This change does not affect static addresses in other currencies and networks (for example, USDT BEP20 and others) or temporary addresses (the "**Invoice**" field).

![](<../../../.gitbook/assets/image (14).png>)
{% endhint %}

## Merchant Dashboard Settings

Register or log in to the [Heleket system](https://dash.heleket.com/signup).

{% hint style="warning" %}
To connect to the service and receive a special exchanger rate, contact a [Heleket service representative](https://t.me/business_Heleket) on Telegram and mention that you were referred by Premium Exchanger.

**Disclaimer:** When integrating your website with any service, please independently assess any potential risks involved in the partnership.
{% endhint %}

Go to the "**Merchants**" section.

<figure><img src="../../../.gitbook/assets/image (2082).png" alt="" width="563"><figcaption></figcaption></figure>

Click the "**Create merchant**" button.

<figure><img src="../../../.gitbook/assets/image (2075).png" alt=""><figcaption></figcaption></figure>

In the window that appears, enter your project name and click "**Create merchant**".

<figure><img src="../../../.gitbook/assets/image (2074).png" alt="" width="563"><figcaption></figcaption></figure>

After successfully adding the merchant, proceed to configure it.

<figure><img src="../../../.gitbook/assets/image (2076).png" alt="" width="375"><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (2077).png" alt=""><figcaption></figcaption></figure>

Submit a request to obtain API access for your website.

<figure><img src="../../../.gitbook/assets/image (2078).png" alt=""><figcaption></figcaption></figure>

Your merchant’s ID will be displayed in the "**Merchant ID**" field—save it in a text file.

<figure><img src="../../../.gitbook/assets/image (2081).png" alt="" width="414"><figcaption></figcaption></figure>

Enter your website’s domain and name.

<figure><img src="../../../.gitbook/assets/image (2079).png" alt="" width="563"><figcaption></figcaption></figure>

Verify domain ownership using one of the three available methods (the fastest is uploading an HTML file to your website’s root folder).

<figure><img src="../../../.gitbook/assets/image (2080).png" alt="" width="563"><figcaption></figcaption></figure>

Wait for your project to complete the moderation process.

On the "**API Integration**" tab in the merchant settings, you will find the merchant ID as well as the keys for receiving and withdrawing funds.

<figure><img src="../../../.gitbook/assets/image (2083).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (2087).png" alt="" width="563"><figcaption></figcaption></figure>

If needed, regenerate the key and save all the information in a text file.

## Module Settings

In the admin panel, go to "**Merchants**" -> "**Merchants**", click the "**Add**" button, and select Heleket.

<figure><img src="../../../.gitbook/assets/image (2071).png" alt="" width="443"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (1140).png" alt="" width="460"><figcaption></figcaption></figure>

**Merchant ID** — the Merchant ID from your Heleket personal account

**API key** — the Payment API key generated in your Heleket personal account

## Special Fields

<figure><img src="../../../.gitbook/assets/image (1441).png" alt="" width="329"><figcaption></figcaption></figure>

**Type** — the type of wallet that will be issued in the request (a new wallet for each request)  
• **Invoice** — a temporary wallet address created for a specific transaction, with a limited lifetime after being issued in the request (receiving funds to this wallet is **time-limited** — 12 hours from the moment it is issued in the request)  
_This wallet type requires setting up a cron job on your server._  
• **Address** — a permanent wallet address linked to your merchant personal account, with no time limit (receiving funds to this wallet is **not time-limited**)  
_Payment status is checked via callback; no cron job is required for this wallet type._

{% hint style="warning" %}
When using invoices, we recommend mentioning this in the request text so that clients do not send funds to the wallet after the invoice has expired.
{% endhint %}

**Currency Code** — specify the code of the accepted currency according to the merchant’s requirements

**Network** — specify the network of the accepted currency according to the merchant’s requirements

{% hint style="info" %}
**Useful links:**

Merchant fees (information available only to authorized users) — [dash.heleket.com/ru/business/merchant/{your_merchant_id}/commissions](https://dash.heleket.com/ru/business/merchant/ccc8c2c5-0966-40ed-b35d-40554d0d0791/commissions)  
![](<../../../.gitbook/assets/image (15).png>)

List of supported currencies and networks — [doc.heleket.com/ru/other/reference](https://doc.heleket.com/ru/other/reference)
{% endhint %}

{% hint style="warning" %}
You can convert the currency received from your client into USDT at the market rate — to do this, enable the option for the applicable currencies in the merchant settings:

![](<../../../.gitbook/assets/image (2085).png>)\

Here is the list of currencies for which auto-conversion can be enabled:

![](<../../../.gitbook/assets/image (2086).png>)
{% endhint %}

## Continuing the Setup

Next, configure your merchant account by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).