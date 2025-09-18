# Update List

## Version 2.7

*   **Client Upload of Receipts in Requests (Module "Payment Receipts")**

    This module allows clients to upload receipts or other data through images in their created requests.

    ![Settings for the specified block in the request (section "Modules" -> "Payment Receipts")](../../.gitbook/assets/image%20\(1988\).png)

    ![Module settings (tab "Payment Receipts" in exchange direction settings)](../../.gitbook/assets/image%20\(1956\).png)

    ![In the request, click the "Choose file" button](../../.gitbook/assets/image%20\(1954\).png)

    ![Select the desired file and upload it](../../.gitbook/assets/image%20\(1952\).png)

    ![After the client uploads the image, it will be displayed in the request under the "Requests" section](../../.gitbook/assets/image%20\(1955\).png)
*   **Grouping Exchange Directions for Quick Filtering (Module "Direction Groups")**

    ![Add the desired number of groups in the "Direction Groups" section](../../.gitbook/assets/image%20\(1959\).png)

    ![In the direction settings, assign the necessary group on the "Main Settings" tab](../../.gitbook/assets/image%20\(1960\).png)

    ![In the table of all directions, select the desired group and, for example, make all directions from this group inactive.](../../.gitbook/assets/image%20\(1961\).png)
*   **Setting Individual Profit Percentage for Each City for Cash Exchange Directions**

    ![Tab "Cities" in the exchange direction settings](../../.gitbook/assets/image%20\(1962\).png)
*   **Ability to Set "Completed Request" Status via API (Method `success_bid`)**

    This method applies only to requests created directly via the API.

    ![To identify the request, you need to pass its hash (displayed in the response for the method create\_bid when creating a request via API)](../../.gitbook/assets/image%20\(1963\).png)

    ![Changing request statuses via API](../../.gitbook/assets/image%20\(1964\).png)
*   **Mass Information Editor — Added Filter by Direction Group**

    ![Filter by direction group](../../.gitbook/assets/image%20\(1965\).png)

    Additionally, you can specify commissions and exchange amounts in one window for selected directions.

    ![Selecting an entity for editing](../../.gitbook/assets/image%20\(1966\).png)

    ![Editing payment system commissions](../../.gitbook/assets/image%20\(1967\).png) ![Editing exchange amounts](../../.gitbook/assets/image%20\(1970\).png)
*   **Option to Completely Disable Merchant Logs and Auto-Payments**

    ![The option is located in the settings of each merchant and auto-payment module](../../.gitbook/assets/image%20\(283\).png)
*   **Prohibition on Creating Requests with the Same Amount for Exchange Direction**

    ![Tab "Restrictions and Checks" in the exchange direction settings](../../.gitbook/assets/image%20\(285\).png)

    ![When creating a second request with an unpaid first request for the same amount, the client will receive an error](../../.gitbook/assets/image%20\(286\).png)
*   **Direction and Currency Sorting Module — Only Active Currencies Will Be Displayed**

    ![Only active currencies will be displayed](../../.gitbook/assets/image%20\(274\).png)
*   **"Live Operator" Module (`many_operators`)**

    This module now allows displaying only requests from specific exchange directions, as well as requests from specific merchants for each user with access to the admin panel.

    ![With this setting, the operator will only see requests that used the Advcash merchant](../../.gitbook/assets/image%20\(276\).png)

    ![With this setting, the operator will only see requests from specified exchange directions](../../.gitbook/assets/image%20\(277\).png)

    ![With this setting, the operator will see requests from specified exchange directions, as well as requests from all exchange directions that used the Advcash merchant](../../.gitbook/assets/image%20\(278\).png)

    You can also use a reverse filter:

    ![With this setting, the operator will see requests from all exchange directions except the specified ones](../../.gitbook/assets/image%20\(279\).png)

    **Warning:** Do not use positive and negative values in filters simultaneously — filtering operates on an OR basis, so negative filters will not be considered if specified alongside positive ones.

    ![With this setting, the operator will see all requests from exchange direction 1340 (even if the Bova merchant was used), as well as requests from all exchange directions where the Bova merchant was not used.](../../.gitbook/assets/image%20\(281\).png)

    ![With this setting, the operator will see requests from all exchange directions (even if the Bova merchant was not used), as well as requests from all exchange directions where the Bova merchant was used (even if it is direction 1340).](../../.gitbook/assets/image%20\(282\).png)
