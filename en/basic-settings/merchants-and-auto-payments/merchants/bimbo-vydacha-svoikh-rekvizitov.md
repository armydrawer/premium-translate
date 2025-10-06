# BimBo (Issuing Your Payment Details)

{% hint style="info" %}
If you need to update the module on the server, please refer to the [instructions](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat).
{% endhint %}

## Module Settings

In the admin panel, create a new merchant in the "**Merchants**" section by selecting "**Add Merchant**."

Choose either "**BimBo Link**" or "**BimBo Invoice**" from the dropdown menu in the "**Module**" field, provide a name for the module, and click "**Save**."

* **BimBo Link** — generates a link that the client will use to make a payment.
* **BimBo Invoice** — provides payment details directly in the application.

<figure><img src="../../../.gitbook/assets/image (2110)_eng.png" alt="" width="501"><figcaption></figcaption></figure>

## Special Fields

{% tabs %}
{% tab title="BimBo Invoice" %}
<figure><img src="../../../.gitbook/assets/image (2111)_eng.png" alt=""><figcaption></figcaption></figure>

**Invoice Number** — enter the payment details that will be provided in the application for receiving funds from the client (these details will always be issued in the application when using this merchant).
{% endtab %}

{% tab title="BimBo Link" %}
<figure><img src="../../../.gitbook/assets/image (2112)_eng.png" alt=""><figcaption></figcaption></figure>

**Link** — specify the URL of the page where the client should make the payment or view the payment details.

**Error Message for Link** — the text that will be displayed in the application instead of the link when it is not provided.
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
For each invoice/link, you need to create a separate copy of the merchant module, specifying the invoice/link, and then connect this copy in the "**Merchants and Payments**" tab in the exchange direction settings, where the currency in "**I Give**" will match the appropriate currency.
{% endhint %}

## Continuing the Setup

Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).