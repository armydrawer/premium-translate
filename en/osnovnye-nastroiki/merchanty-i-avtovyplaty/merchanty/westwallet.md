# WestWallet

{% hint style="info" %}
If you need to update the module on your server, please follow the [instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-merchantov).
{% endhint %}

## Merchant Account Settings

Register on the [WestWallet website](https://westwallet.io/). After your registration is confirmed by the service, log in to your personal account and go to the "**Settings**" section.

<figure><img src="../../../.gitbook/assets/image (1412).png" alt=""><figcaption></figcaption></figure>

In the "**API Keys**" section, click the "**Add API Key**" button.

<figure><img src="../../../.gitbook/assets/image (1414).png" alt="" width="563"><figcaption></figcaption></figure>

In the window that appears, select the necessary permissions depending on how you plan to work with the merchant (to receive payments, it’s enough to select "**Generate Addresses**" and "**Check Transaction Status**").

For added security, it’s also recommended to specify your server’s IP address.

Save the public and private keys to a text file. Then click "**Save**".

<figure><img src="../../../.gitbook/assets/image (1413).png" alt="" width="438"><figcaption></figcaption></figure>

## Module Settings

In the admin panel, create a new merchant by going to "**Merchants**" -> "**Add Merchant**."

Select WestWallet from the dropdown menu in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (1415).png" alt="" width="563"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (1416).png" alt="" width="461"><figcaption></figcaption></figure>

**Number of confirmations required to consider a payment complete** — a confirmed payment means it has been included in a block and thus added to the blockchain. The payment is verified and recorded; it cannot be altered or reversed. For a transaction to be considered valid, it must receive a certain number of confirmations. Each additional confirmation exponentially reduces the risk of the transaction being reversed.

{% hint style="info" %}
* <mark style="color:green;">Recommended!</mark> Set the value to 0 so that the order is considered paid only after the required number of confirmations is received on the exchange.
* <mark style="color:red;">Not recommended!</mark> If you set a value other than 0, the exchanger will change the order status to "Paid" according to this setting, regardless of the transaction status shown in the exchange’s payment history. By enabling this option, you accept the associated risks.
{% endhint %}

**Public Key** — the public key generated in the WestWallet personal account

**Private Key** — the private key generated in the WestWallet personal account

## Continuing the setup

Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).