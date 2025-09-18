# WestWallet

{% hint style="info" %}
If you need to update the module on the server, please refer to the [instructions](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat).
{% endhint %}

## Settings in the Merchant's Personal Account

Register on the [WestWallet](https://westwallet.io/) website. After your registration is confirmed by the service, log in to your personal account and navigate to the "**Settings**" section.

<figure><img src="../../../.gitbook/assets/image (1412).png" alt=""><figcaption></figcaption></figure>

In the "**API Keys**" section, click the "**Add API Key**" button.

<figure><img src="../../../.gitbook/assets/image (1414).png" alt="" width="563"><figcaption></figcaption></figure>

In the window that opens, select the necessary permissions based on how you will work with the merchant (to receive funds, it is sufficient to choose "**Generate Addresses**" and "**Check Transaction Status**").

It is also advisable to specify the IP address of your server for enhanced security when working with the merchant.

Save the public and private key data in a text file. Click the "**Save**" button.

<figure><img src="../../../.gitbook/assets/image (1413).png" alt="" width="438"><figcaption></figcaption></figure>

## Module Settings

In the admin panel, create a new merchant in the "**Merchants**" -> "**Add Merchant**" section.

Select WestWallet from the dropdown list in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (1415).png" alt="" width="563"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (1416).png" alt="" width="461"><figcaption></figcaption></figure>

**Number of confirmations required for a payment to be considered completed** — a confirmed payment means that it has been included in a block and, consequently, in the blockchain. The payment has been verified and recorded, and it cannot be altered or canceled. To be legitimate, the transaction must receive a certain number of confirmations. Each new confirmation exponentially reduces the risk of the transaction being reversed.

{% hint style="info" %}
* <mark style="color:green;">Recommended!</mark> Set the value to 0 so that the request is considered paid only after receiving the required number of confirmations on the exchange.
* <mark style="color:red;">Not recommended!</mark> If you set a value other than 0, the exchange will change the status of the request to "Paid" according to this setting, regardless of the transaction status displayed in the payment history of the exchange. By enabling this option, you accept any associated risks.
{% endhint %}

**Public Key** — the public key generated in the WestWallet personal account.

**Private Key** — the private key generated in the WestWallet personal account.

## Continuing the Setup

Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).