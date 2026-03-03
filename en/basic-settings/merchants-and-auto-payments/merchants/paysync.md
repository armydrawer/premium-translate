# PaySync

{% hint style="info" %}
If you need to update the module on the server, please refer to the [instructions](https://premium.gitbook.io/main/en/basic-settings/faq/updating-script-files-on-the-server/how-to-update-files-on-the-server#merchant-and-auto-payout-modules).
{% endhint %}

## Merchant Account Settings

{% hint style="warning" %}
To discuss working conditions, please contact a [service representative](https://t.me/psync).

**Disclaimer**: When connecting your website to any service, please assess the potential risks of collaboration on your own.
{% endhint %}

{% hint style="info" %}
Please note that when using the PaySync module for receiving funds, the amount in the request is rounded to 0 decimal places (in the "Payment Instructions for the User," the amount is formatted according to the merchant's requirements).
{% endhint %}

Register for the PaySync service through a service representative and log in to your merchant account.

## Module Settings

In the admin panel, create a new merchant in the "**Merchants**" section ➔ "**Add Merchant**."

Select PaySync from the dropdown menu in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/изображение (215).png" alt="" width="359"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/изображение (218).png" alt="" width="400"><figcaption></figcaption></figure>

**Domain** — leave this field empty.

**API Key** — the API key copied from your PaySync account.

<figure><img src="../../../.gitbook/assets/изображение (214).png" alt=""><figcaption></figcaption></figure>

**Client ID** — the ID copied from your PaySync account.

<figure><img src="../../../.gitbook/assets/изображение (213).png" alt="" width="217"><figcaption></figcaption></figure>

## Special Fields

<figure><img src="../../../.gitbook/assets/изображение (217).png" alt="" width="289"><figcaption></figcaption></figure>

**Merchant Type** (the selected option is fixed for this module copy and cannot be changed later):

* **Payment Link** — returns a link for payment via QR code in the request; this option works with the selected payment method.
* **Requisites** — returns a card or phone number for transferring funds in the request using the shortcode \[to\_account].

<figure><img src="../../../.gitbook/assets/изображение (220).png" alt="" width="563"><figcaption></figcaption></figure>

**Payment Method** — select the appropriate method for receiving funds from the client:

{% hint style="info" %}
All methods can be used for obtaining requisites and for links, except SBPQR, which is only for obtaining links.
{% endhint %}

Order — use the currency code from the exchange direction to select requisites (choose **\[Send] Currency code**).

**Custom Fields** — use the [additional currency field](https://premium.gitbook.io/main/osnovnye-nastroiki/valyuty-i-napravleniya-obmena/dopolnitelnye-polya#dopolnitelnye-polya-dlya-valyuty) "**Send**" to select requisites.

**Payment Method** — manually select the currency for requisites selection.

To update the statuses of requests based on payments made through the merchant, specify the webhook link in your PaySync account, taken from the merchant module settings.

<figure><img src="../../../.gitbook/assets/изображение (222).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/изображение (221).png" alt=""><figcaption></figcaption></figure>

## Continuing the Setup

Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).
