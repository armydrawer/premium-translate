# Optimoney

{% hint style="info" %}
If you need to update the module on the server, please refer to the [instructions](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat).
{% endhint %}

## Merchant Account Settings

{% hint style="warning" %}
To discuss the terms of service, please contact a service representative.

**Disclaimer**: When connecting your website to any service, please assess the potential risks of collaboration on your own.
{% endhint %}

Register on the [Optimoney](https://client.optimoney.com/register) service. Log in to your account and create a new USD wallet (name the wallet as you wish).

<figure><img src="../../../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

Create a new merchant in your account.

<figure><img src="../../../.gitbook/assets/image (2242).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (2241).png" alt=""><figcaption></figcaption></figure>

After verifying the domain, enter its name (as you wish) in the merchant settings and select the created wallet for receiving funds.

Provide 3 URLs for the corresponding fields (copy all URLs from the merchant module settings in the Premium Exchanger admin panel).

Copy the merchant API key from these settings.

<figure><img src="../../../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

## Module Settings

In the admin panel, create a new merchant in the "**Merchants**" ➔ "**Add Merchant**" section.

Select Optimoney from the dropdown list in the "**Module**" field, provide a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (2238).png" alt=""><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (2239).png" alt=""><figcaption></figcaption></figure>

**Domain** — leave this field empty.

**API Key** — the API key provided to you by the Optimoney representative.

**Secret Key** — the API key provided to you by the Optimoney representative.

**Merchant ID** — the ID from the "**Merchant No.**" field in the merchant account.

<figure><img src="../../../.gitbook/assets/image (2243).png" alt=""><figcaption></figcaption></figure>

**Merchant API Key** — the API key you copied earlier from the settings of the created merchant.

<figure><img src="../../../.gitbook/assets/image (2244).png" alt=""><figcaption></figcaption></figure>

## Special Fields

## Continuing the Setup

Next, proceed with the merchant setup by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).