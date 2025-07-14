Here is a natural, fluent English translation of the provided text:

---

noIndex: true

---

# Koshelek

{% hint style="info" %}
If you need to update the module on your server, please follow the [instructions here](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-merchantov).
{% endhint %}

## Settings in the Merchant Dashboard

Register and verify your account at [Koshelek](https://koshelek.ru/). Then go to the [**API Keys** page](https://koshelek.ru/account/keysApi) and click the "**Create API Key**" button.

<figure><img src="../../../.gitbook/assets/image (1757).png" alt=""><figcaption></figcaption></figure>

In the window that opens, enter any name for your key and select the API methods you want to enable (to accept payments, select "**Deposit**" and "**Read**"). Then click "**Save**".

<figure><img src="../../../.gitbook/assets/image (1759).png" alt="" width="464"><figcaption></figcaption></figure>

Copy the generated keys from the next window and save them in a text file for later use.

<figure><img src="../../../.gitbook/assets/image (1760).png" alt="" width="474"><figcaption></figcaption></figure>

## Module Settings

In the admin panel, create a new merchant by going to "**Merchants**" -> "**Add Merchant**".

Select Koshelek from the "**Module**" dropdown, enter a name for the module, and click "**Save**".

<figure><img src="../../../.gitbook/assets/image (1749).png" alt="" width="422"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (1751).png" alt="" width="426"><figcaption></figcaption></figure>

**Public Key** — the **public ID** generated in your Koshelek dashboard

**Secret Key** — the **secret key** generated in your Koshelek dashboard

## Special Fields

<figure><img src="../../../.gitbook/assets/image (1752).png" alt="" width="302"><figcaption></figcaption></figure>

**Network** — specify the network to ensure the correct details are provided in payment requests when using this merchant

## Continuing Setup

Next, complete the merchant setup by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).

---

If you need any further help or adjustments, just let me know!