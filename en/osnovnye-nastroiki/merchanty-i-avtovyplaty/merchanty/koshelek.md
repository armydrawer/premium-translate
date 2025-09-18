# Koshelek

{% hint style="info" %}
If you need to update the module on the server, please refer to the [instructions](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat).
{% endhint %}

## Settings in the Merchant's Personal Account

First, register and verify your account with the [Koshelek](https://koshelek.ru/) service. Then, go to the [**"API Keys"** page](https://koshelek.ru/account/keysApi) and click the "**Create API Key**" button.

<figure><img src="../../../.gitbook/assets/image (1757).png" alt=""><figcaption></figcaption></figure>

In the pop-up window, enter a name for the key and select the methods for working with the API (to receive funds, choose "**Deposit**" and "**Read**"). Click the "**Save**" button.

<figure><img src="../../../.gitbook/assets/image (1759).png" alt="" width="464"><figcaption></figcaption></figure>

In the next window, copy the generated keys and save them in a text file.

<figure><img src="../../../.gitbook/assets/image (1760).png" alt="" width="474"><figcaption></figcaption></figure>

## Module Settings

In the admin panel, create a new merchant in the "**Merchants**" -> "**Add Merchant**" section.

Select Koshelek from the drop-down list in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (1749).png" alt="" width="422"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (1751).png" alt="" width="426"><figcaption></figcaption></figure>

**Public Key** — **public ID** generated in the Koshelek personal account.

**Secret Key** — **secret key** generated in the Koshelek personal account.

## Special Fields

<figure><img src="../../../.gitbook/assets/image (1752).png" alt="" width="302"><figcaption></figcaption></figure>

**Network** — specify the network to ensure correct details are provided in the request when using the merchant.

## Continuing the Setup

Next, proceed with the merchant setup by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).