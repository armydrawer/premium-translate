# Diffpay

{% hint style="info" %}
If you need to update the module on your server, please follow the [instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-merchantov).
{% endhint %}

## Settings in the Merchant Dashboard

{% hint style="warning" %}
To discuss terms and setup, please contact the [service representative](https://t.me/diffpay).

**Disclaimer:** When connecting your website to any service, please independently assess any potential risks involved in the partnership.
{% endhint %}

Register and log in to the [Diffpay service](https://diffpay.pro/login).

Go to the "**Profile**" section and copy the issued API key to your clipboard or save it in a text file.

<figure><img src="../../../.gitbook/assets/image (1857).png" alt="" width="563"><figcaption></figcaption></figure>

## Module Configuration

In the admin panel, create a new merchant by navigating to "**Merchants**" -> "**Add Merchant**."

Select Diffpay from the dropdown menu in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (1856).png" alt="" width="374"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (1897).png" alt="" width="455"><figcaption></figcaption></figure>

**Domain** — merchant’s domain (enter [https://diffpay.pro](https://diffpay.pro) in this field)

**API Key** — the **API Key** from your Diffpay dashboard

## Special Fields

<figure><img src="../../../.gitbook/assets/image (1854).png" alt="" width="353"><figcaption></figcaption></figure>

**Payment Method** — select the desired payment method for receiving funds (the list of methods will only appear after entering a valid API key for module authorization)

{% hint style="warning" %}
For each payment method you want to use, you need to create a separate copy of the merchant module, select the corresponding method in it, and then connect this copy on the "**Merchants and Payouts**" tab in the exchange direction settings, where the "**Give**" currency matches the appropriate currency.
{% endhint %}

## Continuing Setup

Next, continue configuring your merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).