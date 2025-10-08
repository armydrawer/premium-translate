# General Merchant Settings

Most of the settings mentioned in this section are used across all developed modules for merchants. Some merchants have specific parameters that will be addressed directly in the setup instructions for those merchants.

## Module Settings

Since each merchant has its own API for authorization, the fields in this section may vary. Please enter the authorization data provided by the merchant according to the field names.

{% tabs %}
{% tab title="Option 1" %}
<figure><img src="../../../.gitbook/assets/image (125)_eng.png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Option 2" %}
<figure><img src="../../../.gitbook/assets/image (8)_eng.png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Option 3" %}
<figure><img src="../../../.gitbook/assets/image (10)_eng.png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Option 4" %}
<figure><img src="../../../.gitbook/assets/image (20)_eng.png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Option 5" %}
<figure><img src="../../../.gitbook/assets/image (138)_eng.png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Option 6" %}
<figure><img src="../../../.gitbook/assets/image (120)_eng.png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

## Settings

{% hint style="warning" %}
Please note that when using certain merchant modules, you need to create a [separate copy of the merchant module](#user-content-fn-1)[^1] <mark style="color:red;">**for each fiat currency/cryptocurrency/blockchain**</mark>. In each copy, you must select/specify the corresponding item (this could be a fillable field or a dropdown list labeled "**Network**"/"**Payment Method**"/"**Transaction Type**"), and then connect this copy of the module on the "**Merchants and Payouts**" tab in the exchange direction settings, where the currency in "**I Give**" uses the specified currency.
{% endhint %}

{% hint style="danger" %}
If the merchant module settings display the field "**Payment Note**," you must fill it in with the text **`ID Request: [exchange_id]`** or simply **`[exchange_id]`**.

This is necessary to link the request to the transaction with the merchant — without this shortcode, the request status will not change.

![](<../../../.gitbook/assets/image (1508)_eng.png>)
{% endhint %}

The block below outlines the general settings for the merchant's operation.

<figure><img src="../../../.gitbook/assets/image (2204)_eng.png" alt="" width="531"><figcaption></figcaption></figure>

* **Payment Instructions for the User —** provide payment instructions for the user that will be displayed on the page with the "**Proceed to Payment**" button.

{% hint style="warning" %}
To display the details received from the merchant directly in the request, use the shortcode **\[to\_account]** in the "**Payment Instructions for the User**" field when the merchant is connected in the exchange direction.\
![](<../../../.gitbook/assets/image (1263)_eng.png>)

A suitable text for the "**Payment Instructions for the User**" field could be:

{% code overflow="wrap" %}
```
<p>Please transfer <strong>[copytext][sum1c][/copytext][currency_code_give] [psys_give]</strong></p>
<p>To the address: [breakword]<strong>[copytext][to_account][/copytext], the details belong to [dest_tag]</strong>[/breakword]</p>
<p>[qr_code size="200"][to_account][/qr_code]</p>
<p><strong>Attention!</strong> The address has a limited lifespan — do not send funds after the request expires, as this will result in a loss of funds!</p>
<p>You have:</p>
[js_timer][bid_delete_time][/js_timer]
The system will automatically process the payment as soon as it appears on the network.
```
{% endcode %}

The shortcode \[breakword] will correctly break a long (30 characters or more) wallet number \[to\_account] — for example, for the cryptocurrency Monero (XMR).

Of course, you can adjust the above instructions as you see fit.
{% endhint %}

* **Payment Note** — if this field appears in the merchant module settings, <mark style="color:red;">**it is mandatory**</mark> to fill it in, as it will be passed to the merchant. A correct payment note looks like this: **`Request [exchange_id]`**
* **Payment Amount Tolerance** — if necessary, specify the tolerance (absolute value in the payment currency or % of the request amount). In this case, the merchant will check the payment amount from the user against the specified tolerance (to the lower side).

{% hint style="info" %}
**Example 1:**\
Tolerance set to 0.5. The user is supposed to pay 50 USDT but mistakenly pays 49.9 USDT. When checked by the merchant, this payment will be accepted, as the underpayment is 0.1 USDT, which falls within the specified tolerance of 0.5.

\
**Example 2:**\
Tolerance set to 1.5%. The user is supposed to pay 1000 DOGE but mistakenly pays 990 DOGE. When checked by the merchant, this payment will be accepted, as the underpayment is 10 DOGE, which falls within the specified tolerance of 1.5% (1000*1.5%=15 DOGE).
{% endhint %}

* **Daily Limit for the Merchant** — if necessary, set a daily limit on the amount of funds the merchant can receive. The merchant will not be able to accept payments exceeding the specified limit. This is indicated in the currency you plan to accept.

{% hint style="warning" %}
If you plan to use options for setting limits and/or min/max payout amounts, and a single merchant module is used for receiving different currencies, then **it is necessary** to create copies of the module for each currency.
{% endhint %}

* **Monthly Limit for the Merchant** — if necessary, set a monthly limit on the amount of funds the merchant can receive. The merchant will not be able to accept payments exceeding the specified limit.
* **Minimum Payment Amount for One Request** — if necessary, set a minimum payment amount for one request. The merchant will not be able to accept payments below the specified limit.
* **Maximum Payment Amount for One Request** — if necessary, set a maximum payment amount for one request. The merchant will not be able to accept payments exceeding the specified limit.
* **Daily Request Limit (number) for the Merchant** — the number of completed requests that can be created within a day.
* **Hide "Cancel Request" Button:**\
  • **Yes** — remove the button from the request page for the client\
  • **No** — display the button
* **Hide "Proceed to Payment" Button:**\
  • **Yes** — remove the button **"Proceed to Payment"/"I Paid for the Request"** from the request page for the client\
  • **No** — display the button
* **Payment Amount for the User** — the amount that will be displayed to the user when creating a request:\
  • **Amount You Give (additional fee)**\
  • **Amount You Give (with additional fee and payment system commission)**\
  • **Amount for Reserve**\
  • **Amount You Give**
* **Expected Amount to be Credited** — the amount expected to be credited to the merchant's account:\
  • **Amount You Give (additional fee)**\
  • **Amount You Give (with additional fee and payment system commission)**\
  • **Amount for Reserve**\
  • **Amount You Give**

{% hint style="warning" %}
If the merchant charges a fee for incoming payments, it is important to ensure that the correct type is selected for the **expected amount to be credited** to ensure the module works correctly and the request status changes to "**Paid**" upon receipt of funds from the client.

To do this, when the merchant is connected in the exchange direction, create a request, do not pay for it, expand it using the "**Info**" button in the "**Requests**" section, and select the type of amount that matches one of the specified amounts that will be credited to the merchant's account after the fee is deducted. 

![](<../../../.gitbook/assets/image (2013)_eng.png>)

Often, this is the type "**Amount for Reserve**" in the merchant module settings — check this first. Select the appropriate item, save the settings, and pay for the request. If the request changes to "**Paid**" after payment of the full amount, then the settings are correct.

![](<../../../.gitbook/assets/image (2014)_eng.png>)
{% endhint %}

* **Allowed IP Addresses (one per line)** — specify the IP address(es) of the payment system that will be allowed access to the merchant's status URL. The payment system sends payment information to this URL. Specifying allowed IP addresses enhances the security of working with the merchant.

{% hint style="info" %}
You can find out the IP address(es) of the payment system that sends payment information to the status URL by contacting the technical support of the payment system.
{% endhint %}

* **Cron File Hash** — **create** and specify a hash that will complement the Cron job URL (a random set of 20-40 Latin letters and numbers).

{% hint style="danger" %}
Don't forget to create a Cron job on the server to check the payment — [**setup instructions**](https://premium.gitbook.io/main/en/basic-settings/faq/kak-sozdat-zadanie-cron-na-servere).
{% endhint %}

Here’s a naturalistic English translation of the provided text:

---

* **Hash for Status/Result URL** — **create** and specify a hash that will complement the merchant's status URL. The payment system sends payment information to this URL. By setting a hash, the status URL becomes unique, enhancing security when working with the merchant. We recommend using a hash that is 20-50 characters long, containing Latin letters and numbers. An example of a hash is `ImYkwGsq2fjhuWypiasq2QJzVvCpis8umbxs8umbx`.

{% hint style="danger" %}
If the settings for a specific merchant module or auto-payment display a line with Status URL/Callback URL, but there is no mention of it in the module's setup instructions, you can ignore this URL (it is handled at the code level without administrator configuration).\
\
When configuring the merchant on the payment system side, specify the status address (usually this is the Status URL or Return URL) with the hash already included!
{% endhint %}

* **Debug Mode** — activate this option only during initial setup or when experiencing issues with the merchant. When enabled, an extended merchant log will be recorded in the "**Merchants**" ➔ "**Merchant Logs**":\
  • **No**\
  • **Yes**

## Managing Application Statuses

In this section, you can configure how the merchant handles specific rules for transitioning applications between statuses.

<figure><img src="../../../.gitbook/assets/image (806)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

* **Account number from which the payment was made does not match the one specified in the application** — if the account numbers do not match, you can either change the application status or keep the current one:\
  • **keep the application status as "New Application"**\
  • **change the application status to "Under Review"**\
  • **change the application status to "Paid Application"**
* **Payment amount is less than required** — if the user made a transaction for a lesser amount than specified in the application, you can either change the application status or keep the current one:\
  • **keep the application status as "New Application"**\
  • **change the application status to "Under Review"**\
  • **change the application status to "Paid Application"**
* **Payment amount is greater than required** — if the user made a transaction for a greater amount than specified in the application, you can either change the application status or keep the current one:\
  • **keep the application status as "New Application"**\
  • **change the application status to "Under Review"**\
  • **change the application status to "Paid Application"**
* **Priority** — specify a priority from 1 to 10 (where: 0 or an empty field indicates no priority or the lowest priority module, and 1 and above indicate increasing priority (0<1<2<3<...<9)), if multiple merchant modules are used in the exchange direction.

{% hint style="warning" %}
The most suitable merchant for a specific application is automatically selected based on priority. A merchant cannot be replaced if it has already been used in the application.
{% endhint %}

## Proxy Settings (use only if necessary)

In this section, specify a particular IP address if there is no access to the merchant from a regular IP address.

<figure><img src="../../../.gitbook/assets/image (3)_eng.png" alt=""><figcaption></figcaption></figure>

* **IP Address** — the address of the proxy server
* **Port** — the port of the proxy server
* **Login** — your login for accessing the proxy server
* **Password** — your password for accessing the proxy server
* **Disable Proxy Tunnel** — disable this option when the above fields are filled out:\
  • **No**\
  • **Yes**

## **Special Options**

### Connecting Multiple Merchants

{% hint style="success" %}
Starting from version 2.6, there is an option to switch merchants if it fails to obtain payment details for any reason (errors on the service side, authorization errors in the module, lack of available details from the merchant, etc.).
{% endhint %}

The following options are available (in the "**Exchange Settings**" -> "**Basic Settings**"):

{% hint style="info" %}
If you want to continue using the logic from version 2.5, select the option "**Connect Merchant**".
{% endhint %}

<figure><img src="../../../.gitbook/assets/image (459)_eng.png" alt=""><figcaption></figcaption></figure>

**Action if the merchant fails**:

* **Connect Merchant** — after an unsuccessful attempt to obtain details, the application will remain in the status "**New Application**", and instead of the shortcode **\[to_account]**, the text from the field "**Error Message if Account Not Specified**" will be displayed (if merchant details should be shown in the application).

<figure><img src="../../../.gitbook/assets/image (1639)_eng.png" alt="" width="485"><figcaption></figcaption></figure>

Or (starting from version 2.6), there is an option to change the text on the button leading to the merchant's payment page if, for some reason, the merchant (Bitconce Link, Firekassa Link, etc.) could not provide payment details **in the form of a payment page** (the text field for the button when an error occurs is located in the settings of the used merchant module).

<div><figure><img src="../../../.gitbook/assets/image (1642)_eng.png" alt=""><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/image (1643)_eng.png" alt="" width="563"><figcaption></figcaption></figure></div>

* **Transfer application to merchant error** — after an unsuccessful attempt to obtain details, the application will switch to the status "**Merchant Error**".
* **Try to connect another merchant** — attempts will be made to obtain details from other merchants connected in this exchange direction (according to the priority specified in the settings of each module).

{% hint style="warning" %}
If the merchant module settings include the option "**Merchant Error Status**":

<img src="../../../.gitbook/assets/image (2067)_eng.png" alt="" data-size="original">

You can further configure it (this option allows you to automatically re-request details from the merchant if they were not obtained when creating the application):

*   **Error Status** — the selected action from the option "**Action if the Merchant Fails**" (in the "**Exchange Settings**" -> "**Basic Settings**").\

    <figure><img src="../../../.gitbook/assets/image (2068)_eng.png" alt=""><figcaption></figcaption></figure>
* **Waiting for details from the merchant** — the application will switch to the status "**Waiting for Merchant Details**" if the merchant cannot immediately provide details. The application will revert to the status "**New Application**" once the details are obtained upon re-request.
{% endhint %}

{% hint style="warning" %}
If only one merchant is connected in the exchange direction and the option "**Try to Connect Another Merchant**" is selected with a filled template for the field "**Error Message if Account Not Specified**", the application will remain in the status "**New Application**", and instead of the shortcode **\[to_account]**, the text from the field "**Error Message if Account Not Specified**" will be displayed <mark style="background-color:yellow;">(if merchant details should be shown in the application)</mark> or a button with the error text will be displayed to redirect to the payment page <mark style="background-color:yellow;">(if payment details are provided by the merchant on their own payment page)</mark>.
{% endhint %}

* **Show QR Code on Payment Page** — display a QR code when proceeding to payment on the application page:\
  • **No**\
  • **Yes**
* **Custom Status Settings that Can Be Accepted** — a list of application statuses that the merchant will work with when receiving payment notifications from the payment system.

{% hint style="warning" %}
Do not use the option "**Custom Status Settings that Can Be Accepted**" unless necessary!

If no options are selected, the merchant will work with default statuses. If statuses are selected from the list, the merchant will work **only** with the selected statuses.
{% endhint %}

* **Assign an error status to the application in case of API error** — when there is an error response from the merchant, assign the application an error status:\
  • **No**\
  • **Yes**

{% hint style="info" %}
Starting from version 2.6, there is an option to change the text on the button leading to the merchant's payment page if, for some reason, the merchant (Bitconce Link, Firekassa Link, etc.) could not provide payment details.

![](<../../../.gitbook/assets/image (1642)_eng.png>)![](<../../../.gitbook/assets/image (1643)_eng.png>)
{% endhint %}

[^1]: Please specify a unique name for each copy in the "Title" field for easier subsequent configuration.