# Merchant Diagnostics

## Module Settings

If an error occurs immediately after clicking the "**Proceed to Payment**" button, please follow these steps:

* Ensure that a payment note is set in the merchant settings under "**Merchants → Merchants**." For some payment systems, such as Yandex.Money and Privat24, the payment note is a mandatory parameter. Typically, the payment note looks like this: **`Request [exchange_id]`.**

<figure><img src="../../../.gitbook/assets/image (902)_eng.png" alt=""><figcaption></figcaption></figure>

* In the merchant settings under "**Merchants → Merchants**," enable the "**Debug Mode**" option and try to proceed to payment again. The error message obtained in the "**Merchants**" → "**Merchant Logs**" section will indicate the existing problem.

<figure><img src="../../../.gitbook/assets/image (1232)_eng.png" alt=""><figcaption></figcaption></figure>

In the website control panel under "**Modules → Modules**," activate the module "**!Do not activate unless necessary! Merchant Logs**."

{% hint style="warning" %}
After testing, be sure to disable the module.
{% endhint %}

Create a test request and make a payment for it. Then, in the "**Merchants → Merchant Logs**" section, find the log for the test request from the payment system you used to make the payment.

<figure><img src="../../../.gitbook/assets/image (1106)_eng.png" alt=""><figcaption></figcaption></figure>

If the **log was recorded** after payment but the request status did not change, please take the following actions:

* Re-enter the merchant settings in the "**Merchants → Merchants**" section.
* Check that the amount received in the wallet matches or exceeds the amount specified in the test request.
* For merchants like Yandex.Money, Privat24 (and other merchants that charge a fee from the exchanger for incoming payments), you need to enable the "**Non-standard Merchant Fee**" option in the merchant settings under "**Merchants → Merchants**," and also in the specific exchange direction settings under the "**Payment System Fees**" tab, check the box for "**non-standard fee**" and specify the percentage of the payment system's fee.

<figure><img src="../../../.gitbook/assets/image (978)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

* For some merchants, it is necessary to configure a [task scheduler (Cron)](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-sozdat-zadanie-cron-na-servere) that checks the status of the request after the user makes a payment. Try opening the Cron link in your browser. If the request status changes when you access the link, it means that either the task scheduler is not set up or it is configured incorrectly and does not trigger automatically. Contact your hosting provider's technical support for assistance in setting up the task scheduler.
* If the log shows an error indicating that the server's IP address is not in the whitelist, contact the merchant's technical support to request that this IP address be added, and then re-submit the request.

<figure><img src="../../../.gitbook/assets/image (1268)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

If the **log was not recorded** after payment, please check the following settings:

* If the "**Allowed IP Addresses**" option is used for the merchant's status file, ensure that the current IP addresses are set in the merchant settings under "**Merchants → Merchants**." Remove IP addresses during testing.

<figure><img src="../../../.gitbook/assets/image (958)_eng.png" alt=""><figcaption></figcaption></figure>

* The payment system settings must include the correct STATUS/RESULT URL, which can be found in the merchant settings under "**Merchants → Merchants**" at the bottom of the merchant settings page.

<figure><img src="../../../.gitbook/assets/image (1014)_eng.png" alt=""><figcaption></figcaption></figure>

If the "**Hash for Status/Result URL**" option was not previously used and you later added a hash in the specified field, ensure that the payment system settings include the correct address considering the specified hash. Make sure that the STATUS/RESULT URL on the payment system side is specified with **http** or **https** depending on the type of connection on your site.

<figure><img src="../../../.gitbook/assets/image (894)_eng.png" alt=""><figcaption></figcaption></figure>

* Ensure that the Firewall on the server, or if the site is connected to a CDN service like Cloudflare, is not blocking the payment system's access to the STATUS/RESULT URL merchant status file.