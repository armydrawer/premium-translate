# OnlyPays

{% hint style="info" %}
If you need to update the module on your server, please follow the [instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-merchantov).
{% endhint %}

## Settings in the Merchant’s Personal Account

{% hint style="warning" %}
To discuss terms and set up your connection, please contact the [service representative](https://t.me/only7pay).

**Disclaimer:** When connecting your website to any service, please independently assess any potential risks involved in the partnership.
{% endhint %}

After registering your account through the OnlyPays service representative, activate the bot ([LK_onLy_Pays_bot](https://t.me/LK_onLy_Pays_bot)) by clicking the "**Start**" button. Through this bot, you will gain access to your personal account.

<figure><img src="../../../.gitbook/assets/image (2172).png" alt="" width="434"><figcaption></figcaption></figure>

## Module Setup

In the admin panel, create a new merchant by going to "**Merchants**" ➔ "**Add Merchant**."

Select OnlyPays from the dropdown menu under the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (2170).png" alt="" width="447"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (2169).png" alt="" width="454"><figcaption></figcaption></figure>

- **Domain** — leave this field empty  
- **Project ID** — your project ID provided by the OnlyPays representative  
- **Secret Key** — the API key provided by the OnlyPays representative  

## Special Fields

<figure><img src="../../../.gitbook/assets/image (2171).png" alt=""><figcaption></figcaption></figure>

- **SBP** — enables issuing bank card details or phone numbers for payment via the SBP system

{% hint style="success" %}
To automatically update the status of requests without setting up a cron job on your server, provide the merchant with a webhook URL (the "**Webhook URL**" field) and ask them to configure it for receiving updates in the module.

![](<../../../.gitbook/assets/image (2173).png>)
{% endhint %}

## Continuing the Setup

Next, complete the merchant setup by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).