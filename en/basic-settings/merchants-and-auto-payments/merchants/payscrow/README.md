# Payscrow

{% hint style="info" %}
If you need to update the module on the server, please refer to the [instructions](https://premium.gitbook.io/main/en/en/basic-settings/faq/updating-script-files-on-the-server/how-to-update-files-on-the-server#merchant-and-auto-payout-modules).
{% endhint %}

{% hint style="info" %}
To display the cardholder's full name on the client application for cards issued by the merchant, add the shortcode \[dest\_tag] in the instructions within the merchant settings.

![](<../../../../.gitbook/assets/image (1627)_eng.png>)
{% endhint %}

## Merchant Account Settings

Register in the [Payscrow](https://payscrow.io/) system. Log in to your merchant account and navigate to the "**API Settings**" section.

<figure><img src="../../../../.gitbook/assets/image (539)_eng.png" alt=""><figcaption></figcaption></figure>

In this section, you will find the keys for API access. Save them in a text file.

<figure><img src="../../../../.gitbook/assets/image (540)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

{% hint style="warning" %}
For this merchant, payment verification for changing the status of applications is available via both callback and cron job.

![](<../../../../.gitbook/assets/image (1623)_eng.png>)

When using cron, create a job on the server following the [instructions](https://premium.gitbook.io/main/en/basic-settings/faq/kak-sozdat-zadanie-cron-na-servere).

When using a callback, add the URL from the "**STATUS URL**" field into the "**Purchase Status**" field in the merchant account (under the "**API Settings**" section).

![](<../../../../.gitbook/assets/image (1626)_eng.png>)
{% endhint %}

## Module Settings

In the admin panel, create a new merchant in the "**Merchants**" -> "**Add Merchant**" section.

Select Payscrow from the dropdown list in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../../.gitbook/assets/image (537)_eng.png" alt="" width="461"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../../.gitbook/assets/image (538)_eng.png" alt="" width="449"><figcaption></figcaption></figure>

**Domain** — the domain provided by Payscrow after API access is created (each client is assigned a unique domain in the format `ec69bb31.merchant.payscrow.io`).

**Public Key** — the API key generated in the Payscrow account.

**Secret Key** — the signature key generated in the Payscrow account.

## Special Fields

<div><figure><img src="../../../../.gitbook/assets/image (541)_eng.png" alt="" width="482"><figcaption></figcaption></figure> <figure><img src="../../../../.gitbook/assets/image (534)_eng.png" alt="" width="476"><figcaption></figcaption></figure></div>

<div><figure><img src="../../../../.gitbook/assets/image (534)_eng.png" alt="" width="476"><figcaption></figcaption></figure> <figure><img src="../../../../.gitbook/assets/image (535)_eng.png" alt="" width="479"><figcaption></figcaption></figure></div>

**Payment Method** — available types of information provision for clients (the minimum amount for an application is 500 RUB).

* **\[BankCard] Smart order** — automatic bank selection determined by the client's card number (for this method, the option **"Display 'From Account' Field"** must be activated in the currency settings).

<figure><img src="../../../../.gitbook/assets/image (533)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

* **\[BankCard, RUB] {bank_name}** — issuance of a card number from the specified bank.
* **\[BankCard, RUB] Any bank in Russia** — issuance of a card number from any bank.
* **\[SBP,RUB] SBP** — issuance of a phone number for payment.
* **\[SBP,RUB] SBP {bank_name}** — issuance of a phone number for payment linked to the selected bank's card.

## Continuing Setup

Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/main/en/en/basic-settings/merchants-and-auto-payments/merchants/general-merchant-settings).