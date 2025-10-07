# Koshelek

{% hint style="danger" %}
<mark style="color:red;">Before setting up auto payouts, please read the</mark> [<mark style="color:blue;">risk warning</mark>](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/preduprezhdenie-o-riskakh)<mark style="color:blue;">!</mark>
{% endhint %}

{% hint style="info" %}
If you need to update the module on the server, please refer to the [instructions](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat).
{% endhint %}

## Merchant Account Settings

Register and verify your account with [Koshelek](https://koshelek.ru/). Go to the [**"API Keys"** page](https://koshelek.ru/account/keysApi) and click the "**Create API Key**" button.

<figure><img src="../../../.gitbook/assets/image (1757)_eng.png" alt=""><figcaption></figcaption></figure>

In the pop-up window, enter a name for the key and select the methods for API access (for fund payouts, choose "**Deposit**," "**Withdrawal**," and "**Read**"). Click the "**Save**" button.

<figure><img src="../../../.gitbook/assets/image (1761)_eng.png" alt="" width="467"><figcaption></figcaption></figure>

In the next window, copy the generated keys and save them in a text file.

<figure><img src="../../../.gitbook/assets/image (1760)_eng.png" alt="" width="474"><figcaption></figcaption></figure>

## Module Settings

In the admin panel, create a new merchant under the "**Auto Payouts**" section by clicking "**Add Auto Payout**."

Select Koshelek from the drop-down menu in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (1750)_eng.png" alt="" width="419"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (1753)_eng.png" alt="" width="426"><figcaption></figcaption></figure>

**Public Key** — **public ID** generated in your Koshelek account

**Secret Key** — **secret key** generated in your Koshelek account

## Special Fields

<figure><img src="../../../.gitbook/assets/image (1754)_eng.png" alt="" width="302"><figcaption></figcaption></figure>

**Network** — specify the currency network for the auto payout to function correctly

## Continuing the Setup

Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-merchantov-avtovyplat).