# Bankoro

{% hint style="info" %}
If you need to update a module on the server, please refer to the [instructions](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat).
{% endhint %}

## Settings in the Merchant's Personal Account

{% hint style="warning" %}
To discuss the terms of service, please contact a [service representative](https://t.me/bankoro_crypto).

**Disclaimer**: When connecting your website to any service, please assess the potential risks of collaboration on your own.
{% endhint %}

[Register on the Bankoro service](https://bankoro.io/registration), log into your personal account, go to the "**API Connection**" section, and add a new pair of API keys.

<figure><img src="../../../.gitbook/assets/image (3) (1).png" alt=""><figcaption></figcaption></figure>

Fill in the fields as you see fit (just make sure to provide access for receiving funds and/or making payouts) and generate the API keys by clicking the "**Create**" button. Copy both keys to your clipboard or a text file.

<figure><img src="../../../.gitbook/assets/image (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

## Module Settings

In the admin panel, create a new merchant in the "**Merchants**" ➔ "**Add Merchant**" section.

Select Bankoro from the dropdown menu in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (3) (1) (1).png" alt=""><figcaption></figcaption></figure>

Fill in the specified authorization fields.

<figure><img src="../../../.gitbook/assets/image (2) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

**Domain** — leave this field empty.

**API Key** — the public key you copied earlier from your Bankoro account.

**Secret Key** — the secret key you copied earlier from your Bankoro account.

## Special Fields

<figure><img src="../../../.gitbook/assets/image (2221).png" alt=""><figcaption></figcaption></figure>

**Payment Method** — select the currency for issuing the wallet address (if you choose "**Automatically**," the currency code for "**Giving**" will be used).

* **Add** — add your own currency code.

## Continuing the Setup

Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).