# OnlyPays

{% hint style="danger" %}
<mark style="color:red;">Before setting up auto payouts, be sure to read</mark> [<mark style="color:blue;">the risk warning</mark>](https://premiumexchanger.com/wiki/preduprezhdenie-auto/)<mark style="color:blue;">!</mark>
{% endhint %}

{% hint style="warning" %}
If you need to update the module on your server, please follow this [instruction](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-merchantov).
{% endhint %}

## Merchant Account Settings

{% hint style="warning" %}
To discuss terms and get connected, please contact the [service representative](https://t.me/only7pay).

**Disclaimer:** When integrating your website with any service, please independently assess the potential risks involved in the partnership.
{% endhint %}

After registering your account through the OnlyPays service representative, activate the bot ([LK_onLy_Pays_bot](https://t.me/LK_onLy_Pays_bot)) by clicking the "**Start**" button. Through this bot, you will gain access to your personal account.

<figure><img src="../../../.gitbook/assets/image (2172).png" alt="" width="434"><figcaption></figcaption></figure>

## Module Setup

In the admin panel, create a new merchant under "**Auto Payouts**" ➔ "**Add Auto Payout**."

Select OnlyPays from the dropdown menu in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (2174).png" alt="" width="441"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (2169).png" alt="" width="454"><figcaption></figcaption></figure>

- **Domain** — leave this field empty  
- **Project ID** — your project ID provided by the OnlyPays representative  
- **Secret Key** — the secret key provided by the OnlyPays representative  

## Special Fields

<figure><img src="../../../.gitbook/assets/image (2171).png" alt=""><figcaption></figcaption></figure>

- **SBP** — payout to a bank card or phone number linked to the SBP system (Fast Payment System)

{% hint style="success" %}
To automatically update the status of payout requests without setting up a cron job on your server, provide the merchant with the webhook URL (the "**Webhook URL**" field) and ask them to configure it for incoming requests on the module.

![](<../../../.gitbook/assets/image (2175).png>)
{% endhint %}

## Continuing Setup

Next, complete the merchant setup by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-merchantov-avtovyplat).