# Creating a New Currency

{% hint style="info" %}
Below is a description of all possible parameters that can be presented in the currency addition form. However, by default, some parameters may not be displayed. This is because certain modules responsible for displaying specific parameters in the form are inactive in the "**Modules**" → "**Modules**" section. The order of parameters in the currency creation form on your site may differ from the order presented below.
{% endhint %}

Navigate to the "**Currencies**" → "**Currencies**" section located in the sidebar of the admin panel.

<figure><img src="../../.gitbook/assets/image (1432).png" alt=""><figcaption></figcaption></figure>

Here, you will see a table listing all the currencies created by default in your exchange. On this page, you can also add a new currency to be used in your exchange. To do this, click the "**Add**" button located above the table.

<figure><img src="../../.gitbook/assets/image (1115).png" alt=""><figcaption></figcaption></figure>

## "Basic Settings" Tab

<figure><img src="../../.gitbook/assets/image (1156).png" alt=""><figcaption></figcaption></figure>

In the window that opens, you need to fill in the fields describing the new currency:

**Payment System Name** — select the name of the payment system from the dropdown list.

{% hint style="info" %}
If you cannot find a suitable option in the basic list of payment systems, create a new payment system name in the "**Currencies**" → "**Payment Systems**" section without specifying a currency code.

For example, **Perfect Money**, but not **Perfect Money USD.**
{% endhint %}

**Currency Code** — select the currency code from the basic list (currency codes can be added and edited in the "**Currencies**" → "**Currency Codes**" section).

For example, for US dollars, select the currency code USD.

{% hint style="info" %}
If the required code is not found in the basic list of currency codes, create a new code in the "**Currencies**" → "**Currency Codes**" section.

It is recommended to use the commonly accepted currency code designations — USD, EUR, USDT, BTC, etc.
{% endhint %}

{% hint style="warning" %}
In the "**Currencies**" → "**Currency Codes**" section, in the field "**Internal Rate for 1 USD**," specify the rate for 1 USD for the currency being created, i.e., indicate how much of the created currency can be bought for 1 USD. For example, for BTC, this value is approximately ~0.00004, and for DOGE ~13.5 (as of March 2023).
{% endhint %}

**Main Logo** — click the camera button, select from the uploaded options (the "**File Library**" tab in the opened window), or upload your own payment system logo (the "**Upload Files**" tab).

**Additional Logo** — optional.

**XML Designation** — specify the abbreviated name of the currency.

{% hint style="warning" %}
**The XML currency code must meet the following requirements:**

