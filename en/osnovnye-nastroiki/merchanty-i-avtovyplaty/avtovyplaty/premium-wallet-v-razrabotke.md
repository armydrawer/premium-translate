# Premium Wallet (in development)

{% hint style="danger" %}
<mark style="color:red;">Before setting up automatic payouts, be sure to read</mark> [<mark style="color:blue;">the risk warning</mark>](https://premiumexchanger.com/wiki/preduprezhdenie-auto/)<mark style="color:blue;">!</mark>
{% endhint %}

{% hint style="info" %}
If you need to update the module on your server, please follow this [instruction](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-avtovyplat).
{% endhint %}

<figure><img src="../../../.gitbook/assets/image (2101).png" alt=""><figcaption></figcaption></figure>

## Merchant Account Settings

{% hint style="warning" %}
To discuss terms and get connected, please contact the [service representative](https://t.me/ipichipich).

**Disclaimer:** When integrating your website with any service, please independently assess the potential risks involved in the partnership.
{% endhint %}

In your merchant account, fill in the "**Webhook URL**" field and copy the values from the "**Client ID**" and "**API Secret**" fields to your clipboard or a text file.

<figure><img src="../../../.gitbook/assets/image (2102).png" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
In the "**Webhook URL**" field, enter the URL from the "**Callback URL**" field found in the automatic payout module settings.

<img src="../../../.gitbook/assets/image (2101).png" alt="" data-size="original">
{% endhint %}

## Module Settings

In the admin panel, go to "**Merchants**" ➔ "**Automatic Payouts**", click "**Add**", and select Premium Wallet.

<figure><img src="../../../.gitbook/assets/image (116).png" alt="" width="464"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (115).png" alt="" width="430"><figcaption></figcaption></figure>

**Domain** —&#x20;

**Client ID** — the ID you copied earlier from the merchant account

**Secret Key** — the key you copied earlier from the merchant account

## Continuing Setup

Next, complete the merchant setup by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-merchantov-avtovyplat).