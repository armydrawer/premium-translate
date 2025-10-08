# WestWallet

{% hint style="danger" %}
<mark style="color:red;">Before setting up auto payouts, please read the</mark> [<mark style="color:blue;">risk warning</mark>](https://premium.gitbook.io/main/en/basic-settings/merchants-and-auto-payments/auto-payments/risk-warning)<mark style="color:blue;">!</mark>
{% endhint %}

{% hint style="info" %}
If you need to update the module on the server, please refer to the [instructions](https://premium.gitbook.io/main/en/en/basic-settings/faq/updating-script-files-on-the-server/how-to-update-files-on-the-server#merchant-and-auto-payout-modules).
{% endhint %}

{% hint style="danger" %}
Please note that when updating the auto payout module files for WestWallet on the server, the transaction fee setting will reset to **medium**.

If you had selected a value other than **medium** before the update, please reselect it in the module settings!

![](<../../../.gitbook/assets/image (1742)_eng.png>)
{% endhint %}

## Merchant Account Settings

Register on the [WestWallet](https://westwallet.io/) website. After your registration is confirmed by the service, log in to your account and go to the "**Settings**" section.

<figure><img src="../../../.gitbook/assets/image (1412)_eng.png" alt=""><figcaption></figcaption></figure>

In the "**API Keys**" section, click the "**Add API Key**" button.

<figure><img src="../../../.gitbook/assets/image (1414)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

In the window that opens, select the necessary permissions based on how you will work with the merchant (to process payouts, you need to check all options except "**Generate Addresses**").

It is also advisable to specify your server's IP address for enhanced security when working with the merchant.

Save the public and private keys in a text file. Click the "**Save**" button.

<figure><img src="../../../.gitbook/assets/image (1413)_eng.png" alt="" width="438"><figcaption></figcaption></figure>

## Module Settings

In the admin panel, create a new merchant in the "**Auto Payouts**" -> "**Add Auto Payout**" section.

Select WestWallet from the dropdown list in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (689)_eng.png" alt="" width="505"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (690)_eng.png" alt="" width="453"><figcaption></figcaption></figure>

**Public Key** — the public key generated in your WestWallet account.

**Private Key** — the private key generated in your WestWallet account.

### Continuing the Setup

Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/main/en/basic-settings/merchants-and-auto-payments/auto-payments/obshie-nastroiki-avtovyplat).

## **Special Fields**

<figure><img src="../../../.gitbook/assets/image (691)_eng.png" alt=""><figcaption></figcaption></figure>

**Transaction Fee** — select the fee amount that will be charged by the service for providing its services. The higher the fee, the faster the payout will be processed.

{% hint style="danger" %}
Please note that if you select the "**low**" option, the payout will be processed within 36-48 hours.

![](<../../../.gitbook/assets/image (1632)_eng.png>)
{% endhint %}