# Creating a New Currency

{% hint style="info" %}
Below is a description of all possible parameters that can be included in the currency creation form. However, by default, some parameters may not be displayed. This is because certain modules responsible for showing these parameters in the form are inactive in the "**Modules**" → "**Modules**" section. The order of parameters in the currency creation form on your website may differ from the order presented below.
{% endhint %}

Navigate to the "**Currencies**" → "**Currencies**" section in the side menu of the admin panel.

<figure><img src="../../.gitbook/assets/image (1432).png" alt=""><figcaption></figcaption></figure>

Here, you will see a table listing all the currencies that are pre-configured in your exchange platform. On this page, you can also add a new currency to be used in your exchange. To do this, click the "**Add**" button located above the table.

<figure><img src="../../.gitbook/assets/image (1115).png" alt=""><figcaption></figcaption></figure>

## "Basic Settings" Tab

<figure><img src="../../.gitbook/assets/image (1156).png" alt=""><figcaption></figcaption></figure>

In the window that opens, you need to fill in the fields describing the new currency:

**Payment System Name** — Select the name of the payment system from the dropdown list.

{% hint style="info" %}
If the default list of payment systems does not include a suitable option, create a new payment system name in the "**Currencies**" → "**Payment Systems**" section without specifying the currency code.

For example, **Perfect Money**, but not **Perfect Money USD.**
{% endhint %}

**Currency Code** — Select the currency code from the default list (currency codes can be added or edited in the "**Currencies**" → "**Currency Codes**" section).

For example, for US dollars, select the currency code USD.

{% hint style="info" %}
If the default list of currency codes does not include the required code, create a new code in the "**Currencies**" → "**Currency Codes**" section.

We recommend using standard currency codes such as USD, EUR, USDT, BTC, etc.
{% endhint %}

{% hint style="warning" %}
In the "**Currencies**" → "**Currency Codes**" section, in the "**Internal Rate per 1 USD**" field for the selected code, specify the exchange rate for 1 USD for the currency being created. This means you need to indicate how much of the new currency can be purchased for 1 USD. For example, for BTC, this value is approximately \~0.00004, and for DOGE, it is \~13.5 (as of March 2023).
{% endhint %}

**Main Logo** — Click the camera button to select an image from the uploaded options (via the "**File Library**" tab in the opened window) or upload your own payment system logo (via the "**Upload Files**" tab).

**Additional Logo** — Optional field.

**XML Designation** — Enter the abbreviated name of the currency.

{% hint style="warning" %}
**The XML currency code must meet the following requirements:**

* The code must be unique and not overlap with other currencies.
* It can only contain Latin letters, numbers, and **\_**.
* It must adhere to standard conventions.

