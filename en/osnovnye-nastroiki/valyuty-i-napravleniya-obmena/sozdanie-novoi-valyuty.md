# Creating a New Currency

{% hint style="info" %}
Below is a description of all possible parameters that can appear in the currency addition form. However, by default, some parameters may not be displayed. This is because certain modules responsible for showing specific parameters in the form are inactive in the "**Modules**" → "**Modules**" section. The order of parameters in the currency creation form on your site may differ from the order shown here.
{% endhint %}

Go to the "**Currencies**" → "**Currencies**" section located in the admin panel’s sidebar menu.

<figure><img src="../../.gitbook/assets/image (1432).png" alt=""><figcaption></figcaption></figure>

Here you will see a table listing all the currencies currently created in your exchange by default. On this same page, you can add a new currency to be used in your exchange. To do this, click the "**Add**" button located above the table.

<figure><img src="../../.gitbook/assets/image (1115).png" alt=""><figcaption></figcaption></figure>

## "Basic Settings" Tab

<figure><img src="../../.gitbook/assets/image (1156).png" alt=""><figcaption></figcaption></figure>

In the window that opens, you need to fill in the fields describing the new currency:

**Payment System Name** — select the name of the payment system from the dropdown list.

{% hint style="info" %}
If you don’t find a suitable payment system in the default list, create a new payment system name in the "**Currencies**" → "**Payment Systems**" section without specifying a currency code.

For example, use **Perfect Money**, not **Perfect Money USD**.
{% endhint %}

**Currency Code** — select the currency code from the default list (currency codes can be added and edited in the "**Currencies**" → "**Currency Codes**" section).

For example, for US dollars, select the currency code USD.

{% hint style="info" %}
If the required currency code is not in the default list, create a new code in the "**Currencies**" → "**Currency Codes**" section.

We recommend using the standard currency code format — USD, EUR, USDT, BTC, etc.
{% endhint %}

{% hint style="warning" %}
In the "**Currencies**" section -> "**Currency Codes**," enter the exchange rate for 1 USD in the "**Internal rate per 1 USD**" field for the selected currency code. This means you should specify how much of the new currency can be bought for 1 USD. For example, for BTC this value is approximately ~0.00004, and for DOGE it’s about ~13.5 (as of March 2023).
{% endhint %}

**Main Logo** — click the camera icon button, then choose from the uploaded options (under the "**File Library**" tab in the window that opens) or upload your own payment system logo (under the "**Upload Files**" tab).

**Additional Logo** — optional.

**XML Designation** — enter the abbreviated currency name.

{% hint style="warning" %}
**The XML currency code must meet the following requirements:**

