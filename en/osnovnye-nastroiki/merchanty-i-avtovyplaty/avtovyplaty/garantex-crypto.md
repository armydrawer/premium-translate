# Garantex Crypto

{% hint style="danger" %}
<mark style="color:red;">Before setting up automatic payouts, please read the</mark> [<mark style="color:blue;">risk warning</mark>](https://premiumexchanger.com/wiki/preduprezhdenie-auto/)<mark style="color:blue;">!</mark>
{% endhint %}

{% hint style="info" %}
If you need to update the module on the server, please refer to the [instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-avtovyplat).
{% endhint %}

## Merchant Account Settings

Register on the [Garantex](https://garantex.org/) website. After your registration is confirmed by the service, log in to your account. Enable 2FA for your account.

<figure><img src="../../../.gitbook/assets/image (641).png" alt=""><figcaption></figcaption></figure>

Once logged into your account, submit a request to customer support to enable the API for your account.

<figure><img src="../../../.gitbook/assets/image (640).png" alt="" width="516"><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (636).png" alt="" width="325"><figcaption></figcaption></figure>

After API access is granted, go to the "Settings" section and create a new access key.

<figure><img src="../../../.gitbook/assets/image (637).png" alt="" width="563"><figcaption></figcaption></figure>

Save the data highlighted in the box to a text file.

<figure><img src="../../../.gitbook/assets/image (643).png" alt=""><figcaption></figcaption></figure>

Navigate to the created key by clicking on the "**View / Edit**" button.

<figure><img src="../../../.gitbook/assets/image (644).png" alt="" width="563"><figcaption></figcaption></figure>

To work with the merchant for fund withdrawals, you need to activate the "**Withdraw**" method. If you plan to use automatic conversion for purchasing currency for payouts, activate the "**Trading**" method.

**Make sure** to specify your server's IP address in the "IPs" field for enhanced security when working with the merchant.

<figure><img src="../../../.gitbook/assets/image (645).png" alt=""><figcaption></figcaption></figure>

## **Module Settings**

In the admin panel, create a new merchant in the "**Automatic Payouts**" -> "**Add Automatic Payout**" section.

Select Garantex Crypto from the dropdown menu in the "**Module**" field, provide a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (623).png" alt="" width="474"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (633).png" alt="" width="431"><figcaption></figcaption></figure>

**Private Key** — the private key generated in Garantex when creating API access (field "**Private Key**")

**UID** — the access ID generated in Garantex when creating API access (field "**API UID**")

**Host** — choose any domain

## Special Fields

<figure><img src="../../../.gitbook/assets/image (1480).png" alt=""><figcaption></figcaption></figure>

* **Buy the missing crypto amount for payout:**\
  • **No** — the payout will be made directly from the balance of the specified currency\
  • **Yes** — if there is not enough currency for the payout, the missing amount will be purchased at the market rate and the full amount will be paid out (the balance of the paid currency will be zero after the payout)\
  • **Buy and do not withdraw** — the full amount will be purchased at the market rate in the payout currency for storage on the balance (the balance of the currency will remain the same as before the payout)\
  • **Buy the entire amount** — the full amount will be purchased at the market rate in the payout currency for subsequent payout (the balance in the specified currency will not be affected)
* **Determine the trading operation code:**\
  • **Automatically** — the currency for purchasing the payout currency will be selected automatically based on your currency balances with the merchant\
  • **Manually** — the currency from the "**Trading Operation Code**" field will be used
* **Trading Operation Code (if Manual)** — specify the currency for manual purchase (usually USDT)

## Continuing the Setup

Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-merchantov-avtovyplat).