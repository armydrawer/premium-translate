# Update List

## Version 2.7

* **Uploading receipts by clients within a request (module "**Payment Receipts**" (**paychecks**))**

    <figure><img src="../../.gitbook/assets/image (1957).png" alt="" width="563"><figcaption></figcaption></figure>

    This module allows clients to upload receipts or other documents as images directly within a created request.

<figure><img src="../../.gitbook/assets/image (1988).png" alt="" width="474"><figcaption><p>Text settings for the specified block in the request (under "<strong>Modules</strong>" -> "<strong>Payment Receipts</strong>")</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (1956).png" alt="" width="327"><figcaption><p>Module settings (the "Payment Receipts" tab in the exchange direction settings)</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (1954).png" alt="" width="563"><figcaption><p>In the request, click the "<strong>Choose file</strong>" button</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (1952).png" alt="" width="563"><figcaption><p>Select the desired file and upload it</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (1955).png" alt="" width="563"><figcaption><p>After the client uploads the image, it will be displayed in the request under the "<strong>Requests</strong>" section</p></figcaption></figure>

* **Grouping exchange directions for quick filtering (module "**Direction Groups**" (**direction_groups**))**

    <figure><img src="../../.gitbook/assets/image (1958).png" alt="" width="563"><figcaption></figcaption></figure>

    <figure><img src="../../.gitbook/assets/image (1959).png" alt="" width="464"><figcaption><p>Add the desired number of groups in the "<strong>Direction Groups</strong>" section</p></figcaption></figure>

    <figure><img src="../../.gitbook/assets/image (1960).png" alt="" width="563"><figcaption><p>In the direction settings, under the "<strong>Main Settings</strong>" tab, assign the appropriate group to the direction</p></figcaption></figure>

    <div data-full-width="true"><figure><img src="../../.gitbook/assets/image (1961).png" alt=""><figcaption><p>In the table listing all directions, select the desired group and, for example, mark all directions in that group as inactive.</p></figcaption></figure></div>

