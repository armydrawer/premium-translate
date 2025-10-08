# Diffpay

{% hint style="info" %}
If you need to update the module on the server, please refer to the [instructions](https://premium.gitbook.io/main/en/basic-settings/faq/updating-script-files-on-the-server/how-to-update-files-on-the-server#merchant-and-auto-payout-modules).
{% endhint %}

## Settings in the Merchant's Personal Account

{% hint style="warning" %}
To discuss terms and connection, please contact a [service representative](https://t.me/diffpay).

**Disclaimer**: When connecting your website to any service, please assess the potential risks of collaboration on your own.
{% endhint %}

Register and log in to the [Diffpay](https://diffpay.pro/login) service.

Go to the "**Profile**" section and copy the generated API key to your clipboard or a text file.

<figure><img src="../../../.gitbook/assets/image (1857)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

## Module Settings

In the admin panel, create a new merchant in the "**Merchants**" -> "**Add Merchant**" section.

Select Diffpay from the dropdown menu in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (1856)_eng.png" alt="" width="374"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (1897)_eng.png" alt="" width="455"><figcaption></figcaption></figure>

**Domain** — the merchant's domain (enter [https://diffpay.pro](https://diffpay.pro) in this field)

**API Key** — the **API Key** from your Diffpay account

## Special Fields

<figure><img src="../../../.gitbook/assets/image (1854)_eng.png" alt="" width="353"><figcaption></figcaption></figure>

**Payment Method** — select the required method for receiving funds (the list of methods will only appear after entering the correct API key for module authorization)

{% hint style="warning" %}
For each payment method used, you need to create a separate copy of the merchant module, select the corresponding method, and then connect this copy in the "**Merchants and Payments**" tab in the exchange direction settings, where the currency in "**I Give**" will be the appropriate currency.
{% endhint %}

## Continuing the Setup

Next, proceed to configure the merchant by following the [general setup instructions](https://premium.gitbook.io/main/en/basic-settings/merchants-and-auto-payments/merchants/general-merchant-settings).