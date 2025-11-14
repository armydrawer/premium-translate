# Lazytrade

{% hint style="info" %}
If you need to update the module on the server, please refer to the [instructions](https://premium.gitbook.io/main/en/en/basic-settings/faq/updating-script-files-on-the-server/how-to-update-files-on-the-server#merchant-and-auto-payout-modules).
{% endhint %}

## Merchant Account Settings

{% hint style="warning" %}
To discuss the terms and conditions, please contact a service representative.

**Disclaimer:** When connecting your website to a particular service, please independently assess the possible risks of cooperation.
{% endhint %}

Register on the LazyTrade service with the help of a service representative and request API keys to connect to Premium Exchanger.

## Module Settings

In the admin panel, create a new merchant in the "**Merchants**" section by clicking "**Add Merchant**."

Select Lazytrade from the dropdown menu in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (20).png" alt="" width="346"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (21).png" alt="" width="369"><figcaption></figcaption></figure>

**Domain** — leave this field blank.

**API key** — the API key provided to you earlier by a LazyTrade representative.

**Secret key** — the secret key provided to you earlier by a LazyTrade representative.

## Special Fields

<figure><img src="../../../.gitbook/assets/image (23).png" alt="" width="297"><figcaption></figcaption></figure>

**Payment method** — select the required method for receiving funds from the customer:

* **CARD** — issuing bank card details
* **CARD\_CIS** — issuing card details for international transfers (cross-border)
* **CIS** — issuing a phone number for international transfers (cross-border)
* **QR\_NSPK** — issue a link to follow and pay via QR code on the page that opens (it takes up to 30-40 seconds to generate the link)
* **SBP** — issue a phone number to receive funds via SBP

<figure><img src="../../../.gitbook/assets/image (24).png" alt=""><figcaption></figcaption></figure>

**Bank** — selection of the bank whose details will be provided in the application

**Individual time for deleting unpaid applications (minutes)** — the time that LazyTrade will wait for payment (default 60 minutes (when 0 is displayed in the field))

## Continuing the Setup

Next, proceed to configure the merchant by following the [general setup instructions](https://premium.gitbook.io/main/en/en/basic-settings/merchants-and-auto-payments/merchants/general-merchant-settings).
