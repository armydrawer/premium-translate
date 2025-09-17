# Creating a New Exchange Direction

**Note:** Below is a description of all the options that may appear in the exchange direction configuration form. However, by default, some parameters are not displayed. This is because certain modules in the "**Modules**" → "**Modules**" section are inactive, which prevents the display of specific parameters in the form. The order of parameters in the exchange direction creation form on your website may differ from the order presented below.

After adding [new currencies](https://premium.gitbook.io/rukovodstvo-polzovatelya/navigaciya/valyuty-i-napravleniya/dobavlenie-novoi-valyuty) and specifying their [reserves](https://premium.gitbook.io/rukovodstvo-polzovatelya/navigaciya/rezervy), create an exchange direction. To do this, go to the "**Exchange Directions**" section in the control panel. Click the "**Add**" button located above the list of existing exchanges.

On the page that opens, fill in the required fields to create the exchange direction.

---

## **Tab: "Basic Settings"**

<figure><img src="../../.gitbook/assets/image (1205).png" alt=""><figcaption></figcaption></figure>

- **Direction** — Specify the currencies for "**Give**" and "**Receive**."
- **Technical Name** — The name of the exchange direction displayed in the website's control panel. Leave this field blank to automatically generate a name.
- **Permanent Link** — Manually set the URL segment for the exchange direction: `https://your_domain/exchange-`**`LINK`**`.` This link will provide access to the created exchange direction on the website.

{% hint style="success" %}
The permanent link is automatically generated based on the selected currencies for the exchange direction, but you can customize it.
{% endhint %}

- **Status** — Set the current status of the exchange direction.

---

## **Tab: "Rate"**

<figure><img src="../../.gitbook/assets/image (1152).png" alt=""><figcaption></figcaption></figure>

- **Exchange Rate** — Specify the current exchange rate.
- **Rate Depending on Exchange Amount** — If needed, specify the exchange rate based on the user's exchange amount.

This option also has a settings block in the "**Modules**" ➔ "**Rate Depending on Exchange Amount**" section.

<figure><img src="../../.gitbook/assets/image (2149).png" alt="" width="411"><figcaption></figcaption></figure>

- **Rate Formation Method:**  
  • **Set the rate directly** — Display rates for different amounts, considering specified percentages.  
  <figure><img src="../../.gitbook/assets/image (2152).png" alt="" width="357"><figcaption></figcaption></figure>  
  • **Add a percentage to the rate** — Display the percentage applied to the base exchange rate for different amounts.  
  <figure><img src="../../.gitbook/assets/image (2151).png" alt="" width="355"><figcaption></figcaption></figure>

- **Include in XML 2.0 File with Rates** — Add tiered rates from the exchange direction settings to a new export XML file:  
  • **Yes**  
  • **No**

<figure><img src="../../.gitbook/assets/image (2150).png" alt="" width="375"><figcaption></figcaption></figure>

<details>
<summary>Example</summary>

For instance, you can create a tiered structure where users exchanging smaller amounts receive a less favorable rate compared to the standard rate — encouraging them to exchange larger amounts.

Setting a dependency for the "**Receive**" side of the exchange rate (e.g., BTC-USDT rate):  
#### ![](<../../.gitbook/assets/64fc192780700472f4cff803 (1).png>)

Similarly, you can set a dependency for the "**Give**" side of the exchange rate (e.g., USDT-BTC rate).  

<mark style="color:red;">It is not recommended to set a percentage for the side where "1" is used</mark> — <mark style="color:red;">this will result in a rate like 0.98 to XXX or 1.32 to XXX in the exchange form</mark>.

</details>

- **Rate Depending on Currency Reserve** — If needed, specify the exchange rate based on the reserve of the "**Receive**" currency.

This option also has a settings block in the "**Modules**" ➔ "**Rate Depending on Reserve**" section.

<figure><img src="../../.gitbook/assets/image (2153).png" alt="" width="458"><figcaption></figcaption></figure>

- **Rate Formation Method:**  
  • **Set the rate directly** — Display rates for different reserves, considering specified percentages.  
  • **Add a percentage to the rate** — Display the percentage applied to the base exchange rate for different reserves.

- **Update Rates:**  
  • **During currency actions** — Rates will update when the currency reserve changes.  
  • **On the fly** — Rates will update during the calculation of amounts in an exchange request.

<details>
<summary>Example</summary>

For instance, you can create a tiered structure where, as the currency reserve decreases, the currency becomes more expensive for users. The reserve is always set for the "**Receive**" currency.

![](<../../.gitbook/assets/image (784).png>)

<mark style="color:red;">It is not recommended to set a percentage for the side where "1" is used</mark> — <mark style="color:red;">this will result in a rate like 0.98 to XXX or 1.32 to XXX in the exchange form</mark>.

</details>

{% hint style="danger" %}
If you use the "**Rate Depending on Amount or Reserve**" option, the "**Receive**" field in the exchange form will not be editable (due to technical limitations of the calculation tool).

![](<../../.gitbook/assets/image (1773).png>)
{% endhint %}

- **Exchange Rate from File** — More details can be found [here](https://premium.gitbook.io/rukovodstvo-polzovatelya/navigaciya/kursy/kurs-iz-faila).

- **Exchange Amount Multiplicity** — If this option is enabled, the value selected in the dropdown will be rounded:  
  <figure><img src="../../.gitbook/assets/image (855).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
For example, if "Give" is selected and the multiplicity is 100, when the user enters 12345 in the "Give" field, the value will round down to 12300.
{% endhint %}

- **Profit** — Specify the profit as a percentage or a fixed amount you earn from the exchange. Partner rewards are calculated based on the specified profit.

For monitoring services, standard values are 30% of the profit or 1% of the exchange amount. Each exchange direction can only use one principle (based on amount or profit) for all partners.

If the profit is set to zero, the partner will not receive a reward. If the profit is set to 100%, the partner will effectively earn a reward based on the exchange amount. Detailed information is available in the article ["**Profit and Partner Percentage**"](https://premium.gitbook.io/rukovodstvo-polzovatelya/navigaciya/partnerskaya-programma/pribyl-i-partnerskii-procent).

{% hint style="warning" %}
If the "**Profit**" block is not displayed on the tab, disable the "**Automatic Profit Calculation**" module in the "**Modules**" section.

![](<../../.gitbook/assets/image (604).png>)
{% endhint %}

---

## **Tab: "Cities"**

To select a city for the exchange direction, you must first create a city with the correct code (according to [BestChange rules](https://www.bestchange.ru/wiki/rates.html)) in the "**Cities**" section:

<figure><img src="../../.gitbook/assets/image (837).png" alt="" width="504"><figcaption></figcaption></figure>

Then, in the exchange direction settings, select the city on the "**Cities**" tab and, if necessary, specify additional parameters for the city:

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

- **Add to Rate (Give/Receive)** — Specify an absolute value to be added or subtracted from the base exchange rate.  
  To add a percentage, enter, for example, `*0.9` (≈ -10%) to decrease the rate or `/0.9` (≈ +11%) to increase the rate relative to the base exchange rate.
- **Minimum/Maximum Amount** — Specify the limits for the exchange amount for the selected city (minimum and maximum amounts are specified for the "Give" currency). These limits apply to exchanges on the website and in the export XML file.
- **Profit (from Give/Receive amount)** — Individual profit values that may differ from the general profit values on the "**Rate**" tab.
- **Tags for the "param" Parameter** — Specify parameters according to [BestChange requirements](https://www.bestchange.ru/wiki/rates.html).

<figure><img src="../../.gitbook/assets/image (159).png" alt=""><figcaption></figcaption></figure>

---

## **Tab: "BestChange API Parser" and "BestChange Parser"**

<figure><img src="../../.gitbook/assets/image (856).png" alt=""><figcaption></figcaption></figure>

Detailed descriptions of the options are available in the articles ["**BestChange API Parser**"](https://premium.gitbook.io/main/osnovnye-nastroiki/kursy-valyut/bestchange-api-parser-new-nachinaya-s-v2.6) and ["**BestChange Parser**"](https://premium.gitbook.io/main/osnovnye-nastroiki/kursy-valyut/bestchange-parser-old).

---

## **Tab: "Auto-Rate Adjustment"**

<figure><img src="../../.gitbook/assets/image (883).png" alt=""><figcaption></figcaption></figure>

- **Auto-Rate Adjustment** — Select the source and direction for automatic rate updates on the website.

### Automatic Exchange Rate Updates

To enable automatic exchange rate updates, you need to configure a [task scheduler (cron)](https://premium.gitbook.io/main/osnovnye-nastroiki/kursy-valyut/parser-kursov-valyut-parsery-2.0) on your server. At the top of the "**Parsers 2.0**" section, you’ll find a link labeled "**Cron URL for updating Central Bank and cryptocurrency rates**." This URL must be added to your server’s task scheduler. Updates can be set to run every minute. For more detailed instructions, refer to [this link](https://premium.gitbook.io/main/osnovnye-nastroiki/kursy-valyut/parser-kursov-valyut-parsery-2.0).

---

### Adjusting the Exchange Rate

The "**Add to Rate**" parameter allows you to customize the exchange rate fetched from the source. For the column representing the currency you are giving, leave the value as "**0**" (zero). In the column for the currency you are receiving, you can specify a percentage or a numerical value (negative values are also allowed). This adjustment will automatically be added to the source rate and displayed on the website with the corresponding modification.

---

### Loyalty Program for Authorized Users

Authorized users are automatically enrolled in a loyalty program, which rewards them with discounts based on the total amount they’ve exchanged with you. This discount is automatically applied to the specified rate. To configure the loyalty program, navigate to the "**User Discounts**" section. In the opened window, you can modify the parameters of your loyalty program.

---

## **Exchange Rate Limits Tab**

**Min. Rate/Max. Rate** — If needed, you can set minimum and maximum rate values within which the exchange rate parser will operate. If the rate goes beyond these limits, you can either reset it to the standard rate or keep the last received value until the rate returns to the specified range.

**Standard Rate** — Specify a standard rate to which the system will revert if the rate goes outside the defined range.

---

## **Reserve Tab**

**Reserve** — You can set a custom reserve value for a specific exchange direction. This setting will take precedence over the reserve value specified in the "**Receiving**" currency settings under the "**Currencies**" section. You can also configure a [reserve from a file](https://premium.gitbook.io/rukovodstvo-polzovatelya/navigaciya/rezervy/rezerv-iz-faila), enable auto-reserve, or define a reserve using the field below.

**Reserve Field** — If needed, select "**—From the field below—**" for the "**Reserve**" option, and specify the reserve value in the "**Reserve Field**" parameter. This value will be displayed on the website for the selected exchange direction. This option acts as a limit for the current reserve value and will only work if a reserve is set in the "**Reserve Adjustment**" section. For example, if you set a reserve of 100,000 in the "**Reserve Adjustment**" section but need to limit it to 50,000 for a specific exchange direction, use the "**Reserve Field**" parameter to impose this limit.

**Calculator** — If needed, select "**—By Formula—**" for the "**Reserve**" option, and specify a reserve formula in the "**Calculator**" parameter. For more details, refer to [this link](https://premium.gitbook.io/main/osnovnye-nastroiki/rezervy-valyut/rezerv-ot-drugoi-valyuty/primery-nastroiki-slozhnogo-rezerva-s-ispolzovaniem-formul).

---

## **Payment System Fees Tab**

**Payment System Fees** — Specify the standard percentage or amount charged by the payment system for transactions. This fee will be factored into the exchange calculations for users.

**Payment System Fees (for verified accounts)** — Specify the standard percentage or amount charged by the payment system for transactions involving verified wallets. This fee will also be factored into the exchange calculations for users.

**Exchange Service Pays the Fee** — Check this box if you cover the payment system’s fee on behalf of the client.

**Non-Standard Fee** — Check this box if the payment system charges a fee for incoming payments to the exchange service when using a merchant (e.g., Yandex.Money, Privat24, Liqpay, Qiwi). For more details, refer to [this link](https://premium.gitbook.io/rukovodstvo-polzovatelya/navigaciya/faq/chto-takoe-nestandartnaya-komissiya-v-nastroikakh-merchanta-i-kak-ona-rabotaet).

**Min. Fee Amount** — Specify the minimum fee amount that the payment system can deduct for a transaction, if applicable. If you set this to "**0**" (zero), there will be no restrictions. If a restriction is set, certain fields in the application form will become inactive.

---

## **Exchange Service Fees Tab**

**Additional Fee from Sender** — Specify an additional fee (fromfee) that will be added to the payment amount if required by the exchange service’s policy. This value will appear in the XML file with rates for monitoring services under the \<fromfee> parameter.

**Additional Fee from Recipient** — Specify an additional fee (tofee) that will be deducted from the received amount if required by the exchange service’s policy. This value will appear in the XML file with rates for monitoring services under the \<tofee> parameter.

**Fee Based on Exchange Amount** — Set a fee that varies depending on the exchange amount.

{% hint style="danger" %}
Note: When this option is enabled, the values specified in the "**Additional Fee from Sender/Recipient**" fields will not be used in calculations.

![](<../../.gitbook/assets/image (149).png>)
{% endhint %}

{% hint style="info" %}
If you use the "**Fee Based on Exchange Amount**" option, the "**Receiving**" field in the exchange form will be disabled due to technical limitations of the calculation tool.

![](<../../.gitbook/assets/image (398).png>)
{% endhint %}

<details>
<summary>Example Fee Configuration</summary>

You can create an unlimited number of fee rules.

In the "**Amount**" field, specify the "**Sending**" currency value above which the fee will apply. Fees can be set as percentages or in the exchange currencies:

<img src="../../.gitbook/assets/image (1301).png" alt="" data-size="original">

Note: Once a fee based on the exchange amount is configured, you can only specify the exchange amount in the "**Sending**" field:\
![](<../../.gitbook/assets/image (1302).png>)<img src="../../.gitbook/assets/image (1303).png" alt="" data-size="original">

</details>

**Minimum Fee from Sender** — Specify the minimum additional fee for the sending amount.

**Minimum Fee from Recipient** — Specify the minimum additional fee for the receiving amount.

**Fee Based on Exchange Amount** — Set an additional fee for the exchange service based on the "**Sending**" amount.

**Deduct Fee from Payment Amount** — Check this box if the payment amount should be reduced by the additional fee from the sender.

**Add Fee to Payout Amount** — Check this box if the payout amount should be increased by the additional fee from the recipient.

---

## **Exchange Amount Tab**

**Min/Max Amounts** — Specify the minimum and maximum amounts for exchange requests for the selected currencies.

<figure><img src="../../.gitbook/assets/image (2141).png" alt="" width="563"><figcaption><p>Admin Panel Configuration</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (2140).png" alt="" width="563"><figcaption><p>Limits Displayed on the Website</p></figcaption></figure>

{% hint style="warning" %}
You can also set min/max amounts for only one currency and enable automatic limit recalculation for the other currency based on the exchange rate in the "**Exchange Service Settings**" ➔ "**General Settings**" section.\
![](<../../.gitbook/assets/image (2143).png>)\
In this case, automatic limits will be applied to the second currency.\
![](<../../.gitbook/assets/image (2142).png>)

![](<../../.gitbook/assets/image (2145).png>)
{% endhint %}

---

## **User Information Tab**

<figure><img src="../../.gitbook/assets/image (858).png" alt=""><figcaption></figcaption></figure>

Here’s a naturalistic English translation of the provided text:

---

{% hint style="info" %}
Use exchange direction templates to simplify the process of creating new exchange directions. You can add templates in the website's admin panel under "**Exchange Directions**" → "**Exchange Direction Templates**". For each parameter, add a template whose text will automatically populate the corresponding field when creating a new exchange direction.
{% endhint %}

**Exchange Description** — In this field, include SEO-optimized text that improves your website's search engine rankings and describes the specific exchange. This information is not visible to users when they create an exchange request from the main page.

**Exchange Processing Time** — Specify the time required to complete the exchange. This information will be displayed on the page of the selected exchange.

**Application Status: "Pending Application"** — If the identity/account verification module settings allow users to create applications without prior verification, provide instructions for identity/account verification for users. [Identity Verification](https://premium.gitbook.io/rukovodstvo-polzovatelya/navigaciya/verifikaciya/verifikaciya-lichnosti) / [Account Verification](https://premium.gitbook.io/rukovodstvo-polzovatelya/navigaciya/verifikaciya/verifikaciya-scheta).

**Application Status: "New Application"** — Provide your payment details for this exchange direction and a brief guide on the steps involved in the exchange process. These details will appear on the screen after the user creates an exchange request. Once the user completes the specified steps, they click the "I Paid" button, and the exchange administrator receives a notification. If a payment merchant is used for the outgoing currency, include the necessary payment instructions in the relevant section (see "[Merchant Settings](https://premium.gitbook.io/rukovodstvo-polzovatelya/navigaciya/merchanty-i-vyplaty)").

You can customize the following application statuses as needed, keeping in mind that the text will appear on the user's screen after they complete the corresponding exchange stage:  
• **"Application Canceled by User"**  
• **"Application Not Created"**  
• **"Application Pending Verification"**  
• **"Application Canceled by User"**  
• **"Deleted Application"**  
• **"When User Navigates to Payment Page"**  
• **"User Marked Application as Paid"**  
• **"Awaiting Merchant Confirmation"**  
• **"Partially Paid"**  
• **"Paid Application"**  
• **"Application Under Review"**  
• **"Awaiting AML Check"**  
• **"AML Check Failed"**  
• **"Awaiting Merchant Details"**  
• **"Merchant Error"**  
• **"Erroneous Application"**  
• **"Auto-Payout Error"**  
• **"Auto-Payout Error (Payment System API)"**  
• **"Awaiting Auto-Payout Module Confirmation"**  
• **"Partial Payout"**  
• **"Completed Application"**  
• **Notification to Complete Identity Verification**  
• **Notification to Complete Identity Verification (Based on Exchange Amount)**  

## "Restrictions and Checks" Tab

<figure><img src="../../.gitbook/assets/image (161).png" alt=""><figcaption></figcaption></figure>

**Visibility of Exchange Directions for Guests** — You can set privacy settings for exchange directions for users who are not registered on the site. Additional settings can be found under "**Exchange Settings**" → "**Exchange Filters**".

**Reserve Limit for the Direction** — You can limit the available funds for exchange by specifying the desired amount.

**Language** — Select the language for which the exchange direction will be available. If you select only Russian, users accessing the English version of the site will not see this exchange direction. Additional settings can be found under "**Exchange Settings**" → "**Exchange Filters**".

**User Discount** — Enable or disable the cumulative discount feature.

**Maximum User Discount** — Set the maximum cumulative discount for this direction. If a user’s current discount exceeds this value, it will be capped at the specified limit.

**Wallet Verification Check in Payment System** — You can verify the status of a user’s wallet based on the number they provide when filling out the exchange form. To enable this feature, activate payment systems under "**Merchants**" → "**Wallet Verification Checker**".

**Require Verified Wallet in Payment System** — You can require users to have a verified wallet in the payment system.

**Restricted Countries** — Specify a list of countries where users will be denied access to the exchange direction. The system will automatically determine the user’s country based on their IP address and block access if there’s a match. To enable this feature, activate the country list in the admin panel under "**GEO IP**". Additional settings can be found under "**Exchange Settings**" → "**Exchange Filters**".

**Allowed Countries** — Specify a list of countries where users will be granted access to the exchange direction. The system will automatically determine the user’s country based on their IP address and allow access if there’s a match. All other users will be denied access. To enable this feature, activate the country list in the admin panel under "**GEO IP**". Additional settings can be found under "**Exchange Settings**" → "**Exchange Filters**".

**Email Verification** — You can send users an email with a code they must enter before the "**Proceed to Payment**" button appears. The email will be sent to the address specified in one of the following fields: "**From Account**", "**To Account**", or "**Email**". To enable this feature, activate the "**Email Verification**" module under "**Modules**" → "**Modules**". Configure the module settings under "**Modules**" → "**Email Verification Settings**" and [set up the corresponding email template](https://premium.gitbook.io/rukovodstvo-polzovatelya/navigaciya/uvedomleniya/opovesheniya-po-e-mail).

**Show Field for Entering Money Transfer Number** — Select "**Yes**" if you want to display a field for entering the money transfer number before the "**I Paid**"/"**Proceed to Payment**" button appears. The entered number will be displayed in the admin panel under "**Applications**".

**Field Name for Money Transfer Number** — You can specify a custom name for this field.

**SMS Code Verification** — You can send users an SMS with a code they must enter before the "**Proceed to Payment**" button appears. The SMS will be sent to the phone number specified in one of the following fields: "**From Account**", "**To Account**", or "**Phone**". To enable this feature, activate the "**SMS Verification**" module under "**Modules**" → "**Modules**". Configure the module settings under "**Modules**" → "**SMS Code Verification Settings**" and set up the [SMS gateway](https://premium.gitbook.io/rukovodstvo-polzovatelya/navigaciya/uvedomleniya/opovesheniya-po-sms).

**Blocked IP Addresses and Masks (One Per Line)** — You can specify IP addresses and masks that will be denied access to the exchange direction. Enter each value on a new line.

<figure><img src="../../.gitbook/assets/image (160).png" alt="" width="563"><figcaption></figcaption></figure>

**Max Number of Exchange Applications Per IP Per Day** — Limit the number of applications that can be created from a single IP address in a day.

**Max Number of Exchange Applications Per "From Account" Per Day** — Limit the number of applications that can be created from a single "From Account" in a day.

**Max Number of Exchange Applications Per "To Account" Per Day** — Limit the number of applications that can be created from a single "To Account" in a day.

**Max Number of Exchange Applications Per User Per Day** — Limit the number of applications that can be created by a single user in a day.

**Max Number of Exchange Applications Per Email Per Day** — Limit the number of applications that can be created from a single email address in a day.

--- 

Let me know if you need further refinements!

### Maximum Number of Active Requests per User
This refers to the maximum number of open requests that a single user can have at any given time.

### Prohibit Creating Requests with the Same "Giving" Amount
This setting prevents users from having multiple open requests with the same "giving" amount.

### X19
For exchanges involving the WebMoney payment system, it is necessary to configure the exchange type to ensure proper verification. WebMoney requires this verification process to be completed for all exchanges. You can find more details about configuring the X19 module in this [section](https://premium.gitbook.io/rukovodstvo-polzovatelya/navigaciya/nastroiki/kh19).

### Max Exchange Amount for "Giving" for New Users
This sets the maximum exchange amount for users who have not yet completed any exchanges.

---

## "Notification Settings" Tab

<figure><img src="../../.gitbook/assets/image (162).png" alt="" width="563"><figcaption></figcaption></figure>

{% hint style="success" %}
In version 2.7, the "**Exchange Direction Template**" tab has been renamed to "**Notification Settings**."
{% endhint %}

### Template
This is a text template that can be used via the shortcode `[dirtemp]` in emails related to specific exchange directions.

<figure><img src="../../.gitbook/assets/image (2215).png" alt=""><figcaption></figcaption></figure>

### Admin Contact Information (Email/Phone/Telegram)
These are the administrator/operator contact details for request-related emails. If one or more contact fields are filled out, the data from the template above will only be sent to the specified contacts, ignoring the recipient list in the general template.

---

## "Additional Fields" Tab

<figure><img src="../../.gitbook/assets/image (1075).png" alt="" width="563"><figcaption></figcaption></figure>

Select the fields that users must fill out when completing the exchange form. If you have enabled the "**Cash in Office ↔ WM**" verification in X19, the "**Passport Number**" field becomes mandatory.

---

## "AML" Tab

<figure><img src="../../.gitbook/assets/image (163).png" alt="" width="563"><figcaption></figcaption></figure>

AML (Anti-Money Laundering) settings for exchange directions are described in a [separate guide](https://premium.gitbook.io/main/osnovnye-nastroiki/proverka-aml/nastroika-v-v.2.7#nastroika-modulya-v-napravlenii-obmena).

---

## "Unpaid Requests Deletion" Tab

<figure><img src="../../.gitbook/assets/image (1223).png" alt="" width="563"><figcaption></figcaption></figure>

### Delete Requests with Status
Select the request status(es) that should be automatically deleted after a specified time. It is generally recommended to delete requests with the status "**New Request**."

### Custom Time for Deleting Unpaid Requests
If needed, set a custom time for deleting unpaid requests. If no custom time is specified, unpaid requests will be deleted according to the settings in the "**Exchange Directions → Automatic Deletion of Unpaid Requests**" section.

---

## "Verification" Tab

<figure><img src="../../.gitbook/assets/image (164).png" alt="" width="563"><figcaption></figcaption></figure>

### Only for Verified Accounts on the Website
This option allows you to restrict exchange directions to verified accounts/wallets. Users must complete a specific verification process on your website to access the exchange direction. You can configure this option in the "**User Accounts**" section or the "**Currencies**" section (when creating/editing a currency). More details can be found [here](https://premium.gitbook.io/rukovodstvo-polzovatelya/navigaciya/verifikaciya/verifikaciya-scheta).

### Only for Verified Users on the Website
This option restricts exchange directions to verified users. Users must complete a specific verification process on your website to access the exchange direction. You can configure this option in the "**Verification**" section. Additionally, you can require verification if the exchange amount in "**Giving**" or "**Receiving**" exceeds a specified value. To do this, select the "**If exchange amount exceeds**" parameter and set the amount in the "**Exchange Amount for Giving/Receiving**" field.

---

## "Currency Accounts" Tab

<figure><img src="../../.gitbook/assets/image (884).png" alt="" width="458"><figcaption></figcaption></figure>

### Method:
- **Random**: Accounts will be assigned in rotation, allowing for reuse (this is the most commonly used method).
- **Once per Direction per Day**: Each account will only be assigned to one request per day.
- **Once per Direction per Month**: Each account will only be assigned to one request per month.

### Accounts
Select the accounts to be used for this exchange direction.

---

## "TXT and XML Export Settings" Tab

<figure><img src="../../.gitbook/assets/image (949).png" alt="" width="563"><figcaption></figcaption></figure>

### Show in File:
- **Yes**: Include the exchange direction in XML and TXT files with rates.
- **No**: Exclude the exchange direction from XML and TXT files with rates.
- **By Schedule**: Include the exchange direction in XML and TXT files with rates according to a specified schedule (e.g., from 10:00 to 22:00).

### Show Exchange Direction by Schedule
Specify the time period (hours and minutes) during which the exchange direction will appear in XML and TXT files with rates. Outside of this time, the exchange direction will be hidden.

### City Where Cash Exchange is Available
If the exchange direction involves cash, specify the city code where cash is accepted or issued. City codes can be found [here](https://www.bestchange.ru/wiki/rates.html).

### Tags for the "param" Parameter
[Additional tags](https://www.bestchange.ru/wiki/rates.html) that will appear in the `<param></param>` field in XML files with rates.

### Other Options:
- **floating**: Sets a [floating rate tag](https://www.bestchange.ru/wiki/labels.html#floating). Specify the time in minutes for which the exchange rate will be fixed. Use `0` for no fixation. You can also use a `%` sign to fix the rate until the market exchange rate changes by the specified percentage.
- **delay**: Sets a [delay tag](https://www.bestchange.ru/wiki/labels.html#delay) for the exchange. Specify the delay time in minutes.
- **Default Exchange Mode**: The exchange mode (automatic or manual) will be determined based on the auto-payout module settings.
- **Force Automatic Exchange Mode**: Forces the exchange to be conducted in automatic mode. This will be reflected in XML and TXT files with rates.
- **Force Manual Exchange Mode**: Forces the exchange to be conducted in manual mode. This will be reflected in XML and TXT files with rates.
- **Transfer from Individual**: Indicates that transfers from the exchanger are made on behalf of an individual.
- **Transfer from Legal Entity**: Indicates that transfers from the exchanger are made on behalf of a legal entity.

---

## "Payment Receipts" Tab

<figure><img src="../../.gitbook/assets/image (165).png" alt="" width="308"><figcaption></figcaption></figure>

### Order Status for Enabling Upload
Select the statuses in which the field for uploading receipts will be displayed.

### Disable "I Paid" Button Until Receipt is Uploaded
Before clicking the "I Paid" button, the client will be required to upload a receipt.

---

## "Request Recalculation" Tab

{% hint style="danger" %}
The Electrum module for receiving funds allows transactions to be canceled or replaced, which could result in the exchanger losing funds if the settings below are not configured. While no such cases have been reported for other merchants, we recommend using the settings below to fully protect your funds.
{% endhint %}

### Using Merchants for Payment Processing

When using merchants to accept payments, it is **necessary** to recalculate the application amount, at the very least, for the "**Paid Application**" status in the exchange direction settings (other statuses can be marked optionally at your discretion).

![](<../../.gitbook/assets/image (329).png>)

Alternatively, you can configure automatic transfer of applications to the "**Under Review**" status if the actual payment amount is less than the original amount. This option is available in the merchant module settings for payment acceptance.

<img src="../../.gitbook/assets/image (328).png" alt="" data-size="original">

{% hint style="info" %}
The recalculation logic for applications based on the exchange rate can be further configured in the "**Exchange Settings**" -> "**General Settings**" section.

![](<../../.gitbook/assets/image (1526).png>)\
• **When changing the application status** — recalculation will occur only when the application status changes to one of the statuses marked in the recalculation settings.

• **By cron** — recalculation will occur when a [cron job](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-sozdat-zadanie-cron-na-servere) is executed on the server (the link for the cron job is located under the "**Cron File**" button in the screenshot below), provided the application is in one of the statuses marked in the recalculation settings.

![](<../../.gitbook/assets/image (1528).png>)

• **Always** — recalculation will occur both when the application status changes and when the cron job is executed.
{% endhint %}

<figure><img src="../../.gitbook/assets/image (956).png" alt="" width="563"><figcaption></figcaption></figure>

These options are used to recalculate the exchange amount if the exchange rate or payment amount in the application changes.

---

### **Recalculation Based on Payment Amount**

{% hint style="danger" %}
The Electrum service for receiving BTC allows transactions to be canceled or replaced, which could lead to financial losses for the exchange service if the following settings are not configured and a fraudster attempts to exploit this feature. If you are using the [Electrum module](https://premium.gitbook.io/main/osnovnye-nastroiki/modul-electrum), it is **mandatory** to configure the following settings.

When using merchants to accept payments, it is **mandatory** to recalculate the application amount at least for the "**Paid Application**" status in the exchange direction settings.

![](<../../.gitbook/assets/image (329).png>)

Additionally, you must configure automatic transfer of applications to the "**Under Review**" status if the actual payment amount is less than the original amount. This option can be found in the merchant module settings under the "**Merchants**" section.

<img src="../../.gitbook/assets/image (328).png" alt="" data-size="original">
{% endhint %}

Select the conditions under which the payout amount will be recalculated if the [payment amount](#user-content-fn-1)[^1] changes.

**Recalculation of the application if the payment amount changes** — conditions under which recalculation will occur:

{% hint style="info" %}
Example:\
**A user created an application to exchange USD for DOGE:**\
• **Exchange rate: 12.853 to 1**\
• **Amount to pay: 1000 USD**\
• **Amount to receive: 77.803 DOGE**

**The payout and receiving amounts were fixed when the application was created.**

If the option is enabled, the payout amount will be recalculated based on the condition:

![](<../../.gitbook/assets/image (1040).png>)

• **No** — the option is disabled.\
• **Yes, always** — recalculation will occur for any changes in the application.\
• **Yes, if the payment amount changes** — recalculation will occur for any change in the payment amount.

_If the actual amount paid by the user changes to 990 USD (with no change in the exchange rate), the amount to receive will become 77.024 DOGE._\
_If the actual amount paid by the user changes to 1010 USD (with no change in the exchange rate), the amount to receive will become 78.58 DOGE._

• **Yes, if the payment amount increases** — recalculation will occur only if the payment amount increases.\
_If the actual amount paid by the user changes to 990 USD, the amount to receive will not change._\
_If the actual amount paid by the user changes to 1010 USD, the amount to receive will become 78.58 DOGE._

• **Yes, if the payment amount decreases** — recalculation will occur only if the payment amount decreases.\
_If the actual amount paid by the user changes to 990 USD, the amount to receive will become 77.024 DOGE._\
_If the actual amount paid by the user changes to 1010 USD, the amount to receive will not change._
{% endhint %}

---

### **Recalculation Based on Exchange Rate**

{% hint style="warning" %}
You can configure recalculation based on the exchange rate on a schedule using the option in the "**Exchange Settings**" -> "**General Settings**" section.\
<img src="../../.gitbook/assets/image (621).png" alt="" data-size="original">

* **When changing the application status** — recalculation will occur similarly to recalculation based on payment amount — **only** when the application status changes.
* **By cron** — set up a [cron job](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-sozdat-zadanie-cron-na-servere) to trigger recalculation on a schedule.\
  The cron job link is located in the "**Settings**" -> "**Cron**" section.\
  ![](<../../.gitbook/assets/image (622).png>)
* **Always** — recalculation will occur both when the cron job is executed and when the application status changes.
{% endhint %}

Select the conditions under which the exchange amount will be recalculated if the exchange rate changes.

**Recalculation of the application if the exchange rate changes** — conditions under which recalculation will occur:

{% hint style="info" %}
Example:\
**A user created an application to exchange USD for DOGE:**\
• **Exchange rate: 12.853 to 1**\
• **Amount to pay: 1000 USD**\
• **Amount to receive: 77.803 DOGE**

**The payout and receiving amounts were fixed when the application was created.**

Exchange rates constantly fluctuate — if the option is enabled, the rate will be recalculated based on the condition:

![](<../../.gitbook/assets/image (1225).png>)\
• **No** — the option is disabled.\
• **Yes, always** — recalculation will occur for any changes in the exchange rate.\
• **Yes, if the exchange rate changes** — recalculation will occur for any change in the exchange rate.

_If the rate changes from 12.853 to 12.85, the amount to receive will become 77.821 DOGE._\
_If the rate changes from 12.853 to 12.9, the amount to receive will become 77.519 DOGE._

• **Yes, if the rate increases** — recalculation will occur only if the rate increases.\
_If the rate changes from 12.853 to 12.8, the amount to receive will not change._\
_If the rate changes from 12.853 to 12.9, the amount to receive will become 77.519 DOGE._

• **Yes, if the rate decreases** — recalculation will occur only if the rate decreases.\
_If the rate changes from 12.853 to 12.8, the amount to receive will become 78.125 DOGE._\
_If the rate changes from 12.853 to 12.9, the amount to receive will not change._

In the admin panel, click on the "**Exchange Rate Recalculation Time**" row.

![](<../../.gitbook/assets/image (19).png>)\
All changes to the rate and amounts for the selected application will be displayed on a separate page.\
![](<../../.gitbook/assets/image (20).png>)
{% endhint %}

---

### **SEO Tab**

<figure><img src="../../.gitbook/assets/image (1077).png" alt="" width="563"><figcaption></figcaption></figure>

**Exchange Name (H1)** — the title for the exchange direction on the exchange page.

<figure><img src="../../.gitbook/assets/Screenshot_9 (3).png" alt="" width="563"><figcaption><p><strong>Exchange Name (H1)</strong></p></figcaption></figure>

**Title, Keywords, Description** — meta tags (title, keywords, description) for the exchange direction.

**OGP Title, OGP Description** — the title and description for social media when sharing a link to the exchange direction.

---

### **Merchants and Payouts Tab**

<figure><img src="../../.gitbook/assets/image (872).png" alt="" width="563"><figcaption></figcaption></figure>

**Merchant** — if you want payments for applications to be processed through a merchant, select the appropriate merchant for accepting payments from clients. A merchant allows payments to be accepted via the payment system's website. If no merchant is selected, the client will need to make the payment manually following the instructions provided after the application is created. Learn more about [merchant settings](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).

**Daily Merchant Limit** — the daily limit for accepting payments through the merchant. The merchant will not be able to accept payments exceeding this limit.

**Monthly Merchant Limit** — the monthly limit for accepting payments through the merchant. The merchant will not be able to accept payments exceeding this limit.

Here’s the translated text in natural, professional English:

---

**Maximum Payment Amount per Request** — This is the maximum payment amount allowed for a single request. Merchants will not be able to accept payments exceeding this limit.

**Auto-Payouts** — If you want the system to automatically pay out funds to the client based on their request, select the appropriate payment system through which the auto-payout will be processed. If no payment system is selected, payouts will need to be processed manually by the administrator/operator of the exchange service. Learn more about [auto-payout settings](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-avtovyplat).

**Auto-Payout for Requests with the Status "Paid Request":**  
• **Yes** — Auto-payout will be processed automatically without operator involvement when the request status is "Paid Request."  
• **No** — The auto-payout must be manually confirmed for the request.  
• **Default** — This option will follow the default settings configured in the corresponding auto-payout module.

**Auto-Payout for Requests with the Status "Under Review":**  
• **Yes** — Auto-payout will be processed automatically without operator involvement when the request status is "Under Review."  
• **No** — The auto-payout must be manually confirmed for the request.  
• **Default** — This option will follow the default settings configured in the corresponding auto-payout module.

**Daily Auto-Payout Limit** — The daily withdrawal limit for the module. Auto-payouts cannot exceed this limit.

**Monthly Auto-Payout Limit** — The monthly withdrawal limit for the module. Auto-payouts cannot exceed this limit.

**Minimum Auto-Payout Amount per Request** — The minimum amount for automatic payouts for a single request. If the payout amount for a request is equal to or less than this value, the payout will not be processed automatically. Such requests will need to be handled manually.

**Maximum Auto-Payout Amount per Request** — The maximum amount for automatic payouts for a single request. If the payout amount for a request is equal to or exceeds this value, the payout will not be processed automatically. Such requests will need to be handled manually.

**Auto-Payout Delay (in hours)** — The number of hours by which the auto-payout will be delayed. Once the specified time has elapsed, the auto-payout will be processed. Additional configuration of the [task scheduler (cron)](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-sozdat-zadanie-cron-na-servere) on the server is required to check the auto-payout timing. The script can be set to run every minute.

**Who the Delay Applies To:**  
• "**For everyone**," "**For unregistered users**," or "**For unverified users on the site**" — Delay auto-payouts for all users, unregistered users, or unverified users on the site, respectively.  
• "**For new users**" — Delay auto-payouts only for users making their first exchange. The system identifies "new users" based on the settings configured in "**Exchange Settings" → "Exchange Configuration" → "New User Check."**

---

## **"Affiliate Program" Tab**

<figure><img src="../../.gitbook/assets/image (166).png" alt="" width="563"><figcaption></figcaption></figure>

**Affiliate Commissions** — Enable or disable commission payouts for the affiliate program for the selected exchange direction.

**Fixed Payout Amount for Partner** — A fixed amount that the partner will receive from the exchange, regardless of the exchange service's profit.

**Minimum Payout Amount for Partner** — The minimum amount a partner can request for withdrawal.

**Maximum Payout Amount for Partner** — The maximum amount a partner can request for withdrawal.

**Custom Affiliate Program Percentage** — A custom affiliate percentage for the selected exchange direction. This percentage will override the standard affiliate percentage settings. You can configure the standard affiliate percentages in the "**Affiliate Program" → "Commissions"** section of the admin panel.

**Maximum Affiliate Percentage** — The maximum affiliate percentage specified in the "**Affiliate Program" → "Commissions"** section.

[^1]: The user paid less or more than the original amount.

--- 

Let me know if you need further refinements!