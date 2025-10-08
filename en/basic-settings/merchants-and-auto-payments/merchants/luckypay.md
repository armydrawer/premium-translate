# Luckypay

{% hint style="info" %}
If you need to update the module on the server, please refer to the [instructions](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat).
{% endhint %}

## Settings in Your Personal Account

Register for the [Luckypay](https://luckypay.io/) service. Log into your personal account, go to the "**Terminals**" section, select an existing terminal or create a new one, and copy the API key provided in its settings.

<figure><img src="../../../.gitbook/assets/image (2158)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

## Merchant Account Settings

{% hint style="warning" %}
To discuss terms and setup, please contact a [service representative](https://t.me/luckypay_accounting).

**Disclaimer**: When connecting your website to any service, please assess the potential risks of collaboration on your own.
{% endhint %}

Log into your merchant account and make sure to enter the URL from the merchant module settings (Callback URL) in the "**Order Status**" field in the "**Terminals**" section.

<figure><img src="../../../.gitbook/assets/image (2049)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (17)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

## Module Settings

In the admin panel, create a new merchant in the "**Merchants**" -> "**Add Merchant**" section.

Select Luckypay from the dropdown menu in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (319)_eng.png" alt="" width="418"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/Arc_5NJ6WqIhsR (1)_eng.png" alt="" width="435"><figcaption></figcaption></figure>

**API Key** — the key you previously copied from your Luckypay personal account.

## Special Fields

<div><figure><img src="../../../.gitbook/assets/image (316)_eng.png" alt="" width="217"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/image (318)_eng.png" alt="" width="215"><figcaption></figcaption></figure></div>

**Payment Method** — select the appropriate method for receiving funds from the customer (the options in your settings may differ from those mentioned above).

## Continuing the Setup

Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/main/en/basic-settings/merchants-and-auto-payments/merchants/general-merchant-settings).