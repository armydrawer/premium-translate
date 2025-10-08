# Yobit

{% hint style="danger" %}
<mark style="color:red;">Before setting up auto payouts, please read the</mark> [<mark style="color:blue;">risk warning</mark>](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/preduprezhdenie-o-riskakh)<mark style="color:blue;">!</mark>
{% endhint %}

{% hint style="info" %}
If you need to update the module on the server, please refer to the [instructions](https://premium.gitbook.io/main/en/basic-settings/faq/updating-script-files-on-the-server/how-to-update-files-on-the-server#merchant-and-auto-payout-modules).
{% endhint %}

## Merchant Account Settings

Submit a registration request on the [Yobit](https://yobit.net/) website. After your registration is confirmed by the service, log in to your personal account.

Go to the [**API Keys**](https://yobit.net/ru/api/keys/) section and generate a new key with permissions based on how you will work with the merchant:

<figure><img src="../../../.gitbook/assets/image (1407)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

* **info only** - view transaction history only (not used)
* **info & trade & deposits** - view transaction history and accept funds into merchant accounts (accepting funds only)
* **info & trade & deposits & withdrawals** - view transaction history, accept funds, and make payouts using merchant accounts (accepting and paying out funds) - **choose this option if you will be making payouts**

After selecting the permissions and clicking the "**Create New Key**" button, the key will appear in the block below but will be inactive. To activate it, follow the instructions sent to your email.

<figure><img src="../../../.gitbook/assets/image (1408)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

Confirm the activation of the key and save the key and secret data in a text file.

## **Module Settings**

In the admin panel, create a new merchant in the "**Auto Payouts**" -> "**Add Auto Payout**" section.

Select Yobit from the dropdown list in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (705)_eng.png" alt="" width="507"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (1410)_eng.png" alt="" width="453"><figcaption></figcaption></figure>

**API Key** — the public key generated in your Yobit account (field "**Key**")

**API Secret** — the private key generated in your Yobit account (field "**Secret**")

## Special Fields

<figure><img src="../../../.gitbook/assets/image (1514)_eng.png" alt=""><figcaption></figcaption></figure>

**Purchase the missing crypto amount for payouts** — options for auto-purchasing currency for payouts:\
• **No** — do not purchase currency for payouts, pay directly from the wallet (the wallet must have a sufficient reserve of the currency being paid out)\
• **Yes** — auto-purchase currency for payouts only when there is an insufficient reserve of the currency being paid out\
• **Purchase and do not withdraw** — auto-purchase the currency being paid out to restore the reserve level after paying out currency directly from the wallet

**Trade Operation Code** — select the currency code from the dropdown list that will be used to purchase currency for payouts (usually USDT TRC20 is used)

{% hint style="warning" %}
Possible pairs for buying/selling currency:

* BTC - USDT ERC20
* BTC - ETH
* ETH - BTC
* ETH - RUR
* RUR - ETH
* USDT ERC20 - BTC
* USDT ERC20 - USDT TRC20
* USDT TRC20 - USDT ERC20
{% endhint %}

## Continuing the Setup

Next, proceed to configure the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-avtovyplat).