# Luckypay

{% hint style="danger" %}
<mark style="color:red;">Before setting up automatic payouts, please read the</mark> [<mark style="color:blue;">risk warning</mark>](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/preduprezhdenie-o-riskakh)<mark style="color:blue;">!</mark>
{% endhint %}

{% hint style="info" %}
If you need to update the module on the server, please refer to the [instructions](https://premium.gitbook.io/main/en/basic-settings/faq/updating-script-files-on-the-server/how-to-update-files-on-the-server#merchant-and-auto-payout-modules).
{% endhint %}

## Merchant Account Settings <a href="#nastroiki-v-lichnom-kabinete-merchanta" id="nastroiki-v-lichnom-kabinete-merchanta"></a>

{% hint style="warning" %}
To discuss terms and connection, please contact a [service representative](https://t.me/luckypay_accounting).

**Disclaimer**: When connecting your website to any service, please assess the potential risks of collaboration on your own.
{% endhint %}

Log in to your [Merchant Account](https://merchant.luckypay.io/). In the "**API**" section, copy the API key for authorization in the automatic payout module.

<figure><img src="../../../.gitbook/assets/image (1987)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

Make sure to specify the URL from the automatic payout module settings (Callback URL) in the "**Order Status to Sell**" field.

<figure><img src="../../../.gitbook/assets/image (1986)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (18)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

## Module Settings <a href="#nastroiki-modulya" id="nastroiki-modulya"></a>

In the admin panel, create a new merchant in the "**Automatic Payouts**" -> "**Add Automatic Payout**" section.

Select Luckypay from the dropdown list in the "**Module**" field, provide a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (315)_eng.png" alt="" width="418"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/Arc_5NJ6WqIhsR_eng.png" alt="" width="435"><figcaption></figcaption></figure>

**API Key** — the key you previously copied from your Luckypay account.

## Special Fields

<div><figure><img src="../../../.gitbook/assets/image (316)_eng.png" alt="" width="217"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/image (318)_eng.png" alt="" width="215"><figcaption></figcaption></figure></div>

**Payment Method** — select the appropriate method for making payouts.

## Continuing the Setup

Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-merchantov-avtovyplat).