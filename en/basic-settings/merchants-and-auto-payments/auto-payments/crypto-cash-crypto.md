# Crypto-Cash Crypto

{% hint style="danger" %}
<mark style="color:red;">Before setting up auto payouts, please read the</mark> [<mark style="color:blue;">risk warning!</mark>](https://premium.gitbook.io/main/en/basic-settings/merchants-and-auto-payments/auto-payments/risk-warning)
{% endhint %}

{% hint style="info" %}
If you need to update the module on the server, please refer to the [instructions](https://premium.gitbook.io/main/en/en/basic-settings/faq/updating-script-files-on-the-server/how-to-update-files-on-the-server#merchant-and-auto-payout-modules).
{% endhint %}

## Merchant Account Settings

{% hint style="warning" %}
To discuss the terms of service, please contact a [service representative](https://t.me/CCW_Admin).

**Disclaimer**: When connecting your website to any service, please assess the potential risks of collaboration on your own.
{% endhint %}

[Register for the Crypto-Cash service](https://account.crypto-cash.world/registration), log into your account, and navigate to the [“Merchant Settings”](https://account.crypto-cash.world/settings) section.

<figure><img src="../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1)_eng.png" alt=""><figcaption></figcaption></figure>

Generate a private API key by clicking the "**Generate API Key**" button. Copy both keys to your clipboard or a text file.

<figure><img src="../../../.gitbook/assets/image (3) (1) (1) (1)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

## Module Settings

In the admin panel, create a new merchant in the "**Merchants**" ➔ "**Add Auto Payout**" section.

Select Crypto-Cash Crypto from the dropdown menu in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (3) (1) (1) (1) (1) (1)_eng.png" alt="" width="490"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1)_eng.png" alt="" width="437"><figcaption></figcaption></figure>

**Domain** — leave this field empty.

**Public Key** — the public key you copied earlier in your account.

**Secret Key** — the secret key you copied earlier in your account.

## Special Fields

<figure><img src="../../../.gitbook/assets/image (2217)_eng.png" alt="" width="437"><figcaption></figcaption></figure>

**Currency** — select the currency for auto payouts (if you choose "**Automatically**," the currency code "**Receiving**" will be used).

* **Add** — to add your own currency code.

## Continuing the Setup

Next, proceed with the merchant setup by following the [general setup instructions](https://premium.gitbook.io/main/en/en/basic-settings/merchants-and-auto-payments/merchants/general-merchant-settings).