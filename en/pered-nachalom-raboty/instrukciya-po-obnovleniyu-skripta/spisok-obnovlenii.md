# Update List

## Version 2.7

*   **Uploading Receipts by Clients in Applications** (module "**Payment Receipts**" (**paychecks**))  

    <figure><img src="../../.gitbook/assets/image (1957).png" alt="" width="563"><figcaption></figcaption></figure>

    This module allows clients to upload receipts or other data as images within an application.

    <figure><img src="../../.gitbook/assets/image (1988).png" alt="" width="474"><figcaption><p>Text settings for the specified block in the application (section "<strong>Modules</strong>" -> "<strong>Payment Receipts</strong>")</p></figcaption></figure>

    <figure><img src="../../.gitbook/assets/image (1956).png" alt="" width="327"><figcaption><p>Module settings (the "Payment Receipts" tab in the exchange direction settings)</p></figcaption></figure>

    <figure><img src="../../.gitbook/assets/image (1954).png" alt="" width="563"><figcaption><p>In the application, click the "<strong>Choose file</strong>" button</p></figcaption></figure>

    <figure><img src="../../.gitbook/assets/image (1952).png" alt="" width="563"><figcaption><p>Select the desired file and upload it</p></figcaption></figure>

    <figure><img src="../../.gitbook/assets/image (1955).png" alt="" width="563"><figcaption><p>Once the client uploads the image, it will be displayed in the application under the "<strong>Applications</strong>" section</p></figcaption></figure>

*   **Grouping Exchange Directions for Quick Filtering** (module "**Direction Groups**" (**direction_groups**))  

    <figure><img src="../../.gitbook/assets/image (1958).png" alt="" width="563"><figcaption></figcaption></figure>

    <figure><img src="../../.gitbook/assets/image (1959).png" alt="" width="464"><figcaption><p>Add the required number of groups in the "<strong>Direction Groups</strong>" section</p></figcaption></figure>

    <figure><img src="../../.gitbook/assets/image (1960).png" alt="" width="563"><figcaption><p>Assign a group to a direction in the "<strong>General Settings</strong>" tab of the direction settings</p></figcaption></figure>

    <div data-full-width="true"><figure><img src="../../.gitbook/assets/image (1961).png" alt=""><figcaption><p>In the table of all directions, select the desired group and, for example, deactivate all directions within that group.</p></figcaption></figure></div>

