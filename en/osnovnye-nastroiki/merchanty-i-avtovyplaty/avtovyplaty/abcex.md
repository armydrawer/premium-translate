# ABCEx

{% hint style="danger" %}
<mark style="color:red;">Before setting up auto payouts, be sure to read</mark> [<mark style="color:blue;">the risk warning</mark>](https://premiumexchanger.com/wiki/preduprezhdenie-auto/)<mark style="color:blue;">!</mark>
{% endhint %}

{% hint style="info" %}
If you need to update the module on your server, please follow this [instruction](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-avtovyplat).
{% endhint %}

## Merchant Account Settings <a href="#merchant-account-settings" id="merchant-account-settings"></a>

Register on the exchange [ABCEx](https://abcex.io/). Complete the KYC process and enable 2FA in your account under the "**Profile**" section.

<figure><img src="../../../.gitbook/assets/image (223).png" alt=""><figcaption></figcaption></figure>

## Module Settings <a href="#module-settings" id="module-settings"></a>

In the admin panel, create a new merchant by going to "**Auto Payouts**" -> "**Add Auto Payout**."

Select ABCEx from the dropdown menu in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (220).png" alt="" width="442"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (221).png" alt="" width="453"><figcaption></figcaption></figure>

**API Key** — the key provided to you by your ABCEx manager after completing KYC. To request an API key, contact [https://t.me/ABCEX_management](https://t.me/ABCEX_management).

## Special Fields

<figure><img src="../../../.gitbook/assets/image (222).png" alt="" width="368"><figcaption></figcaption></figure>

**Wallet** — select the currency you want to use for client payouts (currently, only USDT is supported).

**Network** — choose the appropriate network for the currency: ETH (ERC20) or TRX (TRC20).

## Continuing Setup

Next, complete the merchant setup by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-merchantov-avtovyplat).