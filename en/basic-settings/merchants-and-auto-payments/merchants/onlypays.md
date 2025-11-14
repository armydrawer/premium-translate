# OnlyPays

{% hint style="info" %}
If you need to update the module on the server, please refer to the [instructions](https://premium.gitbook.io/main/en/en/basic-settings/faq/updating-script-files-on-the-server/how-to-update-files-on-the-server#merchant-and-auto-payout-modules).
{% endhint %}

## Merchant Account Settings

{% hint style="warning" %}
To discuss terms and setup, please contact a [service representative](https://t.me/only7pay).

**Disclaimer**: When connecting your website to any service, please assess the potential risks of collaboration on your own.
{% endhint %}

After registering your account through a representative of OnlyPays, activate the bot ([LK\_onLy\_Pays\_bot](https://t.me/LK_onLy_Pays_bot)) by clicking the "**Start**" button. Through the bot, you will gain access to your personal account.

<figure><img src="../../../../ru/.gitbook/assets/image (2172) (1).png" alt="" width="434"><figcaption></figcaption></figure>

## Module Settings

In the admin panel, create a new merchant in the "**Merchants**" ➔ "**Add Merchant**" section.

Select OnlyPays from the dropdown menu in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../../ru/.gitbook/assets/image (2170) (1).png" alt="" width="447"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../../ru/.gitbook/assets/image (2169) (1).png" alt="" width="454"><figcaption></figcaption></figure>

**Domain** — leave this field empty.

**Project ID** — the ID of your project provided by the OnlyPays representative.

**Secret Key** — the API key issued to you by the OnlyPays representative.

## Special Fields

<figure><img src="../../../../ru/.gitbook/assets/image (2171) (1).png" alt=""><figcaption></figcaption></figure>

**SBP** — provides bank card details or phone numbers for payments via SBP.

{% hint style="success" %}
To automatically update the status of requests without creating a cron job on the server, provide the merchant with a link for the webhook (in the "**Webhook URL**" field) and ask them to set it up for the module to receive. ![](<../../../../ru/.gitbook/assets/image (2173) (1).png>)
{% endhint %}

## Continuing the Setup

Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/main/en/en/basic-settings/merchants-and-auto-payments/merchants/general-merchant-settings).