The XML currency code should follow the standards outlined by [BestChange](https://www.bestchange.ru/wiki/rates.html). The page linked provides the signatures for all currencies, which should be used as XML designations.

Alternative sources for verifying currency codes:
[Jsons.info](https://jsons.info/signatures/currencies#electronic-currencies/)  
[Exchange.sumo](https://exchangesumo.com/nazvaniya-valjut-eksportnogo-fajla-kursov/)

Example: For the currency **Tether (USDT) ERC20**, the XML code should be **USDTERC20**.

**Custom Currency:** If the currency you are creating is unique and does not have a standard designation, specify your own XML code that is unique and does not conflict with existing standards. Conflicts may result in incorrect export of rates to monitoring systems from your XML file.
{% endhint %}

**Decimal Places** — Specify the number of decimal places to be used for this currency across the site and in the admin panel (e.g., in exchange rates, transaction amounts, reserves, etc.).

## "Reserve and Limits" Tab

<figure><img src="../../.gitbook/assets/image (854).png" alt=""><figcaption></figcaption></figure>

**Currency Reserve** — Allows you to calculate the current reserve of the currency based on completed transactions. To do this, select the "**--calculate based on transactions--**" option. You can also retrieve the current reserve from a wallet in real-time, but this requires configuring the appropriate [auto-payout module](https://premium.gitbook.io/rukovodstvo-polzovatelya/navigaciya/merchanty-i-vyplaty/vyplaty) and selecting the corresponding wallet from the list. Alternatively, you can retrieve the [reserve from a file](https://premium.gitbook.io/rukovodstvo-polzovatelya/navigaciya/rezervy/rezerv-iz-faila) or calculate it [using a formula](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/rezervy-valyut/rezerv-ot-drugoi-valyuty/primery-nastroiki-slozhnogo-rezerva-s-ispolzovaniem-formul).

**Link Reserve to Currency ID Reserve** — Allows you to link the reserves of different currencies. When the reserve of one currency is updated, the reserve of the linked currency will also be updated. Enter the ID(s) of the currency (or multiple currencies separated by commas) to link. This procedure must be repeated for all currencies involved in the linkage.

**Max Displayed Reserve Value** — Sets a limit on the reserve value displayed on the website. The displayed reserve cannot exceed the actual reserve.

**Daily Limit for "Give"** — Limits the amount of this currency the platform can purchase in a day. The exchange cannot buy more than the specified amount.

**Daily Limit for "Receive"** — Limits the amount of this currency the platform can sell in a day. The exchange cannot sell more than the specified amount.

**Monthly Limit for "Give"** — Limits the amount of this currency the platform can purchase in a month. The exchange cannot buy more than the specified amount.

**Monthly Limit for "Receive"** — Limits the amount of this currency the platform can sell in a month. The exchange cannot sell more than the specified amount.

## "Field Settings" Tab

<figure><img src="../../.gitbook/assets/image (2063).png" alt=""><figcaption></figcaption></figure>

**Allow Users to Add Account Numbers in Profile** — Lets clients save their payment system details in their user account and select them when filling out exchange forms.

**Display "From Account/To Account" Fields** — Allows you to hide wallet input fields for "Give" and "Receive" currencies if needed.

**Min/Max Number of Characters** — Ensures the user-provided wallet number meets the required format. If incorrect, the site will notify the user.

**Starting Characters** — Specifies the initial characters of an account number to validate user input. For example, for a Webmoney Z wallet, the first character might be "Z." Multiple options can be separated by commas.

**Allowed Characters** — Specifies the types of characters allowed in the account number.

**Remove Spaces in Details** — Automatically removes spaces from account details entered by the user in the exchange form.

**Field Names for "From Account/To Account"** — These are displayed to users when they are asked to provide the account numbers for sending and receiving funds. You can rename these fields, e.g., to **"From Card"** and **"To Card"**. If necessary, these fields can be hidden in the exchange request form.

**Tooltip for "From Account/To Account" Fields** — Adds a tooltip that appears when users hover over the field in the exchange form.

**Account Number Validator** — Enables validation of bank card numbers or cryptocurrency wallet addresses. More details are available [here](https://premium.gitbook.io/rukovodstvo-polzovatelya/navigaciya/nastroiki/validator-kripto-koshelka).

**Bank Names (One Per Line) for "Give/Receive" Side** — [Bank card validator settings](https://premium.gitbook.io/main/osnovnye-nastroiki/nastroiki/validator-bankovskoi-karty#opciya-v-nastroikakh-valyuty).

## "Additional Fields" Tab

<figure><img src="../../.gitbook/assets/image (1198).png" alt=""><figcaption></figcaption></figure>

In this section, you can select additional fields (previously created in the "**Additional Currency Fields**" section) to display in exchange directions for this currency.

## "Verification" Tab

<figure><img src="../../.gitbook/assets/image (1091).png" alt=""><figcaption></figcaption></figure>

**Account Verification Option** — enables the activation of account verification for the user in the selected currency.

**Number of Uploadable Images** — sets a limit on the number of images that can be uploaded. The client can complete account verification through their personal account dashboard.

**Account Verification Instructions** — provides users with a guide on how to complete account verification. Account verification typically requires the user to upload an image or photo. For example, to verify a bank card, the user may be asked to upload a photo of the front side of the card against the background of your website.

**Wallet Verification in the Payment System** — allows you to select the payment system where the wallet number will be checked for verification. Available payment systems can be activated in the "**Merchants → Wallet Verification Checker**" section.

**Text Indicating a Verified Wallet** — the text that will appear in the exchange form below the field for entering the account number.

## **"Affiliate Program" Tab**

<figure><img src="../../.gitbook/assets/image (964).png" alt=""><figcaption></figcaption></figure>

**Allow Withdrawal of Affiliate Funds** — enables or disables the withdrawal of affiliate funds in the selected currency through the affiliate dashboard.

**Payment System Fee for Affiliate Payouts** — allows you to set a payment system fee that will be deducted from the affiliate when they request a payout of their earnings. The affiliate will receive an amount reduced by the specified fee.