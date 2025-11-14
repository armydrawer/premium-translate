# PSPWare

{% hint style="info" %}
If you need to update a module on the server, please refer to the [instructions](https://premium.gitbook.io/main/en/en/basic-settings/faq/updating-script-files-on-the-server/how-to-update-files-on-the-server#merchant-and-auto-payout-modules).
{% endhint %}

{% hint style="warning" %}
For discussions regarding terms and connections, please contact a [service representative](https://t.me/pspware_ceo).

**Disclaimer**: When connecting your website to any service, please assess the potential risks of collaboration on your own.
{% endhint %}

## Module Settings

In the admin panel, create a new merchant in the "**Merchants**" section by selecting "**Add Merchant**."

Choose PSPWare from the dropdown menu in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../../ru/.gitbook/assets/image (2157) (1).png" alt="" width="410"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../../ru/.gitbook/assets/image (2154) (1).png" alt="" width="464"><figcaption></figcaption></figure>

**Domain** — leave this field empty.

**Merchant ID** — the ID provided to you by the PSPWare representative.

**API Key** — the key provided to you by the PSPWare representative.

## Special Fields

<figure><img src="../../../../ru/.gitbook/assets/image (2155) (1).png" alt=""><figcaption></figcaption></figure>

**SBP** — provide a phone number for payments via SBP instead of card details in requests.

{% hint style="warning" %}
Please note that you also need to forward the URL for the Webhook from the module settings to the service representative, requesting them to set it up for you. Without this URL being installed, requests with underpayments/overpayments **will not change their statuses**!

<img src="../../../../ru/.gitbook/assets/image (2156) (1).png" alt="" data-size="original">
{% endhint %}

## Continuing the Setup

Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/main/en/en/basic-settings/merchants-and-auto-payments/merchants/general-merchant-settings).