*   **Transfer of User Coefficients for Parsers 2.0 to a Separate Section**

    ![Section in the sidebar](../../.gitbook/assets/image%20\(1971\).png)

    ![Coefficient settings](../../.gitbook/assets/image%20\(1972\).png)

    * **Index Name** — the desired name to be used in formulas as a shortcode
    * **Formula Value** — enter a number or mathematical formula in the field
    * **Index Value** — value for the formula specified above (if a formula is provided)
    * **Index Type:**
      * **Substituting Formula into Rate**: The formula will be directly substituted into the rate without parentheses, and then the rate value will be calculated.
      * **Index Value**: The coefficient value will be calculated first, and then it will be substituted into the rate.
    * **Comment** — a field for your notes
*   **Removed the Setting for Creating a Task to Update Rates for the "On the Site" Option**

    This option was causing the server to overload with unnecessary requests.

    ![Version 2.6](../../.gitbook/assets/image%20\(1976\).png) ![Version 2.7](../../.gitbook/assets/image%20\(1975\).png)
*   **Results of Recalculations for Requests Moved to a Separate Section "Recalculation Log"**

    ![Recalculation log](../../.gitbook/assets/image%20\(1977\).png)
*   **"Blacklist" Module — Added the Ability to Check the Real Account from Which the Payment Came**

    ![Checking the real account](../../.gitbook/assets/image%20\(265\).png)

    Added the ability to customize blacklist elements individually.

    ![Individual settings for blacklist elements](../../.gitbook/assets/image%20\(266\).png)

    * **Method:**
      * **From General Settings** — the method selected in the general settings of the module will be applied.
      * **Show Error** — if this element is in the blacklist, an error will be displayed when creating a request, even if "Stop Auto-Payment" is selected in the general settings.
      * **Stop Auto-Payment** — if this element is in the blacklist, the request will be created (and checked at the auto-payment stage), even if "Show Error" is selected in the general settings.
*   **"AML" Module - All AML Modules and Logs Now Located in One Section**

    ![AML module section](../../.gitbook/assets/image%20\(268\).png)

    Added the ability to quickly replace the module in the exchange direction settings.

    ![Quick module replacement](../../.gitbook/assets/image%20\(269\).png)

    New statuses for requests added when there is a long response from the AML service.

    ![New request statuses](../../.gitbook/assets/image%20\(270\).png)

    If no response is received from the service within the time specified in the module settings,

    ![Response time settings](../../.gitbook/assets/image%20\(271\).png)

