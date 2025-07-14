# WestWallet

{% hint style="danger" %}
<mark style="color:red;">Before setting up auto payouts, be sure to read</mark> [<mark style="color:blue;">the risk warning</mark>](https://premiumexchanger.com/wiki/preduprezhdenie-auto/)<mark style="color:blue;">!</mark>
{% endhint %}

{% hint style="info" %}
If you need to update the module on your server, please follow this [instruction](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-avtovyplat).
{% endhint %}

{% hint style="danger" %}
Please note that when updating the WestWallet auto payout module files on your server, the transaction fee setting will reset to **medium**.

If you had selected a value other than **medium** before the update, please reselect it in the module settings!
  
![](<../../../.gitbook/assets/image (1742).png>)
{% endhint %}

## Merchant Account Settings

Register on the [WestWallet website](https://westwallet.io/). After your registration is confirmed by the service, log in to your personal account and go to the "**Settings**" section.

<figure><img src="../../../.gitbook/assets/image (1412).png" alt=""><figcaption></figcaption></figure>

In the "**API Keys**" section, click the "**Add API Key**" button.

<figure><img src="../../../.gitbook/assets/image (1414).png" alt="" width="563"><figcaption></figcaption></figure>

In the window that opens, select the necessary permissions depending on how you will work with the merchant account (to enable payouts, check all options except "**Generate Addresses**").

For enhanced security, it is also recommended to specify your server’s IP address.

Save the public and private keys to a text file. Then click "**Save**".

<figure><img src="../../../.gitbook/assets/image (1413).png" alt="" width="438"><figcaption></figcaption></figure>

## Module Settings

In the admin panel, create a new merchant under "**Auto Payouts**" -> "**Add Auto Payout**."

Select WestWallet from the dropdown menu in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (689).png" alt="" width="505"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure src="../../../.gitbook/assets/image (690).png" alt="" width="453"><figcaption></figcaption></figure>

**Public Key** — the public key generated in your WestWallet personal account

**Private Key** — the private key generated in your WestWallet personal account

### Continuing Setup



Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-avtovyplat).

## **Special Fields**

<figure><img src="../../../.gitbook/assets/image (691).png" alt=""><figcaption></figcaption></figure>

**Transaction Fee** — select the fee rate that the service will charge for providing its services. The higher the fee, the faster the payout will be processed.

{% hint style="danger" %}
Please note that if you select the "**low**" option, the payout will be processed within 36-48 hours.

![](<../../../.gitbook/assets/image (1632).png>)
{% endhint %}