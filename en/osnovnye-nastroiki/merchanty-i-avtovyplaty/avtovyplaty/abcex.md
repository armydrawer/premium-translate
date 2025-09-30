# ABCEx

{% hint style="danger" %}
<mark style="color:red;">Before setting up auto payouts, please read the</mark> [<mark style="color:blue;">risk warning!</mark>](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/preduprezhdenie-o-riskakh)
{% endhint %}

{% hint style="info" %}
If you need to update the module on the server, please refer to the [instructions](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat)
{% endhint %}

## Merchant Account Settings <a href="#nastroiki-v-lichnom-kabinete-merchanta" id="nastroiki-v-lichnom-kabinete-merchanta"></a>

Register on the [ABCEx](https://abcex.io/) exchange. Complete the KYC process and enable 2FA in your account under the "**Profile**" section.

<figure><img src="../../../.gitbook/assets/image (223)_eng.png" alt=""><figcaption></figcaption></figure>

## Module Settings <a href="#nastroiki-modulya" id="nastroiki-modulya"></a>

In the admin panel, create a new merchant in the "**Auto Payouts**" -> "**Add Auto Payout**" section.

Select ABCEx from the dropdown menu in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (220)_eng.png" alt="" width="442"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (221)_eng.png" alt="" width="453"><figcaption></figcaption></figure>

**API Key** — This is the key sent to you by your ABCEx manager after completing KYC. To request your API key, contact [https://t.me/ABCEX_management](https://t.me/ABCEX_management).

## Special Fields

<figure><img src="../../../.gitbook/assets/image (222)_eng.png" alt="" width="368"><figcaption></figcaption></figure>

**Wallet** — Select the currency for client payouts (currently, only USDT is available).

**Network** — Choose the appropriate network for the currency: ETH (ERC20) or TRX (TRC20).

## Continuing the Setup

Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-merchantov-avtovyplat).