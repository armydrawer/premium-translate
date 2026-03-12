# MEXC

{% hint style="danger" %}
<mark style="color:red;">Before setting up automatic payouts, please read the</mark> [<mark style="color:blue;">risk warning!</mark>](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/preduprezhdenie-o-riskakh)
{% endhint %}

{% hint style="info" %}
If you need to update the module on the server, please refer to the [instructions](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat)
{% endhint %}

## Merchant Account Settings

{% hint style="warning" %}
**Disclaimer**: When connecting your website to any service, please assess the potential risks of collaboration on your own.
{% endhint %}

[Register on the MEXC exchange](https://www.mexc.com/register), log into your account, and navigate to the "**API Management**" section.

<figure><img src="../../../.gitbook/assets/изображение (226).png" alt=""><figcaption></figcaption></figure>

Generate API keys with the permissions indicated in the screenshot.

<figure><img src="../../../.gitbook/assets/изображение (227).png" alt=""><figcaption></figcaption></figure>

Complete the security verification when generating the keys.

<figure><img src="../../../.gitbook/assets/изображение (228).png" alt=""><figcaption></figcaption></figure>

Copy the generated keys to your clipboard or save them in a text file.

<figure><img src="../../../.gitbook/assets/изображение (229).png" alt=""><figcaption></figcaption></figure>

## Module Settings

In the admin panel, create a new merchant in the "**Merchants**" ➔ "**Add Automatic Payout**" section.

Select MEXC from the dropdown menu in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/изображение (225).png" alt=""><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/изображение (224).png" alt=""><figcaption></figcaption></figure>

**Domain** — leave this field empty

**API Key** — Access Key, copied earlier from your MEXC account

**Secret Key** — Secret Key, copied earlier from your MEXC account

## Special Fields

<figure><img src="../../../.gitbook/assets/изображение (223).png" alt=""><figcaption></figcaption></figure>

**Payment Method** — select the cryptocurrency for automatic payouts

* **Add** — add your own currency code

## Continuing the Setup

Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).<br>
