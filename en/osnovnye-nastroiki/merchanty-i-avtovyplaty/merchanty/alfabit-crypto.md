# Alfabit Crypto

{% hint style="info" %}
If you need to update the module on your server, please follow the [instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-merchantov).
{% endhint %}

{% hint style="warning" %}
To discuss terms and set up a connection, please contact the [service representative](https://t.me/AlfaBitSupportVIP).

**Disclaimer:** When connecting your website to any service, please independently assess the potential risks involved in the partnership.
{% endhint %}

## Merchant Account Settings

Register and verify your account on the [Alfabit](https://pay.alfabit.org/) platform. Then go to the "**Merchants**" section and click the "**Create Merchant**" button.

<figure><img src="../../../.gitbook/assets/image (364).png" alt=""><figcaption></figcaption></figure>

Fill in the required fields and click "**Create Project**."

<div><figure><img src="../../../.gitbook/assets/image (365).png" alt="" width="375"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/image (368).png" alt="" width="357"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/image (367).png" alt="" width="356"><figcaption></figcaption></figure></div>

Go to the merchant settings, select the "**API Keys**" tab, and click "**Add**."

<figure><img src="../../../.gitbook/assets/image (371).png" alt=""><figcaption></figcaption></figure>

Fill in the required fields and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (370).png" alt="" width="363"><figcaption></figcaption></figure>

{% hint style="info" %}
Select one or both options "**Accept Funds / Withdraw Funds**" depending on how you intend to use the merchant account.

Optionally, add your server’s IP address under "**Trusted IPs**" (recommended).
{% endhint %}

<figure><img src="../../../.gitbook/assets/Arc_qmcPit3Hgb.png" alt="" width="352"><figcaption></figcaption></figure>

Save the generated key to a text file and click "**Done**."

## Module Settings

In the admin panel, create a new merchant by going to "**Merchants**" -> "**Add Merchant**."

Select Alfabit Crypto from the "**Module**" dropdown menu, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/Arc_NAxwA0DrS1.png" alt="" width="473"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure src="../../../.gitbook/assets/image (372).png" alt="" width="458"><figcaption></figcaption></figure>

**API Key** — the **public key** generated in your Alfabit personal account.

## Special Fields

<figure><img src="../../../.gitbook/assets/Arc_wNtMcO8Eyp.png" alt="" width="455"><figcaption></figcaption></figure>

**Currency** — select the currency you want to receive funds in, or choose "**Automatic**" (in this case, the wallet address will be requested based on the currency code from the exchange direction where the merchant is connected; the list of methods will only appear after entering a valid API key for module authorization).

<figure><img src="../../../.gitbook/assets/image (1790).png" alt="" width="435"><figcaption></figcaption></figure>

{% hint style="warning" %}
Please note the minimum acceptance amounts for the currencies you use (found under "**Merchants**", "**Rates**" tab in the Alfabit personal account) — the amounts in your requests must exceed these minimums; otherwise, the merchant will not process the payment:\
![](<../../../.gitbook/assets/image (1797).png>)
{% endhint %}

**Convert to** — select the currency to which the payment received from the client will be converted (at the merchant’s exchange rate at the time of conversion), or choose "**No**" to disable conversion. The tooltip below the field shows the possible currency pairs for conversion (the list of methods will only appear after entering a valid API key for module authorization).

<figure><img src="../../../.gitbook/assets/image (1894).png" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
Please note that requests with an amount equivalent to less than 12 USDT will not be converted (merchant-side restriction) when this option is enabled — funds from such requests will be credited to the account in the original currency.

![](<../../../.gitbook/assets/image (1788).png>)
{% endhint %}

## Continuing the setup

Next, proceed with configuring the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).