# Premium Wallet (in development)

{% hint style="info" %}
If you need to update the module on the server, please refer to the [instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-merchantov).
{% endhint %}

## Merchant Account Settings

{% hint style="warning" %}
To discuss terms and connection, please contact a [service representative](https://t.me/ipichipich).

**Disclaimer**: When connecting your website to any service, please assess the potential risks of collaboration on your own.
{% endhint %}

After receiving your login credentials from the service representative, log in to the [Premium Wallet account](https://pw-api.elastoo.com/login). Navigate to the "**Settings**" section.

In your account, fill in the "**Webhook URL**" field and copy the data from the "**Client ID**" and "**API Secret**" fields to your clipboard or a text file.

<figure><img src="../../../.gitbook/assets/image (2106)_eng.png" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
In the "**Webhook URL**" field, enter the URL from the "**Status URL**" field in the merchant module settings.

![](<../../../.gitbook/assets/image (2105)_eng.png>)
{% endhint %}

## Module Settings

In the admin panel, create a new merchant in the "**Merchants**" ➔ "**Add Merchant**" section.

Select Premium Wallet from the dropdown list in the "**Module**" field, provide a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (2104)_eng.png" alt="" width="446"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (2103)_eng.png" alt="" width="430"><figcaption></figcaption></figure>

**Domain** — the link provided to you by the Premium Wallet service representative.

**Client ID** — the ID you copied earlier from the merchant account.

**Secret Key** — the key you copied earlier from the merchant account.

## Continuing the Setup

Next, proceed with the merchant setup by following the [general setup instructions](https://premium.gitbook.io/main/en/basic-settings/merchants-and-auto-payments/merchants/general-merchant-settings).