* **Setting an individual profit percentage for each city for cash exchange directions, similar to the [overall profit percentage for an exchange direction](https://premium.gitbook.io/main/osnovnye-nastroiki/partnerskaya-programma/pribyl-i-partnerskii-procent#nastroika-pribyli-dlya-napravleniya-obmena).**

    <figure><img src="../../.gitbook/assets/image (1962).png" alt="" width="563"><figcaption><p>The "<strong>Cities</strong>" tab in the exchange direction settings</p></figcaption></figure>

* **Ability to set the status "**Completed Request**" via API (method `success_bid`).** Like other API methods for changing request statuses, this method applies only to requests created directly through the API.

Here is a natural English translation of the provided text:

---

<figure><img src="../../.gitbook/assets/image (1963).png" alt=""><figcaption><p>To identify a bid, you need to provide its hash (this is shown in the response to the <code>create_bid</code> API method when creating a bid)</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (1964).png" alt=""><figcaption><p>Changing bid statuses via the API</p></figcaption></figure>

* Bulk information editor — a filter by direction group has been added,

<figure><img src="../../.gitbook/assets/image (1965).png" alt="" width="445"><figcaption><p>Filter by direction group</p></figcaption></figure>

as well as the ability to specify commissions and exchange amounts in a single window for selected directions.

<figure><img src="../../.gitbook/assets/image (1966).png" alt="" width="445"><figcaption><p>Selecting an entity to edit</p></figcaption></figure>

<div><figure><img src="../../.gitbook/assets/image (1967).png" alt="" width="563"><figcaption><p>Editing payment system commissions</p></figcaption></figure> <figure><img src="../../.gitbook/assets/image (1970).png" alt="" width="563"><figcaption><p>Editing exchange amounts</p></figcaption></figure></div>

* The option to completely disable merchant logs and automatic payouts

<figure><img src="../../.gitbook/assets/image (283).png" alt=""><figcaption><p>This option is available in the settings of each merchant module and automatic payout module</p></figcaption></figure>

* Restriction on creating bids with the same amount for a given exchange direction

<figure><img src="../../.gitbook/assets/image (285).png" alt="" width="422"><figcaption><p>The "<strong>Restrictions and Checks</strong>" tab in the exchange direction settings</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (286).png" alt="" width="532"><figcaption><p>If a second bid is created while there is an unpaid first bid for the same amount, the client will receive an error</p></figcaption></figure>

* Directions and currencies sorting module — only active currencies will be shown in this section (previously, all currencies were displayed)

<figure><img src="../../.gitbook/assets/image (274).png" alt="" width="477"><figcaption></figcaption></figure>

* "**Operator live**" module (`many_operators`)

<figure><img src="../../.gitbook/assets/image (275).png" alt="" width="563"><figcaption></figcaption></figure>

Added the ability to display only bids from specific exchange directions, as well as bids involving certain merchants on the receiving side, for each user with access to the admin panel.

<figure><img src="../../.gitbook/assets/image (276).png" alt=""><figcaption><p>With this setting, the operator will see only bids where the Advcash merchant was used</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (277).png" alt=""><figcaption><p>With this setting, the operator will see only bids from the specified exchange directions</p></figcaption></figure>

---

If you need the text adapted for a particular audience or style, please let me know!

Here is a natural English translation of the provided text:

---

<figure><img src="../../.gitbook/assets/image (278).png" alt=""><figcaption><p>With this setting, the operator will see only requests from the specified exchange directions, as well as requests from all exchange directions where the merchant Advcash was used.</p></figcaption></figure>

You can also use the inverse filter:

<figure><img src="../../.gitbook/assets/image (279).png" alt=""><figcaption><p>With this setting, the operator will see requests from <strong>all</strong> exchange directions except for the specified ones.</p></figcaption></figure>

{% hint style="warning" %}
Do not use positive and negative filter values simultaneously — filtering works on an OR basis, so negative filters will be ignored if they are combined with positive ones.
{% endhint %}

<figure><img src="../../.gitbook/assets/image (281).png" alt=""><figcaption><p>With this setting, the operator will see <strong>all</strong> requests from exchange direction 1340 (even if the merchant Bova was used), as well as requests from <strong>all</strong> exchange directions where the merchant Bova was <strong>not</strong> used.<br>In other words, the negative filter for merchant Bova will not be applied if it is used in direction 1340.</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (282).png" alt=""><figcaption><p>With this setting, the operator will see requests from all exchange directions (even if the merchant Bova was <strong>not</strong> used), as well as requests from <strong>all</strong> exchange directions where the merchant Bova was used (even if that is direction 1340).<br>In other words, the negative filter for direction 1340 will not be applied if there are requests in this direction with merchant Bova.</p></figcaption></figure>

* Moving user coefficients for Parsers 2.0 to a separate section

<figure><img src="../../.gitbook/assets/image (1971).png" alt=""><figcaption><p>Sidebar section</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (1972).png" alt="" width="449"><figcaption><p>Coefficient settings</p></figcaption></figure>

Index name — the desired name that will be used as a shortcode in formulas  
Value formula — enter a number or a mathematical formula here  
Index value — the value for the formula specified above (if a formula is used)  
Index type:  
• Formula substitution in the rate

---

If you need the translation adapted for a specific audience or style, please let me know!

Here is a naturalistic English translation of the provided text:

---

<figure><img src="../../.gitbook/assets/image (1974).png" alt=""><figcaption><p>The formula will be inserted directly into the rate without parentheses, and then the rate value itself will be calculated.</p></figcaption></figure>

• Index value

<figure><img src="../../.gitbook/assets/image (1973).png" alt=""><figcaption><p>First, the coefficient value will be calculated, and then it will be applied to the rate.</p></figcaption></figure>

Comment — a field for your notes  
* The option to create a task for updating rates when using the "**On the website**" option has been removed (this option caused the server to overload with unnecessary requests).

<div><figure><img src="../../.gitbook/assets/image (1976).png" alt=""><figcaption><p>Version 2.6</p></figcaption></figure> <figure><img src="../../.gitbook/assets/image (1975).png" alt=""><figcaption><p>Version 2.7</p></figcaption></figure></div>

* The results of recalculations for requests have been moved to a separate section called "**Recalculation Log**."

<figure><img src="../../.gitbook/assets/image (1977).png" alt="" width="563"><figcaption></figcaption></figure>

* The "**Blacklist**" module — added the ability to verify the actual account from which the client’s payment originated.

<figure><img src="../../.gitbook/assets/image (265).png" alt="" width="404"><figcaption></figcaption></figure>

Added the ability to customize blacklist elements individually.

<figure><img src="../../.gitbook/assets/image (266).png" alt="" width="418"><figcaption></figcaption></figure>

Method:  
• **From general settings** — the method selected in the module’s general settings will be applied.  
• **Show error** — if this blacklist element is present, an error will be shown on the exchange form when creating a request, even if the general settings method is set to "**Stop auto payout**."  
• **Stop auto payout** — if this blacklist element is present, the request will be created (and checked during the auto payout stage), even if the general settings method is set to "**Show error**."

* The "**AML**" module — all AML modules and logs related to AML module operations are now located in a single section.

<figure><img src="../../.gitbook/assets/image (268).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (267).png" alt=""><figcaption></figcaption></figure>

Added the ability to quickly switch AML modules in the exchange direction settings.

<figure><img src="../../.gitbook/assets/image (269).png" alt="" width="241"><figcaption></figcaption></figure>

New statuses have been added for requests when there is a delayed response from the AML service.

<figure><img src="../../.gitbook/assets/image (270).png" alt="" width="287"><figcaption></figcaption></figure>

If no response is received from the service within the time specified in the module settings,

---

If you need the continuation or any further adjustments, please let me know!

Here is a natural English translation of the provided text:

---

Then the request will change its status to "**Pending**" and return to the previous status (if the client’s details are successfully verified) or to "**AML Check Failed**" (if the risk threshold is exceeded) after receiving a response from the AML service. To enable this feature, you need to add a [cron job](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-sozdat-zadanie-cron-na-servere) on the server (the link for setting this up can be found in the "AML" section).

---

{% hint style="warning" %}
This option applies only to requests that have already been created (if the check for this exchange direction is enabled as "**On Payment**" or "**Before Auto Payout**").

![](<../../.gitbook/assets/image (249).png>)
{% endhint %}

---

* Added logging of operator/manager actions. The following will be displayed:  
  • Date and time of the changes  
  • User who made the changes  
  • Data that was changed (old data shown in red, new data in black)

---

The following sections are logged:  
• Exchange direction settings  
• Currency settings  
• Currency rates in the "**Parsers 2.0**" -> "**Rates**" section  
• Settings for **Bestchange parsers** and **Bestchange API**

---

* Added the ability to wait for receiving details from the merchant (only for fiat merchants who provide details in the API response and support repeated requests for details).

---

For this option to work, the "**Mark request as merchant error**" option must also be enabled in "**Exchange Settings**" -> "**General Settings**" (only then will the details be requested again or the request will change to the status "**Merchant Error**").

---

If you need any further adjustments or clarifications, feel free to ask!

{% hint style="warning" %}
Please note that making repeated requests to the merchant within a short time frame (if the payment details were not received on the first request) often causes the merchant to treat such requests as spam, which may result in your exchanger being blocked by the merchant’s spam filter.

To avoid this, we recommend informing the merchant’s representatives in advance that your exchanger may send repeated requests for the same order if the payment details were not obtained initially. This way, the merchant can whitelist your exchanger in their spam filter.
{% endhint %}

## Version 2.6

<details>

<summary>Changelog</summary>

* **"Bestchange Blacklist" Module (blacklist_bestchange):** Added the ability to halt payouts on an order if one or more client details are found in the Bestchange blacklist when using this module. Module settings can be found under "**Modules**" -> "**Bestchange Blacklist**."

    ![](https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FIYShnbIVsQtdyzn1bKip%252Fimage.png%3Falt%3Dmedia%26token%3D69302b5b-7f4f-4847-b874-c928ea29ae01&width=768&dpr=4&quality=100&sign=52626c56&sv=1)
* **Blacklist:** Updated similarly to the **blacklist_bestchange** module, allowing you to accept funds and stop payouts if a user is on the blacklist. Module settings are located under "**Blacklist**" -> "**Settings**."

    ![](https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252F18OpRTbt1jzLD5l2HMZ4%252Fimage.png%3Falt%3Dmedia%26token%3Dcd4f10d7-7da0-49f2-b46a-ebf0e58efe1e&width=768&dpr=4&quality=100&sign=3df31e7f&sv=1)

- **AML Check:** Added the option to perform a risk check immediately before sending currency to the client’s wallet, with the order marked as an error if the risk level is exceeded. Risk level settings are available under "**Modules**" -> "**AML Bot**" or "**Getblock**" (depending on which service you have integrated).  
  The logic for running the check is configured in the exchange direction settings, under the "**AML Bot**" or "**Getblock**" tab.

</details>

Here is a natural English translation of the provided text:

---

* **Getblock AML Service, Sleep Function**: Added the ability to set a wait time for the service response in case the verification result is not returned immediately. This setting can be found under "**Modules**" -> "**Getblock**."

    ![](https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FUCwqQIbUxlfFgP0SyEdU%252Fimage.png%3Falt%3Dmedia%26token%3D1a328e43-5f40-46f9-a44f-687546201bdb&width=768&dpr=4&quality=100&sign=fdf901cd&sv=1)

* **Email Confirmation**: Added the option to request client email confirmation before creating a request. The module "**Email Confirmation Before Request Creation**" (**confirmexchmail**) must be activated in the "**Modules**" section. Module settings are located under "**Modules**" -> "**Email Confirmation Before Request Creation**."

    ![](https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FNqMA0JHfsAhhn1AdvZ01%252Fimage.png%3Falt%3Dmedia%26token%3D6a490aa4-14e5-45e7-a3fa-2642afb47054&width=768&dpr=4&quality=100&sign=320c412&sv=1)

* **Archiving**: The module structure has been updated. Added filtering by **request status / merchant-provided details / transaction hash for incoming and outgoing payments** in "**Requests**" -> "**Archived Requests**."

    ![](https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252F1n2WBW6PYrXoMCgg71RI%252Fimage.png%3Falt%3Dmedia%26token%3D2e1f1089-95be-4fa0-8867-6bd81a2f8042&width=768&dpr=4&quality=100&sign=2d57193b&sv=1)

You can also view comments on archived requests.

![](https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FivYchvvmMsQYN9c7guAN%252Fimage.png%3Falt%3Dmedia%26token%3D1db134fb-a823-467b-9118-46387ab80d11&width=768&dpr=4&quality=100&sign=f75c4b9a&sv=1)

Adding comments to requests is available in the "**Requests**" section.

---

Let me know if you need it adapted for a specific audience or style!

Here is a natural English translation of the provided text:

---

**Viewing Requests in the "Requests" Section -> "Archived Requests"**

![Archived Requests](https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FiaLmFJ4MBhewlPCKBM5O%252Fimage.png%3Falt%3Dmedia%26token%3D438be925-6698-4c02-a250-6ede35195354&width=768&dpr=4&quality=100&sign=4236fbb4&sv=1)

**Viewing Added Comments**

<mark style="color:red;">Searching with the specified filters and viewing comments on requests will only work for requests archived in version 2.6.</mark>

---

### BestChange API Parser (bestchangeapi)

- A module for working with the API has been added. Module settings can be found under "**BestChange API Parser**" -> "**Settings**" and on the **"BestChange API Parser"** tab in the exchange directions settings.

![General parser settings](https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FB0oDC0uNelBlhxx0TmB3%252Fimage.png%3Falt%3Dmedia%26token%3Dca52b0f7-e79d-4128-aefb-58e721f74026&width=768&dpr=4&quality=100&sign=b8b71d3&sv=1)

*General parser settings*

![Exchange rate setting](https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FnGSQZPgneaUqDSB3JUi3%252Fimage.png%3Falt%3Dmedia%26token%3D1a6c6185-bd92-4cac-b27b-bbbb9b52988d&width=768&dpr=4&quality=100&sign=65b6dce4&sv=1)

*Setting the exchange rate received from the parser for the exchange direction*

---

### Exchange Directions Filtering

- A filter by payment systems has been added in the "**Exchange Directions**" section.

![Payment systems filter](https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252F9xdx6Yn7jEL1kWLrC3ga%252Fimage.png%3Falt%3Dmedia%26token%3Dc85f4a49-b77c-4a6e-9c2a-383e9735755d&width=768&dpr=4&quality=100&sign=51546725&sv=1)

---

### Profit Values in Notifications

- It is now possible to specify **preset (not calculated!) profit values set in the exchange directions settings (on the "Rate" tab)** via shortcodes for displaying these values in emails and Telegram messages sent to administrators.

---

If you need any further help or adjustments, feel free to ask!

- **Replacement of the e-mail confirmation module**: After updating, you need to deactivate and then delete the **rconfirm** module from the server, and use the **confirmregmail** module instead. For more details, see the [**update instructions**](https://premium.gitbook.io/main/pered-nachalom-raboty/instrukciya-po-obnovleniyu-skripta/obnovlenie-s-versii-2.5-do-2.6#izmeneniya-v-paneli-administratora). When installing version 2.6 of the script from scratch, the **rconfirm** module will not be included by default.

- **Template text splitting**: A new feature has been added that allows you to split the text from the exchange direction template, which will be displayed when working with requests via the API and on the website using shortcodes.

- **“Financial Statistics” section**: The financial statistics module now includes overall statistics on the number of exchanges and the total exchange amount in USD for the selected period.

- **“Proceed to Payment” button**: It is now possible to hide this button in the merchant module settings for receiving payments. This is useful if the payment details are already shown in the text for the "**New Request**" status via the `[to_account]` shortcode.

Here is the translation into natural English:

---

* **List of countries in exchange direction restrictions**: Countries marked with a checkmark are displayed at the top of the list.

* **Merchant copying**: Added the ability to create a copy of a merchant with all settings by clicking a button. To use this feature, activate the "**Merchant copying and auto-payouts**" module in the "Modules" section after updating the script.

* **Bulk merchant addition**: Added the ability to add merchants in bulk to exchange directions within the merchant settings.

* **Currency ID**: Added the ability to search by currency ID when creating an exchange direction.

* **Viewing currency IDs**

---

Let me know if you need any further adjustments!

Search by ID  
* **Module Access:** Access is available to all users with access to the admin panel, but only administrators are allowed to activate or deactivate modules.  
* **Submitting Requests Without Authorization:** It is now possible to submit a request without logging in for directions that require verification of details, provided the account/card number has been previously verified.  
* **Coupons:** A new **"Discount Coupons" (coupons)** module has been added to offer personalized discounts to customers via promo codes. The module settings can be found under the "**Discount Coupons**" section.  

When the module is activated, an optional "**Discount Coupon**" field will appear on the exchange form (this field can be enabled for each exchange direction on the "**Restrictions and Checks**" tab).  

---

**Adding a New Coupon**  

---

**Coupon List in the Admin Panel**  

---

**Enabling the Option for an Exchange Direction**  

---

**Coupon Input Field on the Exchange Form**

Here is a natural English translation of the provided text:

---

* **Using Multiple Merchants for Acceptance:** A new option has been added to enable the use of alternative merchants (if multiple merchants are configured) for exchange directions in cases where the highest-priority merchant fails to provide payment details. For more information on how this option works, please refer to the [**instructions**](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov#podklyuchenie-neskolkikh-merchantov).

* **Payment Systems:** You can now sort payment systems by name in the "**Currencies**" -> "**Payment Systems**" section.

    ![](https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FrVcx6Fl3VIVnZnUY1Gdb%252Fimage.png%3Falt%3Dmedia%26token%3D930ef314-3dfb-4df4-812a-b739d343dd63\&width=768\&dpr=4\&quality=100\&sign=e448d909\&sv=1)

* **Parser Search:** A search field has been added to find parsers by text within the exchange direction settings (under the "**Auto Rate Adjustment**" tab). The search scans the entire string, including the rate itself.

    ![](https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FJfHORHxxLfjtQlvr29bI%252Fimage.png%3Falt%3Dmedia%26token%3D761d2bc0-50e6-4a5a-9e7a-d4e72a30eeb5\&width=768\&dpr=4\&quality=100\&sign=c1c75399\&sv=1)

* **Country Sorting:** Sorting by country code has been replaced with sorting by country name on the "**Restrictions and Checks**" tab within exchange direction settings.

    ![](https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252Fc37Ig1etNulPLbV5eHNK%252Fimage.png%3Falt%3Dmedia%26token%3Db984986e-2365-4a0e-aa23-15f67e33faea\&width=768\&dpr=4\&quality=100\&sign=7a22a5b0\&sv=1)

* **List of Recalculated Rates:** When rate recalculation is enabled, the list of old rates in an application under the "**Applications**" section can become very tall vertically. To fix this, the "**Old Rates**" block is now fixed in size, with the rates scrolling vertically inside the block.

---

Let me know if you need it adapted for a specific audience or style!

Here is the text translated into natural, fluent English:

---

* **Request Deletion Timer:** Seconds have been added to the timer.

* Shortcode for the timer is now available in the template settings.

* Timer display now shows seconds in the request.

* **"Captcha for Website (Image Selection)" Module (sitecaptcha_img):** The module has been upgraded to improve security. It now automatically generates captcha options. The ability to create custom captcha options has been removed.

* Captcha display in the exchange form.

* **Telegram Bot for Notifications:** Added the ability to send messages by user ID without requiring a username (you can find your ID using the [@getMyID](https://t.me/getmyid_bot) bot). Sending messages from the bot to groups is not supported.  
  ![View ID via @getMyID bot](https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FsgS66ZwqNQwLSXqyzGoT%252Fimage.png%3Falt%3Dmedia%26token%3D5b4428e2-0c66-4c7b-ab9f-abb012f51eb5%26width%3D768%26dpr%3D4%26quality%3D100%26sign%3Dd11ad25%26sv%3D1)

* Adding message recipients in the template settings.

Additionally, settings to block bots have been added. These module settings can be found under "**Telegram**" -> "**Settings**".

---

If you need any further adjustments or a more formal tone, just let me know!

Here is a natural English translation of the provided text:

---

**Customer Notifications:**  
The "**Exchange Direction Template**" tab has been renamed to "**Notification Settings**" within the exchange direction settings (this includes a template for sending in emails or Telegram messages using the shortcode `[dirtemp]`). A new option has been added to specify personal **email/Telegram account/phone number** for receiving notifications about requests in this direction by the administrator/operator. If one or more contact fields are filled in, the data from the template above will be sent **only to the specified contacts**, ignoring the recipient list in the general template. These option settings can be found in the exchange direction settings under the "**Notification Settings**" tab.

![image]

**Timing of Payment Details Request:**  
The option to choose when to request payment details has been removed — starting from version 2.6, the request for payment details from the merchant will always occur at the moment the request is created.

**Button Text Replacement on Merchant Error (payment details shown in the request):**  
An option has been added to replace the text displayed instead of the shortcode `[to_account]` if, for some reason, the merchant was unable to provide payment details. This option is located under "**Exchange Settings**" -> "**General Settings**".

---

Let me know if you need it adapted for a specific audience or format!

Here is a natural, fluent English translation of the provided text:

---

* **Changing the button text on merchant error (link to payment page):**  
An option has been added to replace the text on the button that links to the merchant’s payment page if, for some reason, the merchant (Bitconce Link, Firekassa Link, etc.) fails to provide payment details. This option can be found in the merchant module settings, accessible via the button that leads to the payment details.

![Option in merchant module settings](https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FjppuhwSeQph8BijExiVZ%252Fimage.png%3Falt%3Dmedia%26token%3D7341c172-60fa-4001-9060-6943e90a97f4&width=768&dpr=4&quality=100&sign=cf12dc0c&sv=1)  
*Option in the merchant module settings*

![Error text displayed on the button in the request](https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FUjIpanbwP0kKiWmVh18G%252Fimage.png%3Falt%3Dmedia%26token%3D994a2160-4376-4afc-bc79-3e6eb816d2e2&width=768&dpr=4&quality=100&sign=662dc581&sv=1)  
*Error text displayed on the button in the request*

* **Verification of payment details:**  
In the main table listing card/account/wallet number verification requests, it is now possible to specify the reason for verification denial. This view is available only to administrators and operators working with the module. The option is located under "**User Accounts**" -> "**Account Verification**."

![Verification denial reason option](https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FPN2GX1l8AmJZvGy3xdsr%252Fimage.png%3Falt%3Dmedia%26token%3Dce4d42fc-1038-4a2e-9623-23d1e0611e55&width=768&dpr=4&quality=100&sign=d0e7014b&sv=1)

* **Internal accounts:**  
A new version of the internal account module (**iac**) has been released, including merchant and auto-payout features for internal accounts, with the ability to make payouts to internal accounts via API. The old module version (**domacc**) has been removed from the script starting with version 2.6. For details on migrating existing accounts to the new module, please refer to the [**update instructions**](https://premium.gitbook.io/main/pered-nachalom-raboty/instrukciya-po-obnovleniyu-skripta/obnovlenie-s-versii-2.5-do-2.6#izmeneniya-v-paneli-administratora).

---

If you need the translation in a different style or more concise, just let me know!

## Version 2.5

<details>

<summary>Update List</summary>

* Added the ability to insert an example photo for card verification in the currency settings using the img shortcode.

    <figure><img src="../../.gitbook/assets/image (462).png" alt=""><figcaption></figcaption></figure>

```
<img src="https://premiumexchanger.com/images.jpg" alt="" />, 
where src is the full URL to your image
```

* A list of application statuses that the merchant will work with when receiving payment notifications from the payment system. If none of the options are selected, the merchant will operate with the statuses as configured in version 2.4.

If one or more statuses are selected from the list, the merchant will work **only** with the selected statuses!

Why is this needed? For example, if you select the status "**Deleted application**," then if the application has already been deleted but the merchant receives a payment notification for it, the merchant will process the application with that status and mark it as paid.

<img src="../../.gitbook/assets/Добавить мерчант ‹ Premium Exchanger — WordPress - Google Chrome_2023-03-18_09_07_40 (1).png" alt="" data-size="original">

</details>

Here is a natural English translation of the provided text:

---

* API interface for the exchanger. [API interface documentation](https://premium.gitbook.io/main/api-premium-exchanger/api-v1).  
* All merchants and automatic payouts have been updated.  
* Code refactoring completed and bugs fixed.  
* Added support for PHP 8.1.  
* Three new statuses added for merchants and automatic payouts: "**Partial Payment**", "**Merchant Error**", "**Partial Payout**".  
* Currencies now have categories.  
* Contact form settings added: stop words, email blacklist, banned email domains, and banned IP addresses.  
* Added hreflang tags to pages when automatic language detection for users is disabled.  
* The registration agreement link can now be set in the settings.  
* Added a separate checkbox for AML/KYC rules.  
* Added settings to restrict reviews.  
* In the currency accounts module, a uniqueness feature was added: the account number will not be shown for payment in a request if there are active requests using that account.  
* Minimum amount limits added for merchants.  
* In the automatic registration module, added a setting to disable auto-registration for specific directions.  
* Added a MOEX parser.  
* Added the ability to send Telegram notifications about parsing errors.  
* Old exchange rates have been added to the recalculation module.  
* Internal accounts can now be adjusted.  
* Individual maximum partner commission percentage added.  
* Account verification can now be done on the request creation page via a popup window, with the option to upload a sample image in the instructions.  
* Merchants and payouts now support connection priority within a direction if multiple are connected to the same direction.  
* New fields added to requests: txid_in, txid_out, agent.  
* For merchants, you can choose at which step of request creation the API call will be made.  
* Email templates for crypto merchants have been unified.  
* For currency accounts, a mode was added where the account is hidden as long as there is an active request associated with it.

---

Let me know if you need the text adapted for a specific audience or style!