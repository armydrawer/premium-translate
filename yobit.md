# Yobit

{% hint style="info" %}
If you need to update a module on the server, please refer to the [instructions](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat).
{% endhint %}

## Merchant Account Settings

Submit a registration request on the [Yobit](https://yobit.net/) website. After your registration is confirmed by the service, log in to your personal account.

Go to the [“API Keys” section](https://yobit.net/ru/api/keys/) and generate a new key with permissions based on how you plan to work with the merchant:

<figure><img src="../../../.gitbook/assets/image (1407)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

* **info only** - view transaction history only (not used)
* **info & trade & deposits** - view transaction history and accept funds into merchant accounts (accepting funds only)
* **info & trade & deposits & withdrawals** - view transaction history, accept funds, and make withdrawals using merchant accounts (accepting and withdrawing funds)

After selecting the permissions and clicking the “**Create New Key**” button, the key will appear in the block below but will be inactive. To activate it, follow the instructions sent to your email.

<figure><img src="../../../.gitbook/assets/image (1408)_eng.png" alt=""><figcaption></figcaption></figure>

Confirm the activation of the key and save the key and secret data in a text file.

## Module Settings

In the admin panel, create a new merchant in the “**Merchants**” -> “**Add Merchant**” section.

Select Yobit from the dropdown list in the “**Module**” field, enter a name for the module, and click “**Save**.”

<figure><img src="../../../.gitbook/assets/image (1409)_eng.png" alt="" width="533"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (1410)_eng.png" alt="" width="453"><figcaption></figcaption></figure>

**API Key** - the public key generated in your Yobit account (field “**Key**”)

**API Secret** - the private key generated in your Yobit account (field “**Secret**”)

## Special Fields

<figure><img src="../../../.gitbook/assets/image (1350)_eng.png" alt=""><figcaption></figcaption></figure>

**Required Number of Transaction Confirmations** - a confirmed transaction means it has been included in a block and, therefore, in the blockchain. It has been verified and recorded, the payment has been processed, and it cannot be changed or canceled. To be considered legitimate, the operation must receive a certain number of confirmations. Each new confirmation exponentially reduces the risk of the transaction being canceled.

{% hint style="info" %}
* <mark style="color:green;">Recommended!</mark> Set the value to 0 so that the request is considered paid only after receiving the required number of confirmations on the exchange.
* <mark style="color:red;">Not recommended!</mark> If you set a value other than 0, the exchange will change the status of the request to "Paid" based on this setting, regardless of the transaction status displayed in the exchange's payment history. By enabling this option, you accept any potential risks.
{% endhint %}

## Continuing the Setup

Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).