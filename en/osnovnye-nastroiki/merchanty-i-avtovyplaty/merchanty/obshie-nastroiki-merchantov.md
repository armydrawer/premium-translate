# General Merchant Settings

Most of the settings described in this section are used across all developed merchant modules. Some merchants have specific parameters, which will be covered directly in the setup instructions for those particular merchants.

## Module Settings

Since each merchant has their own API for authorization, the fields in this section may vary. Please enter the authorization details provided by the merchant according to the field names.

{% tabs %}
{% tab title="Option 1" %}
<figure><img src="../../../.gitbook/assets/изображение (125).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Option 2" %}
<figure><img src="../../../.gitbook/assets/изображение (8).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Option 3" %}
<figure><img src="../../../.gitbook/assets/изображение (10).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Option 4" %}
<figure><img src="../../../.gitbook/assets/изображение (20).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Option 5" %}
<figure><img src="../../../.gitbook/assets/изображение (138).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Option 6" %}
<figure><img src="../../../.gitbook/assets/изображение (120).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

## Settings

{% hint style="warning" %}
Please note that when using certain merchant modules, you need to create a [separate copy of the merchant module](#user-content-fn-1)[^1] <mark style="color:red;">**for each fiat currency/cryptocurrency/cryptocurrency network**</mark>. In each copy, you must select or specify the corresponding option (this could be a field or a dropdown labeled "**Network**", "**Payment Method**", or "**Transaction Type**"), and then connect that module copy on the "**Merchants and Payouts**" tab within the exchange direction settings where the "**Give**" currency matches the specified currency.
{% endhint %}

{% hint style="danger" %}
If the merchant module settings include a field labeled "**Payment Note**," be sure to fill it with the text **`Order ID: [exchange_id]`** or simply **`[exchange_id]`**.

This is required to link the order to its transaction on the merchant’s side — without this shortcode, the order status will not update.

![](<../../../.gitbook/assets/image (1508).png>)
{% endhint %}

Below is the section where you enter the general settings for the merchant’s operation.

<figure><img src="../../../.gitbook/assets/изображение (174).png" alt=""><figcaption></figcaption></figure>

Here is a natural, fluent English translation of the provided text:

---

* **Payment Instructions for the User** – specify the payment instructions that will be shown to the user on the page with the "**Proceed to Payment**" button.

{% hint style="warning" %}
To display the payment details received from the merchant directly within the order, use the shortcode **\[to_account]** in the "**Payment Instructions for the User**" field when the merchant is connected in the exchange direction.  
![](<../../../.gitbook/assets/image (1263).png>)

A suitable example text for the "**Payment Instructions for the User**" field:

{% code overflow="wrap" %}
```
<p>Please transfer <strong>[copytext][sum1c][/copytext][currency_code_give] [psys_give]</strong></p>
<p>To the address: [breakword]<strong>[copytext][to_account][/copytext], account belongs to [dest_tag]</strong>[/breakword]</p>
<p>[qr_code size="200"][to_account][/qr_code]</p>
<p><strong>Attention!</strong> The address is valid for a limited time only — do not send funds after the order expires, as this will result in loss of funds!</p>
<p>Time left to complete the payment:</p>
[js_timer][bid_delete_time][/js_timer]
The system will automatically process the payment as soon as it appears on the network.
```
{% endcode %}

The shortcode \[breakword] here correctly breaks up a long wallet number (30+ characters) such as a Monero (XMR) address.

Of course, you can customize the above instructions as you see fit.
{% endhint %}

* **Payment Note** – if this field appears in the merchant module settings, it is <mark style="color:red;">**mandatory**</mark> to fill it out. This note will be sent to the merchant. A correct payment note looks like this: **`Order [exchange_id]`**
* **Payment Amount Tolerance** – if needed, specify a tolerance (either an absolute amount in the payment currency or a percentage of the order amount). In this case, the merchant will accept payments from the user within the specified tolerance (downward).

{% hint style="info" %}
**Example 1:**  
A tolerance of 0.5 is set. The user should pay 50 USDT but accidentally pays 49.9 USDT. The merchant will accept this payment because the shortfall of 0.1 USDT is within the allowed tolerance of 0.5.
{% endhint %}

---

If you want, I can also help you adapt or polish the text further!

**Example 2:**  
The allowed margin of error is 1.5%. The user is supposed to pay 1000 DOGE but mistakenly pays 990 DOGE. When the merchant checks the payment, it will be accepted because the underpayment of 10 DOGE falls within the allowed margin of 1.5% (1000 × 1.5% = 15 DOGE).

---

* **Daily limit for the merchant** — if needed, set a daily limit on the amount the merchant can receive. The merchant will not be able to accept payments exceeding this limit. The limit should be specified in the currency you plan to accept.

{% hint style="warning" %}  
If you plan to use options for setting limits and/or minimum/maximum payout amounts, and you use a single merchant module to accept multiple currencies, then **you must** create separate copies of the module for each currency.  
{% endhint %}

* **Monthly limit for the merchant** — if needed, set a monthly limit on the amount the merchant can receive. The merchant will not be able to accept payments exceeding this limit.  
* **Minimum payment amount per request** — if needed, set a minimum payment amount for each request. The merchant will not accept payments below this limit.  
* **Maximum payment amount per request** — if needed, set a maximum payment amount for each request. The merchant will not accept payments above this limit.  
* **Daily request limit (number) for the merchant** — the maximum number of requests that can be created within one day.  
* **Hide the "Cancel Request" button:**  
  • **Yes** — hide the button on the request page for the client  
  • **No** — show the button  
* **Payment amount shown to the user** — the amount displayed to the user when creating a request:  
  • **Amount to send (additional fee included)**  
  • **Amount to send (including additional fee and payment system commission)**  
  • **Amount reserved**  
  • **Amount to send**  
* **Expected amount to be credited** — the amount expected to be credited to the merchant’s account:  
  • **Amount to send (additional fee included)**  
  • **Amount to send (including additional fee and payment system commission)**  
  • **Amount reserved**  
  • **Amount to send**

{% hint style="warning" %}
If the merchant charges a fee on incoming payments, it is important to select the **correct type of expected credited amount** to ensure the module works properly and the order status changes to "**Paid**" when funds are received from the customer.

To do this, with the merchant direction enabled, create an order but do not pay it yet. Then open the order details by clicking the "**Info**" button in the "**Orders**" section. Select the amount type whose value matches one of the amounts that will be credited to the merchant’s account after the fee is deducted.

![](<../../../.gitbook/assets/image (2013).png>)

Often, this amount type is "**Reserve Amount**" in the merchant module settings — check this first. Choose the appropriate option, save the settings, and then pay the order. If after full payment the order status changes to "**Paid**," the settings are correct.

![](<../../../.gitbook/assets/image (2014).png>)
{% endhint %}

* **Allowed IP addresses (one per line)** — specify the IP address(es) of the payment system that will be allowed to access the merchant’s status URL. The payment system sends payment information to this URL. Setting allowed IP addresses enhances security when working with the merchant.

{% hint style="info" %}
You can find out the IP address(es) from which the payment system sends payment information to the status URL by contacting the payment system’s technical support.
{% endhint %}

* **Cron file hash** — specify a hash that will be appended to the Cron job URL (a random string of 20–40 Latin letters and digits).

{% hint style="danger" %}
Don’t forget to create a Cron job on your server to check payments — [**setup instructions**](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-sozdat-zadanie-cron-na-servere)
{% endhint %}

Here is a natural, fluent English translation of the provided text:

---

* **Hash for Status/Result URL** — specify a hash that will be appended to the merchant’s status URL. The payment system sends payment information to this URL. By adding a hash, the status URL becomes unique, which enhances security when working with the merchant. We recommend using a hash 20–50 characters long, containing Latin letters and numbers. Example hash: `ImYkwGsq2fjhuWypiasq2QJzVvCpis8umbxs8umbx`

{% hint style="danger" %}
If the merchant module or auto-payout settings show a line with Status URL/Callback URL but there is no mention of it in the module’s setup instructions, you can ignore this URL (it is handled at the code level without administrator configuration).  
When configuring the merchant on the payment system side, always specify the status address (usually Status URL or Return URL) including the hash you set!
{% endhint %}

* **Debug Mode** — enable this option only during initial setup or if you encounter issues with the merchant. When enabled, an extended merchant log will be recorded under "**Merchants**" -> "**Merchant Logs**":  
  • **No**  
  • **Yes**

## Managing Application Statuses

This section configures how the merchant handles specific rules for transitioning application statuses.

<figure><img src="../../../.gitbook/assets/image (806).png" alt="" width="563"><figcaption></figcaption></figure>

---

Let me know if you need it adapted for a particular audience or style!

* **The account number from which the payment was made does not match the one specified in the application** — if the account numbers don’t match, you can either change the application status or leave it as is:  
  • **Keep the status as "New Application"**  
  • **Change the status to "Under Review"**  
  • **Change the status to "Paid Application"**

* **The payment amount is less than required** — if the user made a payment for less than the amount specified in the application, you can either change the application status or leave it as is:  
  • **Keep the status as "New Application"**  
  • **Change the status to "Under Review"**  
  • **Change the status to "Paid Application"**

* **The payment amount is more than required** — if the user made a payment for more than the amount specified in the application, you can either change the application status or leave it as is:  
  • **Keep the status as "New Application"**  
  • **Change the status to "Under Review"**  
  • **Change the status to "Paid Application"**

* **Priority** — specify a priority from 1 to 10 (where 0 or an empty field means no priority or the last module to be used; from 1 upwards indicates increasing priority of use (0 < 1 < 2 < 3 < ... < n)), if multiple merchant modules are used in the exchange direction.

{% hint style="warning" %}
The most suitable merchant for a specific application is selected automatically based on priority. The merchant cannot be changed once it has been used in the application.
{% endhint %}

## Proxy Settings (use only if necessary)

This section is for specifying a particular IP address if access to the merchant is not possible from the usual IP address.

<figure><img src="../../../.gitbook/assets/изображение (3).png" alt=""><figcaption></figcaption></figure>

* **IP Address** — the proxy server’s IP address  
* **Port** — the proxy server’s port  
* **Login** — your login for accessing the proxy server  
* **Password** — your password for accessing the proxy server  
* **Disable proxy tunnel** — disable this option if the above fields are filled in:  
  • **No**  
  • **Yes**

## **Special Options**

### Connecting Multiple Merchants

Starting from version 2.6, there is an option to switch the merchant if it was not possible to obtain payment details from them for any reason (service-side errors, authorization errors in the module, lack of available merchant details, etc.).

The following options are available (under "**Exchange Settings**" -> "**General Settings**"):

{% hint style="info" %}
If you want to continue using the logic from version 2.5, select "**Connect Merchant**".
{% endhint %}

<figure><img src="../../../.gitbook/assets/image (459).png" alt=""><figcaption></figcaption></figure>

**Action if the merchant fails:**

* **Connect Merchant** — after a failed attempt to get payment details, the request will remain in the "**New Request**" status. Instead of the shortcode **\[to_account]**, the text from the "**Error text if no account specified**" field will be displayed (if merchant details are supposed to appear in the request).

<figure><img src="../../../.gitbook/assets/image (1639).png" alt="" width="485"><figcaption></figcaption></figure>

Alternatively (starting from version 2.6), there is an option to replace the text on the button that links to the merchant’s payment page if, for some reason, the merchant (Bitconce Link, Firekassa Link, etc.) was unable to provide payment details **in the form of a payment page** (the button text for this error is set in the settings of the merchant module being used).

<div><figure><img src="../../../.gitbook/assets/image (1642).png" alt=""><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/image (1643).png" alt="" width="563"><figcaption></figcaption></figure></div>

* **Mark request as merchant error** — after a failed attempt to get payment details, the request status will change to "**Merchant Error**".
* **Try another merchant** — attempts will be made to obtain payment details from other merchants connected to this exchange direction (according to the priority set in each module’s settings).

{% hint style="warning" %}
If the merchant module settings include the "**Merchant error status**" option:

<img src="../../../.gitbook/assets/image (2067).png" alt="" data-size="original">

You can configure it further (this option allows automatic retries to request payment details from the merchant if they were not obtained when the request was created):
{% endhint %}

Here is a natural, fluent English translation of the provided text:

---

* **Error Status** — the selected action from the "**Action if merchant fails**" option will be executed (found under "**Exchange Settings**" -> "**General Settings**").

<figure><img src="../../../.gitbook/assets/image (2068).png" alt=""><figcaption></figcaption></figure>

* **Waiting for merchant details** — the request will move to the status "**Waiting for merchant details**" if the merchant cannot immediately provide the required details. The request will return to the status "**New request**" once the details are received after a repeated query.

{% endhint %}

{% hint style="warning" %}
If only one merchant is connected for the exchange direction and the option "**Try connecting another merchant**" is enabled with a filled-in template for the field "**Error text if account is not specified**," then the request will remain in the "**New request**" status. Instead of the shortcode **\[to_account]**, the text from the "**Error text if account is not specified**" field will be displayed <mark style="background-color:yellow;">(if merchant details are supposed to be shown in the request)</mark>, or a button with the error text will appear to redirect to the payment page <mark style="background-color:yellow;">(if payment details are provided by the merchant on their own payment page)</mark>.
{% endhint %}

* **Show QR code on the payment page** — display a QR code when proceeding to payment on the request page:  
  • **No**  
  • **Yes**

* **Custom status settings that can be accepted** — a list of request statuses that the merchant will recognize when receiving payment notifications from the payment system.

{% hint style="warning" %}
Do not use the "**Custom status settings that can be accepted**" option unless necessary!

If no statuses are selected, the merchant will work with the default statuses. If statuses are selected from the list, the merchant will work **only** with those selected statuses.
{% endhint %}

* **Assign error status to the request in case of API error** — if there is an error response from the merchant, assign the request the error status:  
  • **No**  
  • **Yes**

---

Let me know if you need the formatting adjusted or further clarifications!

Starting from version 2.6, there is an option to customize the text on the button that directs users to the merchant’s payment page, in case the merchant (such as Bitconce Link, Firekassa Link, etc.) is unable to provide payment details for any reason.

![](<../../../.gitbook/assets/image (1642).png>)![](<../../../.gitbook/assets/image (1643).png>)

[^1]: Please specify a unique name for each copy in the "Title" field to make future configuration easier.