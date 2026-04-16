# PayPlay

{% hint style="info" %}
If you need to update the module on the server, please refer to the [instructions](https://premium.gitbook.io/main/en/basic-settings/faq/updating-script-files-on-the-server/how-to-update-files-on-the-server#merchant-and-auto-payout-modules).
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

<figure><img src="../../../.gitbook/assets/изображение (4) (1) (1).png" alt="" width="359"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/изображение (1) (1) (1) (1).png" alt="" width="415"><figcaption></figcaption></figure>

**Domain** — leave this field empty.

**API Key** — the API key displayed in your PayPlay account settings.

<figure><img src="../../../.gitbook/assets/изображение (2) (1) (1) (1).png" alt="" width="560"><figcaption></figcaption></figure>

**Slug** — the ID of the payment page, displayed in your PayPlay account.

<figure><img src="../../../.gitbook/assets/изображение (3) (1) (1) (1).png" alt="" width="500"><figcaption></figcaption></figure>

**WT Token** — token displayed in the PayPlay personal account after specifying the webhook link from the merchant module settings ("**Payment pages**" section).

{% hint style="warning" %}
Please note that for merchants using the "**Payment Link**" method, it is essential to specify the webhook URL for proper payment verification.
{% endhint %}

<figure><img src="../../../.gitbook/assets/изображение (5).png" alt=""><figcaption><p>Module settings in the Premium Exchanger admin panel</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/изображение (236).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/изображение (237).png" alt=""><figcaption></figcaption></figure>

After saving the webhook, be sure to select the methods to work with it and save the changes.

<figure><img src="../../../.gitbook/assets/изображение (234).png" alt=""><figcaption></figcaption></figure>

## Special Fields

<figure><img src="../../../.gitbook/assets/изображение (7).png" alt=""><figcaption></figcaption></figure>

**Merchant Type** (the selected option is tied to the module copy and cannot be changed later for this copy):

* **Payment Link** — returns a payment link in the request; this option works in conjunction with the payment method selected below.
* **Requisites** — returns the card number or phone number for transferring funds in the request using the shortcode `[to_account]`.

<figure><img src="../../../.gitbook/assets/изображение (8).png" alt="" width="510"><figcaption></figcaption></figure>

**Payment Method** — select the appropriate method for receiving funds from the client.

**Custom Fields** — use the [custom currency field](https://premium.gitbook.io/main/osnovnye-nastroiki/valyuty-i-napravleniya-obmena/dopolnitelnye-polya#dopolnitelnye-polya-dlya-valyuty) from the currency "**I Give**" in the exchange direction to select requisites.

**Payment Method** — manually select the currency for requisites selection.

## Continuing the Setup

Next, proceed to configure the merchant by following the [general setup instructions](https://premium.gitbook.io/main/en/basic-settings/merchants-and-auto-payments/merchants/general-merchant-settings).