*   **Setting Individual Profit Percentages for Each City** for cash exchange directions, similar to the [general profit percentage for exchange directions](https://premium.gitbook.io/main/osnovnye-nastroiki/partnerskaya-programma/pribyl-i-partnerskii-procent#nastroika-pribyli-dlya-napravleniya-obmena).  

    <figure><img src="../../.gitbook/assets/image (1962).png" alt="" width="563"><figcaption><p>The "<strong>Cities</strong>" tab in the exchange direction settings</p></figcaption></figure>

*   **Ability to Set the "Completed Application" Status via API** (method `success_bid`). Like other API methods for changing application statuses, this method applies only to applications created via the API.  

    <figure><img src="../../.gitbook/assets/image (1963).png" alt=""><figcaption><p>To identify the application, its hash must be passed (displayed in the response of the <code>create_bid</code> method when creating an application via API)</p></figcaption></figure>

    <figure><img src="../../.gitbook/assets/image (1964).png" alt=""><figcaption><p>Changing application statuses via API</p></figcaption></figure>

*   **Bulk Information Editor** — added a filter by direction group  

    <figure><img src="../../.gitbook/assets/image (1965).png" alt="" width="445"><figcaption><p>Filter by direction group</p></figcaption></figure>

    Additionally, you can specify fees and exchange amounts in a single window for selected directions.  

    <figure><img src="../../.gitbook/assets/image (1966).png" alt="" width="445"><figcaption><p>Selecting an entity for editing</p></figcaption></figure>

    <div><figure><img src="../../.gitbook/assets/image (1967).png" alt="" width="563"><figcaption><p>Editing payment system fees</p></figcaption></figure> <figure><img src="../../.gitbook/assets/image (1970).png" alt="" width="563"><figcaption><p>Editing exchange amounts</p></figcaption></figure></div>

*   **Option to Completely Disable Merchant Logs and Auto-Payouts**  

    <figure><img src="../../.gitbook/assets/image (283).png" alt=""><figcaption><p>This option is located in the settings of each merchant and auto-payout module</p></figcaption></figure>

*   **Restriction on Creating Applications with the Same Amount for an Exchange Direction**  

    <figure><img src="../../.gitbook/assets/image (285).png" alt="" width="422"><figcaption><p>The "<strong>Restrictions and Checks</strong>" tab in the exchange direction settings</p></figcaption></figure>

    <figure><img src="../../.gitbook/assets/image (286).png" alt="" width="532"><figcaption><p>If a second application is created while the first one with the same amount remains unpaid, the client will receive an error</p></figcaption></figure>

*   **Sorting Module for Directions and Currencies** — only active currencies will now be displayed in the section (previously, all currencies were shown).  

    <figure><img src="../../.gitbook/assets/image (274).png" alt="" width="477"><figcaption></figcaption></figure>

*   **"Live Operator" Module** (`many_operators`)  

    <figure><img src="../../.gitbook/assets/image (275).png" alt="" width="563"><figcaption></figcaption></figure>

    Added the ability to display only applications from specific exchange directions or applications with specific merchants for each user with admin panel access.  

    <figure><img src="../../.gitbook/assets/image (276).png" alt=""><figcaption><p>With this setting, the operator will only see applications where the Advcash merchant was used</p></figcaption></figure>

    <figure><img src="../../.gitbook/assets/image (277).png" alt=""><figcaption><p>With this setting, the operator will only see applications from the specified exchange directions</p></figcaption></figure>

    <figure><img src="../../.gitbook/assets/image (278).png" alt=""><figcaption><p>With this setting, the operator will see applications from the specified exchange directions, as well as all applications from directions where the Advcash merchant was used</p></figcaption></figure>

    Reverse filtering is also available:  

    <figure><img src="../../.gitbook/assets/image (279).png" alt=""><figcaption><p>With this setting, the operator will see applications from <strong>all</strong> exchange directions except the specified ones</p></figcaption></figure>

    {% hint style="warning" %}
    Do not use both positive and negative values in filters simultaneously — filtering works on an OR basis, so negative filters will not be applied if positive ones are also specified.
    {% endhint %}

    <figure><img src="../../.gitbook/assets/image (281).png" alt=""><figcaption><p>With this setting, the operator will see <strong>all</strong> applications from exchange direction 1340 (even if the Bova merchant was used), as well as applications from <strong>all</strong> exchange directions where the Bova merchant was <strong>not</strong> used.<br>In this case, the negative filter for the Bova merchant will not be applied if it was used in direction 1340.</p></figcaption></figure>

    <figure><img src="../../.gitbook/assets/image (282).png" alt=""><figcaption><p>With this setting, the operator will see applications from all exchange directions (even if the Bova merchant was <strong>not</strong> used), as well as applications from <strong>all</strong> exchange directions where the Bova merchant was used (even if it was direction 1340).<br>In this case, the negative filter for direction 1340 will not be applied if there were applications in this direction with the Bova merchant.</p></figcaption></figure>

*   **User Coefficients for Parsers 2.0 Moved to a Separate Section**  

    <figure><img src="../../.gitbook/assets/image (1971).png" alt=""><figcaption><p>Sidebar section</p></figcaption></figure>

    <figure><img src="../../.gitbook/assets/image (1972).png" alt="" width="449"><figcaption><p>Coefficient settings</p></figcaption></figure>

    - **Index Name** — desired name to be used in formulas as a shortcode  
    - **Formula Value** — a number or mathematical formula can be entered here  
    - **Index Value** — the value for the formula specified above (if a formula is provided)  
    - **Index Type:**  
        • **Formula Substitution in Rate**  

        <figure><img src="../../.gitbook/assets/image (1974).png" alt=""><figcaption><p>The formula will be directly substituted into the rate without brackets, and the rate value will then be calculated</p></figcaption></figure>

        • **Index Value**  

        <figure><img src="../../.gitbook/assets/image (1973).png" alt=""><figcaption><p>The coefficient value will first be calculated, and then it will be substituted into the rate</p></figcaption></figure>

    - **Comment** — a field for your notes  

*   **Removed the Task Creation Setting for Rate Updates** for the "**On the Website**" option (using this option caused unnecessary server load).  

    <div><figure><img src="../../.gitbook/assets/image (1976).png" alt=""><figcaption><p>Version 2.6</p></figcaption></figure> <figure><img src="../../.gitbook/assets/image (1975).png" alt=""><figcaption><p>Version 2.7</p></figcaption></figure></div>

*   **Results of Application Recalculations Moved to a Separate Section** ("**Recalculation Log**")  

    <figure><img src="../../.gitbook/assets/image (1977).png" alt="" width="563"><figcaption></figcaption></figure>

*   **"Blacklist" Module** — added the ability to verify the actual account from which the client’s payment was made.  

    <figure><img src="../../.gitbook/assets/image (265).png" alt="" width="404"><figcaption></figcaption></figure>

    Added the ability to customize blacklist elements individually.  

    <figure><img src="../../.gitbook/assets/image (266).png" alt="" width="418"><figcaption></figcaption></figure>

    Methods:  
    - **From General Settings** — the method selected in the module’s general settings will be applied.  
    - **Display Error** — if this blacklist element is present in the exchange form, an error will be displayed when creating an application, even if the general settings specify the "**Stop Auto-Payout**" method.  
    - **Stop Auto-Payout** — if this blacklist element is present in the exchange form, the application will be created (and checked during the auto-payout stage), even if the general settings specify the "**Display Error**" method.  

*   **AML Module** — all AML modules and logs are now consolidated into one section.  

    <figure><img src="../../.gitbook/assets/image (268).png" alt=""><figcaption></figcaption></figure>

    <figure><img src="../../.gitbook/assets/image (267).png" alt=""><figcaption></figcaption></figure>

    Added the ability to quickly replace the module in the exchange direction settings.  

    <figure><img src="../../.gitbook/assets/image (269).png" alt="" width="241"><figcaption></figcaption></figure>

    Added new statuses for applications in case of delayed responses from the AML service.  

    <figure><img src="../../.gitbook/assets/image (270).png" alt="" width="287"><figcaption></figcaption></figure>

    If no response is received from the service within the time specified in the module settings:  

    <figure><img src="../../.gitbook/assets/image (271).png" alt="" width="314"><figcaption></figcaption></figure>

Here’s the provided text translated into natural, fluent English:

---

If the application changes its status to "**Pending**," it will either return to its previous status (if the client’s details are successfully verified) or switch to "**AML Check Failed**" (if the risk level is exceeded) after receiving a response from the AML service. To enable this feature, you need to add a [cron job](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-sozdat-zadanie-cron-na-servere) on the server (the link for the job can be found in the "AML" section).

<figure><img src="../../.gitbook/assets/image (273).png" alt="" width="528"><figcaption></figcaption></figure>

{% hint style="warning" %}
The above feature applies only to already created applications (if the verification for this exchange direction is enabled as "**Upon Payment**" or "**Before Auto-Payout**").

![](<../../.gitbook/assets/image (249).png>)
{% endhint %}

* **Operator/Manager Action Logging Added**: The following details will now be logged:  
  • Date and time of changes  
  • User who made the changes  
  • Data that was modified (old data will be displayed in red, new data in black)  

  <figure><img src="../../.gitbook/assets/image (1978).png" alt="" width="511"><figcaption></figcaption></figure>

  The following sections will be logged:  
  • Exchange direction settings  
  • Currency settings  
  • Currency rates in the "**Parsers 2.0**" -> "**Rates**" section  
  • Settings for **Bestchange parsers** and **Bestchange API**

* **Added Option to Wait for Merchant Details**: This feature is available only for fiat merchants that provide details in their API response and support repeated requests for details.  

  <figure><img src="../../.gitbook/assets/image (1980).png" alt="" width="433"><figcaption><p>Option in the merchant module settings</p></figcaption></figure>

  To enable this feature, the "**Mark Application as Merchant Error**" option must also be activated in the "**Exchange Settings**" -> "**General Settings**" section. Only in this case will details be re-requested, or the application will switch to the "**Merchant Error**" status.  

  <figure><img src="../../.gitbook/assets/image (1981).png" alt="" width="467"><figcaption></figcaption></figure>

{% hint style="warning" %}
Please note that repeated requests to the merchant within a short interval (if details were not received during the first request) may cause the merchant to treat such requests as spam, potentially leading to your exchange being flagged by the merchant’s spam filter.

To avoid such situations, we recommend informing the merchant in advance that your exchange may send repeated requests for the same application if details are not received during the initial request. In this case, the merchant can whitelist your exchange in their spam filter.
{% endhint %}

---

## Version 2.6

<details>

<summary>Update List</summary>

* **"Bestchange Blacklist" Module (blacklist_bestchange)**: Added the ability to stop payouts for an application if one or more client details are found in the Bestchange blacklist when using this module. The module settings can be found in the "**Modules**" -> "**Bestchange Blacklist**" section.  

  ![](https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FIYShnbIVsQtdyzn1bKip%252Fimage.png%3Falt%3Dmedia%26token%3D69302b5b-7f4f-4847-b874-c928ea29ae01\&width=768\&dpr=4\&quality=100\&sign=52626c56\&sv=1)

* **Blacklist Module**: Similar updates were made to the **Blacklist** module, allowing funds to be received but payouts to be stopped if the user is in the blacklist. The settings can be found in the "**Blacklist**" -> "**Settings**" section.  

  ![](https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252F18OpRTbt1jzLD5l2HMZ4%252Fimage.png%3Falt%3Dmedia%26token%3Dcd4f10d7-7da0-49f2-b46a-ebf0e58efe1e\&width=768\&dpr=4\&quality=100\&sign=3df31e7f\&sv=1)

* **AML Check**: Added the ability to perform AML checks right before sending funds to the client’s wallet, with the application being marked as an error if the risk level is exceeded. Risk level settings can be configured in the "**Modules**" -> "**AML Bot**" or "**Getblock**" section, depending on the connected service.  

  AML check logic can be configured in the exchange direction settings under the "**AML Bot**" or "**Getblock**" tab.  

  ![](https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FwkCrPNGRW8VjYjVzWBrM%252Fimage.png%3Falt%3Dmedia%26token%3D7df1e4b9-62ea-43c1-b715-55ae021fe80e\&width=768\&dpr=4\&quality=100\&sign=8ab4efdd\&sv=1)

* **Getblock AML Service, Sleep Function**: Added the ability to set a waiting time for a response from the service in case the check result is not immediately available. This setting can be found in the "**Modules**" -> "**Getblock**" section.  

  ![](https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FUCwqQIbUxlfFgP0SyEdU%252Fimage.png%3Falt%3Dmedia%26token%3D1a328e43-5f40-46f9-a44f-687546201bdb\&width=768\&dpr=4\&quality=100\&sign=fdf901cd\&sv=1)

* **Email Confirmation**: Added the ability to request email confirmation from the client before creating an application. The "**Email Confirmation Before Application Creation**" module (**confirmexchmail**) must be activated in the "**Modules**" section. The module settings can be found in "**Modules**" -> "**Email Confirmation Before Application Creation**."  

  ![](https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FNqMA0JHfsAhhn1AdvZ01%252Fimage.png%3Falt%3Dmedia%26token%3D6a490aa4-14e5-45e7-a3fa-2642afb47054\&width=768\&dpr=4\&quality=100\&sign=320c412\&sv=1)

* **Archiving**: The module structure has been updated, and filtering by **application status/merchant-provided details/transaction hash for receiving and sending funds** has been added in the "**Applications**" -> "**Archived Applications**" section.  

  ![](https://premium.gitbook.io/~gitbook/image...)

---

Let me know if you'd like me to continue or clarify anything!

Here’s the naturalistic English translation of the provided text:

---

### **Email Confirmation Module Replacement**
After updating, you need to deactivate and remove the **rconfirm** module from the server. Instead, use the **confirmregmail** module. For more details, refer to the [**update instructions**](https://premium.gitbook.io/main/pered-nachalom-raboty/instrukciya-po-obnovleniyu-skripta/obnovlenie-s-versii-2.5-do-2.6#izmeneniya-v-paneli-administratora). If you’re installing version 2.6 from scratch, the **rconfirm** module will not be included by default.

---

### **Template Text Splitting**
You can now split the text from the exchange direction template. This text will be displayed when working with requests via API or the website using shortcodes.

---

### **Financial Statistics Section**
The financial statistics module now includes an overview of the total number of exchanges and the total exchange amount in USD for a selected period.

---

### **"Proceed to Payment" Button**
A new option allows you to hide the "Proceed to Payment" button in the merchant module settings. This is useful if payment details are displayed in the text for the "**New Request**" status using the `[to_account]` shortcode.

---

### **Country List in Exchange Direction Restrictions**
Countries marked with a checkmark are now displayed at the top of the list.

---

### **Merchant Duplication**
You can now create a copy of a merchant along with all its settings with a single button. To use this feature, activate the "**Merchant Duplication and Auto-Payouts**" module in the "Modules" section after updating the script.

---

### **Bulk Merchant Addition**
A new feature allows you to add merchants in bulk to exchange directions in the merchant settings.

---

### **Currency ID**
You can now search by currency ID when creating an exchange direction.

- **View Currency ID**
- **Search by ID**

---

### **Module Access**
All users with access to the admin panel can view modules, but only administrators can activate or deactivate them.

---

### **Creating Requests Without Authorization**
It is now possible to create a request without authorization for directions that require account verification, provided the account/card number has already been verified.

---

### **Coupons**
A new **"Discount Coupons" (coupons)** module has been added, allowing you to offer personalized discounts to clients via promo codes. The module settings can be found in the "**Discount Coupons**" section.

When the module is activated, an optional "**Discount Coupon**" field will appear in the exchange form. This field can be enabled for each exchange direction in the "**Restrictions and Checks**" tab.

- **Adding a New Coupon**
- **Coupon List in the Admin Panel**
- **Enabling the Option for an Exchange Direction**
- **Coupon Input Field in the Exchange Form**

---

### **Using Multiple Merchants for Payments**
If multiple merchants are configured, you can now enable the use of alternative merchants for exchange directions. This ensures that if the primary merchant fails to provide payment details, another merchant will be used. For more details, refer to the [**instructions**](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov#podklyuchenie-neskolkikh-merchantov).

---

### **Payment Systems**
You can now sort payment systems by name in the "**Currencies**" -> "**Payment Systems**" section.

---

### **Parser Search**
A search field has been added to the exchange direction settings (in the "**Auto Rate Adjustment**" tab). You can now search for parsers by text, including the rate itself.

---

### **Country Sorting**
Country sorting by code has been replaced with sorting by country name in the "**Restrictions and Checks**" tab of the exchange direction settings.

---

### **List of Recalculated Rates**
When rate recalculation is enabled, the list of old rates in the "**Requests**" section could take up a lot of vertical space. To address this, the "**Old Rates**" block now has a fixed size, and the rates can be scrolled vertically within the block.

---

### **Request Deletion Timer**
The timer now includes seconds.

- **Shortcode for Timer in Template Settings**
- **Displaying the Timer with Seconds in Requests**

---

### **"Captcha for Website (Image Selection)" Module**
The **sitecaptcha_img** module has been upgraded to enhance security. It now generates captcha options automatically. The ability to create custom captcha options has been removed.

--- 

This translation aims to maintain the original meaning while ensuring clarity and natural flow in English. Let me know if you need further adjustments!

### Translation into Naturalistic English:

---

### Version 2.6 Updates

#### **Captcha Display in the Exchange Form**
- Captcha is now displayed directly in the exchange form.

#### **Telegram Bot for Notifications**
- Added the ability to send messages to users via their Telegram ID, even if they don’t have a username. You can find your Telegram ID using the bot [@getMyID](https://t.me/getmyid_bot). Note: Sending messages to groups is not supported.

  ![Example of Telegram Bot Notification](https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FsgS66ZwqNQwLSXqyzGoT%252Fimage.png%3Falt%3Dmedia%26token%3D5b4428e2-0c66-4c7b-ab9f-abb012f51eb5\&width=768\&dpr=4\&quality=100\&sign=d11ad25\&sv=1)

- You can view your Telegram ID using the bot [@getMyID](https://t.me/getmyid_bot).

#### **Adding Message Recipients in Template Settings**
- Added the ability to configure message recipients in template settings.
- New settings have been introduced to block bots. These settings can be found under "**Telegram**" -> "**Settings**."

  ![Telegram Settings Example](https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FPCQLTFYN6dONk7Vi3NLg%252Fimage.png%3Falt%3Dmedia%26token%3Dcf7e1e61-86c5-460a-92df-963e3d480f6b\&width=768\&dpr=4\&quality=100\&sign=3ded5c2b\&sv=1)

#### **Client Notifications**
- The "**Exchange Direction Template**" tab has been renamed to "**Notification Settings**" in the exchange direction settings. This allows you to configure notifications for specific exchange directions.
- Added the ability to specify individual **email addresses, Telegram accounts, or phone numbers** for administrators/operators to receive notifications about specific exchange requests. If any of these fields are filled, notifications will only be sent to the specified contacts, ignoring the general recipient list in the template.

  ![Notification Settings Example](https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252F6OENVKlwLssqKLCDuHfN%252Fimage.png%3Falt%3Dmedia%26token%3D03ad39ae-43cc-451d-9aeb-027df01143c4\&width=768\&dpr=4\&quality=100\&sign=d7bdd293\&sv=1)

#### **Requesting Payment Details**
- The option to choose when to request payment details has been removed. Starting from version 2.6, payment details will always be requested from the merchant at the time of creating the request.

#### **Custom Error Messages for Merchant Issues**
1. **Error Text for Payment Details in Requests**: Added an option to replace the text displayed in place of the `[to_account]` shortcode if the merchant fails to provide payment details. This setting can be found under "**Exchange Settings**" -> "**General Settings**."

   ![Error Text Example](https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FYwxmczrmSFykCqiHOKN7%252Fimage.png%3Falt%3Dmedia%26token%3Dbb68e6c0-7ad1-4863-bdaa-3c60319899a7\&width=768\&dpr=4\&quality=100\&sign=c5c7c199\&sv=1)

2. **Error Text for Payment Page Links**: Added an option to customize the button text for payment page links if the merchant (e.g., Bitconce Link, Firekassa Link) fails to provide payment details. This setting is available in the merchant module settings.

   ![Payment Page Error Example](https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FjppuhwSeQph8BijExiVZ%252Fimage.png%3Falt%3Dmedia%26token%3D7341c172-60fa-4001-9060-6943e90a97f4\&width=768\&dpr=4\&quality=100\&sign=cf12dc0c\&sv=1)

#### **Verification of Payment Details**
- In the general table for verifying cards/accounts/wallet numbers, administrators and operators can now specify the reason for rejecting a verification request. This option is available under "**User Accounts**" -> "**Account Verification**."

  ![Verification Example](https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FPN2GX1l8AmJZvGy3xdsr%252Fimage.png%3Falt%3Dmedia%26token%3Dce4d42fc-1038-4a2e-9623-23d1e0611e55\&width=768\&dpr=4\&quality=100\&sign=d0e7014b\&sv=1)

#### **Internal Accounts**
- A new version of the internal account module (**iac**) has been released, including a merchant and auto-payout feature for internal accounts with API support. The old module (**domacc**) has been removed starting from version 2.6. Instructions for migrating existing accounts to the new module can be found in the [**update guide**](https://premium.gitbook.io/main/pered-nachalom-raboty/instrukciya-po-obnovleniyu-skripta/obnovlenie-s-versii-2.5-do-2.6#izmeneniya-v-paneli-administratora).

---

### Version 2.5 Updates

#### **Verification Image Example**
- Added the ability to insert an example image for card verification in currency settings using the `img` shortcode.

#### **Merchant Status Updates**
- Merchants can now work with specific request statuses when receiving payment notifications. If no statuses are selected, the merchant will operate as configured in version 2.4. If specific statuses are selected, the merchant will only process those.

#### **API Interface**
- Introduced an API interface for the exchange system. [API Documentation](https://premium.gitbook.io/main/api-premium-exchanger/api-v1).

#### **Additional Updates**
- Support for PHP 8.1.
- Added new statuses for merchants and auto-payouts: "**Partial Payment**," "**Merchant Error**," and "**Partial Payout**."
- Improved currency account settings, including unique account visibility rules.
- Added individual partner commission limits.
- Enhanced AML/KYC compliance settings.
- Added support for Moex parser and Telegram notifications for parsing errors.

--- 

This translation provides a clear and natural explanation of the updates and features in versions 2.6 and 2.5. Let me know if you need further clarification!