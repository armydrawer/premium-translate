# OTC

{% hint style="danger" %}
<mark style="color:red;">Before setting up auto payouts, please read the</mark> [<mark style="color:blue;">risk warning</mark>](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/preduprezhdenie-o-riskakh)<mark style="color:blue;">!</mark>
{% endhint %}

{% hint style="info" %}
If you need to update the module on the server, please refer to the [instructions](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat).
{% endhint %}

## Merchant Account Settings

Register in the [OTC](https://globalotc.ru/auth) system.

Log into your account, then go to the "**API**" section and generate your API keys.

<figure><img src="../../../.gitbook/assets/image%20(722)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

Click the "**Create API Keys**" button and enter a name for the keys in the pop-up window.

<figure><img src="../../../.gitbook/assets/image%20(723)_eng.png" alt=""><figcaption></figcaption></figure>

After entering the name, click "**Create**" — a pair of keys will be displayed in the form.

<figure><img src="../../../.gitbook/assets/image%20(724)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

Copy them by clicking the copy buttons and save them in a text file.

<figure><img src="../../../.gitbook/assets/image%20(725)_eng.png" alt="" width="194"><figcaption></figcaption></figure>

## **Module Settings**

In the admin panel, create a new merchant in the "**Auto Payouts**" -> "**Add Auto Payout**" section.

Select OTC from the dropdown list in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image%20(726)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image%20(727)_eng.png" alt=""><figcaption></figcaption></figure>

**API Key** - The API key generated in your OTC account when creating the API key.

**Secret Key** - The secret key generated in your OTC account when creating the API key.

## Special Fields

<figure><img src="../../../.gitbook/assets/image%20(688)_eng.png" alt=""><figcaption></figcaption></figure>

**Payment Method** — Choose the currency/bank from the dropdown list that will be used for the payout.

<figure><img src="../../../.gitbook/assets/image%20(506)_eng.png" alt=""><figcaption></figcaption></figure>

**Conversion from USDT** — Activates payouts from USDT without the need to hold **rubles** in OTC accounts (the conversion from USDT to RUB for payouts will be done at the exchange rate at the time of the payout request) — <mark style="color:red;">**this option only works for payouts in RUB**</mark>

{% hint style="warning" %}
When making payouts in AZN, EUR, or USD using the merchant, it is **necessary** to add additional fields to the exchange form for the client to fill out when creating a request.

To do this, add [additional fields](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/valyuty-i-napravleniya/dobavlenie-novoi-valyuty#vkladka-dop.-polya) to the corresponding currencies:\
![](../../../.gitbook/assets/image%20\(730\)_eng.png)![](../../../.gitbook/assets/image%20\(731\)_eng.png)

Make sure to specify the "**Unique ID**" field (use lowercase names):\
• `get_cardholder` (field "[**Full Name**](#user-content-fn-1)[^1]")

• `get_cardexpire` (field "[**Card Expiration Date**](#user-content-fn-1)[^1]")

Example of filling out the additional field "**Card Expiration Date**"\
![](../../../.gitbook/assets/image%20\(732\)_eng.png)
{% endhint %}

{% hint style="warning" %}
When making payouts via SBP, rename the "**To Account**" field to "**Your Phone Number**" in the currency settings under the "**Field Settings**" tab, and ensure that only numbers are available for filling in the exchange form.\
The **minimum** payout limit via SBP is **10,000 RUB**.

<img src="../../../.gitbook/assets/image%20(1406)_eng.png" alt="" data-size="original">
{% endhint %}

{% hint style="warning" %}
Additionally, when making payouts via SBP, you can offer the client a choice of bank on the exchange page (the choice of **payment method** in the module settings will not matter — select any item from the list).

To do this, add an [additional field for the **payout currency**](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/valyuty-i-napravleniya/dobavlenie-novoi-valyuty#vkladka-dop.-polya) with the type of additional field "**Choice**," specifying the following settings (the names of the banks and their codes are shown in the screenshot below; you can only include the banks you use in the additional field settings):\
![](../../../.gitbook/assets/image%20\(507\)_eng.png)

• Correctly filled additional field with unique ID — **bankname:**

![](../../../.gitbook/assets/image%20\(509\)_eng.png)\
\&#xNAN;**`Sberbank / Sber`**\
&#xNAN;**`Tinkoff / Tinkoff Bank`**\
&#xNAN;**`VTB Bank`**\
&#xNAN;**`ALFA-BANK`**\
&#xNAN;**`Raiffeisenbank`**\
&#xNAN;**`OPEN BANK`**\
&#xNAN;**`Gazprombank`**\
&#xNAN;**`Promsvyazbank`**\
&#xNAN;**`Home Credit`**

After adding the field, it will appear in the exchange form, allowing the client to select a bank from the list from which they will receive funds from the exchanger.

<img src="../../../.gitbook/assets/image%20(510)_eng.png" alt="" data-size="original">
{% endhint %}

## Continuing the Setup

Next, proceed to configure the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-merchantov-avtovyplat).

[^1]: The field can have any name.
