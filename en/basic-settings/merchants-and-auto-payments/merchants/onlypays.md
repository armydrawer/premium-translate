# OnlyPays

{% hint style="info" %}
If you need to update the module on the server, please refer to the [instructions](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat).
{% endhint %}

## Merchant Account Settings

{% hint style="warning" %}
To discuss terms and setup, please contact a [service representative](https://t.me/only7pay).

**Disclaimer**: When connecting your website to any service, please assess the potential risks of collaboration on your own.
{% endhint %}

After registering your account through a representative of OnlyPays, activate the bot ([LK_onLy_Pays_bot](https://t.me/LK_onLy_Pays_bot)) by clicking the "**Start**" button. Through the bot, you will gain access to your personal account.

<figure><img src="../../../.gitbook/assets/image (2172)_eng.png" alt="" width="434"><figcaption></figcaption></figure>

## Module Settings

In the admin panel, create a new merchant in the "**Merchants**" ➔ "**Add Merchant**" section.

Select OnlyPays from the dropdown menu in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (2170)_eng.png" alt="" width="447"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (2169)_eng.png" alt="" width="454"><figcaption></figcaption></figure>

**Domain** — leave this field empty.

**Project ID** — the ID of your project provided by the OnlyPays representative.

**Secret Key** — the API key issued to you by the OnlyPays representative.

## Special Fields

<figure><img src="../../../.gitbook/assets/image (2171)_eng.png" alt=""><figcaption></figcaption></figure>

**SBP** — provides bank card details or phone numbers for payments via SBP.

{% hint style="success" %}
To automatically update the status of requests without creating a cron job on the server, provide the merchant with a link for the webhook (in the "**Webhook URL**" field) and ask them to set it up for the module to receive.
![](<../../../.gitbook/assets/image (2173)_eng.png>)
{% endhint %}

## Continuing the Setup

Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/main/en/basic-settings/merchants-and-auto-payments/merchants/general-merchant-settings).