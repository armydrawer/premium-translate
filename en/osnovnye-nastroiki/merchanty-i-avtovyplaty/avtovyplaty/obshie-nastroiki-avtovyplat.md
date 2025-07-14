# General Auto-Payout Settings

Most of the settings described in this section are used across all developed auto-payout merchant modules. Some merchants have specific parameters that will be covered directly in the setup instructions for those particular merchants.

{% hint style="warning" %}
Please note that for each currency, you need to create a [separate copy of the auto-payout module](#user-content-fn-1)[^1], select the corresponding currency in that copy, and then link this copy on the "**Merchants and Payouts**" tab within the exchange direction settings, where the "**Receiving**" currency will be set to the chosen currency.

![](<../../../.gitbook/assets/image (729).png>)
{% endhint %}

## Module Settings:

Since each auto-payout merchant uses its own API for authorization, the fields in this section may vary. Enter the authorization details provided by the merchant according to the field names.

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

This section contains the general settings for the operation of the auto-payout merchant.

<figure><img src="../../../.gitbook/assets/image (703).png" alt="" width="563"><figcaption></figcaption></figure>

* **Payout Instructions for the User** — guidance for the client regarding the payout process, which will be displayed on the page with the "**Proceed to Payment**" button.

{% hint style="info" %}
Sample instruction text:\
\
"**Please wait for the funds to be credited to your account.**"
{% endhint %}

* **Payment Note** — if this field is present in the auto-payout settings, it is <mark style="color:red;">**mandatory**</mark> to include the text from the shortcode "**Request ID**" (displayed as \[exchange_id]). This is required to pass the request ID from the system to the merchant.

[^1]: Each currency requires its own module copy to ensure proper handling of payouts in that currency.

Here is a natural English translation of the provided text:

---

* **Auto payout when the request status is "Paid request":**  
  • **No**  
  • **Yes**

* **Auto payout when the request status is "Under review":**  
  • **No**  
  • **Yes**

* **Manual payout button in the request** — display a button in the "**Requests**" section to allow the operator to manually process payouts  
  • **No**  
  • **Yes**

{% hint style="warning" %}
To use the manual payout button "**Transfer**" in the "**Requests**" section, you must set "**No**" for both "**Auto payout when the request status is 'Paid request'**" and "**Auto payout when the request status is 'Under review'**".
{% endhint %}

* **Daily auto payout limit** — the maximum total amount that can be paid out per day. The merchant will not be able to make payouts exceeding this limit. The limit is specified in the payout currency.

* **Monthly auto payout limit** — the maximum total amount that can be paid out per month. The merchant will not be able to make payouts exceeding this limit.

* **Minimum auto payout amount per request** — the minimum payout amount allowed for a single request. The merchant cannot make a payout less than this amount.

* **Maximum auto payout amount per request** — the maximum payout amount allowed for a single request. The merchant cannot make a payout exceeding this amount.

{% hint style="warning" %}
Limits are specified in the payout currency. If you process payouts in multiple currencies using a single merchant account and want to apply limits, you need to create a separate copy of the merchant account for each currency.
{% endhint %}

* **Amount to be paid out** — the type of amount that will be paid to the user:  
  • **Amount you receive (excluding additional fees)**  
  • **Amount you receive (including additional fees and payment system commission)**  
  • **Amount reserved**  
  • **Discounted amount**

* **Allowed IP addresses (one per line)** — specify the IP address(es) of the payment system that are allowed to access the merchant’s status URL. The payment system sends payment status information to this URL. Specifying allowed IP addresses enhances the security of working with the merchant.

---

If you need any further adjustments or clarifications, feel free to ask!

Here is a natural, fluent English translation of the provided text:

---

{% hint style="info" %}
You can find out the IP address(es) of the payment system from which it sends payment information to the status URL by contacting the payment system’s technical support.
{% endhint %}

* **Cron File Hash** — specify a hash that will be appended to the Cron job URL (a random string of 20-50 Latin letters and digits).

{% hint style="danger" %}
Don’t forget to create a Cron job on your server to check payments — see the [setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-sozdat-zadanie-cron-na-servere).
{% endhint %}

* **Hash for Status/Result URL** — specify a hash to append to the merchant’s status URL. The payment system sends payment information to this URL. Adding a hash makes the status URL unique, which enhances security when working with the merchant. We recommend using a hash 20-50 characters long, containing Latin letters and digits. Example hash: `ImYkwGsq2fjhuWypiasqpis8umbxs8umbx`

{% hint style="danger" %}
When setting up automatic payouts on the payment system side, always specify the status address (usually the Status URL or Return URL) including the hash!
{% endhint %}

* **Debug Mode** — enable this mode only if you experience issues with merchants using automatic payouts. When enabled, an extended merchant log will be recorded:  
  • **No**  
  • **Yes**

* **Auto Payout Delay (in hours)** — delay automatic payouts if you need to manually review requests before payout.

{% hint style="info" %}
For example, to set a 5-minute delay, enter 0.08; for a 25-minute delay, enter 0.33.
{% endhint %}

* **Delay Applies To** — select the user category for which the payout delay applies (if using the delay feature):  
  • **All users**  
  • **New users**  
  • **Unregistered users**  
  • **Unverified users on the site**

* **API Status Error** — select the status to assign to the request in case of an API error from the dropdown menu.

* **Priority** — specify the priority [from 1 to 10](#user-content-fn-2)[^2] when using automatic payouts if multiple payout modules are used for the exchange direction.

---

If you need the text adapted for a specific audience or style, just let me know!

{% hint style="warning" %}
The most suitable auto-payout for a specific request is selected automatically based on priority. Once an auto-payout has been used in a request, it cannot be replaced.
{% endhint %}

### Proxy Settings

In this section, specify a particular IP address if access to the merchant is not possible from a regular IP address.

<figure><img src="../../../.gitbook/assets/изображение (3).png" alt=""><figcaption></figcaption></figure>

* **IP Address** — the proxy server’s IP address  
* **Port** — the proxy server’s port  
* **Login** — your login for accessing the proxy server  
* **Password** — your password for accessing the proxy server  
* **Disable Proxy Tunnel** — disable this option if the fields above are filled in  
  • **No**  
  • **Yes**

[^1]: Enter a unique name for each copy in the "Title" field for easier configuration later.

[^2]: Where:  
 0 or empty — no priority or lowest priority (executed last),  
 1 and up — increasing priority (n > ... > 3 > 2 > 1 > 0)