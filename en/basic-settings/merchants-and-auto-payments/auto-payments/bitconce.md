# Bitconce

## Merchant Account Settings

To get started, register or log in to the Bitconce system. Enter your Bitconce account by inputting your token:

<figure><img src="../../../.gitbook/assets/изображение (116)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

Next, navigate to the "API" section:

<figure><img src="../../../.gitbook/assets/изображение (92)_eng.png" alt="" width="341"><figcaption></figcaption></figure>

To obtain a token, click the "**Create**" button in the "API Token" section:

<figure><img src="../../../.gitbook/assets/изображение (100)_eng.png" alt=""><figcaption></figcaption></figure>

## Module Settings

In the admin panel, go to the "**Merchants**" -> "**Auto Payments**" section, click the "**Add**" button, and select Bitconce.

<figure><img src="../../../.gitbook/assets/image (1270)_eng.png" alt=""><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (1271)_eng.png" alt=""><figcaption></figcaption></figure>

**Token** — the token obtained from your Bitconce account.

## Special Fields

<figure><img src="../../../.gitbook/assets/image (1272)_eng.png" alt=""><figcaption></figcaption></figure>

**Direction** — select the bank for auto payments

* **qiwi** — payment from a Qiwi wallet
* **yandex** — payment from a YuMoney account
* **banks** — user-selected bank
* **SBP** — payment via SBP

{% hint style="info" %}
You can offer your client a choice of banks for making payments on the exchange page. To do this, select the "**banks**" option in the merchant settings and add an [additional field for the payment currency](https://premium.gitbook.io/main/en/basic-settings/valyuty-i-napravleniya/dobavlenie-novoi-valyuty#vkladka-dop.-polya), specifying the following settings (the module only works with the following banks — **Sberbank, Raiffeisen, Tinkoff**):

![](<../../../.gitbook/assets/image (247)_eng.png>)\
Once the field is added, it will appear in the exchange form, allowing the client to choose the bank from which they will receive funds from the exchanger.
{% endhint %}

## Continuing the Setup

Next, proceed to configure the auto payment merchant by following the [general setup instructions](https://premium.gitbook.io/main/en/basic-settings/merchants-and-auto-payments/auto-payments/obshie-nastroiki-merchantov-avtovyplat).