* The code must be unique and not conflict with other currencies.
* It can contain only Latin letters, numbers, and **_** (underscore).
* It must comply with commonly accepted standards.\
  \
  The currency code for the XML file should follow the [BestChange](https://www.bestchange.ru/wiki/rates.html) standards. The linked page lists the signatures of all currencies that should be used as XML designations.\
  \
  Alternative sources to verify the correctness of currency codes:\
  [Jsons.info](https://jsons.info/signatures/currencies#electronic-currencies/)\
  [Exchange.sumo](https://exchangesumo.com/nazvaniya-valjut-eksportnogo-fajla-kursov/)\
\
Example: For the currency **Tether (USDT) ERC20**, the XML code should be set as **USDTERC20**.\
\
**Custom Currency:** If the currency you are creating is unique and does not have a standard designation, specify your own XML code that is unique and does not conflict with existing standards. Otherwise, this may cause errors when exporting rates to monitoring services from your XML file.
{% endhint %}

**Decimal Places** — controls the number of digits after the decimal point. This setting will apply to this currency throughout the website and admin panel (in exchange rates, transaction amounts, reserves, etc.).

## "Reserve and Limits" Tab

<figure><img src="../../.gitbook/assets/image (854).png" alt=""><figcaption></figcaption></figure>

**Currency Reserve** — allows you to calculate the current currency reserve based on completed orders. To do this, select the option "**--calculate based on orders--**". You can also get the current reserve directly from your wallet in real-time, but this requires setting up the appropriate [auto-payout module](https://premium.gitbook.io/rukovodstvo-polzovatelya/navigaciya/merchanty-i-vyplaty/vyplaty) and then selecting the corresponding wallet from the list. Additionally, you can obtain the [reserve from a file](https://premium.gitbook.io/rukovodstvo-polzovatelya/navigaciya/rezervy/rezerv-iz-faila) and calculate it using a [formula](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/rezervy-valyut/rezerv-ot-drugoi-valyuty/primery-nastroiki-slozhnogo-rezerva-s-ispolzovaniem-formul).

**Link reserve with currency reserve ID** — allows you to make currency reserves interdependent. When the reserve of one currency is updated, the reserve of the linked currency (or currencies) will update automatically as well. In this field, enter the ID of the currency (or multiple IDs separated by commas) you want to link. This procedure must be repeated for all currencies involved in the linkage.

**Max. displayed currency reserve value** — limits the reserve amount shown on the website. The displayed reserve cannot exceed the actual available amount.

**Daily limit for "Giving"** — restricts the amount of currency the site can buy per day. The exchanger will not be able to purchase more than this set amount of the currency.

**Daily limit for "Receiving"** — restricts the amount of currency the site can sell per day. The exchanger will not be able to sell more than this set amount of the currency.

**Monthly limit for "Giving"** — restricts the amount of currency the exchanger can buy per month. The exchanger will not be able to purchase more than this set amount of the currency.

**Monthly limit for "Receiving"** — restricts the amount of currency the exchanger can sell per month. The exchanger will not be able to sell more than this set amount of the currency.

## "Field Settings" Tab

<figure><img src="../../.gitbook/assets/image (2063).png" alt=""><figcaption></figcaption></figure>

**Allow users to add account numbers in their profile** — lets clients save their payment system details in their personal account, so they can easily select the desired details later when filling out an exchange form.

**Show "From account"/"To account" fields** — allows you to hide the wallet input fields for the "**Giving**" and "**Receiving**" currencies if needed.

**Minimum/maximum number of characters** — lets you verify that the wallet number entered by the user meets length requirements. If there’s an error, the site will automatically notify the user about the incorrect wallet number.

**Starting characters** — lets you specify the initial characters of the account number that will be checked when the client enters their account number. For example, for a Webmoney Z wallet, the first character might be the letter Z. Multiple options can be entered, separated by commas.

**Allowed characters** — lets you define which types of characters are permitted when entering the account number.

**Remove spaces in payment details** — automatically removes any spaces entered by the user in the payment details on the exchange form.

**Field names "From account"/"To account"** — these labels are shown to users when they submit an exchange request, prompting them to enter the account number from which funds will be sent and the account number where funds should be received. You can rename these fields—for example, to "**From card**" and "**To card**." If needed, you can also disable these fields from appearing on the request form.

**Tooltip for the "From account"/"To account" fields** — lets you set a tooltip that appears when the user hovers over the field on the exchange page.

**Account number validator** — enables validation to check the correctness of a bank card number or cryptocurrency wallet address. More detailed information is available at [this link](https://premium.gitbook.io/rukovodstvo-polzovatelya/navigaciya/nastroiki/validator-kripto-koshelka).

**Bank names (each on a new line) for this currency on the "Give/Receive" side** — [bank card validator settings](https://premium.gitbook.io/main/osnovnye-nastroiki/nastroiki/validator-bankovskoi-karty#opciya-v-nastroikakh-valyuty)

## "Additional Fields" Tab

<figure><img src="../../.gitbook/assets/image (1198).png" alt=""><figcaption></figcaption></figure>

In this section, you can select previously created additional fields from the "**Currency Additional Fields**" section that will be displayed in the exchange directions for this currency.

## "Verification" Tab

<figure><img src="../../.gitbook/assets/image (1091).png" alt=""><figcaption></figcaption></figure>

**Enable account verification** — allows you to activate user account verification for the currency being created.

**Number of images to upload** — limits the number of images the user can upload. The client can complete account verification in their personal account.

**Account verification instructions** — instructions for the user on how to complete account verification. Account verification means the user must upload an image or photo. For example, to verify a bank card, you might ask the user to upload a photo of the front side of their bank card against the background of your website.

**Wallet verification check in the payment system** — lets you select the payment system where the wallet number will be verified. Available payment systems can be activated in "**Merchants → Wallet Verification Checker**."

**Text indicating a verified wallet** — the text that will appear in the exchange form below the account number input field.

## "Affiliate Program" Tab

<figure><img src="../../.gitbook/assets/image (964).png" alt=""><figcaption></figcaption></figure>

**Allow withdrawal of affiliate funds** — enables or disables the withdrawal of affiliate funds in this currency within users’ affiliate accounts.

**Payment system fee when paying out funds to a partner** — allows you to set a payment system fee that will be deducted from the partner when they request a payout of their partner reward. The partner will receive an amount reduced by the specified fee.