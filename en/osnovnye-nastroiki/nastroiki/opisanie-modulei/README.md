# Module Descriptions

The modules described below can be activated or deactivated in the "**Modules" → "Modules"** section.

<details>

<summary>Exchange Rate Auto-Broker</summary>

This module allows you to link the exchange rate on your site to the rate of another exchange service.

</details>

<details>

<summary>Automatic User Registration</summary>

This module enables automatic user registration on the site when an exchange is made.

To ensure the module works correctly, you need to configure the email template in the "**Messages" → "Email Templates" → "Registration Form"** section.

</details>

<details>

<summary>Automatic Currency Reserve Updates (via Cron)</summary>

This module allows for updating currency reserves using a task scheduler (Cron). This option is relevant only for automatic reserves.

The link for the task scheduler can be found in the "**Currencies"** section under the "**Cron Link"** column.

</details>

<details>

<summary>Automatic Deletion of Unpaid Requests</summary>

This module allows you to set a time for the automatic deletion of requests with the statuses: "**new request**", "**when the user navigated to the payment page**", "**the user marked the request as paid**".

Module settings can be found in the "**Exchange Directions" → "Automatic Deletion of Unpaid Requests"** section. Additionally, each exchange direction has its own settings for the automatic deletion of unpaid requests, located in the direction settings under the "**Deletion of Unpaid Requests"** tab.

</details>

<details>

<summary>Archiving Old Requests</summary>

This module allows you to archive requests that are older than two months. Archived requests are moved to the "**Requests" → "Archived Requests"** section. If archiving is already in operation, deactivating the module will cause issues with displaying currency reserves, partner balances, and user discount amounts.

</details>

<details>

<summary>Advantages Block</summary>

This module allows you to display the advantages of your site on the homepage. You can set an icon and a description for it.

Module settings can be found in the "**Advantages"** section.

</details>

<details>

<summary>Partners Block</summary>

This module allows you to display a block with partner logos on the homepage.

Module settings can be found in the "**Partners"** section.

</details>

<details>

<summary>Account Number Validator</summary>

This module allows you to check the validity (correctness) of a Bitcoin address and bank card number during request creation.

Module settings can be found in the "**Merchants" → "Account Number Validator"** section.

</details>

<details>

<summary>User Verification</summary>

This module allows users to undergo identity verification with the option to upload images.

For more details about the module's capabilities, read [here](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/verifikaciya/verifikaciya-lichnosti).

</details>

<details>

<summary>User Account Verification</summary>

This module allows all registered users to verify their accounts by uploading images/photos.

For example, a user can upload a photo of the front side of their bank card. There is also an option to restrict request creation for unverified accounts on the site. For more details about the module's settings, read [here](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/verifikaciya/verifikaciya-scheta).

</details>

<details>

<summary>Request Status Check Widget</summary>

This module allows users to check the status of their requests on the site. The form for checking request status is available in a sidebar widget and as a separate page.

Module settings can be found in the "**Appearance" → "Widgets" → "Request Status Check"** section.

</details>

<details>

<summary>Internal Account</summary>

This module allows users to make exchanges on the site using their internal account, which is accessible in their personal dashboard.

For more details about the module's capabilities, read [here](https://premium.gitbook.io/main/osnovnye-nastroiki/nastroiki/vnutrennie-scheta/obmen-s-uchastiem-vnutrennego-scheta-polzovatelya).

</details>

<details>

<summary>Hotkeys</summary>

This module allows you to manage the status of requests using keyboard shortcuts.

Module settings can be found in the "**Hotkeys"** section.

</details>

<details>

<summary>IP Address Detector</summary>

This module allows you to determine the user's country based on their IP address. It is an addition to the GEO IP module.

</details>

<details>

<summary>Additional Exchange Point Commission in the General Table</summary>

This module allows you to display the parameters "**Additional Commission from Sender**" and "**Additional Commission from Recipient**" in the general table of exchange directions in the site management panel for quick access.

</details>

<details>

<summary>Additional Commission Based on Exchange Amount</summary>

This module allows you to set the exchange point's commission based on the amount being exchanged.

Module settings can be found in the settings of any exchange direction under the "**Exchange Point Commissions**" tab with the parameter "**Additional Commission Based on Exchange Amount**".

</details>

<details>

<summary>Additional Filters for the "Requests" Section</summary>

This module allows you to display additional buttons for filtering requests based on specific parameters.

The filters can be found in the "**Requests"** section under each request.

</details>

<details>

