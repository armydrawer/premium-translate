# PandaPay

{% hint style="info" %}
If you need to update the module on the server, please refer to the [instructions](https://premium.gitbook.io/main/en/en/basic-settings/faq/updating-script-files-on-the-server/how-to-update-files-on-the-server#merchant-and-auto-payout-modules).
{% endhint %}

## Merchant Account Settings

{% hint style="warning" %}
To discuss terms and connection, please contact a [service representative](https://t.me/PandaPaySup).

**Disclaimer**: When connecting your website to any service, please assess the potential risks of collaboration on your own.
{% endhint %}

After receiving your login credentials from the service representative, log in to your [PandaPay](https://pandapay24.com/) account. Navigate to the "**Settings**" section.

<figure><img src="../../../../ru/.gitbook/assets/image (122) (1).png" alt="" width="563"><figcaption></figcaption></figure>

Add the Callback URL in the appropriate field.

<figure><img src="../../../../ru/.gitbook/assets/image (120) (1).png" alt="" width="563"><figcaption></figcaption></figure>

{% hint style="success" %}
To update the status of requests, specify the current Callback URL in the merchant account — you can find the URL in the module settings (the "**Webhook**" line).

<img src="../../../../ru/.gitbook/assets/image (121) (1).png" alt="" data-size="original">
{% endhint %}

Create new access keys and copy them to your clipboard or a text file.

<figure><img src="../../../../ru/.gitbook/assets/image (119) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## Module Settings

In the admin panel, create a new merchant in the "**Merchants**" ➔ "**Add Merchant**" section.

Select PandaPay from the dropdown list in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (2092)_eng.png" alt="" width="445"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (2093)_eng.png" alt="" width="458"><figcaption></figcaption></figure>

**API Key** — the copied API key from the merchant account.

**Secret Key** — the copied secret key from the merchant account.

## Special Fields

<figure><img src="../../../.gitbook/assets/image (2094)_eng.png" alt="" width="456"><figcaption></figcaption></figure>

**Allowed Countries** — a list of countries for which account details will be searched.

**If "ANY" is selected**, the search will be conducted across all countries.\
**If one or more specific countries are selected**, the search will be limited to those countries.\
**If no options are selected**, the search will be conducted based on the currency code "**Give**" from the exchange direction.

**Payment Method** — the method for searching account details:

<figure><img src="../../../.gitbook/assets/image (2097)_eng.png" alt="" width="354"><figcaption></figcaption></figure>

* **accountNumber** — bank account number
* **card** — bank card number
* **crossBorderTransfer** — funds transfer between countries
* **SBP** — phone number for transferring funds via SBP

{% hint style="info" %}
The "**Add**" buttons allow you to add new methods without updating the module on the server (use these options **only** if the merchant representative has informed you that it is necessary).
{% endhint %}

## Continuing the Setup

Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/main/en/en/basic-settings/merchants-and-auto-payments/merchants/general-merchant-settings).
