# Exchange Settings

This section displays the main settings for the exchange service, applicable to all exchange directions and currencies.

## General Settings

<figure><img src="../../.gitbook/assets/image (1776).png" alt="" width="292"><figcaption></figcaption></figure>

**Update Mode** — The update mode is automatically activated after the exchange service is switched to maintenance mode or after reactivating the Premium Exchanger plugin in the "**Plugins**" section. To return the exchange service to normal operation, this option must be deactivated.

**Remember Successful Security Password Entry** — When this option is enabled, after the first entry of [each set password](https://premium.gitbook.io/main/osnovnye-nastroiki/nastroiki/paroli-bezopasnosti) (such as saving settings in the merchant module, attempting auto-payment, etc.), the password will not be requested again, and the action will be executed immediately.

**Remove Copy Button in Requests** — When this option is activated, the quick copy button for account details will be removed from the "Requests" section.

<figure><img src="../../.gitbook/assets/image (1782).png" alt=""><figcaption></figcaption></figure>

**Store Request Data in a File** — When this option is activated, a file containing data from requests will be generated on the server.

## Exchange Settings

<figure><img src="../../.gitbook/assets/image (1777).png" alt="" width="466"><figcaption></figcaption></figure>

**Type of Currency Exchange Direction Table** — Choose the [table](https://premium.gitbook.io/main/osnovnye-nastroiki/vneshnii-vid/vidy-tablic-napravlenii-obmena) to display on the main page of the website.

**Default Exchange Direction in the Selection Table** — Select the exchange direction that will be displayed by default when navigating to the main page of the website.

**If a Non-existent Direction is Selected:**

* **Show Error** — An error will be displayed if a non-existent exchange direction is selected.
* **Show Nearest** — The nearest active exchange direction will be displayed.

**Show in Exchange Form:**

* **All Currencies** — All currencies created in the exchange service will be displayed.
* **Only Available Currencies for Exchange** — Only currencies available for exchange will be displayed.

**Hide Currency Codes Above the Exchange Direction Selection Table** — When this option is activated, the filter panel for currency type/code will be hidden on the main page of the website.

<figure><img src="../../.gitbook/assets/image (1783).png" alt="" width="563"><figcaption></figcaption></figure>

**Exchange Form (**≥ v**2.6)** — Choose how the exchange direction will open.

* **On the Main Page** — The exchange form will open on the main page without changing the URL.
* **On a New Page** — The exchange form will open on a new page.

**Hide Min and Max Amount Errors in the Selection Table** — When this option is activated, errors will not be displayed if the amount entered by the client is outside the min/max range; however, the request will not be created.

## Exchange Form Settings

<figure><img src="../../.gitbook/assets/image (1778).png" alt="" width="465"><figcaption></figcaption></figure>

**Show in Exchange Form:**

* **All Currencies** — All currencies created in the exchange service will be displayed.
* **Only Available Currencies for Exchange** — Only currencies available for exchange will be displayed.

**If a Non-existent Direction is Selected:**

* **Show Error** — An error will be displayed if a non-existent exchange direction is selected.
* **Show Nearest** — The nearest active exchange direction will be displayed.

**Hide Min and Max Amount Errors in the Selection Table** — When this option is activated, errors will not be displayed if the amount entered by the client is outside the min/max range; however, the request will not be created.

**Prevent Saving Request Data** — When this option is activated, the checkbox for saving the data entered in the exchange form will be disabled, and the data will not be saved (if the client creates a new request in the same direction, they will need to re-enter all data).

<figure><img src="../../.gitbook/assets/image (1784).png" alt="" width="563"><figcaption></figcaption></figure>

## Other Settings

<figure><img src="../../.gitbook/assets/image (1779).png" alt="" width="563"><figcaption></figcaption></figure>

**Use Step 2 of the Exchange, Where the User Confirms Their Details** — When this option is activated, agreement to the exchange terms will be moved to the next step after clicking the "**Continue**" button.

<figure><img src="../../.gitbook/assets/image (1798).png" alt="" width="375"><figcaption></figcaption></figure>

**Text for Acceptance Checkbox Before Creating a Request** — Text for the line accepting the [exchange rules](https://premium.gitbook.io/main/osnovnye-nastroiki/nastroiki/stranicy-pravila-saita-pravila-provedeniya-proverok-aml-kyc-kyt).

**Exchange Amount is** — Choose the type of amount that will be used as the main amount for exchange statistics calculations.

<figure><img src="../../.gitbook/assets/image (1799).png" alt="" width="340"><figcaption></figcaption></figure>

**Show Block of Other Directions:**

* **No** — The block of other directions will not be displayed under the exchange form.
* **By Currency "Giving"** — A block of other exchange directions with the same currency in "**Giving**" will be displayed under the exchange form.
  
<figure><img src="../../.gitbook/assets/image (1800).png" alt="" width="563"><figcaption></figcaption></figure>

* **By Currency "Receiving"** — A block of other exchange directions with the same currency in "**Receiving**" will be displayed under the exchange form.

**Disable Additional Commission Addition to Reserve** — Additional commissions will not be added to the reserve amount deducted from the currency reserve when creating a request.

**Dependency of Minimum and Maximum Amount:**

* **No** — The exchange form will only show the min/max limits specified in the "**Exchange Amount**" tab in the exchange direction settings.

<figure><img src="../../.gitbook/assets/image (1803).png" alt=""><figcaption></figcaption></figure>

* **Yes, Site-wide** — The exchange form (as well as in the [export XML file](https://premium.gitbook.io/main/osnovnye-nastroiki/nastroiki/opisanie-modulei#nastroika-vyvoda-napravlenii-obmena-v-xml-txt-faile)) will display amount limits for both currencies, even if the min or max amount is not filled for one of the two currencies in the "**Exchange Amount**" tab in the exchange direction settings. Amounts that are not specified will be recalculated according to the exchange rate for that exchange direction.

<figure><img src="../../.gitbook/assets/image (1804).png" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
In the XML file, min/max amounts are always displayed **only** for the currency in "**Giving**" from the exchange direction. \
![](<../../.gitbook/assets/image (1805).png>)\
If the option for "**Dependency of Minimum and Maximum Amount**" is set to "**No**" and min/max amounts are specified only for the currency in "**Receiving**," there will be no exchange amount limits in the XML file for that exchange direction.
{% endhint %}

* **Yes, in Export File** — Min/max amounts will be recalculated for the currency in "**Giving**" if no limits were set for that currency in the exchange direction settings; the recalculated values will apply **only** to the XML file, while the exchange form on the website will display only the values specified in the "**Exchange Amount**" tab in the exchange direction settings.

**Send Email to Admin if Admin Changes Request Status** — Disable sending emails to the administrator specified in the "**Messages**" -> "**Email Templates**" section for active [admin templates](https://premium.gitbook.io/main/osnovnye-nastroiki/uvedomleniya-administratoram-i-klientam/uvedomleniya-po-e-mail#nastroika-shablonov-pisem) for request statuses if the administrator manually changes the request status in the "**Requests**" section.

**Calculate Limits "On the Fly"** — Calculate limit amounts for exchange directions.

**Allow Managing Requests from Another Browser** — Enable the ability to open a request in another browser. If this option is deactivated, the client will not be able to open the request in another browser.

<figure><img src="../../.gitbook/assets/image (1806).png" alt="" width="563"><figcaption></figcaption></figure>

**Visibility of Personal Data in Requests** — Display sensitive client data in requests.

* **Completely Hide**
* **Do Not Hide First 4 Characters**
* **Do Not Hide Last 4 Characters**
* **Do Not Hide First 4 and Last 4 Characters**

**Merchant's Place of Work (Recommended Option for Selection — **"Upon Request Creation"):**

* **Upon Request Creation** — Request for details from the merchant will be made during the request creation.
* **On the Request Page** — Request for details from the merchant will be made for an already created request.
* **On the Merchant Module Page** — Request for details from the merchant will be made when opening the merchant's payment page (relevant only if all used merchants employ this format).

**Page Header Style for Redirection** — Choose the color scheme for the header of the page displaying payment details.

* **White Style**
* **Dark Style**

Here’s a naturalistic English translation of the provided text:

---

**If no payment instructions are set for the merchant, then** — display the text on the application page according to the selected option below for the status "**New Application**"

* Do not display anything
* Show the relevant payment instructions from the exchange direction

**If no payment instructions are set for the auto-payment module, then** — display the text on the application page according to the selected option below for the status "**Paid Application**"

* Do not display anything
* Show the relevant payment instructions from the exchange direction

**Enable auto-payment if the received amount exceeds the required amount** — the option to enable automatic payment if the amount actually paid by the client exceeds the original amount from the application.

**Number of applications processed within the payment timeout cron** — the number of pending/frozen applications using auto-payments for which payment attempts will be made.

<figure><img src="../../.gitbook/assets/image (1780).png" alt="" width="519"><figcaption></figcaption></figure>

**Select application statuses for notifications in the top bar** — notifications with a counter of applications in the selected statuses in the "**Applications**" section of the top bar.

<figure><img src="../../.gitbook/assets/image (347).png" alt=""><figcaption></figcaption></figure>

**Show all zeros in the exchange rate** — hiding zeros that do not affect the formation of the exchange rate in the exchange form.

<figure><img src="../../.gitbook/assets/image (346).png" alt="" width="455"><figcaption><p>Displaying the rate with zeros</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (345).png" alt="" width="441"><figcaption><p>Displaying the rate without zeros</p></figcaption></figure>

**Separate numbers in the exchange rate with spaces** — separating large numbers by thousands for easier readability.

**Max. number of decimal places in calculations on the site** — the number of decimal places used in calculations (applies only to the recording of values in the database).

**Max. number of decimal places in calculations for currency reserves** — the number of decimal places used for currency reserves (applies only to the recording of values in the database).

**Max. number of decimal places in calculations for currency exchange rates** — the number of decimal places used in calculations for currency rates (applies only to the recording of values in the database).

**Blocked email domains** — email domains from which users will not be able to create applications (relevant when applications are created by bots aiming to disrupt the stable operation of the exchange service).

<figure><img src="../../.gitbook/assets/image (1781).png" alt="" width="563"><figcaption></figcaption></figure>

**Hide exchange directions from guests** — 

**Newbie check** — 

**Method for determining newbies** — 

**Warning text before creating an application for newbies** — 

**Error message if the amount exceeds the specified limit for newbies** — 

**Method for recalculating applications (based on the exchange rate):**

* **Always** — 
* **By cron** — 
* 

--- 

Feel free to ask if you need any further modifications or additional translations!