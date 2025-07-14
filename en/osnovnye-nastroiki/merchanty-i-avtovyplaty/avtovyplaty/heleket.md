# Heleket

{% hint style="danger" %}
<mark style="color:red;">Before setting up auto payouts, be sure to read</mark> [<mark style="color:blue;">the risk warning</mark>](https://premiumexchanger.com/wiki/preduprezhdenie-auto/)<mark style="color:blue;">!</mark>
{% endhint %}

{% hint style="info" %}
If you need to update the module on your server, please follow this [instruction](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-avtovyplat).
{% endhint %}

## Settings in the Merchant Dashboard

Register or log in to the [Heleket system](https://dash.heleket.com/signup).

{% hint style="warning" %}
To connect to the service and receive a special rate for your exchanger, contact a [Heleket service representative](https://t.me/business_Heleket) on Telegram and mention that you were referred by Premium Exchanger.

**Disclaimer:** When connecting your website to any service, please independently assess the potential risks involved in the partnership.
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

Your merchant ID will be shown in the "**Merchant ID**" field — save it to a text file.

<figure><img src="../../../.gitbook/assets/image (2081).png" alt="" width="414"><figcaption></figcaption></figure>

Enter your website’s domain and name.

<figure><img src="../../../.gitbook/assets/image (2079).png" alt="" width="563"><figcaption></figcaption></figure>

Verify domain ownership using one of the three available methods (the fastest is uploading an HTML file to your site’s root directory).

<figure><img src="../../../.gitbook/assets/image (2080).png" alt="" width="563"><figcaption></figcaption></figure>

Wait for your project to be reviewed and approved.

Go to "**Settings**" ➔ "**API**" and generate a new key for auto payouts by clicking the "**Generate**" button.

<figure><img src="../../../.gitbook/assets/image (2073).png" alt=""><figcaption></figcaption></figure>

Save the generated key to a text file.

<figure><img src="../../../.gitbook/assets/image (2072).png" alt="" width="375"><figcaption></figcaption></figure>

On the "**API Integration**" tab in the merchant settings, you will find the merchant ID as well as the keys for receiving and making payments.

<figure><img src="../../../.gitbook/assets/image (2083).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (2084).png" alt="" width="563"><figcaption></figcaption></figure>

If needed, regenerate the keys and save all the information in a text file.

{% hint style="info" %}
If you are using the merchant account only for payouts, the key for receiving funds is not required.
{% endhint %}

{% hint style="danger" %}
Please note that withdrawals will be temporarily blocked for 24 hours after creating or regenerating the payout API key.
{% endhint %}

## Module Settings

In the admin panel, go to "**Merchants**" ➔ "**Auto Payouts**", click the "**Add**" button, and select Heleket.

<figure><img src="../../../.gitbook/assets/image (2070).png" alt="" width="440"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (685).png" alt="" width="463"><figcaption></figcaption></figure>

**Merchant ID** — the Merchant ID from your Heleket personal account

**API Key** — the Payment API key generated in your Heleket personal account

**Payment API Key** — the Payout API key generated in your Heleket personal account

## Special Fields

<figure><img src="../../../.gitbook/assets/image (511).png" alt=""><figcaption></figcaption></figure>

**Priority** — select the commission level charged by the merchant (this affects transaction processing speed):  
• **recommended** — balanced speed and commission (recommended choice)  
• **economy** — slower speed with lower commission  
• **high** — faster speed with higher commission  
• **highest** — maximum speed with very high commission

**Commission** — choose the commission type from the dropdown:  
• **By amount** — commission will be deducted from the payout amount  
• **By balance** — commission will be deducted from your merchant balance upon payout

**Currency Code** — specify the code of the currency to be paid out according to the merchant’s requirements

**Network** — specify the network of the payout currency according to the merchant’s requirements

**Currency Code (Auto-Conversion)** — enables payouts in the currency with the specified code (usually USDT) without the need to hold the **payout currency** in Heleket accounts. The exchange from the **purchase currency** to the **payout currency** will be carried out at the market rate at the time of the payout request.

{% hint style="info" %}
**Useful Links:**

Merchant fees (information available only to authorized users) — [dash.heleket.com/ru/business/merchant/{your_merchant_id}/commissions](https://dash.heleket.com/ru/business/merchant/ccc8c2c5-0966-40ed-b35d-40554d0d0791/commissions)  
![](<../../../.gitbook/assets/image (15).png>)

List of available currencies and networks — [doc.heleket.com/ru/other/reference](https://doc.heleket.com/ru/other/reference)
{% endhint %}

## Continuing Setup

Next, proceed with configuring your merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-merchantov-avtovyplat).