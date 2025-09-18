# Rapira Crypto

{% hint style="danger" %}
<mark style="color:red;">Before setting up auto payouts, please read the</mark> [<mark style="color:blue;">risk warning</mark>](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/preduprezhdenie-o-riskakh)<mark style="color:blue;">!</mark>
{% endhint %}

{% hint style="info" %}
If you need to update the module on the server, please refer to the [instructions](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat).
{% endhint %}

## Merchant Account Settings <a href="#nastroiki-v-lichnom-kabinete-merchanta" id="nastroiki-v-lichnom-kabinete-merchanta"></a>

Register for the [Rapira](https://rapira.net/) service. In your account settings, make sure to enable two-factor authentication under "**Settings**" → "**Security**" → "**GoogleAuth**" (this is a mandatory requirement for issuing API keys).

Go to "**Settings**" → "**API Keys**" and click the "**Create API Key**" button.

<figure><img src="../../../.gitbook/assets/image (1844).png" alt=""><figcaption></figcaption></figure>

In the API key settings, be sure to check the box for "**Withdraw**" to allow fund withdrawals using this key.

<figure><img src="../../../.gitbook/assets/image (1887).png" alt="" width="375"><figcaption></figcaption></figure>

Copy the keys and save them in a text file.

<figure><img src="../../../.gitbook/assets/image (1849).png" alt="" width="342"><figcaption></figcaption></figure>

## Module Settings <a href="#nastroiki-modulya" id="nastroiki-modulya"></a>

In the admin panel, create a new merchant in the "**Auto Payouts**" → "**Add Auto Payout**" section.

Select Rapira from the dropdown list in the "**Module**" field, provide a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (1842).png" alt="" width="419"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (1840).png" alt="" width="422"><figcaption></figcaption></figure>

**Private Key** — The **private key** generated in your Rapira account.

**UID** — The **UID** generated in your Rapira account.

**Host** — Choose either option (rapira.net or rapira.org).

## Special Fields

<figure><img src="../../../.gitbook/assets/image (1843).png" alt=""><figcaption></figcaption></figure>

**XML Currency Code** — <mark style="color:red;">**Not required**</mark> if you are using [standard currency codes from Bestchange](https://www.bestchange.ru/wiki/rates.html). In this case, you can use a single copy of the module for payouts in all cryptocurrencies.

{% hint style="warning" %}
If the XML currency code differs from the Bestchange standard, you may need to fill in this field. You can check the XML currency codes in the "**Currencies**" section → edit currency → "**Basic Settings**" tab → "**XML Designation**" field.
{% endhint %}

**Currency for Conversion** — Specify the currency from which the balance in the merchant's account will be converted to the payout currency (usually USDT or RUB).

<figure><img src="../../../.gitbook/assets/image (1851).png" alt="" width="191"><figcaption></figcaption></figure>

## Continuing the Setup

Next, proceed with the module setup by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-merchantov-avtovyplat).