<summary>Time-Based Access to the Control Panel</summary>

This module allows you to restrict access to the control panel based on a time interval (working hours).

Module settings can be found in the "**Users" → "Time-Based Access to the Control Panel"** section.

</details>

<details>

<summary>Bookmarks for Admin Bar</summary>

This module allows you to save sections of the site as bookmarks for quick access. At the top of the screen, you will see a red heart icon and the text "**Add to Bookmarks**". Navigate to the section you want to bookmark and click on "**Add to Bookmarks**". Hover over the heart icon to see a list of bookmarks for quick access to sections.

Module settings can be found in the "**Modules" → "Bookmark Sorting"** section.

</details>

<details>

<summary>Reserve Request</summary>

This module allows users to submit a request for reserve in an exchange direction.

![](<../../../.gitbook/assets/image (1947).png>)

![](<../../../.gitbook/assets/image (1949).png>)

Requests from clients will be displayed in the "**Reserve Requests**" section.

![](<../../../.gitbook/assets/image (1950).png>)

When the necessary reserve becomes available in the exchange direction, the user will receive a notification via email (if the corresponding template is activated and configured).&#x20;

![](<../../../.gitbook/assets/image (1951).png>)

</details>

<details>

<summary>Captcha for Admin Panel</summary>

Captcha with mathematical operations: multiplication, addition, subtraction.

Module settings can be found in the "**Exchange Settings" → "General Settings"** section.

</details>

<details>

<summary>Captcha for the Site</summary>

Captcha with mathematical operations: multiplication, addition, subtraction.

Module settings can be found in the "**Modules" → "Captcha"** section.

Module settings can also be found in the "**Exchange Settings" → "General Settings"** section.

</details>

<details>

<summary>Captcha for the Site (Image Selection)</summary>

This module allows you to create custom captcha options based on selecting the correct image from those presented.

Module settings can be found in the "**Image Selection Captcha"** section.

</details>

<details>

<summary>Coupon Code for Auto-Payment (do not activate unless necessary)</summary>

This module allows you to display a coupon code in the site management panel in the "**Requests"** section within the request card, as well as for the user in their personal dashboard in the "**Your Operations"** section and via shortcode in the request itself. It is not advisable to activate this module, as if a malicious actor gains access to a user's personal account, they could misuse an unredeemed coupon.

</details>

<details>

<summary>Comments on Requests</summary>

This module allows you to leave comments on requests. There are two types of comments: for the administrator and for the user. User comments can be displayed in the user's request.

</details>

<details>

<summary>Contact Form</summary>

This module allows you to display a feedback form on the site.

</details>

<details>

<summary>Copying Exchange Directions</summary>

In the "**Exchange Directions**" section, there is a button for copying an exchange direction.

</details>

<details>

<summary>Rate Based on Reserve</summary>

This module allows you to set exchange rates that depend on the available reserves.

Here’s a naturalistic English translation of the provided text:

---

<details>

<summary>Exchange Rate Based on Currency Reserve</summary>

This module allows you to set an exchange rate that will vary depending on the currency reserve.

You can find the settings for this option in the exchange direction settings under the "**Rate**" tab.

</details>

<details>

<summary>Exchange Rate Based on Exchange Amount</summary>

This module allows you to set an exchange rate that will change based on the amount being exchanged.

You can find the settings for this option in the exchange direction settings under the "**Rate**" tab.

</details>

<details>

<summary>Currency Reserve Limit</summary>

This module allows you to set daily and monthly limits for receiving and disbursing funds in the settings for each currency.

</details>

<details>

<summary>Currency Reserve Limit by Exchange Direction</summary>

This module allows you to limit the currency reserve for a specific exchange direction. The limit can be set in the settings for each exchange direction under the "**Reserve**" tab.

</details>

<details>

<summary>Application Status Log</summary>

This module allows you to track changes in the status of applications.

The module settings can be found in the "**Applications**" → "**Application Status Log**" section.

</details>

<details>

<summary>Auto-Payment Logs (Do not activate unless necessary)</summary>

This module allows you to log errors that occur during automatic payments. It should only be used for diagnostic purposes, so activating this module without necessity is not recommended.

The module settings can be found in the "**Merchants**" → "**Auto-Payment Log**" section.

</details>

<details>

<summary>Merchant Logs (Do not activate unless necessary)</summary>

This module allows you to log responses from payment systems when processing payments through a merchant. It should only be used for diagnostic purposes, so activating this module without necessity is not recommended.

