# Applications Section

The "Applications" section in the admin panel is designed for managing currency purchase and sale requests. In this section, you can view and manage all the requests created by customers on your website.

For each request, you can see customer information such as their name, email, phone number, cryptocurrency name, exchange amount, exchange rate, and other details. You can also change the status of the request, approve or decline it, and send comments to the customer that will be displayed in the request.

![Request Window](../../.gitbook/assets/image (1611)_eng.png)

Let’s take a closer look at the parameters of a specific request.

![Request Details](../../.gitbook/assets/image (1612)_eng.png)

Data above the request window:

* **Checkbox** — check this box if you want to change the status of a specific request (you can also select multiple requests at once) or delete it.

You can also add the customer's details from the request to a blacklist by selecting "Add to Blacklist" — after this, all of the customer's details (email, account/card/wallet number from "Giving" and/or "Receiving," IP address, Skype) will be added to the "Blacklist" section.

<div>
  <figure><img src="../../.gitbook/assets/image (1619)_eng.png" alt="" width="425"><figcaption></figcaption></figure>
  <figure><img src="../../.gitbook/assets/image (1621)_eng.png" alt="" width="381"><figcaption></figcaption></figure>
</div>

* **Request ID** — an identifier assigned to the request automatically by the script.

{% hint style="info" %}
You can change the initial ID by activating the "**Set Initial Request ID**" module in the "**Modules**" section (after changing the initial ID, subsequent requests will be numbered starting from the specified number).

![](../../.gitbook/assets/image (1613)_eng.png)
{% endhint %}

* **Language Flag** — the language version of the site where the customer created the request.
* **Country Code** — the customer's country (determined by their IP address) who made the request. If "N/A" is displayed instead of a code, it means the customer's country could not be determined by their IP address (this can occur when the customer is using [IPv6](https://ru.wikipedia.org/wiki/IPv6)).

![Country Code](../../.gitbook/assets/image (1614)_eng.png)

* **Customer Name** — the nickname chosen by the customer during registration on the site.

Various notifications for the operator may also appear above the request window:

![Notifications](../../.gitbook/assets/image (549)_eng.png)
![Notifications](../../.gitbook/assets/image (548)_eng.png)
![Notifications](../../.gitbook/assets/image (551)_eng.png)

Below the request window, you will find various filters and buttons:

![Filters and Buttons](../../.gitbook/assets/image (552)_eng.png)

* **Info** — clicking this button reveals additional information about the request.

![Additional Info](../../.gitbook/assets/image (553)_eng.png)

* **Similar** — the general list of requests will be filtered to display only those requests that have the same email, Skype, and phone number as the request under which the button was clicked (client filtering).
* **By "Giving" Account** — only requests with the same "Giving" account as the request under which the button was clicked will be filtered and displayed.
* **By "Receiving" Account** — only requests with the same "Receiving" account as the request under which the button was clicked will be filtered and displayed.
* **By Email** — only requests with the same email as the request under which the button was clicked will be filtered and displayed.
* **By IP** — only requests with the same IP address as the request under which the button was clicked will be filtered and displayed.
* **Edit** — manual editing of the request parameters.

![Edit Request](../../.gitbook/assets/image (554)_eng.png)

* **Recalculate Amount** — the amount for the request will be recalculated (relevant if the customer paid a lesser amount than specified in the request and automatic amount recalculation is not used).
* **Recalculate Rate** — the exchange rate for the request will be recalculated (relevant if automatic exchange rate recalculation is not used).
* **Transfer** — in requests for exchange direction with the auto-payment module enabled and payment by button, a button will appear for manually triggering the connected auto-payment.

![Transfer Button](../../.gitbook/assets/image (1615)_eng.png)

When a merchant is connected for receiving payments, the request will display the merchant's details through which the customer makes the payment, the purpose tag, the merchant transaction ID (for cryptocurrency exchanges), and the actual payment amount (the amount transferred by the customer).

![Merchant Details](../../.gitbook/assets/image (1616)_eng.png)

When auto-payment is enabled, the request will display the auto-payment transaction ID (for cryptocurrency exchanges), the TXID of the payment (for verifying the payment through a blockchain explorer, e.g., [Blockchair](https://blockchair.com/)), and the actual payment amount (the amount transferred to the customer).

![Auto-Payment Details](../../.gitbook/assets/image (1618)_eng.png)

When [AML verification](https://premium.gitbook.io/main/osnovnye-nastroiki/proverka-aml) is enabled for cryptocurrency exchanges, the request will display the likelihood of receiving "dirty" currency and a "**Check**" button for manually initiating the verification.

![AML Verification](../../.gitbook/assets/image (1617)_eng.png)

Let’s look at other parameters of the request:

![Request Parameters](../../.gitbook/assets/image (542)_eng.png)
![Request Parameters](../../.gitbook/assets/image (543)_eng.png)

* **Rate** — the rate at the time the request was created.
* The action window appears when using the paid [Trading Actions module](https://premium.gitbook.io/main/osnovnye-nastroiki/modul-torgovye-deistviya) and is intended for initiating trading actions based on the request.

![Action Window](../../.gitbook/assets/image (547)_eng.png)

* **Creation Date** — the date and time the request was created.
* **Modification Date** — the date and time of any changes made to the request (if applicable).

![Modification Date](../../.gitbook/assets/image (544)_eng.png)

* **Giving** — the currency the customer is giving.
* **Amount (with fees)** — the amount considering the [exchange point fees](https://premium.gitbook.io/main/osnovnye-nastroiki/valyuty-i-napravleniya/sozdanie-novogo-napravleniya-obmena#vkladka-komissii-obmennogo-punkta) (if fees are added).
* **Amount (with fees)** — the amount considering both the exchange point fees and the [payment system fees](https://premium.gitbook.io/main/osnovnye-nastroiki/valyuty-i-napravleniya/sozdanie-novogo-napravleniya-obmena#vkladka-komissii-platezhnykh-sistem) (if fees are added).

![Giving Details](../../.gitbook/assets/image (545)_eng.png)

* **Receiving** — the currency the customer is receiving.
* **Amount (with fees)** — the amount considering the [exchange point fees](https://premium.gitbook.io/main/osnovnye-nastroiki/valyuty-i-napravleniya/sozdanie-novogo-napravleniya-obmena#vkladka-komissii-obmennogo-punkta) (if fees are added).
* **Amount (with fees)** — the amount considering both the exchange point fees and the [payment system fees](https://premium.gitbook.io/main/osnovnye-nastroiki/valyuty-i-napravleniya/sozdanie-novogo-napravleniya-obmena#vkladka-komissii-platezhnykh-sistem) (if fees are added).
* **To Account** — the account specified by the customer when creating the request.

![Receiving Details](../../.gitbook/assets/image (546)_eng.png)

* **Email** — the customer's email provided during the request creation.
* **IP Address** — the customer's IP address.
* **User Agent** — the string that the customer's browser sends to the server when requesting a web page, containing information about their operating system, browser and its version, as well as other data such as device type and language. The web server uses this information to provide an optimized version of the web page for the customer's device and browser.