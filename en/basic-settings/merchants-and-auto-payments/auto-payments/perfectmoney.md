# PerfectMoney

{% hint style="danger" %}
<mark style="color:red;">Before setting up auto payouts, please read the</mark> [<mark style="color:blue;">risk warning</mark>](https://premiumexchanger.com/wiki/preduprezhdenie-auto/)<mark style="color:blue;">!</mark>
{% endhint %}

{% hint style="info" %}
If you need to update the module on the server, please refer to the [instructions](https://premium.gitbook.io/main/en/basic-settings/faq/kak-obnovit-faily-na-servere#moduli-avtovyplat).
{% endhint %}

## Settings in the Merchant's Personal Account

Register on the [PerfectMoney](https://perfectmoney.com/) website. After your registration is confirmed by the service, log in to your personal account.

Go to the "**Settings**" section.

<figure><img src="../../../.gitbook/assets/image (1484)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

Navigate to the settings in the "**Security**" block.

<figure><img src="../../../.gitbook/assets/image (1489)_eng.png" alt=""><figcaption></figcaption></figure>

Enable the API for your account.

<figure><img src="../../../.gitbook/assets/image (1491)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

Enter your server's IP address in the API settings and save the data.

<div align="left"><figure><img src="../../../.gitbook/assets/image (1492)_eng.png" alt="" width="563"><figcaption></figcaption></figure></div>

<figure><img src="../../../.gitbook/assets/image (1493)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

By default, three accounts are created for your account — USD, EUR, GOLD. If needed, you can add an account for BTC and create additional wallets for other currencies.

<figure><img src="../../../.gitbook/assets/image (1487)_eng.png" alt="" width="477"><figcaption></figcaption></figure>

## Module Settings

In the admin panel, create a new merchant in the "**Auto Payouts**" -> "**Add Auto Payout**" section.

Select PerfectMoney from the dropdown list in the "**Module**" field, provide a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (1497)_eng.png" alt="" width="467"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (1498)_eng.png" alt="" width="420"><figcaption></figcaption></figure>

**Account ID** — Your PerfectMoney account ID

**Account Password** — Your PerfectMoney account password

**USD/EUR/GOLD/BTC Accounts** — The account numbers from your PerfectMoney account (specify the accounts you plan to use — it's not necessary to fill in all account fields).

## Special Fields

<figure><img src="../../../.gitbook/assets/image (1499)_eng.png" alt=""><figcaption></figcaption></figure>

**Transaction Type** — Choose the appropriate payout method.

## Continuing the Setup

Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/main/en/basic-settings/merchants-and-auto-payments/auto-payments/obshie-nastroiki-merchantov-avtovyplat).