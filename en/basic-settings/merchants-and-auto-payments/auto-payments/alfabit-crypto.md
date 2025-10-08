# Alfabit Crypto

{% hint style="danger" %}
<mark style="color:red;">Before setting up automatic payouts, please read the</mark> [<mark style="color:blue;">risk warning!</mark>](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/preduprezhdenie-o-riskakh)
{% endhint %}

{% hint style="info" %}
If you need to update the module on the server, please refer to the [instructions](https://premium.gitbook.io/main/en/basic-settings/faq/updating-script-files-on-the-server/how-to-update-files-on-the-server#merchant-and-auto-payout-modules)
{% endhint %}

## Merchant Account Settings <a href="#nastroiki-v-lichnom-kabinete-merchanta" id="nastroiki-v-lichnom-kabinete-merchanta"></a>

{% hint style="warning" %}
To discuss terms and setup, please contact a [service representative](https://t.me/AlfaBitSupportVIP).

**Disclaimer**: When connecting your website to any service, please assess the potential risks of collaboration on your own.
{% endhint %}

Register and verify your account with [Alfabit](https://pay.alfabit.org/). Go to the "**Merchants**" section and click the "**Create Merchant**" button.

<figure><img src="../../../.gitbook/assets/image (358)_eng.png" alt=""><figcaption></figcaption></figure>

Fill in the required fields and click the "**Create Project**" button.

<div><figure><img src="../../../.gitbook/assets/image (359)_eng.png" alt="" width="375"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/image (1795)_eng.png" alt="" width="357"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/image (1796)_eng.png" alt="" width="356"><figcaption></figcaption></figure></div>

Go to the merchant settings, select the "**API Keys**" tab, and click the "**Add**" button.

<figure><img src="../../../.gitbook/assets/image (360)_eng.png" alt=""><figcaption></figcaption></figure>

Fill in the required fields and click the "**Save**" button.

<figure><img src="../../../.gitbook/assets/image (361)_eng.png" alt="" width="363"><figcaption></figcaption></figure>

{% hint style="info" %}
Select one or both options for "**Receiving Funds/Withdrawing Funds**" depending on your intended use of the merchant.

Add your server's IP address to the "**Trusted IPs**" section (recommended).
{% endhint %}

<figure><img src="../../../.gitbook/assets/image (362)_eng.png" alt="" width="352"><figcaption></figcaption></figure>

Save the generated key in a text file and click the "**Done**" button.

## Module Settings <a href="#nastroiki-modulya" id="nastroiki-modulya"></a>

In the admin panel, create a new merchant in the "**Automatic Payouts**" -> "**Add Automatic Payout**" section.

Select Alfabit Crypto from the dropdown list in the "**Module**" field, provide a name for the module, and click "**Save**".

<figure><img src="../../../.gitbook/assets/image (1791)_eng.png" alt="" width="467"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (1792)_eng.png" alt="" width="455"><figcaption></figcaption></figure>

**API Key** — **public key** generated in your Alfabit account.

## Special Fields

**Conversion from another currency (specify code)** — select "**No**" (if you do not plan to use this option) or the currency from which conversion will occur (at the merchant's rate) to the currency for payout just before the payout request.

**Currency** — select the desired currency for payout or "**Automatically**" (in this case, the payout will be made according to the currency code "**Receiving**" from the exchange direction where the automatic payout module is connected) (the list of methods will only be displayed after entering the correct API key for authorization in the module).

<figure><img src="../../../.gitbook/assets/image (1895)_eng.png" alt="" width="476"><figcaption></figcaption></figure>

{% hint style="warning" %}
For each payment method used, you need to create a separate copy of the automatic payout module, selecting the corresponding method, and then connect this copy in the "**Merchants and Payouts**" tab in the exchange direction settings, where the currency in "**Receiving**" will match the appropriate currency.
{% endhint %}

{% hint style="warning" %}
Please pay attention to the minimum payout amounts for the currencies you are using (in the "**Merchants**" section, under the "**Rates**" tab in your Alfabit account) — the amounts for payout requests must exceed the minimum amounts; otherwise, the merchant will not be able to process the payout:\
![](<../../../.gitbook/assets/image (1797)_eng.png>)
{% endhint %}

## Continuing Setup

Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-merchantov-avtovyplat).