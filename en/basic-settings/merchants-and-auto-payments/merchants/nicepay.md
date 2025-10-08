# Nicepay

{% hint style="info" %}
If you need to update the module on the server, please refer to the [instructions](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat).
{% endhint %}

## Settings in the Merchant's Personal Account

{% hint style="warning" %}
To discuss terms and connection, please contact a [service representative](https://t.me/nice_sup).

**Disclaimer**: When connecting your website to any service, please assess the potential risks of collaboration on your own.
{% endhint %}

{% hint style="success" %}
You can use the exchange rates from Nicepay for currency conversion. To do this, go to the "**Parsers 2.0**" ➔ "**Settings**" section and select the source (check the box next to it).

![](<../../../.gitbook/assets/image (23)_eng.png>)

Then, create the necessary exchange rates by following the [instructions](https://premium.gitbook.io/main/osnovnye-nastroiki/valyuty-i-napravleniya-obmena/kursy-valyut/parser-kursov-valyut-parsery-2.0).

Available currency exchange rates:

* USDT ➔ USD
* USDT ➔ RUB (and vice versa)
* USDT ➔ EUR
* USDT ➔ KZT (and vice versa)
* USDT ➔ UAH (and vice versa)
* USDT ➔ TJS

Select the desired exchange rate in the "**Auto-Adjust Rate**" tab.

![](<../../../.gitbook/assets/image (26)_eng.png>)
{% endhint %}

Register on the Nicepay service with the help of a [service representative](https://t.me/nice_sup) and log in to your [personal account](https://nicepay.io/ru/app).

<figure><img src="../../../.gitbook/assets/image (41)_eng.png" alt="" width="506"><figcaption></figcaption></figure>

In the merchant's personal account, create a new project in the "**Payment Solutions**" section.

<figure><img src="../../../.gitbook/assets/image (36)_eng.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (37)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (38)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

Go to the settings of the created project.

<figure><img src="../../../.gitbook/assets/image (40)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

Copy the Merchant ID and Secret Key to your clipboard or a text file.

<figure><img src="../../../.gitbook/assets/image (39)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

## Module Settings

In the admin panel, create a new merchant in the "**Merchants**" -> "**Add Merchant**" section.

Select Nicepay from the dropdown list in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (35)_eng.png" alt="" width="379"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (34)_eng.png" alt="" width="423"><figcaption></figcaption></figure>

**Domain** — leave this field empty.

**Merchant ID** — the Merchant ID you copied earlier from the merchant's personal account.

**Secret Key** — the Secret Key you copied earlier from the merchant's personal account.

## Special Fields

**Merchant Type** — choose the merchant format.

<figure><img src="../../../.gitbook/assets/image (2131)_eng.png" alt=""><figcaption></figcaption></figure>

* **Payment Link** — the details will be displayed on a separate payment page.
* **Requisites** — the details will be displayed in the application itself via the shortcode \[to\_account].

{% hint style="warning" %}
Please note that the selected method is fixed in the module after the first application is created through it. If you need to use a different method, create a separate copy of the module.
{% endhint %}

**Payment Method** — select the necessary method for receiving funds.

<figure><img src="../../../.gitbook/assets/image (30)_eng.png" alt="" width="419"><figcaption></figcaption></figure>

## Continuing the Setup

Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/main/en/basic-settings/merchants-and-auto-payments/merchants/general-merchant-settings).