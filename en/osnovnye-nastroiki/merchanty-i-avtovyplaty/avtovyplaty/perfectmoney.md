# PerfectMoney

{% hint style="danger" %}
<mark style="color:red;">Before setting up auto payouts, be sure to read</mark> [<mark style="color:blue;">the risk warning</mark>](https://premiumexchanger.com/wiki/preduprezhdenie-auto/)<mark style="color:blue;">!</mark>
{% endhint %}

{% hint style="info" %}
If you need to update the module on your server, please follow this [instruction](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-avtovyplat).
{% endhint %}

## Settings in the Merchant Dashboard

Register an account at [PerfectMoney](https://perfectmoney.com/). After your registration is confirmed by the service, log in to your personal dashboard.

Go to the "**Settings**" section.

<figure><img src="../../../.gitbook/assets/image (1484).png" alt="" width="563"><figcaption></figcaption></figure>

Navigate to the "**Security**" settings block.

<figure><img src="../../../.gitbook/assets/image (1489).png" alt=""><figcaption></figcaption></figure>

Enable the API for your account.

<figure><img src="../../../.gitbook/assets/image (1491).png" alt="" width="563"><figcaption></figcaption></figure>

Enter your server’s IP address in the API settings and save the changes.

<div align="left"><figure><img src="../../../.gitbook/assets/image (1492).png" alt="" width="563"><figcaption></figcaption></figure></div>

<figure><img src="../../../.gitbook/assets/image (1493).png" alt="" width="563"><figcaption></figcaption></figure>

By default, your account includes three wallets — USD, EUR, and GOLD. If needed, you can add a BTC wallet and create additional wallets for other currencies.

<figure><img src="../../../.gitbook/assets/image (1487).png" alt="" width="477"><figcaption></figcaption></figure>

## Module Settings

In the admin panel, create a new merchant under "**Auto Payouts**" -> "**Add Auto Payout**."

Select PerfectMoney from the "**Module**" dropdown, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (1497).png" alt="" width="467"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (1498).png" alt="" width="420"><figcaption></figcaption></figure>

**Account ID** — your PerfectMoney account ID

**Account Password** — your PerfectMoney account password

**USD/EUR/GOLD/BTC Wallets** — the wallet numbers from your PerfectMoney account (enter the wallets you plan to use — it’s not necessary to fill in all wallet fields)

## Special Fields

<figure><img src="../../../.gitbook/assets/image (1499).png" alt=""><figcaption></figcaption></figure>

**Transaction Type** — select the appropriate payout method

## Continuing Setup

Next, complete the merchant setup by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-merchantov-avtovyplat).