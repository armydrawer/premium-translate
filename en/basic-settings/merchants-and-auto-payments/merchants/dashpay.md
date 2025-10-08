# DashPay

{% hint style="info" %}
If you need to update the module on the server, please refer to the [instructions](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat).
{% endhint %}

{% hint style="warning" %}
For discussions regarding terms and connection, please contact a [service representative](https://t.me/adamdashpay).

**Disclaimer**: When connecting your website to any service, please assess the potential risks of collaboration on your own.
{% endhint %}

## Settings in the Merchant's Personal Account

Register on the [DashPay](https://dashpayment.pro/) service. Log in to your personal account, go to the "**Profile**" ➔ "**Merchants**" section, and create a new merchant.

<figure><img src="../../../.gitbook/assets/image (131)_eng.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Make sure to copy the links for all fields labeled "**Redirect URL**" later in the settings of the created merchant module and enter them in the corresponding fields (pay attention to the end of the link!). Save these settings.
<img src="../../../.gitbook/assets/image (140)_eng.png" alt="" data-size="original">
![](<../../../.gitbook/assets/image (141)_eng.png>)
{% endhint %}

Copy the "**Basic Token**" for the created merchant to your clipboard or a text file.

<figure><img src="../../../.gitbook/assets/image (138)_eng.png" alt=""><figcaption></figcaption></figure>

Go to the "**Basic Settings**" tab, click the "Update" button, and copy the received API token.

<figure><img src="../../../.gitbook/assets/image (136)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

## Module Settings

In the admin panel, create a new merchant in the "**Merchants**" ➔ "**Add Merchant**" section.

Select DashPay from the dropdown list in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (142)_eng.png" alt="" width="416"><figcaption></figcaption></figure>

Fill in the specified authorization fields.

<figure><img src="../../../.gitbook/assets/image (133)_eng.png" alt="" width="422"><figcaption></figcaption></figure>

**API Token** — the API token copied earlier from the merchant's personal account.

**Basic Token** — the Basic token copied earlier from the merchant's personal account.

## Special Fields

**Merchant Type:**

<figure><img src="../../../.gitbook/assets/image (144)_eng.png" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
The merchant type is fixed to the configured module and cannot be changed after the first application is created using this module.

![](<../../../.gitbook/assets/image (129)_eng.png>)![](<../../../.gitbook/assets/image (130)_eng.png>)\
To use a different merchant type, you must create a separate copy, select a different type, and connect it in the desired exchange direction.
{% endhint %}

* **Requisites** — the merchant's details will be displayed in the application.

<figure><img src="../../../.gitbook/assets/image (147)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

{% hint style="warning" %}
Choosing this type of requisites may increase the application creation time by up to 20 seconds due to the requisites being matched on the merchant's side.
{% endhint %}

* **Payment Link** — a "**Proceed to Payment**" button will be displayed in the application, which, when clicked, will take the client to the merchant's payment page, where the requisites will be displayed or matched.

<figure><img src="../../../.gitbook/assets/image (148)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

**Payment Methods:**

<figure><img src="../../../.gitbook/assets/image (145)_eng.png" alt="" width="360"><figcaption></figcaption></figure>

* **card_number** — bank card number for receiving rubles.
* **payment_account_number** — bank account number for receiving rubles.
* **phone_number** — phone number for receiving rubles via SBP.

## Continuing the Setup

Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/main/en/basic-settings/merchants-and-auto-payments/merchants/general-merchant-settings).