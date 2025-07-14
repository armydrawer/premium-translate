# Exnode

{% hint style="info" %}
If you need to update the module on your server, please follow the [instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-merchantov).
{% endhint %}

{% hint style="warning" %}
Since callbacks from Exnode may be filtered by Cloudflare (if you are using it), you need to request the current IP addresses from Exnode and add them to your whitelist following this [guide](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/dobavlenie-ip-adresov-v-whitelist-v-cloudflare).
{% endhint %}

## Settings in the Merchant Dashboard

{% hint style="warning" %}
To discuss terms and set up the connection, please contact the [service representative](https://t.me/exnode_crypto).

**Disclaimer:** When connecting your website to any service, please independently assess any potential risks involved in the partnership.
{% endhint %}

Register an account with [Exnode](https://pay.exnode.ru/).

Log in to your dashboard, go to the "**Settings**" section, and generate your API keys.

<figure><img src="../../../.gitbook/assets/image (758).png" alt="" width="563"><figcaption></figcaption></figure>

After clicking the "**Regenerate**" button, refresh the page — your [key pair](#user-content-fn-1)[^1] will appear under the "**API Keys**" section. Copy them using the corresponding button and save them in a text file.

<figure><img src="../../../.gitbook/assets/image (759).png" alt="" width="319"><figcaption></figcaption></figure>

## Module Configuration

In the admin panel, create a new merchant by navigating to "**Merchants**" -> "**Add Merchant**."

Select Exnode from the dropdown menu in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (760).png" alt=""><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (761).png" alt=""><figcaption></figcaption></figure>

- **Private Key** — the private key generated in your Exnode dashboard when creating the API key
- **Public Key** — the public key generated in your Exnode dashboard when creating the API key

## Continuing Setup

Next, complete the merchant setup by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).

## Special Fields

<figure><img src="../../../.gitbook/assets/image (504).png" alt=""><figcaption></figcaption></figure>

**Currency Code** — select from the dropdown the currency you expect to receive payments in

<figure><img src="../../../.gitbook/assets/image (505).png" alt=""><figcaption></figcaption></figure>

[^1]: The API key pair consists of a public and a private key used for authenticating requests.

{% hint style="warning" %}
For each currency, you need to create a [separate copy of the merchant module](#user-content-fn-2)[^2], select the corresponding currency in it, and then connect this copy on the "**Merchants and Payouts**" tab in the exchange direction settings, where the "**Give**" currency will be the selected currency.\
![](<../../../.gitbook/assets/image (1377).png>)
{% endhint %}

{% hint style="info" %}
To enable automatic payouts that require passing a destination tag (such as destination tag for Ripple, payment ID for Monero, message for XEM, etc.), you need to create an additional field for the relevant currencies.

Go to "**Currencies**" -> **"Additional Currency Fields"**, create a new additional field for the currency, and set the "**Unique ID**" field to `dest_tag` (this value is the same for all cryptocurrencies like Ripple, Monero, XEM, etc.). After creating the field, activate it in the currency settings (under the "**Additional Fields**" tab).

This field will appear on the order creation form, where the user will be required to enter the destination tag.
{% endhint %}

**Address Type** — select the appropriate address type:

* **STATIC** — creates a permanent wallet for the client
* **SINGLE** — creates a one-time (revolving) wallet for the client

[^1]: public and private

[^2]: assign a unique name to each copy in the "Title" field for easier configuration later