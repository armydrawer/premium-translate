# Rapira Crypto

{% hint style="danger" %}
<mark style="color:red;">Before setting up auto payouts, be sure to read</mark> [<mark style="color:blue;">the risk warning</mark>](https://premiumexchanger.com/wiki/preduprezhdenie-auto/)<mark style="color:blue;">!</mark>
{% endhint %}

{% hint style="info" %}
If you need to update the module on your server, please follow this [instruction](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-avtovyplat).
{% endhint %}

## Settings in the Merchant’s Personal Account <a href="#merchant-personal-account-settings" id="merchant-personal-account-settings"></a>

Register for an account at [Rapira](https://rapira.net/). In your personal account, be sure to enable two-factor authentication by going to "**Settings**" → "**Security**" → "**GoogleAuth**" (this is mandatory to generate API keys).

Next, go to "**Settings**" → "**API Keys**" and click the "**Create API Key**" button.

<figure><img src="../../../.gitbook/assets/image (1844).png" alt=""><figcaption></figcaption></figure>

When configuring the API key, make sure to check the box for "**Withdraw**" to allow withdrawals using this key.

<figure><img src="../../../.gitbook/assets/image (1887).png" alt="" width="375"><figcaption></figcaption></figure>

Copy the keys and save them in a text file.

<figure><img src="../../../.gitbook/assets/image (1849).png" alt="" width="342"><figcaption></figcaption></figure>

## Module Settings <a href="#module-settings" id="module-settings"></a>

In the admin panel, create a new merchant under "**Auto Payouts**" → "**Add Auto Payout**."

Select Rapira from the dropdown menu in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (1842).png" alt="" width="419"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (1840).png" alt="" width="422"><figcaption></figcaption></figure>

**Private Key** — the private key generated in your Rapira personal account

**UID** — the UID generated in your Rapira personal account

**Host** — choose either option (rapira.net or rapira.org)

## Special Fields

<figure><img src="../../../.gitbook/assets/image (1843).png" alt=""><figcaption></figcaption></figure>

**Currency XML Code** — <mark style="color:red;">no need to fill this in</mark> if you are using [standard Bestchange currency codes](https://www.bestchange.ru/wiki/rates.html). In this case, you can use a single instance of the module to pay out all cryptocurrencies.

{% hint style="warning" %}
If the currency’s XML code differs from the Bestchange standard, you may need to fill in this field. You can check the XML currency codes in the "**Currencies**" section → edit the currency → "**General Settings**" tab → "**XML Designation**" field.
{% endhint %}

**Conversion Currency** — specify the currency from which the merchant’s account balance will be converted into the payout currency (most often USDT or RUB).

<figure><img src="../../../.gitbook/assets/image (1851).png" alt="" width="191"><figcaption></figcaption></figure>

## Continuing the Setup

Next, configure the module by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-merchantov-avtovyplat).