The module settings can be found in the "**Merchants**" → "**Merchant Log**" section.

</details>

<details>

<summary>User Login in Application</summary>

This module displays the user's login in the application card.

</details>

<details>

<summary>Admin Action Logging</summary>

This module logs all actions taken by users in the site management panel.

</details>

<details>

<summary>Logging Changes to Currency Exchange Rates</summary>

This module records changes to the rates specified in the "**Currency Codes**" section.

</details>

<details>

<summary>Logging Changes to Exchange Rates</summary>

This module records changes to the exchange rates for specific directions.

</details>

<details>

<summary>Maximum Display Value for Currency Reserve</summary>

This module allows you to limit the current reserve value in the currency settings.

</details>

<details>

<summary>Max Number of Decimal Places in Database</summary>

This module allows you to limit the maximum number of decimal places stored in the database for exchange rates, reserves, etc.

The module settings can be found in the "**Exchange Settings**" → "**Exchange Settings**" → "**Max Number of Decimal Places in Site Calculations / Max Number of Decimal Places in Reserve Calculations / Max Number of Decimal Places in Currency Exchange Rate Calculations**" section.

</details>

<details>

<summary>Mass Reserve Adjustment</summary>

This module allows you to perform mass adjustments of reserves for currencies (for those currencies where the reserve is calculated based on applications).

The module settings can be found in the "**Reserve Adjustment**" → "**Group Reserve Adjustment**" section.

</details>

<details>

<summary>Mobile Version</summary>

This module enables the mobile version of the site.

The module settings can be found in the "**Theme Settings**" → "**Mobile Version and Homepage (Mobile Version)**" and "**Exchange Settings**" → "**Mobile Version Settings**" sections.

</details>

<details>

<summary>Exchange Direction Output Settings</summary>

This module adds the options listed below to the "**Exchange Settings**" ➔ "**Basic Settings**".

![](<../../../.gitbook/assets/image (2050).png>)

</details>

<details>

<summary>Exchange Direction Output Settings in XML/TXT File</summary>

This module allows you to configure the XML/TXT file with exchange rates for monitoring exchange points.

The module settings can be found in the "**Exchange Settings**" → "**TXT and XML Export Settings**" section.

</details>

<details>

<summary>Reserve Settings for Exchange Directions</summary>

This module allows you to set the reserve value in various ways for a specific exchange direction. The limits are set in the settings for each exchange direction under the "**Reserve**" tab.

</details>

<details>

<summary>Language Settings for Exchange Directions</summary>

This module allows you to restrict access to an exchange direction based on the language selected by the user on the site.

The settings for this option can be found in the settings for each exchange direction under the "**Restrictions and Checks**" tab, parameter "**Language**".

</details>

<details>

<summary>Money Transfer Number</summary>

This module allows you to request the user to enter the money transfer number when creating an application. The entered number will be displayed in the application card.

The module settings can be found in the "**Modules**" → "**Money Transfer Number**" section.

</details>

<details>

<summary>User Exchanges</summary>

This module displays the user's exchanges in their personal account.

</details>

<details>

<summary>Real-Time Application Status Update</summary>

This module allows you to update application statuses without reloading the page in the "**Applications**" section.

</details>

<details>

<summary>Personal Data Processing</summary>

This module displays a checkbox for accepting the agreement for personal data processing in the contact and feedback forms.

</details>

<details>

<summary>User Restrictions</summary>

This module allows you to limit the number of applications a user can create from a single IP address.

The module settings can be found in the "**Modules**" → "**User Restrictions**" section. Additionally, the settings for this option can be found in the settings for each exchange direction under the "**Restrictions and Checks**" tab.

</details>

<details>

<summary>Live Operator</summary>

This module allows you to "highlight" an application to other operators if it is already being handled by another operator.

</details>

<details>

<summary>Feedback</summary>

This module allows users to publish reviews about the site.

The module settings can be found in the "**Feedback**" section.

</details>

<details>

<summary>Exchange Rate Parser from File</summary>

This module allows you to link the exchange rate for a direction to a value found in a special file.

For more details about the module's capabilities, read [this link](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/kursy-valyut/kursy-valyut-iz-faila).

</details>

<details>

<summary>Exchange Rate Parser 2.0</summary>

This module allows you to "link" the exchange rate on the site to specific sources of rates: Central Bank, cryptocurrency exchanges, etc.

The module settings can be found in the "**Parsers 2.0**" section.

</details>

<details>

<summary>Reserve Parser from File</summary>

