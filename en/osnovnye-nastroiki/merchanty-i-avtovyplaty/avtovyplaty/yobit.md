# Yobit

{% hint style="danger" %}
<mark style="color:red;">Before setting up auto payouts, be sure to read</mark> [<mark style="color:blue;">the risk warning</mark>](https://premiumexchanger.com/wiki/preduprezhdenie-auto/)<mark style="color:blue;">!</mark>
{% endhint %}

{% hint style="info" %}
If you need to update the module on your server, please follow this [instruction](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-avtovyplat).
{% endhint %}

## Merchant Account Settings

Submit a registration request on the [Yobit website](https://yobit.net/). After your registration is confirmed by the service, log in to your personal account.

Go to the [**API Keys** section](https://yobit.net/ru/api/keys/) and create a new key with permissions depending on how you plan to work with the merchant:

<figure><img src="../../../.gitbook/assets/image (1407).png" alt="" width="563"><figcaption></figcaption></figure>

* **info only** – view transaction history only (not used)
* **info & trade & deposits** – view transaction history and receive funds into the merchant’s accounts (receive funds only)
* **info & trade & deposits & withdrawals** – view transaction history, receive funds, and make payouts using the merchant’s accounts (both receiving and paying out funds) – **choose this option if you will be making payouts**

After selecting the permissions and clicking "**Create new key**," the key will appear below but will be inactive. To activate it, follow the instructions sent to your email.

<figure><img src="../../../.gitbook/assets/image (1408).png" alt=""><figcaption></figcaption></figure>

Confirm the key activation and save the key and secret in a text file.

## Module Settings

In the admin panel, create a new merchant under "**Auto Payouts**" -> "**Add Auto Payout**."

Select Yobit from the dropdown menu in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (705).png" alt="" width="507"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (1410).png" alt="" width="453"><figcaption></figcaption></figure>

**API Key** — the public key generated in your Yobit personal account (the "**Key**" field)

**API Secret** — the private key generated in your Yobit personal account (the "**Secret**" field)

## Special Fields

<figure><img src="../../../.gitbook/assets/image (1514).png" alt=""><figcaption></figcaption></figure>

**Purchasing the missing crypto amount needed for payout** — options for auto-buying currency for payouts:  
• **No** — do not buy currency for payout; pay out directly from the wallet (the wallet must have a sufficient reserve of the payout currency)  
• **Yes** — auto-buy the payout currency only if the wallet’s reserve of that currency is insufficient  
• **Buy and do not withdraw** — auto-buy the payout currency to replenish the reserve after paying out directly from the wallet  

**Trading operation code** — select the currency code from the dropdown list that will be used to purchase the payout currency (usually USDT TRC20)  

{% hint style="warning" %}  
Possible currency pairs for buying/selling:  

* BTC - USDT ERC20  
* BTC - ETH  
* ETH - BTC  
* ETH - RUR  
* RUR - ETH  
* USDT ERC20 - BTC  
* USDT ERC20 - USDT TRC20  
* USDT TRC20 - USDT ERC20  
{% endhint %}  

## Continuing setup  

Next, proceed with configuring the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-avtovyplat).