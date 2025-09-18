# Exnode

{% hint style="info" %}
If you need to update a module on the server, please refer to the [instructions](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat).
{% endhint %}

{% hint style="warning" %}
Since callbacks from Exnode may be filtered by Cloudflare (if you are using it), you need to request the current IP addresses from Exnode and whitelist them according to the [instructions](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/dobavlenie-ip-adresov-v-whitelist-v-cloudflare).
{% endhint %}

## Merchant Account Settings

{% hint style="warning" %}
To discuss terms and setup, please contact a [service representative](https://t.me/exnode_crypto).

**Disclaimer**: When connecting your site to any service, please assess the potential risks of collaboration on your own.
{% endhint %}

Register in the [Exnode](https://pay.exnode.ru/) system.

Log into your account, go to the "**Settings**" section, and generate your API keys.

<figure><img src="../../../.gitbook/assets/image (758).png" alt="" width="563"><figcaption></figcaption></figure>

After clicking the "**Change**" button, refresh the page — your [key pair](#user-content-fn-1)[^1] will be displayed in the "**API Keys**" section. Copy them using the corresponding button and save them in a text file.

<figure><img src="../../../.gitbook/assets/image (759).png" alt="" width="319"><figcaption></figcaption></figure>

## Module Settings

In the admin panel, create a new merchant in the "**Merchants**" -> "**Add Merchant**" section.

Select Exnode from the dropdown menu in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (760).png" alt=""><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (761).png" alt=""><figcaption></figcaption></figure>

**Private Key** - the private key generated in the Exnode account when creating the API key.

**Public Key** - the public key generated in the Exnode account when creating the API key.

## Continuing the Setup

Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).

## Special Fields

<figure><img src="../../../.gitbook/assets/image (504).png" alt=""><figcaption></figcaption></figure>

**Currency Code** — select the currency you will be accepting from the dropdown list.

<figure><img src="../../../.gitbook/assets/image (505).png" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
For each currency, you need to create a [separate copy of the merchant module](#user-content-fn-2)[^2], selecting the corresponding currency, and then connect this copy in the "**Merchants and Payments**" tab in the exchange direction settings, where the currency in "**I Give**" will be the selected currency.
![](<../../../.gitbook/assets/image (1377).png>)
{% endhint %}

{% hint style="info" %}
To perform auto payouts that require a destination tag (such as destination tag for Ripple, payment ID for Monero, message for XEM, etc.), you need to create an additional field for the corresponding currencies.

In the "**Currencies**" -> "**Additional Currency Fields**" section, create a new additional field for the currency and set the value `dest_tag` in the "**Unique ID**" field (this parameter value is the same for any cryptocurrency — Ripple, Monero, XEM, etc.). After creating the field, activate it in the currency settings (under the "**Additional Fields**" tab).

The created field will be displayed in the application creation form, where the user will need to specify the destination tag.
{% endhint %}

**Address Type** — select the appropriate address type:

* **STATIC** — creates a permanent wallet for the client.
* **SINGLE** — creates a one-time (revolving) wallet for the client.

[^1]: public and private

[^2]: specify a unique name for each copy in the "Title" field for easier subsequent configuration.