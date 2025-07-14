# PSPWare

{% hint style="info" %}
If you need to update the module on your server, please follow the [instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-merchantov).
{% endhint %}

{% hint style="warning" %}
To discuss terms and connection details, please contact the [service representative](https://t.me/pspware_ceo).

**Disclaimer:** When connecting your website to any service, please independently assess any potential risks involved in the partnership.
{% endhint %}

## Module Settings

In the admin panel, create a new merchant by going to "**Merchants**" ➔ "**Add Merchant**."

Select PSPWare from the dropdown menu in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (2157).png" alt="" width="410"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (2154).png" alt="" width="464"><figcaption></figcaption></figure>

**Domain** — leave this field empty

**Merchant ID** — the ID provided to you by your PSPWare representative

**API Key** — the key provided to you by your PSPWare representative

## Special Fields

<figure><img src="../../../.gitbook/assets/image (2155).png" alt=""><figcaption></figcaption></figure>

**SBP** — enables providing a phone number for payment via SBP instead of card details in payment requests

{% hint style="warning" %}
Please note that you also need to send the Webhook URL from the module settings to your service representative and ask them to configure it for you. Without this URL being set up, payment requests with underpayments or overpayments **will not update their statuses**!

![](<../../../.gitbook/assets/image (2156).png>)
{% endhint %}

## Continuing Setup

Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).