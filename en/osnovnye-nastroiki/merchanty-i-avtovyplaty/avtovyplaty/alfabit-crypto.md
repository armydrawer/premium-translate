# Alfabit Crypto

{% hint style="danger" %}
<mark style="color:red;">Before setting up auto payouts, be sure to read</mark> [<mark style="color:blue;">the risk warning</mark>](https://premiumexchanger.com/wiki/preduprezhdenie-auto/)<mark style="color:blue;">!</mark>
{% endhint %}

{% hint style="info" %}
If you need to update the module on your server, please follow this [instruction](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-avtovyplat).
{% endhint %}

## Settings in the Merchant’s Personal Account <a href="#nastroiki-v-lichnom-kabinete-merchanta" id="nastroiki-v-lichnom-kabinete-merchanta"></a>

{% hint style="warning" %}
To discuss terms and connection details, please contact the [service representative](https://t.me/AlfaBitSupportVIP).

**Disclaimer:** When connecting your website to any service, please independently assess the potential risks involved in the partnership.
{% endhint %}

Register and verify your account at [Alfabit](https://pay.alfabit.org/). Then go to the "**Merchants**" section and click the "**Create Merchant**" button.

<figure><img src="../../../.gitbook/assets/image (358).png" alt=""><figcaption></figcaption></figure>

Fill in the required fields and click "**Create Project**."

<div><figure><img src="../../../.gitbook/assets/image (359).png" alt="" width="375"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/image (1795).png" alt="" width="357"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/image (1796).png" alt="" width="356"><figcaption></figcaption></figure></div>

Go to the merchant settings, select the "**API Keys**" tab, and click "**Add**."

<figure><img src="../../../.gitbook/assets/image (360).png" alt=""><figcaption></figcaption></figure>

Fill in the required fields and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (361).png" alt="" width="363"><figcaption></figcaption></figure>

{% hint style="info" %}
Select one or both options "**Receive Funds / Withdraw Funds**" depending on how you intend to use the merchant account.

Optionally, add your server’s IP address under "**Trusted IPs**" (recommended).
{% endhint %}

<figure><img src="../../../.gitbook/assets/image (362).png" alt="" width="352"><figcaption></figcaption></figure>

Save the generated key to a text file and click "**Done**."

## Module Settings <a href="#nastroiki-modulya" id="nastroiki-modulya"></a>

In the admin panel, create a new merchant under "**Auto Payouts**" -> "**Add Auto Payout**."

Select Alfabit Crypto from the "**Module**" dropdown, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (1791).png" alt="" width="467"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (1792).png" alt="" width="455"><figcaption></figcaption></figure>

**API Key** — a **public key** generated in the Alfabit personal account.

## Special Fields

**Conversion from another currency (enter code)** — select "**No**" (if you do not plan to use this option) or choose the currency from which the conversion will be made (at the merchant’s exchange rate) into the payout currency immediately before processing the payout request.

**Currency** — select the desired payout currency or choose "**Automatic**" (in this case, the payout will be made according to the "**Receiving**" currency code from the exchange direction where the auto-payout module is connected). (The list of methods will only appear after entering a valid API key for module authorization.)

<figure><img src="../../../.gitbook/assets/image (1895).png" alt="" width="476"><figcaption></figcaption></figure>

{% hint style="warning" %}
For each payment method you use, you need to create a separate copy of the auto-payout module, select the corresponding method in it, and then connect this copy on the "**Merchants and Payouts**" tab in the exchange direction settings, where the "**Receiving**" currency will be the appropriate currency.
{% endhint %}

{% hint style="warning" %}
Please note the minimum payout amounts for the currencies you use (found under "**Merchants**", "**Rates**" tab in the Alfabit personal account). Payout requests must exceed these minimum amounts; otherwise, the merchant will not be able to process the payout:\
![](<../../../.gitbook/assets/image (1797).png>)
{% endhint %}

## Continuing Setup

Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-merchantov-avtovyplat).