* The code must be unique and not overlap with other currencies.
* It can only contain Latin letters, numbers, and **_**.
* It must comply with commonly accepted standards.\
  \
  The currency code for the XML file is specified according to the standards of [BestChange](https://www.bestchange.ru/wiki/rates.html). The page linked contains the signatures of all currencies that should be used as designations for XML.\
  \
  Alternative sources for verifying the correctness of currency codes:\
  [Jsons.info](https://jsons.info/signatures/currencies#electronic-currencies/)\
  [Exchange.sumo](https://exchangesumo.com/nazvaniya-valjut-eksportnogo-fajla-kursov/)\

Example: For the currency **Tether(USDT) ERC20**, the XML code should be set to **USDTERC20**.\
\
**Custom Currency:** If the currency you are creating is unique and does not have a standard designation, specify your own XML code that will be unique and will not overlap with any already accepted standards, as this may lead to erroneous export of rates to monitoring from your XML file.
{% endhint %}

**Decimal Places** — regulate the number of decimal places; this option will be used for this currency throughout the site and in the admin panel (in exchange rates, exchange amounts, reserves, etc.).

## "Reserve and Limits" Tab

<figure><img src="../../.gitbook/assets/image (854).png" alt=""><figcaption></figcaption></figure>

**Currency Reserve** — allows you to calculate the current currency reserve based on completed requests — for this, select the option "**--calculate by requests--**." You can also obtain the current reserve from the wallet in real-time, but for this, you need to set up the corresponding [auto-payment module](https://premium.gitbook.io/rukovodstvo-polzovatelya/navigaciya/merchanty-i-vyplaty/vyplaty), and then select the corresponding wallet from the list. Additionally, you can obtain [reserve from a file](https://premium.gitbook.io/rukovodstvo-polzovatelya/navigaciya/rezervy/rezerv-iz-faila) and calculate it [using a formula](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/rezervy-valyut/rezerv-ot-drugoi-valyuty/primery-nastroiki-slozhnogo-rezerva-s-ispolzovaniem-formul).

**Link Reserve with Currency Reserve ID** — allows you to make the reserves of currencies interdependent. When the reserve of one currency is updated, the reserve of the other currency will automatically update as well. In the field, you need to specify the ID of the currency (or multiple currencies separated by commas) that need to be linked. This procedure should be repeated for all currencies involved in the linkage.

**Max. Displayed Reserve Value** — limits the displayed reserve value of the currency on the site. You cannot set a reserve value higher than what actually exists.

**Daily Limit for Giving** — limits the amount of currency that the site can buy in a day. The exchange will not be able to buy more of this currency than the specified value.

**Daily Limit for Receiving** — limits the amount of currency that the site can sell in a day. The exchange will not be able to sell more of this currency than the specified value.

**Monthly Limit for Giving** — limits the amount of currency that the exchange can buy in a month. The exchange will not be able to buy more of this currency than the specified value.

**Monthly Limit for Receiving** — limits the amount of currency that the exchange can sell in a month. The exchange will not be able to sell more of this currency than the specified value.

## "Field Settings" Tab

<figure><img src="../../.gitbook/assets/image (2063).png" alt=""><figcaption></figcaption></figure>

**Allow users to add account numbers in their profiles** — allows clients to save their payment system details in their user account and later select the necessary details in the exchange form.

**Display "From Account/To Account" Field** — allows you to hide the input fields for wallets for the currencies "**Giving**" and "**Receiving**" if necessary.

**Min/Max Number of Characters** — allows you to check the compliance and correctness of the account number specified by the user. In case of an error, the site will automatically notify the user of an incorrect account number.

**First Characters** — allows you to specify the first characters of the account that will be checked when the client enters their account number. For example, for a Webmoney Z wallet, the first character can be the letter Z. You can specify multiple options separated by commas.

**Allowed Characters** — allows you to select the type of characters that can be used when entering the account number.

**Remove Spaces in Details** — allows you to automatically remove spaces in the details entered by the user in the exchange form.

**Field Name "From Account/To Account"** — displayed to the user during the exchange request process when they are asked to specify the account number from which the transfer will be made and the account number to which the funds should be credited. You have the option to rename these fields. For example, to **"From Card"** and **"To Card."** If necessary, the display of these fields in the request submission form can be disabled.

**Tooltip for "From Account/To Account" Field** — allows you to set a tooltip that will appear when the cursor hovers over the field on the exchange page.

**Account Number Validator** — allows you to activate the validation of the correctness of the input for the bank card number or cryptocurrency wallet address. More detailed information is available [here](https://premium.gitbook.io/rukovodstvo-polzovatelya/navigaciya/nastroiki/validator-kripto-koshelka).

**Bank Names (on a new line) for this currency on the "Giving/Receiving" side** — [bank card validator settings](https://premium.gitbook.io/main/osnovnye-nastroiki/nastroiki/validator-bankovskoi-karty#opciya-v-nastroikakh-valyuty).

## "Additional Fields" Tab

<figure><img src="../../.gitbook/assets/image (1198).png" alt=""><figcaption></figcaption></figure>

In this section, you can select previously created additional fields from the "**Additional Currency Fields**" section that will be displayed in the exchange directions for this currency.

## "Verification" Tab

<figure><img src="../../.gitbook/assets/image (1091).png" alt=""><figcaption></figcaption></figure>

**Account Verification Option** — allows the activation of user account verification for the created currency.

**Number of Images for Upload** — limits the number of images that can be uploaded. Clients can complete account verification in their personal dashboard.

**Account Verification Instructions** — provides users with guidance on how to complete account verification. This process requires users to upload an image or photograph. For example, to verify a bank card, users may be asked to upload a photo of the front side of the card against the backdrop of your website.

**Wallet Verification Check in Payment System** — allows you to select the payment system in which the wallet number will be verified. Available payment systems can be activated in the "**Merchants → Wallet Verification Checker**" section.

**Text Indicating Verified Wallet** — the text that will appear in the exchange form below the account number input field.

## "Affiliate Program" Tab

<figure><img src="../../.gitbook/assets/image (964).png" alt=""><figcaption></figcaption></figure>

**Allow Withdrawal of Affiliate Funds** — option to permit or restrict the withdrawal of affiliate funds in this currency within users' affiliate accounts.

**Payment System Fee for Partner Withdrawals** — allows you to set the fee charged by the payment system, which will be deducted from the partner's payout request. The partner will receive an amount that is less by the specified fee.