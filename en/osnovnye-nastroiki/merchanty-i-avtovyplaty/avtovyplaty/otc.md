# OTC

{% hint style="danger" %}
<mark style="color:red;">Before setting up auto payouts, be sure to read the</mark> [<mark style="color:blue;">risk warning</mark>](https://premiumexchanger.com/wiki/preduprezhdenie-auto/)<mark style="color:blue;">!</mark>
{% endhint %}

{% hint style="info" %}
If you need to update the module on your server, please follow the [instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-avtovyplat).
{% endhint %}

## Merchant Account Settings

Register an account in the [OTC system](https://globalotc.ru/auth).

Log in to your personal account, go to the "**API**" section, and generate your API keys.

<figure><img src="../../../.gitbook/assets/image (722).png" alt="" width="563"><figcaption></figcaption></figure>

Click the "**Create API Keys**" button and enter any name you like for the keys in the popup window.

<figure><img src="../../../.gitbook/assets/image (723).png" alt=""><figcaption></figcaption></figure>

After entering the name, click "**Create**" — the form will display a pair of keys.

<figure><img src="../../../.gitbook/assets/image (724).png" alt="" width="563"><figcaption></figcaption></figure>

Copy the keys by clicking the copy buttons and save them in a text file.

<figure><img src="../../../.gitbook/assets/image (725).png" alt="" width="194"><figcaption></figcaption></figure>

## **Module Settings**

In the admin panel, create a new merchant under "**Auto Payouts**" -> "**Add Auto Payout**."

Select OTC from the dropdown menu in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (726).png" alt="" width="563"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure src="../../../.gitbook/assets/image (727).png" alt=""><figcaption></figcaption></figure>

**API Key** – the API key generated in your OTC personal account when creating the API keys

**Secret Key** – the secret key generated in your OTC personal account when creating the API keys

## Special Fields

<figure><img src="../../../.gitbook/assets/image (688).png" alt=""><figcaption></figcaption></figure>

**Payment Method** — select the currency or bank from the dropdown list that will be used for payouts

<figure><img src="../../../.gitbook/assets/image (506).png" alt=""><figcaption></figcaption></figure>

**Convert from USDT** — enable payouts from USDT without needing to hold **rubles** in your OTC accounts (the exchange from USDT to RUB will be done at the market rate at the time of the payout request) — <mark style="color:red;">**this option works only for payouts in RUB**</mark>

Here is a natural English translation of the provided text:

---

{% hint style="warning" %}
When making payouts in AZN, EUR, or USD using a merchant, it is **mandatory** to add additional fields to the exchange form for the client to fill out when creating a request.

To do this, add [additional fields](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/valyuty-i-napravleniya/dobavlenie-novoi-valyuty#vkladka-dop.-polya) to the corresponding currencies:\
![](<../../../.gitbook/assets/image (730).png>)![](<../../../.gitbook/assets/image (731).png>)

Be sure to specify the following in the "**Unique ID**" field (use lowercase names):\
• `get_cardholder` (field "**Full Name**"[^1])\
• `get_cardexpire` (field "**Card Expiry Date**"[^1])

Example of filling out the additional field "**Card Expiry Date**":\
![](<../../../.gitbook/assets/image (732).png>)
{% endhint %}

{% hint style="warning" %}
For payouts via SBP, in the currency settings under the "**Field Settings**" tab, rename the field "**To Account**" to "**Your Phone Number**" and restrict the input in the exchange form to digits only.\
The **minimum** payout amount via SBP is **10,000 RUB**.

![](<../../../.gitbook/assets/image (1406).png>)
{% endhint %}

{% hint style="warning" %}
Also, when paying out via SBP, you can offer the client a choice of bank on the exchange page (in this case, the selection of **payment method** in the module settings will not matter — just select any option from the list).

To do this, add an [additional field for the **payout currency**](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/valyuty-i-napravleniya/dobavlenie-novoi-valyuty#vkladka-dop.-polya) with the additional field type "**Select**", using the following settings (bank names and their codes are shown in the screenshot below; you can include only the banks you use in the list within the additional field settings):\
![](<../../../.gitbook/assets/image (507).png>)

• Correctly filled additional field with the unique ID — **bankname:**

![](<../../../.gitbook/assets/image (509).png>)\
&#xNAN;**`Sberbank / Sber`**\
**`Tinkoff / Tinkoff Bank`**\
**`VTB Bank`**\
**`ALFA-BANK`**\
**`Raiffeisenbank`**\
**`Otkritie Bank`**\
**`Gazprombank`**\
**`Promsvyazbank`**\
**`Home Credit`**

After adding this field, it will appear in the exchange form, allowing the client to select the bank from which they want to receive funds from the exchanger themselves.

![](<../../../.gitbook/assets/image (510).png>)
{% endhint %}

---

[^1]: Refers to the fields "Full Name" and "Card Expiry Date" mentioned earlier in the documentation.

## Continuing the Setup

Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-merchantov-avtovyplat).

[^1]: the field can have any name