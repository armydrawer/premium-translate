# Creating a New Exchange Direction

**Note:** Below is a description of all the options that may appear in the exchange direction setup form. However, by default, some parameters might not be displayed. This is because certain modules responsible for showing specific options in the form are inactive in the "**Modules**" → "**Modules**" section. The order of parameters in the exchange direction creation form on your site may differ from the order shown here.

After adding [new currencies](https://premium.gitbook.io/rukovodstvo-polzovatelya/navigaciya/valyuty-i-napravleniya/dobavlenie-novoi-valyuty) and specifying [reserves for them](https://premium.gitbook.io/rukovodstvo-polzovatelya/navigaciya/rezervy), create an exchange direction. To do this, go to the "**Exchange Directions**" section in the control panel. Click the "**Add**" button located above the list of existing exchanges.

On the page that opens, fill in the required fields to create the exchange direction.

## Tab "**Basic Settings**"

<figure><img src="../../.gitbook/assets/image (1205).png" alt=""><figcaption></figcaption></figure>

**Direction** — set the currencies for "**Give**" and "**Receive**."

**Technical Name** — the name of the exchange direction displayed in the site’s control panel. Leave this field empty to generate the name automatically.

**Permanent Link** — manually specify the part of the URL for the exchange direction: `https://your_domain/exchange-`**`LINK`**`.` This link will be used to access the exchange direction on the site.

{% hint style="success" %}
The permanent link is generated automatically based on the selected currencies for the exchange direction, but you can customize it if you wish.
{% endhint %}

**Status** — set the current status of the exchange direction.

## Tab "Rate"

<figure><img src="../../.gitbook/assets/image (1152).png" alt=""><figcaption></figcaption></figure>

**Exchange Rate** — enter the current exchange rate.

**Rate Depending on Exchange Amount** — if needed, specify an exchange rate that varies depending on the user’s exchange amount.

This option also has a settings block in the "**Modules**" → "**Rate Depending on Exchange Amount**" section.

**Method of Rate Formation:**  
• **Set the rate directly** — display rates for different amounts, taking into account the specified percentages.

• **Add a percentage to the rate** — display the percentage that will be applied to the base exchange rate for different amounts.

---

**Use in XML 2.0 rate file** — include tiered rates from the exchange direction settings in the new export XML file:  
• **Yes**  
• **No**

<details>

<summary>Example</summary>

For instance, you can create tiers so that a user making a small transaction receives a lower amount per unit of currency than the standard rate — effectively encouraging them to exchange larger sums.

Setting dependency for the "**Receiving**" side of the exchange rate (applicable when 1 unit is in the "**Giving**" currency — for example, the BTC-USDT rate):

Similarly, you can set dependency for the "**Giving**" side of the exchange rate (applicable when 1 unit is in the "**Receiving**" currency — for example, the USDT-BTC rate).

<mark style="color:red;">It is not recommended to set a percentage on the side of the rate where the value is 1</mark> — <mark style="color:red;">this will cause the exchange form to display rates like 0.98 to XXX or 1.32 to XXX</mark>.

</details>

---

**Rate dependent on currency reserve** — if needed, specify the exchange rate depending on the reserve of the "**Receiving**" currency.

This option also has a settings block under "**Modules**" ➔ "**Reserve-dependent Rate**."

---

**Method of Rate Formation:**  
• **Set the rate directly** — display rates for different amounts, taking into account the specified percentages.  
• **Add a percentage to the rate** — display the percentage that will be applied to the base exchange rate for different amounts.

**Updating Exchange Rates:**  
• **During currency operations** — rates will update whenever the currency reserve changes.  
• **On the fly** — rates will update during the calculation of amounts in the transaction request.  

<details>

<summary>Example</summary>

For instance, you can set up a tiered system so that as the currency reserve decreases, the currency becomes increasingly expensive for users. The reserve is always set for the "**Receiving**" currency.

![](<../../.gitbook/assets/image (784).png>)

<mark style="color:red;">It is not recommended to set a percentage on the side of the rate where the value is 1</mark> — <mark style="color:red;">this will cause the exchange rate to display as 0.98 to XXX or 1.32 to XXX in the exchange form</mark>

</details>

{% hint style="danger" %}
If you use the "**Rate dependent on amount or reserve**" option, the "**Receiving**" field in the exchange form will be disabled (due to technical limitations of the calculation engine).

![](<../../.gitbook/assets/image (1773).png>)
{% endhint %}

**Exchange Rate from File** — more detailed information is available [here](https://premium.gitbook.io/rukovodstvo-polzovatelya/navigaciya/kursy/kurs-iz-faila).

**Rounding of Exchange Amount** — when this option is enabled, the amount selected in the dropdown list will be rounded as follows:

<figure><img src="../../.gitbook/assets/image (855).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
For example, if the "You Give" amount is selected and the rounding is set to 100, when a user enters 12,345 in the "You Give" field, the amount will be rounded down to 12,300.
{% endhint %}

**Profit** — specify the profit either as a percentage or a fixed amount that you earn from the exchange. The partner commission is calculated based on the specified profit value.

When working with monitoring services, the standard values are 30% of the profit or 1% of the exchange amount. In the script, for each exchange direction, only one method (based on amount or profit) can be set for all partners.

If the profit is set to zero, the partner will not receive any partner commission. If the profit is set to 100%, the partner’s commission will effectively be calculated based on the exchange amount. For a detailed explanation of this option, see the article ["**Profit and Partner Percentage**"](https://premium.gitbook.io/rukovodstvo-polzovatelya/navigaciya/partnerskaya-programma/pribyl-i-partnerskii-procent).

{% hint style="warning" %}
If the "**Profit**" section does not appear on the tab, disable the "**Automatic Profit Calculation**" module in the "**Modules**" section.

![](<../../.gitbook/assets/image (604).png>)
{% endhint %}

## "Cities" Tab

To select a city for an exchange direction, you first need to create a city with the correct code (according to [BestChange rules](https://www.bestchange.ru/wiki/rates.html)) in the "**Cities**" section:

<figure><img src="../../.gitbook/assets/image (837).png" alt="" width="504"><figcaption></figcaption></figure>

Then, in the exchange direction settings, choose the city on the "**Cities**" tab and, if necessary, specify additional parameters for the city:

<figure><img src="../../.gitbook/assets/image (157).png" alt="" width="549"><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (893).png" alt=""><figcaption></figcaption></figure>

* **Add to rate (Give/Receive)** — enter an absolute value that will be added to or subtracted from the base rate set for the exchange direction.  
  To add a percentage, enter, for example, `*0.9` (≈ -10%) to decrease the rate or `/0.9` (≈ +11%) to increase the rate relative to the base exchange rate.
* **Minimum/Maximum amount** — specify the limits for the exchange amount for this city (this option applies only to the XML file with exchange directions).
* **Profit (from amount given/received)** — individual profit values that can differ from the general profit settings on the "**Rate**" tab.
* **Tags for the param parameter** — specify parameters according to [BestChange requirements](https://www.bestchange.ru/wiki/rates.html).

<figure><img src="../../.gitbook/assets/image (159).png" alt=""><figcaption></figcaption></figure>

## "BestChange API Parser" and "BestChange Parser" Tabs

<figure><img src="../../.gitbook/assets/image (856).png" alt=""><figcaption></figcaption></figure>

For detailed descriptions of these options, see the articles ["**BestChange API Parser**"](https://premium.gitbook.io/main/osnovnye-nastroiki/kursy-valyut/bestchange-api-parser-new-nachinaya-s-v2.6) and ["**BestChange Parser**"](https://premium.gitbook.io/main/osnovnye-nastroiki/kursy-valyut/bestchange-parser-old).

## "Auto Rate Adjustment" Tab

**Automatic Rate Adjustment** — select the source and direction for automatically updating the exchange rate on the website.

{% hint style="warning" %}
To enable automatic rate updates, you need to set up a [task scheduler (cron)](https://premium.gitbook.io/main/osnovnye-nastroiki/kursy-valyut/parser-kursov-valyut-parsery-2.0) on your server. At the top of the "**Parsers 2.0**" section, you’ll find a link labeled "**Cron URL for updating Central Bank and cryptocurrency rates**," which must be added to your server’s task scheduler. You can run the updates as frequently as every minute. For more detailed instructions, see [this link](https://premium.gitbook.io/main/osnovnye-nastroiki/kursy-valyut/parser-kursov-valyut-parsery-2.0).
{% endhint %}

**Add to Rate** — this setting lets you adjust the rate received from the source to better suit your needs. For the column representing the currency you are giving, leave the value at "**0**". For the column representing the currency you are receiving, enter a percentage or numeric value (negative values are allowed). This amount will be automatically added to the source rate and displayed on the site as an adjusted rate.

Please note that registered users automatically participate in a loyalty program that rewards them with discounts based on the total amount they have already exchanged with you. This commission will be automatically added to the displayed rate. To configure the loyalty program, go to the "**User Discounts**" section. There, you will find fields where you can modify the parameters of your loyalty program.

## "Exchange Rate Limits" Tab

**Min. Rate / Max. Rate** — if needed, you can set minimum and maximum rate values within which the rate parser for the selected direction will operate. If the rate goes beyond these limits, you can choose to reset it to the default rate; otherwise, the last received rate will be fixed until the rate returns to the specified range.

**Standard Rate** — if necessary, specify the value of the standard rate to which the system will revert when the exchange rate goes outside the specified range.

## "Reserve" Tab

<figure><img src="../../.gitbook/assets/image (1217).png" alt=""><figcaption></figcaption></figure>

**Reserve** — if needed, you can set a custom reserve amount for the exchange direction. The selected option will override the reserve value set in the "**Receiving**" currency settings under the "**Currencies**" section. You can also set a [reserve from a file](https://premium.gitbook.io/rukovodstvo-polzovatelya/navigaciya/rezervy/rezerv-iz-faila), enable auto-reserve, or specify a reserve amount using the field below.

**Reserve Field** — if you choose "**—From the field below—**" for the "**Reserve**" option, enter the reserve amount in the "**Reserve Field**" parameter. This reserve value will be displayed on the website for the exchange direction being created. This option serves only as a limit for the current reserve value and will work only if a currency reserve is set in the "**Reserve Adjustment**" section. For example, if you set a reserve of 100,000 in the "**Reserve Adjustment**" section but want to limit it to 50,000 for the new exchange direction, use the "**Reserve Field**" parameter to cap the reserve amount.

**Calculator** — if you select "**—By formula—**" for the "**Reserve**" option, specify the reserve formula in the "**Calculator**" parameter. For more detailed information, see [this link](https://premium.gitbook.io/main/osnovnye-nastroiki/rezervy-valyut/rezerv-ot-drugoi-valyuty/primery-nastroiki-slozhnogo-rezerva-s-ispolzovaniem-formul).

## "Payment System Fees" Tab

<figure><img src="../../.gitbook/assets/image (1087).png" alt=""><figcaption></figcaption></figure>

**Payment System Fees** — specify the standard percentage or fixed amount charged by the payment system for processing transfers. This fee will be taken into account when calculating the exchange amount for users.

**Payment System Fees (for Verified Accounts)** — specify the standard percentage or fixed amount charged by the payment system for transfers made from a verified wallet. This fee will be factored into the exchange calculations for users.

**Exchange Pays the Fee** — check this box if your exchange covers the payment system’s commission instead of the client.

**Non-Standard Fee** — check this box if the payment system charges a fee on incoming payments to the exchange when paying via a merchant (typically applies to Yandex.Money, Privat24, Liqpay, Qiwi). For more details, see [this link](https://premium.gitbook.io/rukovodstvo-polzovatelya/navigaciya/faq/chto-takoe-nestandartnaya-komissiya-v-nastroikakh-merchanta-i-kak-ona-rabotaet).

**Minimum Fee Amount** — specify the minimum commission amount the payment system may charge for a transfer, if applicable. Entering “**0**” means no minimum limit. If a minimum is set, some fields in the order creation form will become inactive.

## "Exchange Fees" Tab

<figure><img src="../../.gitbook/assets/image (959).png" alt=""><figcaption></figcaption></figure>

**Additional Fee Charged to Sender** — specify any extra fee (fromfee) added to the payment amount if such a fee is required by the exchange’s regulations. This value will appear in the XML rates file for monitoring under the \<fromfee> parameter.

**Additional Fee Charged to Recipient** — specify any extra fee (to fee) deducted from the received amount if such a fee is required by the exchange’s regulations. This value will appear in the XML rates file for monitoring under the \<tofee> parameter.

**Additional Fee Based on Exchange Amount** — configure a fee charged to the client that varies depending on the exchange amount.

{% hint style="danger" %}
Please note that when using this option, the values entered in the “Additional Fee Charged to Sender/Recipient” fields below will be ignored in calculations.

{% hint style="info" %}
If you use the "**Additional commission based on the exchange amount**" option, the "**Receive**" field in the exchange form will be disabled (due to technical limitations of the calculation calculator).

![](<../../.gitbook/assets/image (398).png>)
{% endhint %}

<details>

<summary>Example of commission settings</summary>

You can create an unlimited number of commission rules.

In the "**Amount**" field, specify the value of the "**Give**" currency above which the commission will apply. Commission values can be set as a percentage or directly in the exchange currencies:

<img src="../../.gitbook/assets/image (1301).png" alt="" data-size="original">

Please note — once a commission based on the exchange amount is set, you will only be able to enter the exchange amount in the "**Give**" field:\
![](<../../.gitbook/assets/image (1302).png>)<img src="../../.gitbook/assets/image (1303).png" alt="" data-size="original">

</details>

**Minimum commission from sender** — specify the minimum amount of additional commission charged on the amount sent.

**Minimum commission from receiver** — specify the minimum amount of additional commission charged on the amount received.

**Additional commission based on exchange amount** — if needed, set an additional exchange point commission depending on the "**Give**" amount.

**Deduct commission from payment amount** — check this box if you want to reduce the payment amount by the sender’s additional commission.

**Add commission to payout amount** — check this box if you want to increase the payout amount by the receiver’s additional commission.

## "Exchange Amount" Tab

<figure><img src="../../.gitbook/assets/image (2146).png" alt="" width="563"><figcaption></figcaption></figure>

**Min/Max amount** — specify the minimum and maximum limits for exchange requests for currencies in the exchange direction.

<figure><img src="../../.gitbook/assets/image (2141).png" alt="" width="563"><figcaption><p>Option settings in the admin panel</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (2140).png" alt="" width="563"><figcaption><p>Displaying limits on the website</p></figcaption></figure>

{% hint style="warning" %}
You can also set minimum and maximum amounts for just one currency and enable automatic recalculation of limits for the other currency based on the exchange rate in the "Exchange Settings" ➔ "General Settings" section.\
![](<../../.gitbook/assets/image (2143).png>)\
In this case, automatic limits will be applied for the second currency.\
![](<../../.gitbook/assets/image (2142).png>)

![](<../../.gitbook/assets/image (2145).png>)
{% endhint %}

## "User Information" Tab

<figure><img src="../../.gitbook/assets/image (858).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Use exchange direction templates to simplify the process of creating new exchange directions. You can add templates in the website control panel under "**Exchange Directions**" → "**Exchange Direction Templates**". For each parameter, add a template whose text will be automatically inserted into the corresponding field when adding a new exchange direction.
{% endhint %}

**Exchange Description** — enter SEO text here to improve your website’s search engine ranking and describe the specific exchange. This information is not visible to users when creating an exchange request from the main page.

**Exchange Processing Time** — specify the time frame within which the exchange will be completed. This information is displayed on the selected exchange’s page.

**"Request Pending" Status** — if in the verification module settings for [identity](https://premium.gitbook.io/rukovodstvo-polzovatelya/navigaciya/verifikaciya/verifikaciya-lichnosti)/[account](https://premium.gitbook.io/rukovodstvo-polzovatelya/navigaciya/verifikaciya/verifikaciya-scheta) you have allowed users to create requests without prior verification, be sure to provide instructions for identity/account verification for users.

**Application Status "New Application"** — please provide your payment details for this exchange direction along with a brief instruction outlining the steps the user should follow to complete the exchange. These details will appear on the screen after the user creates an exchange request. Once the user completes the specified steps, they click the "I have paid the application" button, and the exchange administrator receives a notification. If a payment merchant is used for the currency being given, the necessary payment instructions should be provided in the corresponding section (see the "[Merchant Settings](https://premium.gitbook.io/rukovodstvo-polzovatelya/navigaciya/merchanty-i-vyplaty)" chapter).

You may fill in the following application statuses at your discretion, keeping in mind that the text will be displayed to the user after completing the respective stages of the exchange:  
• **"Application canceled by user"**  
• **"Application not created"**  
• **"Application pending verification"**  
• **"Application canceled by user"**  
• **"Deleted application"**  
• **"User proceeded to payment page"**  
• **"User marked application as paid"**  
• **"Waiting for merchant confirmation"**  
• **"Partially paid"**  
• **"Paid application"**  
• **"Application under review"**  
• **"Awaiting AML check"**  
• **"AML check failed"**  
• **"Waiting for merchant details"**  
• **"Merchant error"**  
• **"Erroneous application"**  
• **"Auto payout error"**  
• **"Auto payout error (payment system API)"**  
• **"Waiting for confirmation from auto payout module"**  
• **"Partial payout"**  
• **"Completed application"**  
• Notification prompting the user to complete identity verification  
• Notification prompting the user to complete identity verification (based on exchange amount)

## Tab: "Restrictions and Checks"

<figure><img src="../../.gitbook/assets/image (161).png" alt=""><figcaption></figcaption></figure>

**Visibility of exchange directions for guests** — you can configure the privacy settings for exchange directions as seen by users who are not registered on the site. Additional settings can also be found under "**Exchange Settings** → **Exchange Filters**."

**Reserve Limit for Exchange Direction** — you can set a limit on the available funds for exchange by specifying the desired amount.

**Language** — select the website language for which this exchange direction will be available. If you choose only Russian, users visiting the English version of the site will not see this exchange direction. Additional settings can be found under "**Exchange Settings → Exchange Filters**."

**User Discount** — enable or disable the use of cumulative discounts.

**Maximum Discount for Users** — set the maximum allowed cumulative discount for this exchange direction. If a user’s current discount exceeds this value, their discount will be capped at the specified maximum.

**Wallet Verification Check in Payment System** — you can verify the client’s wallet status based on the number they enter in the exchange form. For this check to work properly, payment systems must be enabled in "**Merchants → Wallet Verification Checker**."

**Require Verified Wallet in Payment System** — you can require clients to have a verified wallet in the payment system.

**Restricted Countries** — you can specify a list of countries whose users will be blocked from accessing the exchange. The system will automatically detect the user’s country based on their IP address and deny access to the exchange direction if there is a match. All other users will have access. To select countries for exchange restrictions, activate the country list in the control panel under "**GEO IP**." Additional settings are also available under "**Exchange Settings → Exchange Filters**."

**Allowed Countries** — You can specify a list of countries from which users are permitted to access the exchange. The system will automatically detect the user’s country based on their IP address and allow access to the exchange direction only if the country matches. Users from other countries will be denied access. To enable the country list, go to the "**GEO IP**" section in the control panel and activate it so you can select countries for the exchange direction. Additional settings can be found under "**Exchange Settings** → **Exchange Filters**."

**Email Verification** — You can send a code via email that the user must enter before the "**Proceed to Payment**" button appears. The code will be sent to the email address provided in one of the following fields: "**From Account**," "**To Account**," or "**Email**." To enable this feature, activate the "**Email Verification**" module in "**Modules** → **Modules**." Configure the module settings under "**Modules** → **Email Verification Settings**" and set up the corresponding [email template](https://premium.gitbook.io/rukovodstvo-polzovatelya/navigaciya/uvedomleniya/opovesheniya-po-e-mail).

**Show Field for Money Transfer Number** — Select "**Yes**" if you want to display a field for entering the money transfer number before the user sees the "**I Have Paid**" / "**Proceed to Payment**" button. The entered number will be visible in the control panel under "**Requests**."

**Label for Money Transfer Number Field** — You can customize the label for this input field.

**SMS Code Verification** — You can send an SMS with a code that the user must enter before the "**Proceed to Payment**" button appears. The SMS will be sent to the phone number provided in one of the following fields: "**From Account**," "**To Account**," or "**Phone**." To enable SMS sending, activate the "**SMS Verification**" module in "**Modules** → **Modules**." Configure the module settings under "**Modules** → **SMS Verification Settings**" and set up the [SMS gateway](https://premium.gitbook.io/rukovodstvo-polzovatelya/navigaciya/uvedomleniya/opovesheniya-po-sms).

**Blocked IP Addresses and Masks (one per line)** — you can specify IP addresses and masks for which access to the exchange direction will be blocked. Each entry must be on a new line.

<figure><img src="../../.gitbook/assets/image (160).png" alt=""><figcaption></figcaption></figure>

**Max number of exchange requests per IP per day** — you can limit the number of requests that can be created from a single IP address within one day.

**Max number of exchange requests per "Give" account per day** — you can limit the number of requests that can be created from a single "Give" account within one day.

**Max number of exchange requests per "Receive" account per day** — you can limit the number of requests that can be created from a single "Receive" account within one day.

**Max number of exchange requests per user per day** — you can limit the number of requests that a single user can create in one day.

**Max number of exchange requests per email per day** — you can limit the number of requests that can be created from a single email address within one day.

**Maximum number of active requests per user** — the maximum number of open requests allowed for one user.

**Prohibit creating requests with the same "Give" amount** — prevents a user from having multiple open requests with the same "Give" amount.

**X19** — for exchanges involving the Webmoney payment system, it is necessary to set the exchange type to perform the verification correctly. The Webmoney system requires this verification for every exchange. You can find more detailed information about the X19 module settings in this [section](https://premium.gitbook.io/rukovodstvo-polzovatelya/navigaciya/nastroiki/kh19).

**Max exchange amount for "Give" for new users** — the maximum exchange amount allowed for users without completed exchanges.

## "Notification Settings" Tab

<figure><img src="../../.gitbook/assets/image (162).png" alt=""><figcaption></figcaption></figure>

In version 2.7, the tab previously named "**Exchange Direction Template**" has been renamed to "**Notification Settings**".

**Template** — a text template used for transmitting information via the `[dirtemp]` shortcode in emails related to requests for this exchange direction.

**Administrator’s E-mail/Phone/Telegram** — contact details of the administrator/operator for request emails (if one or more contact fields are filled in, data from the above template will be sent **only to the specified contacts**, ignoring the recipient list in the general template).

## "Additional Fields" Tab

<figure><img src="../../.gitbook/assets/image (1075).png" alt=""><figcaption></figcaption></figure>

Select the fields that the user must fill out when completing the exchange form. If you have enabled the "**Cash at office ↔ WM**" check in H19, then the "**Passport Number**" field is mandatory.

## "AML" Tab

<figure><img src="../../.gitbook/assets/image (163).png" alt=""><figcaption></figcaption></figure>

AML settings for the exchange direction are described in a [separate guide](https://premium.gitbook.io/main/osnovnye-nastroiki/proverka-aml/nastroika-v-v.2.7#nastroika-modulya-v-napravlenii-obmena).

## "Deleting Unpaid Requests" Tab

<figure><img src="../../.gitbook/assets/image (1223).png" alt=""><figcaption></figcaption></figure>

**Delete requests with status** — if needed, select the request status(es) that will be automatically deleted after a set period. Typically, it is recommended to delete requests with the status "**New request**."

**Custom deletion time for unpaid requests** — if necessary, set a custom time period for deleting unpaid requests. If no custom deletion time is set, unpaid requests will be deleted according to the settings configured under "**Exchange Directions → Automatic deletion of unpaid requests**."

## "Verification" Tab

<figure><img src="../../.gitbook/assets/image (164).png" alt=""><figcaption></figcaption></figure>

Certainly! Here's a natural, fluent English translation of the provided text:

---

**Only for Verified Accounts on the Website** — You can restrict the exchange direction to be available only for verified accounts/wallets on your site. This means that users must complete a certain verification process on your website to gain access to this exchange direction. In the admin panel, under the "**User Accounts**" section and the "**Currencies**" section (when creating or editing a currency), you can configure the corresponding [settings](https://premium.gitbook.io/rukovodstvo-polzovatelya/navigaciya/verifikaciya/verifikaciya-scheta) for this option.

**Only for Verified Users on the Website** — You can restrict the exchange direction to be available only for verified users. This means users must complete a verification procedure on your website to access this exchange direction. In the admin panel, under the "**Verification**" section, you can configure the relevant [settings](https://premium.gitbook.io/rukovodstvo-polzovatelya/navigaciya/verifikaciya/verifikaciya-lichnosti) for this option.  
There is also an option to require verification if the exchange amount in "**Giving**" or "**Receiving**" exceeds a specified threshold. To enable this, select the "**If exchange amount is greater than**" option and enter the amount in the "**Exchange amount for Giving/Receiving**" field.

---

Only for Verified Users on the Website

Exchange Amount for Giving

Verification of the Giving Account

Only for Verified Accounts on the Website

Exchange Amount for Giving

Verification of the Receiving Account

Only for Verified Accounts on the Website

Exchange Amount for Receiving

Verification via Email

Verification via SMS Code

Show Field for Entering Money Transfer Number

Label for Money Transfer Number Input Field

Wallet Verification in the Payment System

Require Verified Wallet in the Payment System

---

## "Currency Accounts" Tab

<figure><img src="../../.gitbook/assets/image (884).png" alt="" width="458"><figcaption></figcaption></figure>

## "TXT and XML Export Settings" Tab

<figure><img src="../../.gitbook/assets/image (949).png" alt=""><figcaption></figcaption></figure>

---

If you need the text adapted for a specific audience or style, feel free to ask!

**Display in file:**  
• "**Yes**" — include the exchange direction in the XML and TXT files with rates  
• "**No**" — exclude the exchange direction from the XML and TXT files with rates  
• "**Scheduled**" — include the exchange direction in the XML and TXT files with rates according to a set schedule (for example, from 10:00 to 22:00).

**Show exchange direction on schedule** — the time period (hours and minutes) during which the exchange direction will be included in the XML and TXT files with rates. Outside of this time, the exchange direction will be hidden in the XML and TXT files with rates.

**City where cash exchange is available** — if the exchange direction involves cash transactions, specify the city code where cash deposits or withdrawals are made for this direction. You can find city codes at [this link](https://www.bestchange.ru/wiki/rates.html).

**Tags for the param parameter** — [additional tags](https://www.bestchange.ru/wiki/rates.html) that will appear within the \<param>\</param> field in the XML rates file.

**Other options:**

Here is a naturalistic English translation of the provided text:

---

• **floating** — used to set the [floating rate label](https://www.bestchange.ru/wiki/labels.html#floating). Specify the time in minutes during which the exchange rate will be fixed. Enter `0` if no fixation is required. You can also use the `%` sign to indicate that the exchange rate is fixed until the market exchange rate changes by the specified percentage.  
• **delay** — used to set the [delay label](https://www.bestchange.ru/wiki/labels.html#delay) for processing the exchange. Specify the delay time in minutes before the exchange is executed.  
• **Default exchange mode** — the exchange mode (automatic or manual) will be determined based on the configured auto-payout module settings.  
• **Auto exchange mode (forced)** — forcibly set the exchange to operate in automatic mode. A corresponding label will appear in the XML and TXT rate files.  
• **Manual exchange mode (forced)** — forcibly set the exchange to operate in manual mode. A corresponding label will appear in the XML and TXT rate files.  
• **Transfer from an individual** — select this if transfers from the exchanger are made on behalf of a private individual.  
• **Transfer from a legal entity** — select this if transfers from the exchanger are made on behalf of a legal entity.

## "Payment Receipts" Tab

<figure><img src="../../.gitbook/assets/image (165).png" alt=""><figcaption></figcaption></figure>

Order status to enable receipt upload

Disable the "I have paid" button until the receipt is uploaded

## "Recalculation of Requests" Tab

{% hint style="danger" %}
The Electrum funds receiving module allows transactions to be canceled and replaced, which can lead to losses for the exchanger if the settings below are not configured in your exchanger. No such cases have been reported for other merchants, but we recommend applying the settings below to fully protect your funds.

When using merchants for receiving funds, it is <mark style="color:red;">**essential**</mark> to recalculate the request amount at least for the "**Paid request**" status in the exchange direction settings (other statuses can be selected optionally at your discretion).

---

If you need the text adapted for a specific audience or style, please let me know!

Here is a natural, fluent English translation of the provided text:

---

or configure automatic status changes of requests to "**Under Review**" if the actual payment amount is less than the original amount (this option is available in the merchant modules settings for receiving funds).

<img src="../../.gitbook/assets/image (328).png" alt="" data-size="original">

---

{% hint style="info" %}
The principle for recalculating requests based on the exchange rate can be further configured in the "**Exchange Settings**" -> "**General Settings**" section.

![](<../../.gitbook/assets/image (1526).png>)  
• **On status change** — recalculation will occur only when the request status changes to those marked in the recalculation settings.

• **By cron** — recalculation will be performed when the [cron job](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-sozdat-zadanie-cron-na-servere) set up on the server runs (the link for the cron job file is under the "**Cron file**" button in the screenshot below), provided the request is in one of the statuses marked for recalculation.

![](<../../.gitbook/assets/image (1528).png>)

• **Always** — recalculation will happen both on status changes and during cron execution.
{% endhint %}

<figure><img src="../../.gitbook/assets/image (956).png" alt=""><figcaption></figcaption></figure>

These options are used to recalculate the exchange amount if the exchange rate or the payment amount in the request has changed.

### **Recalculation Based on Payment Amount**

{% hint style="danger" %}
The Electrum service for receiving BTC allows transactions to be canceled and replaced, which can lead to losses for the exchanger if the settings below are not configured in your exchanger and a fraudster tries to exploit this Electrum feature. If you are using the [Electrum module](https://premium.gitbook.io/main/osnovnye-nastroiki/modul-electrum), it is **essential** to apply the following configuration.

When using merchants for receiving funds, it is **mandatory** to recalculate the request amount at least for the "**Paid request**" status in the exchange direction settings.

![](<../../.gitbook/assets/image (329).png>)

Additionally, you need to set up automatic status changes of requests to "**Under Review**" if the actual payment amount is less than the original amount (this option is located in the merchant modules settings for receiving funds, under the "**Merchants**" section).

<img src="../../.gitbook/assets/image (328).png" alt="" data-size="original">
{% endhint %}

---

If you need any further help or adjustments, feel free to ask!

Select the conditions under which the payout amount will be recalculated if the [payment amount](#user-content-fn-1)[^1] changes.

**Recalculation of the order if the payment amount changes** — conditions that trigger a recalculation:

{% hint style="info" %}
Example:  
**A user created an order to exchange USD for DOGE:**  
• **Exchange rate: 12.853 to 1**  
• **Amount to pay: 1000 USD**  
• **Amount to receive: 77.803 DOGE**

**The payout and receiving amounts were fixed at the time the order was created.**

If this option is enabled, the payout amount will be recalculated according to the following rule:

![](<../../.gitbook/assets/image (1040).png>)

• **No** — option disabled  
• **Yes, always** — recalculation occurs whenever any changes are made to the order  
• **Yes, if the payment amount changes** — recalculation occurs whenever the payment amount changes

_If the actual amount paid by the user changes to 990 USD and the rate remains the same_ — _the amount to receive becomes 77.024 DOGE_  
_If the actual amount paid changes to 1010 USD and the rate remains the same_ — _the amount to receive becomes 78.58 DOGE_  

• **Yes, if the payment amount increases** — recalculation occurs only if the payment amount increases  
_If the actual amount paid changes to 990 USD and the rate remains the same_ — _the amount to receive does not change_  
_If the actual amount paid changes to 1010 USD and the rate remains the same_ — _the amount to receive becomes 78.58 DOGE_  

• **Yes, if the payment amount decreases** — recalculation occurs only if the payment amount decreases  
_If the actual amount paid changes to 990 USD and the rate remains the same_ — _the amount to receive becomes 77.024 DOGE_  
_If the actual amount paid changes to 1010 USD and the rate remains the same_ — _the amount to receive does not change_
{% endhint %}

### **Recalculation based on the exchange rate**

{% hint style="warning" %}
You can configure recalculation based on the exchange rate on a schedule using the option found under "**Exchange Settings**" -> "**General Settings**"  
<img src="../../.gitbook/assets/image (621).png" alt="" data-size="original">


Certainly! Here's a natural, fluent English translation of the provided text:

---

* **When the order status changes** — the recalculation will be performed similarly to the recalculation based on the exchange amount — **only** when the order status changes.
* **By cron** — set up a [cron job](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-sozdat-zadanie-cron-na-servere) to run the recalculation on a schedule.  
  The link for the cron job setup can be found under "**Settings**" -> "**Cron**".  
  ![](<../../.gitbook/assets/image (622).png>)
* **Always** — recalculation will occur both when the cron job runs and when the order status changes.

---

Select the conditions under which the exchange amount will be recalculated if the exchange rate changes for the given direction.

**Recalculate the order if the rate changes** — conditions under which recalculation will be triggered:

{% hint style="info" %}
Example:  
**A user created an order to exchange USD for DOGE:**  
• **Rate: 12.853 to 1**  
• **Amount to pay: 1000 USD**  
• **Amount to receive: 77.803 DOGE**

**The payout and receiving amounts were fixed at the time the order was created.**

Since exchange rates fluctuate constantly, if this option is enabled, the rate will be recalculated according to the selected condition:

![](<../../.gitbook/assets/image (1225).png>)  
• **No** — option disabled  
• **Yes, always** — recalculation occurs on any change to the order  
• **Yes, if the rate changes** — recalculation occurs whenever the rate changes

_Rate changes from 12.853 to 12.85 — amount to pay changes — amount to receive becomes 77.821 DOGE_  
_Rate changes from 12.853 to 12.9 — amount to pay changes — amount to receive becomes 77.519 DOGE_  
• **Yes, if the rate increases** — recalculation occurs only if the rate goes up  
_Rate changes from 12.853 : 1 to 12.8 : 1 — amounts to pay and receive do not change_  
_Rate changes from 12.853 : 1 to 12.9 : 1 — amount to pay changes — amount to receive becomes 77.519 DOGE_  
• **Yes, if the rate decreases** — recalculation occurs only if the rate goes down

_Rate changes from 12.853 : 1 to 12.8 : 1 — amount to pay changes — amount to receive becomes 78.125 DOGE_  
_Rate changes from 12.853 : 1 to 12.9 : 1 — amounts to pay and receive do not change_

---

In the admin panel, click on the "**Rate Recalculation Time**" row.

---

Let me know if you need it adapted for a specific audience or style!

All changes to the rate and amounts for the selected order will be displayed on a separate page.

**Order status for recalculation** — select the status(es) of orders for which the exchange amount will be recalculated. The recalculation will only occur if the status changes to one of the statuses highlighted in the list.

**Perform recalculation after** — the time delay after the order is created before the recalculation takes place.

> For example, if set to 5 minutes, no recalculation will occur within the first 5 minutes after the order is created, even if the conditions for recalculation are met.

## "SEO" Tab

**Exchange name (H1)** — the main heading for the exchange direction on the exchange page.

**Title, keywords, description** — meta tags (title, keywords, description) for the exchange direction.

**OGP title, OGP description** — the title and description for the exchange direction used when sharing the link on social networks.

## "Merchants and Payments" Tab

**Merchant** — if you want the payment for the order to be processed through a merchant, select the appropriate merchant to receive payment from the client. The merchant enables payment acceptance via the payment system’s website. If no merchant is selected, the client will need to make the payment manually following the instructions shown after the order is created. For more details, see [merchant settings](https://premium.gitbook.io/rukovodstvo-polzovatelya/navigaciya/merchanty-i-vyplaty/merchanty).

**Daily limit for merchant** — set a daily limit on the amount the merchant can receive. The merchant will not be able to accept payments exceeding this limit.

**Monthly limit for merchant** — set a monthly limit on the amount the merchant can receive. The merchant will not be able to accept payments exceeding this limit.

**Maximum Payment Amount per Request** — set the maximum payment amount allowed for a single request. The merchant will not be able to accept payments exceeding this limit.

**Auto Payouts** — if you want the system to automatically pay out funds to the client for a request, select the payment system through which the auto payout will be processed. If you do not select anything, payouts for requests must be handled manually by the administrator/operator of the exchange point. For more details, see [Auto Payout Settings](https://premium.gitbook.io/rukovodstvo-polzovatelya/navigaciya/merchanty-i-vyplaty/vyplaty).

**Auto Payout for Requests with the Status "Paid Request":**  
• **"Yes"** — the payout will be made automatically without operator involvement when the request status is "Paid Request."  
• **"No"** — the auto payout must be confirmed manually.  
• **"Default"** — this option will follow the default settings of the corresponding auto payout module.

**Auto Payout for Requests with the Status "Under Review":**  
• **"Yes"** — the payout will be made automatically without operator involvement when the request status is "Under Review."  
• **"No"** — the auto payout must be confirmed manually.  
• **"Default"** — this option will follow the default settings of the corresponding auto payout module.

**Daily Auto Payout Limit** — the daily withdrawal limit for the module. Auto payouts cannot exceed this limit.

**Monthly Auto Payout Limit** — the monthly withdrawal limit for the module. Auto payouts cannot exceed this limit.

**Minimum Auto Payout Amount per Request** — the minimum amount for automatic payouts per request. If the payout amount for a request is equal to or less than this value, the payout will not be processed automatically and must be handled manually.

**Max Auto-Payout Amount per Request** — the maximum amount for automatic payouts on a single request. If the payout amount for a request equals or exceeds this set value, the payout will not be processed automatically. Such requests must be handled manually.

**Auto-Payout Delay (in hours)** — the number of hours by which the automatic payout will be delayed. Once this time has elapsed, the payout will be processed automatically. This requires additional setup of a [cron job scheduler](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-sozdat-zadanie-cron-na-servere) on the server to check the payout timing. The script can be run every minute.

**Who the delay applies to:**  
• "**for everyone**," "**for unregistered users**," or "**for unverified users on the site**" — delay automatic payouts for all users, unregistered users, or unverified users on the site, respectively.  
• "**for newcomers**" — delay automatic payouts only for users making their first exchange. The system identifies "newcomers" based on the setting found under "**Exchange Settings → Exchange Options → Newcomer Check**."

## "Affiliate Program" Tab

<figure><img src="../../.gitbook/assets/image (166).png" alt=""><figcaption></figcaption></figure>

**Affiliate Commissions** — enable or disable commission payments under the affiliate program for the selected exchange direction.

**Fixed Payout Amount to Affiliate** — a fixed amount the affiliate will receive per exchange, regardless of the exchanger’s profit.

**Min. Payout Amount to Affiliate** — the minimum amount an affiliate can request for withdrawal.

**Max. Payout Amount to Affiliate** — the maximum amount an affiliate can request for withdrawal.

**Individual Partner Program Percentage** — a custom partner percentage for a specific referral. This percentage will override the standard partner percentage settings. You can configure the standard partner percentages in the control panel under "**Partner Program** → **Commissions**."

**Maximum Partner Percentage** — the highest partner percentage set in the "**Partner Program** → **Commissions**" section.

[^1]: the user paid less or more than the original amount