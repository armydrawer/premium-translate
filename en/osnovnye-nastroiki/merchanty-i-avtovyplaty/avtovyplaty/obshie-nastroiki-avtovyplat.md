# General Auto-Payment Settings

Most of the settings outlined in this section are used across all developed modules for merchant auto-payments. Some merchants have specific parameters that will be addressed directly in the setup instructions for those merchants.

{% hint style="warning" %}
Please note that a [separate copy of the auto-payment module](#user-content-fn-1)[^1] must be created for each currency, selecting the appropriate currency in that copy. Then, connect this copy on the "**Merchants and Payments**" tab in the exchange direction settings, where the currency in "**Receiving**" will be the selected currency.

![](<../../../.gitbook/assets/image (729).png>)
{% endhint %}

## Module Settings:

Since each merchant for auto-payments has its own API for authorization, the fields in this section may vary. Please enter the authorization data provided by the merchant according to the field names.

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

This section outlines the general settings for the merchant's auto-payment operations.

<figure><img src="../../../.gitbook/assets/image (703).png" alt="" width="563"><figcaption></figcaption></figure>

* **Payment Instructions for Users** — recommendations for clients regarding payments, which will be displayed on the page with the "**Proceed to Payment**" button.

{% hint style="info" %}
Standard text for instructions:\
\
"**Please wait for the funds to arrive in your account."**
{% endhint %}

* **Payment Note** — if this field is present in the auto-payment settings, <mark style="color:red;">**it is mandatory**</mark> to include the text from the shortcode "**Request ID**" (it will appear as \[exchange\_id]). This is necessary to transmit the request ID from the system to the merchant.

<figure><img src="../../../.gitbook/assets/image (704).png" alt=""><figcaption></figcaption></figure>

* **Auto-Payment when the request status is "Paid Request"**:\
  • **No**\
  • **Yes**
* **Auto-Payment when the request status is "Under Review"**:\
  • **No**\
  • **Yes**
* **Button for Manual Payment in the Request** — display a button in the "**Requests**" section for manual payment by the operator\
  • **No**\
  • **Yes**

{% hint style="warning" %}
To use the manual payment button "**Transfer**" in the "**Requests**" section, set "**No**" for the parameters "**Auto-Payment when the request status is 'Paid Request'**" and **"Auto-Payment when the request status is 'Under Review'**."
{% endhint %}

* **Daily Limit for Auto-Payment** — the daily limit for fund disbursement. The merchant will not be able to make payments exceeding this limit. This is specified in the payment currency.
* **Monthly Limit for Auto-Payment** — the monthly limit for fund disbursement. The merchant will not be able to make payments exceeding this limit.
* **Min. Amount for Auto-Payment per Request** — the minimum amount for auto-payment for a single request. The merchant will not be able to make payments for amounts less than this.
* **Max. Amount for Auto-Payment per Request** — the maximum amount for auto-payment for a single request. The merchant will not be able to make payments for amounts greater than this.

{% hint style="warning" %}
Limits are specified in the payment currency. If you are processing multiple currencies with one merchant and want to use limits, you need to create a separate copy of the merchant for each currency.
{% endhint %}

* **Amount to be Transferred for Payment** — the type of amount that will be paid to the user:\
  • **Amount Received (additional fee)**\
  • **Amount Received (with additional fee and payment system fee)**\
  • **Amount for Reserve**\
  • **Discounted Amount**
* **Allowed IP Addresses (one per line)** — specify the IP address(es) of the payment system that are allowed access to the merchant's status URL. The payment system sends payment information to this URL. Specifying allowed IP addresses enhances security when working with the merchant.

{% hint style="info" %}
You can find out the IP address(es) of the payment system that sends payment information to the status URL by contacting the payment system's technical support.
{% endhint %}

* **Cron File Hash** — specify a hash that will complement the Cron job URL (a random set of 20-50 Latin letters and numbers).

{% hint style="danger" %}
Don't forget to create a Cron job on the server to check the payment - [instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-sozdat-zadanie-cron-na-servere) for setup.
{% endhint %}

* **Hash for Status/Result URL** — specify a hash that will complement the merchant's status URL. The payment system sends payment information to this URL. If a hash is specified, the status URL becomes unique, enhancing security when working with the merchant. It is recommended to use a hash of 20-50 characters containing Latin letters and numbers. Example hash: `ImYkwGsq2fjhuWypiasqpis8umbxs8umbx`.

{% hint style="danger" %}
When setting up auto-payment on the payment system side, specify the status address (usually Status URL or Return URL) with the hash already included!
{% endhint %}

* **Debug Mode** — enable this mode only when there are issues with the merchant's auto-payments. When this option is enabled, an extended log of the merchant will be recorded:\
  • **No**\
  • **Yes**
* **Auto-Payment Delay in Hours** — delay for auto-payment if a manual review of the request is needed before auto-payment.

{% hint style="info" %}
For example, to set a delay of 5 minutes, enter 0.08 in the field; for a delay of 25 minutes, enter 0.33.
{% endhint %}

* **For Whom the Delay Applies** — user category if the auto-payment delay function is used:\
  • **for everyone**\
  • **for newcomers**\
  • **for unregistered users**\
  • **for unverified users on the site**
* **API Status Error** — transition to the request status selected from the dropdown list.
* **Priority** — specify a priority [from 1 to 10](#user-content-fn-2)[^2] when using auto-payments if multiple auto-payment modules are used in the exchange direction.

{% hint style="warning" %}
The most suitable auto-payment for a specific request is automatically selected based on priority. An auto-payment cannot be replaced if it has already been used in the request.
{% endhint %}

### Proxy Settings

This section specifies a specific IP address if there is no access to the merchant from a regular IP address.

<figure><img src="../../../.gitbook/assets/изображение (3).png" alt="" width="402"><figcaption></figcaption></figure>

* **IP Address** — address of the proxy server.
* **Port** — port of the proxy server.
* **Login** — your login for accessing the proxy server.
* **Password** — your password for accessing the proxy server.
* **Disable Proxy Tunnel** — disable this option if the above fields are filled out:\
  • **No**\
  • **Yes**

[^1]: Specify a unique name for each copy in the "Title" field for easier subsequent configuration.

[^2]: where:\
    0 or an empty field - no priority or last to execute, from 1 upwards - increasing priority (n>...>3>2>1>0)