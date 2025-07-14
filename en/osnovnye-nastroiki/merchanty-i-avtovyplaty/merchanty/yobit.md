# Yobit

{% hint style="info" %}
If you need to update the module on your server, please follow the [instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-merchantov).
{% endhint %}

## Merchant Account Settings

Submit a registration request on the [Yobit website](https://yobit.net/). After your registration is approved by the service, log in to your personal account.

Go to the [**API Keys** section](https://yobit.net/ru/api/keys/) and create a new key with permissions depending on how you plan to work with the merchant:

<figure><img src="../../../.gitbook/assets/image (1407).png" alt="" width="563"><figcaption></figcaption></figure>

* **info only** – view transaction history only (not used)
* **info & trade & deposits** – view transaction history and receive funds into the merchant’s accounts (receive funds only)
* **info & trade & deposits & withdrawals** – view transaction history, receive funds, and make payouts using the merchant’s accounts (both receiving and paying out funds)

After selecting the access rights, click "**Create new key**". The key will appear below but will be inactive. To activate it, follow the instructions sent to your email.

<figure><img src="../../../.gitbook/assets/image (1408).png" alt=""><figcaption></figcaption></figure>

Confirm the key activation and save the key and secret to a text file.

## Module Settings

In the admin panel, create a new merchant under "**Merchants**" -> "**Add Merchant**."

Select Yobit from the dropdown menu in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (1409).png" alt="" width="533"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (1410).png" alt="" width="453"><figcaption></figcaption></figure>

**API Key** – the public key generated in your Yobit account (the "**Key**" field)

**API Secret** – the private key generated in your Yobit account (the "**Secret**" field)

## Special Fields

<figure><img src="../../../.gitbook/assets/image (1350).png" alt=""><figcaption></figcaption></figure>

**Required Number of Transaction Confirmations** – A confirmed transaction means it has been included in a block and, consequently, in the blockchain. It has been verified and recorded, the payment has been processed, and it cannot be altered or reversed. For a transaction to be considered valid, it must receive a certain number of confirmations. Each additional confirmation exponentially reduces the risk of the transaction being reversed.

{% hint style="info" %}
* <mark style="color:green;">Recommended!</mark> Set the value to 0 so that the order is considered paid only after the required number of confirmations is received on the exchange.
* <mark style="color:red;">Not recommended!</mark> If you set a value other than 0, the exchanger will mark the order as "Paid" according to this setting, regardless of the transaction status shown in the exchange’s payment history. By enabling this option, you accept the associated risks.
{% endhint %}

## Continuing the Setup

Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).