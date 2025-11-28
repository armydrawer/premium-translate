# Alfabit Crypto

{% hint style="info" %}
If you need to update a module on the server, please refer to the [instructions](https://premium.gitbook.io/main/en/en/basic-settings/faq/updating-script-files-on-the-server/how-to-update-files-on-the-server#merchant-and-auto-payout-modules).
{% endhint %}

{% hint style="warning" %}
For discussions regarding terms and connections, please contact a [service representative](https://t.me/AlfaBitSupportVIP).

**Disclaimer**: When connecting your website to any service, please assess the potential risks of collaboration on your own.
{% endhint %}

## Merchant Account Settings

Register and verify your account with [Alfabit](https://pay.alfabit.org/). Go to the "**Merchants**" section and click the "**Create Merchant**" button.

<figure><img src="../../../.gitbook/assets/image%20(364)_eng.png" alt=""><figcaption></figcaption></figure>

Fill in the required fields and click the "**Create Project**" button.

<div><figure><img src="../../../.gitbook/assets/image%20(365)_eng.png" alt="" width="375"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/image%20(368)_eng.png" alt="" width="357"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/image%20(367)_eng.png" alt="" width="356"><figcaption></figcaption></figure></div>

Go to the merchant settings, select the "**API Keys**" tab, and click the "**Add**" button.

<figure><img src="../../../.gitbook/assets/image%20(371)_eng.png" alt=""><figcaption></figcaption></figure>

Fill in the required fields and click the "**Save**" button.

<figure><img src="../../../.gitbook/assets/image%20(370)_eng.png" alt="" width="363"><figcaption></figcaption></figure>

{% hint style="info" %}
Select one or both options for "**Receive Funds/Withdraw Funds**" depending on the intended use of the merchant.

It's advisable to add your server's IP address under "**Trusted IPs**."
{% endhint %}

<figure><img src="../../../.gitbook/assets/Arc_qmcPit3Hgb (1).png" alt="" width="352"><figcaption></figcaption></figure>

Save the generated key in a text file and click the "**Done**" button.

## Module Settings

In the admin panel, create a new merchant in the "**Merchants**" -> "**Add Merchant**" section.

Select Alfabit Crypto from the dropdown list in the "**Module**" field, provide a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/Arc_NAxwA0DrS1 (1).png" alt="" width="473"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image%20(372)_eng.png" alt="" width="458"><figcaption></figcaption></figure>

**API Key** — **public key** generated in your Alfabit account.

## Special Fields

<figure><img src="../../../.gitbook/assets/Arc_wNtMcO8Eyp (1).png" alt="" width="455"><figcaption></figcaption></figure>

**Currency** — select the currency for receiving funds or choose "**Automatically**" (in this case, the wallet address will be requested according to the currency code from the exchange direction where the merchant is connected; the list of methods will only be displayed after entering the correct API key for module authorization).

<figure><img src="../../../.gitbook/assets/image (1790)_eng.png" alt="" width="435"><figcaption></figcaption></figure>

{% hint style="warning" %}
Please pay attention to the minimum amounts for receiving the currencies you are using (found in the "**Merchants**" section, under the "**Rates**" tab in your Alfabit account) — the amounts for requests must exceed the minimum amounts; otherwise, the merchant will not process the payment:\
![](<../../../.gitbook/assets/image (1797)_eng.png>)
{% endhint %}

**Convert to** — select the currency to which the payment will be converted (at the merchant's rate at the time of conversion) or choose "**None**" to disable conversion. The tooltip below the field indicates the possible pairs for currency conversion (the list of methods will only be displayed after entering the correct API key for module authorization).

<figure><img src="../../../.gitbook/assets/image (1894)_eng.png" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
Please note that requests with amounts equivalent to <12 USDT will not be converted (merchant-side restrictions) when the option is enabled — funds for such requests will arrive in the original currency.

<img src="../../../.gitbook/assets/image (1788)_eng.png" alt="" data-size="original">
{% endhint %}

## Continuing the Setup

Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/main/en/en/basic-settings/merchants-and-auto-payments/merchants/general-merchant-settings).
