# Bankoro

{% hint style="danger" %}
<mark style="color:red;">Before setting up auto payouts, please read the</mark> [<mark style="color:blue;">risk warning!</mark>](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/preduprezhdenie-o-riskakh)
{% endhint %}

{% hint style="info" %}
If you need to update the module on the server, please refer to the [instructions](https://premium.gitbook.io/main/en/basic-settings/faq/updating-script-files-on-the-server/how-to-update-files-on-the-server#merchant-and-auto-payout-modules).
{% endhint %}

## Merchant Account Settings

{% hint style="warning" %}
To discuss working conditions, please contact a [service representative](https://t.me/bankoro_crypto).

**Disclaimer**: When connecting your website to any service, please assess the potential risks of collaboration on your own.
{% endhint %}

[Register on the Bankoro service](https://bankoro.io/registration), log into your account, go to the "**API Connection**" section, and add a new pair of API keys.

<figure><img src="../../../.gitbook/assets/image (3) (1)_eng.png" alt=""><figcaption></figcaption></figure>

Fill in the fields as you see fit (just ensure you provide access for receiving funds and/or making payouts) and generate the API keys by clicking the "**Create**" button. Copy both keys to your clipboard or a text file.

<figure><img src="../../../.gitbook/assets/image (1) (1) (1) (1) (1)_eng.png" alt=""><figcaption></figcaption></figure>

## Module Settings

In the admin panel, create a new merchant in the "**Merchants**" ➔ "**Add Auto Payout**" section.

Select Bankoro from the dropdown menu in the "**Module**" field, provide a name for the module, and click "**Save**".

<figure><img src="../../../.gitbook/assets/image (2223)_eng.png" alt=""><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (2) (1) (1) (1) (1)_eng.png" alt=""><figcaption></figcaption></figure>

**Domain** — leave this field empty.

**API Key** — the public key you copied earlier from your Bankoro account.

**Secret Key** — the secret key you copied earlier from your Bankoro account.

## Special Fields

<figure><img src="../../../.gitbook/assets/image (2221)_eng.png" alt=""><figcaption></figcaption></figure>

**Payment Method** — select the currency for auto payouts (if you choose "**Automatically**," the currency code "**Receiving**" will be used).

* **Add** — add your own currency code.

## Continuing the Setup

Next, proceed to configure the merchant by following the [general setup instructions](https://premium.gitbook.io/main/en/basic-settings/merchants-and-auto-payments/merchants/general-merchant-settings).