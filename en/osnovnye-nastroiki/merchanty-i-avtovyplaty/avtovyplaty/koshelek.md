# Koshelek

{% hint style="danger" %}
<mark style="color:red;">Before setting up auto payouts, be sure to read</mark> [<mark style="color:blue;">the risk warning</mark>](https://premiumexchanger.com/wiki/preduprezhdenie-auto/)<mark style="color:blue;">!</mark>
{% endhint %}

{% hint style="info" %}
If you need to update the module on your server, please follow this [instruction](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-avtovyplat).
{% endhint %}

## Settings in the Merchant Dashboard

Register and verify your account at [Koshelek](https://koshelek.ru/). Then go to the [**API Keys** page](https://koshelek.ru/account/keysApi) and click the "**Create API Key**" button.

<figure><img src="../../../.gitbook/assets/image (1757).png" alt=""><figcaption></figcaption></figure>

In the window that opens, enter any name for your key and select the API methods you want to enable (for payouts, select "**Deposit**", "**Withdrawal**", and "**Read**"). Then click "**Save**".

<figure><img src="../../../.gitbook/assets/image (1761).png" alt="" width="467"><figcaption></figcaption></figure>

In the next window, copy the generated keys and save them in a text file.

<figure><img src="../../../.gitbook/assets/image (1760).png" alt="" width="474"><figcaption></figcaption></figure>

## Module Settings

In the admin panel, create a new merchant under "**Auto Payouts**" -> "**Add Auto Payout**."

Select Koshelek from the dropdown menu in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (1750).png" alt="" width="419"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (1753).png" alt="" width="426"><figcaption></figcaption></figure>

**Public Key** — the **public ID** generated in your Koshelek dashboard

**Secret Key** — the **secret key** generated in your Koshelek dashboard

## Special Fields

<figure><img src="../../../.gitbook/assets/image (1754).png" alt="" width="302"><figcaption></figcaption></figure>

**Network** — specify the currency network to ensure proper functioning of auto payouts

## Continuing Setup

Next, complete the merchant setup by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-merchantov-avtovyplat).