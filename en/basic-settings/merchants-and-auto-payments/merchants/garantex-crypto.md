# Garantex Crypto

{% hint style="info" %}
If you need to update the module on the server, please refer to the [instructions](https://premium.gitbook.io/main/en/basic-settings/faq/kak-obnovit-faily-na-servere#moduli-merchantov).
{% endhint %}

## Settings in the Merchant's Personal Account

Register on the [Garantex](https://garantex.org/) website. After your registration is confirmed by the service, log into your personal account. Enable 2FA for your account.

<figure><img src="../../../.gitbook/assets/image (641)_eng.png" alt=""><figcaption></figcaption></figure>

Once you are logged into your personal account, submit a request to customer support to enable the API for your account.

<figure><img src="../../../.gitbook/assets/image (640)_eng.png" alt="" width="516"><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (636)_eng.png" alt="" width="325"><figcaption></figcaption></figure>

After API access is granted, go to the "Settings" section and create a new access key.

<figure><img src="../../../.gitbook/assets/image (637)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

Save the data highlighted in the frame to a text file.

<figure><img src="../../../.gitbook/assets/image (643)_eng.png" alt=""><figcaption></figcaption></figure>

Navigate to the created key by clicking the "**View / Edit**" button.

<figure><img src="../../../.gitbook/assets/image (644)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

For working with the merchant to accept funds, the "**Readonly**" method is sufficient; do not check other methods. It is advisable to specify your server's IP address in the "IPs" field for enhanced security when working with the merchant.

<figure><img src="../../../.gitbook/assets/image (645)_eng.png" alt=""><figcaption></figcaption></figure>

## Module Settings

In the admin panel, create a new merchant in the "**Merchants**" -> "**Add Merchant**" section.

Select the Garantex module from the dropdown list in the "**Module**" field, provide a name for the module, and click "**Save**".

<figure><img src="../../../.gitbook/assets/image (638)_eng.png" alt="" width="494"><figcaption></figcaption></figure>

Fill in the required authorization fields. You can choose any domain as the host.

<figure><img src="../../../.gitbook/assets/image (639)_eng.png" alt="" width="414"><figcaption></figcaption></figure>

**Private Key** — the private key generated in Garantex when creating API access (field "**Private Key**").

**UID** — the access ID generated in Garantex when creating API access (field "**API UID**").

## Special Fields

<figure><img src="../../../.gitbook/assets/image (646)_eng.png" alt=""><figcaption></figcaption></figure>

* "**Required Number of Transaction Confirmations**" — a confirmed transaction means it has been included in a block and, therefore, in the blockchain. It has been verified and recorded, the payment has been processed, and it cannot be changed or canceled. To be considered legitimate, the operation must receive a certain number of confirmations. Each new confirmation exponentially reduces the risk of the transaction being canceled.

{% hint style="info" %}
- <mark style="color:green;">Recommended!</mark> Set the value to 0 so that the request is considered paid only after receiving the required number of confirmations on the exchange.
- <mark style="color:red;">Not recommended!</mark> If you set a value other than 0, the exchange will change the status of the request to "Paid" according to this setting, regardless of the transaction status displayed in the exchange's payment history. By enabling this option, you accept any potential risks.
{% endhint %}

## Continuing the Setup

Next, proceed to configure the merchant by following the [general setup instructions](https://premium.gitbook.io/main/en/en/basic-settings/merchants-and-auto-payments/merchants/general-merchant-settings).
