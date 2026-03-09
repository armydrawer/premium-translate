# PayPlay

{% hint style="info" %}
If you need to update the module on the server, please refer to the [instructions](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat).
{% endhint %}

## Merchant Account Settings

{% hint style="warning" %}
To discuss working conditions, please contact a [service representative](https://t.me/am_payplay).

**Disclaimer**: When connecting your website to any service, please assess the potential risks of collaboration on your own.
{% endhint %}

Register for the PayPlay service through a service representative and log in to your merchant account.

## Module Settings

In the admin panel, create a new merchant in the "**Merchants**" section by selecting "**Add Merchant**."

Choose PayPlay from the dropdown menu in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/изображение.png" alt="" width="376"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/изображение (1).png" alt="" width="401"><figcaption></figcaption></figure>

**Domain** — leave this field empty.

**API Key** — the API key displayed in your PayPlay account settings.

<figure><img src="../../../.gitbook/assets/изображение (211).png" alt="" width="563"><figcaption></figcaption></figure>

**Slug** — the ID of the payment page, displayed in your PayPlay account.

<figure><img src="../../../.gitbook/assets/изображение (212).png" alt="" width="563"><figcaption></figcaption></figure>

**WT Token** — the token displayed in your PayPlay account after specifying the webhook URL in the merchant module settings.

{% hint style="warning" %}
Please note that for merchants using the "**Payment Link**" method, it is essential to specify the webhook URL for proper payment verification.
{% endhint %}

<figure><img src="../../../.gitbook/assets/изображение (210).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/изображение (209).png" alt="" width="563"><figcaption></figcaption></figure>

## Special Fields

<figure><img src="../../../.gitbook/assets/изображение (3) (1).png" alt=""><figcaption></figcaption></figure>

**Merchant Type** (the selected option is tied to the module copy and cannot be changed later for this copy):

* **Payment Link** — returns a payment link in the request; this option works in conjunction with the payment method selected below.
* **Requisites** — returns the card number or phone number for transferring funds in the request using the shortcode `[to_account]`.

<figure><img src="../../../.gitbook/assets/изображение (2).png" alt="" width="497"><figcaption></figcaption></figure>

**Payment Method** — select the appropriate method for receiving funds from the client.

**Additional Fields** — use the [additional currency field](https://premium.gitbook.io/main/osnovnye-nastroiki/valyuty-i-napravleniya-obmena/dopolnitelnye-polya#dopolnitelnye-polya-dlya-valyuty) from the currency "**I Give**" in the exchange direction to select requisites.

**Payment Method** — manually select the currency for requisites selection.

## Continuing the Setup

Next, proceed to configure the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).