This module allows you to link the currency reserve to a value found in a special file.

For more details about the module's capabilities, read [this link](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/rezervy/rezerv-iz-faila).

</details>

<details>

<summary>Affiliate Program</summary>

This module allows you to organize an affiliate program on the site.

For more details about the module's capabilities, read [this link](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/partnerskaya-programma).

</details>

<details>

<summary>Exchange Amount Recalculation</summary>

This module allows you to automatically recalculate the exchange amount of an application after a specified time based on its status.

The settings for this option can be found in the settings for each exchange direction under the "**Exchange Amount Recalculation**" tab.

</details>

<details>

<summary>Email Registration Confirmation</summary>

This module allows you to send a confirmation link to the user's email upon registration on the site.

</details>

<details>

<summary>Custom Application Statuses</summary>

This module allows you to create custom application statuses. The created statuses can only be assigned to applications manually.

The module settings can be found in the "**Application Statuses**" and "**Exchange Direction**" → "**Exchange Direction Templates**" sections.

</details>

<details>

<summary>Number Formatting</summary>

This module allows you to set the maximum number of decimal places on the site and display the reserve value in a format like 100,000.

</details>

<details>

<summary>New User Check During Exchange</summary>

--- 

Let me know if you need any further assistance!

Here’s a naturalistic English translation of the provided text:

---

**New User Detection Module**

This module allows you to identify users who are making their first exchange at the exchange point. For these users, you can set up a freeze on automatic payouts.

You can find the module settings in the section "**Exchange Settings" → "Exchange Configuration" → "New User Check."**

---

<details>

<summary>Exchange Request Editor</summary>

This module enables you to edit the parameters of a created exchange request.

You can find the edit button for the request in the "**Requests"** section under each individual request.

</details>

<details>

<summary>Redirect to Exchange Directions</summary>

This module allows you to redirect users to a selected exchange direction when they navigate from the monitoring page to the exchange point, passing the parameters cur_from and cur_to.

</details>

<details>

<summary>Maintenance Mode</summary>

This module allows you to disable the website for technical maintenance.

You can find the module settings in the "**Maintenance Mode"** section.

</details>

<details>

<summary>User Discounts</summary>

This module allows you to set a fixed discount for individual users of the exchange. The discount applies to the exchange rate.

Once the module is activated, a field for "**Personal Discount**" will appear in the user's profile, where you can specify the percentage of the discount. This discount takes precedence over cumulative discounts.

</details>

<details>

<summary>Direction Sorting</summary>

This module allows you to sort exchange directions by the columns "**I Give**" and "**I Receive**."

</details>

<details>

<summary>Operator Status</summary>

This module allows you to configure the widget for "**Operator Online/Offline**," which is displayed on the website.

You can find the module settings in the "**Operational Status**" section.

</details>

<details>

<summary>Currency Accounts for Directions</summary>

This module simplifies operations when using a large number of exchange point details during manual exchanges.

For more information about the module's capabilities, read [here](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/ispolzovanie-svoikh-kart-koshelkov-schetov).

</details>

<details>

<summary>User Accounts</summary>

This module allows you to view the accounts that users add in their personal accounts.

You can find the module settings in the "**User Accounts"** section.

</details>

<details>

<summary>Transaction Confirmation Counter (Crypto)</summary>

This module allows you to record the confirmations received for transactions when paying through the relevant merchants (such as Blockchain.info, Block.io, etc.). You can also display the number of confirmations received for a paid request.

You can find the module settings in the "**Requests" → "Confirmation Log"** section.

</details>

<details>

<summary>Countdown Timer</summary>

This module allows you to display a countdown timer on the website for users, indicating when an unpaid request will be deleted.

</details>

<details>

<summary>Rates</summary>

This module allows you to display all exchange directions and their rates in a table format on the website.

</details>

<details>

<summary>Maintenance Notification Text</summary>

This module allows you to set the notification text that appears when the Premium Exchanger plugin is deactivated.

You can find the module settings in the "**Modules" → "Maintenance Notification Text"** section.

</details>

<details>

<summary>Header Notification</summary>

This module allows you to display a warning notification on a red background in the website header according to a schedule and based on the operator's status.

You can find the module settings in the "**Notifications"** section.

</details>

<details>

<summary>Initial Request ID Setup</summary>

This module allows you to set the initial request number on the website. Numbers can only be set to increase.

You can find the module settings in the "**Modules" → "Current Request ID"** section.

</details>

<details>

<summary>Exchange Filter for Guests</summary>

