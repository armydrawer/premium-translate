# XPay

{% hint style="info" %}
If you need to update the module on the server, please refer to the [instructions](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat).
{% endhint %}

## Settings in the Merchant's Personal Account

{% hint style="warning" %}
To connect to the service, please contact the [manager](https://t.me/premiumexchanger_business) — they will create a chat with you and representatives from the payment service to discuss connection terms, rates, and other questions.
{% endhint %}

Register and verify your account with Xpay. Go to the "**Merchants**" section and click the "**Create Merchant**" button.

<figure><img src="../../../.gitbook/assets/image (1826)_eng.png" alt=""><figcaption></figcaption></figure>

Save the generated key in a text file and click the "**Done**" button.

## Module Settings

In the admin panel, create a new merchant in the "**Merchants**" -> "**Add Merchant**" section.

Select XPayPro from the dropdown menu in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (1822)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (1823)_eng.png" alt="" width="421"><figcaption></figcaption></figure>

**API Key** — the key generated in your XPay personal account.

**Host** — select the domain for working with the merchant.

## Special Fields

<figure><img src="../../../.gitbook/assets/image (1825)_eng.png" alt="" width="278"><figcaption></figcaption></figure>

**Payment Method** — choose the type of payment for the customer: SBP or bank card.

<figure><img src="../../../.gitbook/assets/image (1824)_eng.png" alt="" width="327"><figcaption></figcaption></figure>

**Bank** — select the bank whose details will be provided to customers for payment requests.

{% hint style="warning" %}
For **each payment method used**, you need to create a separate copy of the merchant module, selecting the corresponding method, and then connect this copy in the "**Merchants and Payouts**" tab in the exchange direction settings, where the currency in "**I Give**" will be the appropriate currency.
{% endhint %}

## Continuing the Setup

Next, proceed to configure the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).