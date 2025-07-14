# Merchant Diagnostics

Module Settings

If an error occurs immediately after clicking the "**Proceed to Payment**" button, please follow these steps:

* Make sure that a payment note is specified in the merchant settings under "**Merchants → Merchants**." For some payment systems, such as Yandex.Money and Privat24, the payment note is a required parameter. Typically, the payment note looks like this: **`Order [exchange_id]`.**

<figure><img src="../../../.gitbook/assets/image (902).png" alt=""><figcaption></figcaption></figure>

* In the merchant settings under "**Merchants → Merchants**," enable the "**Debug Mode**" option and try proceeding to payment again. The error message generated can be found under "**Merchants → Merchant Logs**" and will indicate the nature of the problem.

<figure><img src="../../../.gitbook/assets/image (1232).png" alt=""><figcaption></figcaption></figure>

In the website control panel, go to "**Modules → Modules**" and activate the module "**!Activate only if necessary! Merchant Logs**."

{% hint style="warning" %}
Be sure to disable this module after testing is complete.
{% endhint %}

Create a test order and complete the payment. Then, in the "**Merchants → Merchant Logs**" section, locate the log entry for the test order from the payment system you used.

<figure><img src="../../../.gitbook/assets/image (1106).png" alt=""><figcaption></figcaption></figure>

If the **log was recorded** after payment but the order status did not update, take the following actions:

* Re-enter the merchant settings under "**Merchants → Merchants**."
* Verify that the amount received in the wallet matches or exceeds the amount specified in the test order.
* For merchants like Yandex.Money, Privat24, and others that charge a commission on incoming payments, enable the "**Non-standard Merchant Commission**" option in the merchant settings under "**Merchants → Merchants**." Also, in the specific exchange direction settings under the "**Payment System Commissions**" tab, check the "**Non-standard commission**" box for the "Giving" currency and specify the payment system’s commission percentage.

Here is a natural, fluent English translation of the provided text:

---

* For some merchants, it is necessary to set up a [task scheduler (Cron)](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-sozdat-zadanie-cron-na-servere) that checks the status of the order after the user’s payment. Try opening the Cron URL in your browser. If the order status changes when you open the link, it means that either the task scheduler is not set up or it is configured incorrectly and does not run automatically. Please contact your hosting provider’s technical support for help with configuring the task scheduler.

* If the log shows an error stating that the server’s IP address is not whitelisted, contact the merchant’s technical support and ask them to add this IP address. After that, try processing the order again.

<figure><img src="../../../.gitbook/assets/image (1268).png" alt="" width="563"><figcaption></figcaption></figure>

If the **log was not recorded** after payment, please check the following settings:

* If the “**Allowed IP Addresses**” option is enabled for the merchant’s status file, make sure that the current IP addresses are specified in the merchant settings under "**Merchants** → **Merchants**." Remove IP addresses during testing.

<figure><img src="../../../.gitbook/assets/image (958).png" alt=""><figcaption></figcaption></figure>

* The payment system settings must include the correct STATUS/RESULT URL, which can be found at the bottom of the merchant settings page under "**Merchants** → **Merchants**."

<figure><img src="../../../.gitbook/assets/image (1014).png" alt=""><figcaption></figcaption></figure>

If you did not previously use the “**Hash for Status/Result URL**” option but later added a hash in this field, make sure that the payment system settings include the updated URL with the hash. Also, verify that the STATUS/RESULT URL in the payment system uses **http** or **https** according to the connection type on your website.

<figure><img src="../../../.gitbook/assets/image (894).png" alt=""><figcaption></figcaption></figure>

* Make sure that the server firewall or, if your site uses a CDN service like Cloudflare, it is not blocking the payment system’s requests to the merchant’s STATUS/RESULT URL.

---

Let me know if you need any adjustments or further help!