This module activates the ability to set various restrictions on the website for users.

You can find the module settings in the "**Exchange Settings" → "Exchange Filters"** section.

</details>

<details>

<summary>User Filtering</summary>

This module allows you to filter registered users on the site by parameters: verified, unverified, and discount size.

You can find the module settings in the "**Users" → "User Filters"** section.

</details>

<details>

<summary>Financial Statistics</summary>

This module allows you to calculate the profit of the exchange point.

You can find the module settings in the "**Financial Statistics"** section.

</details>

<details>

<summary>Wallet Verification Checker</summary>

This module allows you to check the verification status of a wallet in the payment system.

You can find the module settings in the "**Modules" → "Wallet Verification Checker"** section and in the direction settings under the "**Restrictions and Checks**" tab, with parameters for "**Check Wallet Verification in PS**" and "**Require Verified Wallet in PS**," as well as in the currency settings.

</details>

<details>

<summary>Blacklist</summary>

This module allows you to add a client's personal data to a blacklist to prevent requests from being created on the site with that data.

You can find the module settings in the "**Blacklist"** section.

</details>

<details>

<summary>BestChange Blacklist</summary>

This module allows you to check the client's details against the BestChange blacklist and prohibit exchanges if the data is found in the monitoring blacklist.

You can find the module settings in the "**Modules" → "**BestChange Blacklist"** section (the module must be activated in the "Modules" section). Your site must be listed on BestChange.ru to use this check.

To use the module, generate an API key in your BestChange account.

![](<../../../.gitbook/assets/image (169).png>) \

And enter it in the "**Key**" field in the module settings.

![](<../../../.gitbook/assets/image (168).png>)

</details>

<details>

<summary>Email Notification Templates</summary>

This module allows you to set the same sender name and email address for all email templates at once.

You can find the module settings in the "**Messages" → "Email Templates"** section.

</details>

<details>

<summary>Contact Export</summary>

This module allows you to export the contacts of users who have made exchanges on the site to an xls file.

You can find the module settings in the "**Contact Export"** section.

</details>

<details>

<summary>Export/Import</summary>

This module allows you to export and import currencies and exchange directions to an Excel file (CSV format). It also allows you to export requests created on the site to an Excel file (CSV format).

You can find the module settings in the sections "**Modules" → "Exchange Export," "Export/Import Exchange Directions," "Export/Import Currencies."**

</details>

<details>

<summary>BestChange Parser</summary>

For more information about the module's capabilities, read [here](https://premium.gitbook.io/main/osnovnye-nastroiki/kursy-valyut/bestchange-parser).

</details>

<details>

<summary>GEO IP</summary>

This module allows you to create a list of allowed and prohibited countries, restrict access to exchange directions based on the user's country, and completely block access to the site based on the user's country, maintaining black and white lists of IP addresses.

You can find the module settings in the "**GEO IP"** section.

</details>

<details>

<summary>HTML Sitemap</summary>

This module allows you to create an HTML sitemap.

You can find the module settings in the "**Exchange Settings" → "HTML Sitemap Settings"** section.

</details>

<details>

<summary>Email Verification</summary>

This module allows you to request a one-time code that is sent to the user's email during the creation of a request.

You can find the module settings in the "**Modules" → "Email Verification Settings"** section.

</details>

<details>

<summary>LIVE Requests</summary>

This module allows you to display information about incoming requests and notify about requests with a sound alert without reloading the page.

You can find the module settings in the "**Requests" → "LIVE Requests"** section.

</details>

<details>

<summary>QR Code Generator</summary>

This module allows you to display a QR code on the payment page when paying through cryptocurrency merchants.

</details>

<details>

<summary>SEO</summary>

This module allows you to perform SEO settings for the website.

You can find the module settings in the "**SEO"** section.

</details>

<details>

<summary>SMTP</summary>

This module allows you to send emails from the site via SMTP.

For more information about the module's capabilities, read [here](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/uvedomleniya/opovesheniya-po-e-mail#nastroika-smtp).

</details>

<details>

<summary>SMS Verification</summary>

---

Feel free to ask if you need further assistance!

The module allows users to request a one-time code, which is sent to their mobile phone during the application process.

You can find the module settings under "**Modules" → "SMS Code Verification Settings"**.

</details>

<details>

<summary>Webmoney X19</summary>

This module enables the verification of user details through the X19 interface for exchanges involving the Webmoney payment system.

The module settings can be found under "**Modules" → "X19"**.

</details>