# Exnode

{% hint style="danger" %}
<mark style="color:red;">Before setting up auto payouts, be sure to read</mark> [<mark style="color:blue;">the risk warning</mark>](https://premiumexchanger.com/wiki/preduprezhdenie-auto/)<mark style="color:blue;">!</mark>
{% endhint %}

{% hint style="info" %}
If you need to update the module on your server, please follow this [instruction](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-avtovyplat).
{% endhint %}

{% hint style="warning" %}
Since callbacks from Exnode may be filtered by Cloudflare (if you are using it), you need to request the current IP addresses from Exnode and add them to your whitelist following this [guide](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/dobavlenie-ip-adresov-v-whitelist-v-cloudflare).
{% endhint %}

## Settings in the Merchant Dashboard

{% hint style="warning" %}
To discuss terms and setup, please contact the [service representative](https://t.me/exnode_crypto).

**Disclaimer:** When connecting your website to any service, please independently assess the potential risks involved in the partnership.
{% endhint %}

Register an account with [Exnode](https://pay.exnode.ru/).

Log in to your dashboard, go to the "**Settings**" section, and generate your API keys.

<figure><img src="../../../.gitbook/assets/image (1373).png" alt="" width="563"><figcaption></figcaption></figure>

After clicking the "**Change**" button, refresh the page — your [key pair](#user-content-fn-1)[^1] will appear under the "**API Keys**" section. Copy them using the corresponding buttons and save them in a text file.

<figure><img src="../../../.gitbook/assets/image (1374).png" alt="" width="319"><figcaption></figcaption></figure>

## **Module Settings**

In the admin panel, create a new merchant by navigating to "**Auto Payouts**" -> "**Add Auto Payout**."

Select Exnode from the dropdown menu under "**Module**," enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (1375).png" alt=""><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure src="../../../.gitbook/assets/image (1376).png" alt=""><figcaption></figcaption></figure>

**Private Key** – the private key generated in your Exnode dashboard when creating the API key.

**Public Key** – the public key generated in your Exnode dashboard when creating the API key.

### Continuing Setup

Next, complete the merchant setup by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-merchantov-avtovyplat).

## Special Fields

<figure><img src="../../../.gitbook/assets/image (1379).png" alt=""><figcaption></figcaption></figure>

[^1]: The API key pair consists of a public and private key used for authentication with Exnode.

**Currency Code** — select the currency you will be paying out from the dropdown list.

{% hint style="warning" %}
You need to create a [separate copy of the auto-payout module](#user-content-fn-2)[^2] for each currency. In each copy, select the corresponding currency, then connect that copy on the "**Merchants and Payouts**" tab in the exchange direction settings, where the "**Receiving**" currency will be set to the chosen currency.

![](<../../../.gitbook/assets/image (1380).png>)
{% endhint %}

[^1]: public and private

[^2]: assign a unique name to each copy in the "Title" field for easier management later