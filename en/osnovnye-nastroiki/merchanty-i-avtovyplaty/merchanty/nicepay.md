# Nicepay

{% hint style="info" %}
If you need to update the module on your server, please follow the [instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-merchantov).
{% endhint %}

## Merchant Account Settings

{% hint style="warning" %}
To discuss terms and set up your connection, please contact the [service representative](https://t.me/nice_sup).

**Disclaimer:** When integrating your website with any service, please independently assess any potential risks involved in the partnership.
{% endhint %}

{% hint style="success" %}
You can use exchange rates provided by Nicepay for currency conversion. To do this, go to the "**Parsers 2.0**" ➔ "**Settings**" section and select the source by checking its box,

![](<../../../.gitbook/assets/image (23).png>)

then create the required exchange rates following the [instructions](https://premium.gitbook.io/main/osnovnye-nastroiki/valyuty-i-napravleniya-obmena/kursy-valyut/parser-kursov-valyut-parsery-2.0).

Available currency pairs:

* USDT ➔ USD
* USDT ➔ RUB (and reverse)
* USDT ➔ EUR
* USDT ➔ KZT (and reverse)
* USDT ➔ UAH (and reverse)
* USDT ➔ TJS

Select the desired exchange rate under the "**Auto Rate Adjustment**" tab.

![](<../../../.gitbook/assets/image (26).png>)
{% endhint %}

Register on the Nicepay platform through the [service representative](https://t.me/nice_sup) and log in to your [merchant account](https://nicepay.io/ru/app).

<figure><img src="../../../.gitbook/assets/image (41).png" alt="" width="506"><figcaption></figcaption></figure>

In your merchant account, create a new project under the "**Payment Solutions**" section.

<figure><img src="../../../.gitbook/assets/image (36).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (37).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (38).png" alt="" width="563"><figcaption></figcaption></figure>

Go to the settings of the project you just created.

<figure><img src="../../../.gitbook/assets/image (40).png" alt="" width="563"><figcaption></figcaption></figure>

Copy the Merchant ID and Secret Key to your clipboard or save them in a text file.

<figure><img src="../../../.gitbook/assets/image (39).png" alt="" width="563"><figcaption></figcaption></figure>

## Module Configuration

In the admin panel, create a new merchant under "**Merchants**" → "**Add Merchant**."

Select Nicepay from the dropdown menu in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (35).png" alt="" width="379"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (34).png" alt="" width="423"><figcaption></figcaption></figure>

**Domain** — leave this field empty.

**Merchant ID** — the Merchant ID previously copied from the merchant’s personal account (PA)

**Secret Key** — the Secret Key previously copied from the merchant’s personal account (PA)

## Special Fields

**Merchant type** — select the merchant format

<figure><img src="../../../.gitbook/assets/image (2131).png" alt=""><figcaption></figcaption></figure>

* **Payment Link** — payment details will be displayed on a separate payment page
* **Requisites** — payment details will be shown directly within the application using the shortcode \[to_account]

{% hint style="warning" %}
Please note that the selected method is locked in the module after the first application is created using it. If you need to use a different method, create a separate copy of the module.
{% endhint %}

**Payment method** — choose the desired method for receiving funds

<figure><img src="../../../.gitbook/assets/image (30).png" alt="" width="419"><figcaption></figcaption></figure>

## Continuing Setup

Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).