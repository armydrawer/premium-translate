# Exnode

{% hint style="danger" %}
<mark style="color:red;">Before setting up automatic payouts, please read the</mark> [<mark style="color:blue;">risk warning</mark>](https://premium.gitbook.io/main/en/basic-settings/merchants-and-auto-payments/auto-payments/risk-warning)<mark style="color:blue;">!</mark>
{% endhint %}

{% hint style="info" %}
If you need to update the module on the server, please refer to the [instructions](https://premium.gitbook.io/main/en/en/basic-settings/faq/updating-script-files-on-the-server/how-to-update-files-on-the-server#merchant-and-auto-payout-modules).
{% endhint %}

{% hint style="warning" %}
Since callbacks from Exnode may be filtered by Cloudflare (if you are using it), you need to request the current IP addresses from Exnode and whitelist them according to the [instructions](https://premium.gitbook.io/main/en/basic-settings/faq/dobavlenie-ip-adresov-v-whitelist-v-cloudflare).
{% endhint %}

## Merchant Account Settings

{% hint style="warning" %}
To discuss terms and setup, please contact a [service representative](https://t.me/exnode_crypto).

**Disclaimer**: When connecting your site to any service, please assess the potential risks of collaboration on your own.
{% endhint %}

Register in the [Exnode](https://pay.exnode.ru/) system.

Log into your account, go to the "**Settings**" section, and generate your API keys.

<figure><img src="../../../.gitbook/assets/image (1373)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

After clicking the "**Change**" button, refresh the page — your [key pair](#user-content-fn-1)[^1] will be displayed in the "**API Keys**" section. Copy them using the corresponding button and save them in a text file.

<figure><img src="../../../.gitbook/assets/image (1374)_eng.png" alt="" width="319"><figcaption></figcaption></figure>

## **Module Settings**

In the admin panel, create a new merchant in the "**Automatic Payouts**" -> "**Add Automatic Payout**" section.

Select Exnode from the dropdown menu in the "**Module**" field, enter a name for the module, and click "**Save**".

<figure><img src="../../../.gitbook/assets/image (1375)_eng.png" alt=""><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (1376)_eng.png" alt=""><figcaption></figcaption></figure>

**Private Key** - the private key generated in the Exnode account when creating the API key.

**Public Key** - the public key generated in the Exnode account when creating the API key.

### Continuing the Setup

Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/main/en/basic-settings/merchants-and-auto-payments/auto-payments/obshie-nastroiki-merchantov-avtovyplat).

## Special Fields

<figure><img src="../../../.gitbook/assets/image (1378)_eng (1).png" alt=""><figcaption></figcaption></figure>

**Currency Code** — select the currency you will be paying out from the dropdown list.

{% hint style="warning" %}
For each currency, you need to create a [separate copy of the automatic payout module](#user-content-fn-2)[^2], selecting the corresponding currency, and then connect this copy in the "**Merchants and Payouts**" tab in the exchange direction settings, where the currency in "**Receiving**" will be the selected currency.

<img src="../../../.gitbook/assets/image (1380)_eng.png" alt="" data-size="original">
{% endhint %}

[^1]: public and private

[^2]: please provide a unique name for each copy in the "Title" field for easier future configuration.
