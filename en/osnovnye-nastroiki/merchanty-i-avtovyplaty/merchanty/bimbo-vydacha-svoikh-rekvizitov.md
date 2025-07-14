# BimBo (Providing Your Payment Details)

{% hint style="info" %}
If you need to update the module on your server, please follow the [instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-merchantov).
{% endhint %}

## Module Setup

In the admin panel, create a new merchant by going to "**Merchants**" -> "**Add Merchant**."

Select "**BimBo Link**" or "**BimBo Invoice**" from the "**Module**" dropdown menu, enter a name for the module, and click "**Save**."

* **BimBo Link** — generates a link that the client will follow
* **BimBo Invoice** — provides payment details directly within the order

<figure><img src="../../../.gitbook/assets/image (2110).png" alt="" width="501"><figcaption></figcaption></figure>

## Special Fields

{% tabs %}
{% tab title="BimBo Invoice" %}
<figure><img src="../../../.gitbook/assets/image (2111).png" alt=""><figcaption></figcaption></figure>

**Invoice Number** — enter the payment details that will be shown in the order for receiving funds from the client (these details will always be included in orders using this merchant)
{% endtab %}

{% tab title="BimBo Link" %}
<figure><img src="../../../.gitbook/assets/image (2112).png" alt=""><figcaption></figcaption></figure>

**Link** — specify the URL where the client should make the payment or view the payment details

**Link Error Text** — the message that will be displayed in the order instead of the link if no link is provided
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
You need to create a separate copy of the merchant module for each invoice or link, specifying the corresponding invoice or link. Then, connect this copy on the "**Merchants and Payouts**" tab in the exchange direction settings, where the "**Give**" currency matches the appropriate currency.
{% endhint %}

## Continuing Setup

Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).