The application will change its status to "**Pending**" and revert to the previous status (if the client's details are successfully verified) or to "**AML Check Failed**" (if the risk threshold is exceeded) after receiving a response from the AML service. To enable this feature, you need to set up a [cron job](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-sozdat-zadanie-cron-na-servere) on the server (the link for the job can be found in the "AML" section).

{% hint style="warning" %}
The above option applies only to applications that have already been created (if the verification for this exchange direction is enabled as "**Upon Payment**" or "**Before Auto-Payment**").
{% endhint %}

*   Logging of operator/manager actions has been added. The following will be displayed: • Date and time of changes made • User who made the changes • Data that was changed (old data will be shown in red, new data in black)

    The following sections are logged: • Exchange direction settings • Currency settings • Currency rates in the "**Parsers 2.0**" -> "**Rates**" section • Settings for **Bestchange parsers** and **Bestchange API**
*   The ability to wait for details from the merchant has been added (only for fiat merchants that provide details in the API response and support repeated requests for details).

    To use this option, the "**Move Application to Merchant Error**" setting must also be enabled in the "**Exchange Settings**" -> "**General Settings**" section (only in this case will the details be requested again, or the application will switch to the "**Merchant Error**" status).

{% hint style="warning" %}
Please note that repeated requests to the merchant within a short time frame (if the details were not received on the first request) may cause the merchant to treat such requests as spam, and your exchange may end up in the merchant's spam filter.

To avoid such situations, we recommend informing the representatives of the specific merchant in advance that your exchange may send repeated requests for the same application if the details were not received on the first request. In this case, the merchant may add your exchange to the spam filter exceptions.
{% endhint %}

## Version 2.6

<details>

<summary>Update List</summary>

* **Bestchange Blacklist Module (blacklist\_bestchange)**: Added the ability to stop payment on an application if one or more of the client's details are on the Bestchange blacklist when using the module. Module settings can be found in the "**Modules**" -> "**Bestchange Blacklist**" section.
* **Blacklist**: Changes similar to the **blacklist\_bestchange** module have been made, allowing the acceptance of funds and stopping payment if the user is on the blacklist. Module settings can be found in the "**Blacklist**" -> "**Settings**" section.

- **AML Check**: Added the ability to conduct a check right before sending currency to the client's wallet, with the application moving to an error status if the risk level is exceeded. The risk level setting is done in the "**Modules**" -> "**AML Bot**" or "**Getblock**" section (depending on which service you have connected).

* **Getblock AML Service, Sleep Function**: Added the ability to set a wait time for a response from the service in case the check result is not provided immediately. The setting can be found in the "**Modules**" -> "**Getblock**" section.
* **Email Confirmation**: Added the ability to request email confirmation from the client before creating an application. The "**Email Confirmation Before Application Creation**" module (**confirmexchmail**) must be activated in the "**Modules**" section. Module settings can be found in the "**Modules**" -> "**Email Confirmation Before Application Creation**" section.
* **Archiving**: The module structure has been changed, and filtering by **application status/details received from the merchant/transaction hash for receiving and sending funds** has been added in the "**Applications**" -> "**Archived Applications**" section.

Adding comments to an application in the "Applications" section.

Searching by specified filters and viewing comments on applications will only work for applications archived in version 2.6.

* **Bestchange API Parser (bestchangeapi)**: A module for working with the API has been added. Module settings can be found in the "**BestChange API Parser**" -> "**Settings**" section and on the **"BestChange API Parser"** tab in the exchange direction settings.
* **Filtering Exchange Directions**: A filter by payment systems has been added in the "**Exchange Directions**" section.

- **Profit Values in Notifications**: The ability to specify **set (not calculated!) values in the exchange direction settings (in the "Rate" tab)** through shortcodes for displaying values in emails and Telegram messages for administrators has been added.

Here’s a naturalistic English translation of the provided text:

***

* **Email Confirmation Module Replacement**: After the update, you need to deactivate and then remove the **rconfirm** module from the server and replace it with the **confirmregmail** module. For more details, refer to the [**update instructions**](https://premium.gitbook.io/main/pered-nachalom-raboty/instrukciya-po-obnovleniyu-skripta/obnovlenie-s-versii-2.5-do-2.6#izmeneniya-v-paneli-administratora). If you install version 2.6 of the script from scratch, the **rconfirm** module will not be included by default.
* **Template Text Separation**: A new feature has been added that allows you to separate the text in the exchange direction template, which will be displayed when working with requests via the API and the website using shortcodes.
* **Financial Statistics Section**: The financial statistics module now includes overall statistics on the number of exchanges and the total amount exchanged in USD for the selected period.
* **"Proceed to Payment" Button**: You can now hide the button in the merchant settings if the payment details are displayed in the text for the "New Request" status using the shortcode `[to_account]`.
* **Country List in Exchange Direction Restrictions**: Countries marked with a checkbox will now appear first in the list.
* **Merchant Copying**: A new feature allows you to create a copy of a merchant with all settings at the click of a button. To use this option, activate the "**Merchant Copying and Auto-Payments**" module in the "Modules" section after updating the script.
* **Bulk Merchant Addition**: A new option has been added for bulk adding merchants to exchange directions in the merchant settings.
* **Currency ID**: You can now search by currency ID when creating an exchange direction.
* **Module Access**: Access to modules is available to all users with access to the admin panel, but activation and deactivation of modules are restricted to administrators.
* **Creating Requests Without Authorization**: You can now create a request without authorization in directions that require verification of details, provided that the account/card number has been previously verified.
* **Coupons**: A new module called **"Discount Coupons"** has been added to provide personalized discounts to clients in the form of promo codes. The module settings can be found in the "**Discount Coupons**" section. When the module is activated, an optional "**Discount Coupon**" field will appear in the exchange form (this field can be activated for each exchange direction in the "**Restrictions and Checks**" tab).
* **Using Multiple Merchants for Payment**: An option has been added to utilize other merchants (if multiple merchants are used in the settings) in exchange directions if the primary merchant does not provide payment details for any reason. For more information on how this option works, refer to the [**instructions**](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov#podklyuchenie-neskolkikh-merchantov).
* **Payment Systems**: You can now sort payment systems by name in the "**Currencies**" -> "**Payment Systems**" section.
* **Parser Search**: A search field has been added for finding parsers by text in the exchange direction settings (under the "**Auto-Correction of Rates**" tab). The search will include the entire string, including the rate itself.
* **Country Sorting**: The sorting of countries by code has been replaced with sorting by country name in the "**Restrictions and Checks**" tab of the exchange direction settings.
* **List of Recalculated Rates**: When recalculating exchange rates, the list of old rates in the request under the "**Requests**" section can take up a lot of vertical space. To address this, the "**Old Rates**" block has been fixed in size, and the rates can now be scrolled vertically within the block.
* **Request Deletion Timer**: The timer now includes seconds.
* **Shortcode for Timer in Template Settings**: A shortcode for the timer can now be used in the template settings.
* **Displaying Timer with Seconds in Requests**: The timer will now display seconds in requests.
* **"Captcha for Website (Image Selection)" Module**: This module has been upgraded for improved security and now generates captcha options automatically. The ability to create custom captcha options has been removed.

***

This translation aims to maintain clarity and natural flow while conveying the original content's meaning.

Here’s a naturalistic English translation of the provided text:

***

* Displaying CAPTCHA in the exchange form.
* **Telegram Bot for Notifications:** Added the ability to send messages using user ID without requiring a login (you can find your ID through the bot [@getMyID](https://t.me/getmyid_bot)). Sending messages from the bot to groups is not supported.
* View your ID through the bot [@getMyID](https://t.me/getmyid_bot).

***

Adding message recipients in template settings.

Settings for blocking bots have also been added. The module settings can be found under "**Telegram**" -> "**Settings**."

***

* **Client Notifications:** The tab "**Exchange Direction Template**" has been renamed to "**Notification Settings**" in the exchange direction settings (with a template for sending in an email or Telegram message using the shortcode `[dirtemp]`). You can now specify personal **email/Telegram account/phone number** to receive notifications about requests in this direction for the administrator/operator (if one or more contact fields are filled, data from the template above will be sent **only to the specified contacts**, ignoring the recipient list in the general template). The option settings can be found in the exchange direction settings under the tab "**Notification Settings**."

***

* **Requesting Payment Details Timing:** The option to choose when to request payment details has been removed — starting from version 2.6, the request for details from the merchant will always occur at the time of application creation.
* **Button Text Replacement on Merchant Error (Payment Details Displayed in Application):** An option has been added to replace the text displayed instead of the shortcode \[to\_account] if, for any reason, the merchant is unable to provide payment details (this option can be found in the "**Exchange Settings**" -> "**General Settings**").

***

* **Button Text Replacement on Merchant Error (Link to Payment Page):** An option has been added to change the text on the button that leads to the merchant's payment page if, for any reason, the merchant (such as Bitconce Link, Firekassa Link, etc.) cannot provide payment details (this option can be found in the merchant module settings that link to the payment details).

***

Text error display on the button in the application.

* **Verification of Payment Details:** In the general table with applications for verifying cards/accounts/wallet numbers, the ability to specify a reason for verification denial has been added (this view is only available to administrators and operators working with the module). This option can be found under "**User Accounts**" -> "**Account Verification**."

***

* **Internal Accounts:** A new version of the internal account module (**iac**) has been released, allowing for merchant and auto-payment functionality with the option to pay to an internal account via API. The old version of the modules (**domacc**) has been removed from the script starting from version 2.6. More details on transferring already added accounts to the new module can be found in the [**update instructions**](https://premium.gitbook.io/main/pered-nachalom-raboty/instrukciya-po-obnovleniyu-skripta/obnovlenie-s-versii-2.5-do-2.6#izmeneniya-v-paneli-administratora).

***

### Version 2.5

</details>
