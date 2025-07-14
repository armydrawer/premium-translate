# Luckypay

{% hint style="danger" %}
<mark style="color:red;">Before setting up auto payouts, be sure to read</mark> [<mark style="color:blue;">the risk warning</mark>](https://premiumexchanger.com/wiki/preduprezhdenie-auto/)<mark style="color:blue;">!</mark>
{% endhint %}

{% hint style="info" %}
If you need to update the module on your server, please follow this [instruction](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-avtovyplat).
{% endhint %}

## Merchant Account Settings <a href="#merchant-account-settings" id="merchant-account-settings"></a>

{% hint style="warning" %}
To discuss terms and get connected, please contact the [service representative](https://t.me/luckypay_accounting).

**Disclaimer:** When integrating your website with any service, please independently assess the potential risks involved in the partnership.
{% endhint %}

Log in to your [Merchant Account](https://merchant.luckypay.io/). In the "**API**" section, copy the API key to use for authorization in the auto payout module.

<figure><img src="../../../.gitbook/assets/image (1987).png" alt="" width="563"><figcaption></figcaption></figure>

Also, be sure to enter the Callback URL from the auto payout module settings into the "**Order Status Sell**" field.

<figure><img src="../../../.gitbook/assets/image (1986).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (18).png" alt="" width="563"><figcaption></figcaption></figure>

## Module Settings <a href="#module-settings" id="module-settings"></a>

In the admin panel, create a new merchant under "**Auto Payouts**" -> "**Add Auto Payout**."

Select Luckypay from the dropdown menu in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (315).png" alt="" width="418"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/Arc_5NJ6WqIhsR.png" alt="" width="435"><figcaption></figcaption></figure>

**API Key** — the key you copied earlier from your Luckypay merchant account.

## Special Fields

<div><figure><img src="../../../.gitbook/assets/image (316).png" alt="" width="217"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/image (318).png" alt="" width="215"><figcaption></figcaption></figure></div>

**Payment Method** — select the desired payment method for disbursing funds.

## Continuing Setup

Next, complete the merchant setup by following the [general setup guide](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-merchantov-avtovyplat).