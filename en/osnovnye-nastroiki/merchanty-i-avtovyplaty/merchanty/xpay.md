# XPay

{% hint style="info" %}
If you need to update the module on your server, please follow the [instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-merchantov).
{% endhint %}

## Settings in the Merchant Dashboard

{% hint style="warning" %}
To connect to the service, contact the [manager](https://t.me/premiumexchanger_business). They will create a chat with you and the payment service representatives to discuss connection terms, rates, and other questions.
{% endhint %}

Register and verify your account in the XPay service. Then go to the "**Merchants**" section and click the "**Create Merchant**" button.

<figure><img src="../../../.gitbook/assets/image (1826).png" alt=""><figcaption></figcaption></figure>

Save the generated key to a text file and click "**Done**."

## Module Settings

In the admin panel, create a new merchant by going to "**Merchants**" -> "**Add Merchant**."

Select **XPayPro** from the dropdown menu in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (1822).png" alt="" width="563"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (1823).png" alt="" width="421"><figcaption></figcaption></figure>

**API Key** — the key generated in your XPay dashboard

**Host** — select the domain to use with this merchant

## Special Fields

<figure><img src="../../../.gitbook/assets/image (1825).png" alt="" width="278"><figcaption></figcaption></figure>

**Payment Method** — choose the payment type for your customers: SBP (Fast Payment System) or bank card

<figure><img src="../../../.gitbook/assets/image (1824).png" alt="" width="327"><figcaption></figcaption></figure>

**Bank** — select the bank whose details will be provided to customers in payment requests

{% hint style="warning" %}
For **each payment method you use**, you need to create a separate copy of the merchant module, select the corresponding payment method in it, and then connect this copy on the "**Merchants and Payouts**" tab in the exchange direction settings, where the "**Give**" currency matches the appropriate currency.
{% endhint %}

## Continuing Setup

Next, continue configuring the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).