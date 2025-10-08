# OnlyPays

{% hint style="danger" %}
<mark style="color:red;">Before setting up automatic payouts, please read the</mark> [<mark style="color:blue;">risk warning</mark>](https://premium.gitbook.io/main/en/basic-settings/merchants-and-auto-payments/auto-payments/risk-warning)<mark style="color:blue;">!</mark>
{% endhint %}

{% hint style="info" %}
If you need to update the module on the server, please refer to the [instructions](https://premium.gitbook.io/main/en/en/basic-settings/faq/updating-script-files-on-the-server/how-to-update-files-on-the-server#merchant-and-auto-payout-modules).
{% endhint %}

## Merchant Account Settings

{% hint style="warning" %}
To discuss terms and setup, please contact a [service representative](https://t.me/only7pay).

**Disclaimer**: When connecting your website to any service, please assess the potential risks of collaboration on your own.
{% endhint %}

After registering your account through a representative of OnlyPays, activate the bot ([LK_onLy_Pays_bot](https://t.me/LK_onLy_Pays_bot)) by clicking the "**Start**" button. Through the bot, you will gain access to your personal account.

<figure><img src="../../../.gitbook/assets/image (2172)_eng.png" alt="" width="434"><figcaption></figcaption></figure>

## Module Settings

In the admin panel, create a new merchant in the "**Automatic Payouts**" section by clicking "**Add Automatic Payout**."

Select OnlyPays from the dropdown menu in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (2174)_eng.png" alt="" width="441"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (2169)_eng.png" alt="" width="454"><figcaption></figcaption></figure>

**Domain** — leave this field empty.

**Project ID** — the ID of your project provided by the OnlyPays representative.

**Secret Key** — the secret key provided by the OnlyPays representative.

## Special Fields

<figure><img src="../../../.gitbook/assets/image (2171)_eng.png" alt=""><figcaption></figcaption></figure>

**SBP** — payout to a bank card or phone number linked to SBP.

{% hint style="success" %}
To automatically update the status of requests without creating a cron job on the server, provide the merchant with the webhook link (in the "**Webhook URL**" field) and ask them to set it up for the module to receive notifications.

![](<../../../.gitbook/assets/image (2175)_eng.png>)
{% endhint %}

## Continuing Setup

Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/main/en/basic-settings/merchants-and-auto-payments/auto-payments/obshie-nastroiki-merchantov-avtovyplat).