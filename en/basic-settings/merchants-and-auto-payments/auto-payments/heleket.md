# Heleket

{% hint style="danger" %}
<mark style="color:red;">Before setting up auto payouts, please read the</mark> [<mark style="color:blue;">risk warning</mark>](https://premium.gitbook.io/main/en/basic-settings/merchants-and-auto-payments/auto-payments/risk-warning)<mark style="color:blue;">!</mark>
{% endhint %}

{% hint style="info" %}
If you need to update the module on the server, please refer to the [instructions](https://premium.gitbook.io/main/en/en/basic-settings/faq/updating-script-files-on-the-server/how-to-update-files-on-the-server#merchant-and-auto-payout-modules).
{% endhint %}

## Merchant Account Settings

Register or log in to the [Heleket](https://dash.heleket.com/signup) system.

{% hint style="warning" %}
To connect to the service and receive a special rate for the exchange, please contact a [Heleket service representative](https://t.me/business_Heleket) on Telegram and mention that you were referred by Premium Exchanger.

**Disclaimer**: When connecting your website to any service, please assess the potential risks of collaboration on your own.
{% endhint %}

Go to the "**Merchants**" section.

<figure><img src="../../../../ru/.gitbook/assets/image (688) (1).png" alt="" width="563"><figcaption></figcaption></figure>

Click the "**Create merchant**" button.

<figure><img src="../../../../ru/.gitbook/assets/image (681) (1).png" alt=""><figcaption></figcaption></figure>

In the window that opens, enter the name of your project and click "**Create merchant**."

<figure><img src="../../../../ru/.gitbook/assets/image (680) (1).png" alt="" width="563"><figcaption></figcaption></figure>

After successfully adding the merchant, proceed to its settings.

<figure><img src="../../../../ru/.gitbook/assets/image (682) (1).png" alt="" width="375"><figcaption></figcaption></figure>

<figure><img src="../../../../ru/.gitbook/assets/image (683) (1).png" alt=""><figcaption></figcaption></figure>

Send a request to gain access to the API for your website.

<figure><img src="../../../../ru/.gitbook/assets/image (684) (1).png" alt=""><figcaption></figcaption></figure>

In the "**Merchant ID**" field, you will find your merchant's ID; save it in a text file.

<figure><img src="../../../../ru/.gitbook/assets/image (687) (1).png" alt="" width="414"><figcaption></figcaption></figure>

Enter your domain and website name.

<figure><img src="../../../../ru/.gitbook/assets/image (685) (1).png" alt="" width="563"><figcaption></figcaption></figure>

Confirm ownership of the domain using any of the three methods (the quickest option is to place an HTML file in the root folder of your website).

<figure><img src="../../../../ru/.gitbook/assets/image (686) (1).png" alt="" width="563"><figcaption></figcaption></figure>

Wait for your project to be moderated.

Go to the "**Settings**" ➔ "**API**" section and generate a new key for auto payouts by clicking the "**Generate**" button.

<figure><img src="../../../../ru/.gitbook/assets/image (679) (1).png" alt=""><figcaption></figcaption></figure>

Save the generated key in a text file.

<figure><img src="../../../../ru/.gitbook/assets/image (678) (1).png" alt="" width="375"><figcaption></figcaption></figure>

On the "**API Integration**" tab in the merchant settings, you will see the merchant ID as well as the keys for receiving and making payments.

<figure><img src="../../../../ru/.gitbook/assets/image (689) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../ru/.gitbook/assets/image (690) (1).png" alt="" width="563"><figcaption></figcaption></figure>

If necessary, regenerate the keys and save all data in a text file.

{% hint style="info" %}
If you are using the merchant only for making payments, the key for receiving funds is not required.
{% endhint %}

{% hint style="danger" %}
Please note that withdrawals will be temporarily blocked (for 24 hours) after creating or regenerating the API key for payouts (Payout API key).
{% endhint %}

## Module Settings

In the admin panel, go to the "**Merchants**" ➔ "**Auto Payouts**" section, click the "**Add**" button, and select Heleket.

<figure><img src="../../../.gitbook/assets/image (2070)_eng.png" alt="" width="440"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../../ru/.gitbook/assets/image (685) (1).png" alt="" width="463"><figcaption></figcaption></figure>

**Merchant ID** — **Merchant ID** from your Heleket account

**API key** — **Payment API key**, generated in your Heleket account

**Payment API key** — **Payout API key**, generated in your Heleket account

## Special Fields

<figure><img src="../../../.gitbook/assets/image%20(511)_eng.png" alt=""><figcaption></figcaption></figure>

**Priority** — choose the fee size that will be charged by the merchant (this affects transaction processing speed):\
• **recommended** — balanced speed and fee (recommended choice)\
• **economy** — low speed and low fee\
• **high** — high speed and high fee\
• **highest** — maximum speed and very high fee

**Fee** — select the type of fee from the dropdown:\
• **By amount** — the fee will be deducted from the payout request\
• **By balance** — the fee will be deducted from your balance with the merchant upon payout

**Currency code** — specify the code of the currency being paid out according to the merchant's requirements

**Network** — specify the network of the currency being paid out according to the merchant's requirements

**Currency code (auto-conversion)** — activate payouts from a currency with the specified code (usually USDT), without the need to hold the **payout currency** in Heleket accounts (the conversion from **currency for purchase** to **currency for payout** will occur at the exchange rate at the time of the payout request)

{% hint style="info" %}
**Useful links:**

Merchant fees (information available only to authorized users) — [dash.heleket.com/ru/business/merchant/{your\_merchant\_id}/commissions](https://dash.heleket.com/ru/business/merchant/ccc8c2c5-0966-40ed-b35d-40554d0d0791/commissions)\
![](<../../../../ru/.gitbook/assets/image (15) (1).png>)

List of available currencies and networks — [doc.heleket.com/ru/other/reference](https://doc.heleket.com/ru/other/reference)
{% endhint %}

## Continuing Setup

Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/main/en/basic-settings/merchants-and-auto-payments/auto-payments/obshie-nastroiki-merchantov-avtovyplat).
