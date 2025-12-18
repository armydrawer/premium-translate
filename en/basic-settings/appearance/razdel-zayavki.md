# Applications Section

The "Applications" section in the admin panel is designed for managing currency purchase and sale requests. In this section, you can view and manage all requests created by customers on your site.

For each request, you can see customer information such as their name, email, phone number, cryptocurrency name, exchange amount, exchange rate, and other details. You can also change the status of the request, approve or decline it, and send a comment to the customer that will be displayed in the request.

<figure><img src="../../.gitbook/assets/image (1611).png" alt=""><figcaption></figcaption></figure>

Let’s take a closer look at the parameters of a specific request.

<figure><img src="../../.gitbook/assets/image (1612).png" alt=""><figcaption></figcaption></figure>

Data above the request window:

* **Checkbox** — check this box if you want to change the status of a specific request (you can also select multiple requests at once) or delete it.

You can also add the customer's details from the request to the blacklist by selecting "Add to blacklist" — after this, all customer details (email, account/card/wallet number from "Giving" and/or "Receiving," IP address, Skype) will be added to the "Blacklist" section.

<div><figure><img src="../../.gitbook/assets/image (1619).png" alt="" width="425"><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/image (1620) (1).png" alt="" width="381"><figcaption></figcaption></figure></div>

* **Request ID** — the identifier assigned to the request automatically by the script.

{% hint style="info" %}
You can change the initial ID by activating the "**Set Initial Request ID**" module in the "**Modules**" section (after changing the initial ID, subsequent requests will be numbered starting from the specified number).

<img src="../../.gitbook/assets/image (1613).png" alt="" data-size="original">
{% endhint %}

* **Language Flag** — the language version of the site on which the customer created the request.
* **Country Code** — the customer's country (determined by IP address) who made the request. If "N/A" is displayed instead of a country code, it means the customer's country could not be determined by the IP address (this can occur when the customer is using [IPv6](https://ru.wikipedia.org/wiki/IPv6)).

<figure><img src="../../.gitbook/assets/image (1614).png" alt="" width="396"><figcaption></figcaption></figure>

* **Customer Name** — the nickname chosen by the customer during registration on the site.

Various notifications for the operator may also be displayed above the request window:

<figure><img src="../../.gitbook/assets/image (549).png" alt="" width="404"><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (548).png" alt="" width="323"><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (551).png" alt="" width="400"><figcaption></figcaption></figure>

Below the request window, various filters and buttons will be displayed:

<figure><img src="../../.gitbook/assets/image (552).png" alt=""><figcaption></figcaption></figure>

* **Info** — clicking this button reveals additional information about the request.

<figure><img src="../../.gitbook/assets/image (553).png" alt="" width="563"><figcaption></figcaption></figure>

* **Similar** — only requests with the same email, Skype, and phone number as the request under which the button was clicked will be filtered and displayed in the general list of requests (client filtering).
* **By "Giving" Account** — only requests with the same "Giving" account as the request under which the button was clicked will be filtered and displayed.
* **By "Receiving" Account** — only requests with the same "Receiving" account as the request under which the button was clicked will be filtered and displayed.
* **By Email** — only requests with the same email as the request under which the button was clicked will be filtered and displayed.
* **By IP** — only requests with the same IP address as the request under which the button was clicked will be filtered and displayed.
* **Edit** — manual editing of the request parameters.

<figure><img src="../../.gitbook/assets/image (554).png" alt="" width="355"><figcaption></figcaption></figure>

* **Recalculate Amount** — the amount for the request will be recalculated (relevant if the customer paid a lesser amount than specified in the request and automatic amount recalculation is not used) [automatic amount recalculation](https://premium.gitbook.io/main/osnovnye-nastroiki/valyuty-i-napravleniya/sozdanie-novogo-napravleniya-obmena#pereschet-po-summe-oplaty).
* **Recalculate Rate** — the exchange rate for the request will be recalculated (relevant if automatic exchange rate recalculation is not used) [automatic exchange rate recalculation](https://premium.gitbook.io/main/osnovnye-nastroiki/valyuty-i-napravleniya/sozdanie-novogo-napravleniya-obmena#pereschet-po-kursu-obmena).
* **Transfer** — in requests for exchange direction with the connected auto-payment module and payment by button, a button will be displayed for manually triggering the connected auto-payment.

<figure><img src="../../.gitbook/assets/image (1615).png" alt="" width="563"><figcaption></figcaption></figure>

When a merchant is connected, the request will display the merchant's details through which the customer makes the payment, the purpose tag, the merchant transaction ID (when exchanging cryptocurrencies), and the actual payment amount (the amount transferred by the customer).

<figure><img src="../../.gitbook/assets/image (1616).png" alt="" width="411"><figcaption></figcaption></figure>

When auto-payment is connected, the request will display the auto-payment transaction ID (when exchanging cryptocurrencies), the TXID of the payment (for verifying the payment through a blockchain explorer — for example, [Blockchair](https://blockchair.com/)), and the actual payment amount (the amount that was transferred to the customer).

<figure><img src="../../.gitbook/assets/image (1618).png" alt="" width="469"><figcaption></figcaption></figure>

When [AML verification](https://premium.gitbook.io/main/osnovnye-nastroiki/proverka-aml) is connected, the request will display the likelihood of receiving "dirty" currency and a "**Check**" button for manually initiating the verification.

<figure><img src="../../.gitbook/assets/image (1617).png" alt="" width="450"><figcaption></figcaption></figcaption></figure>

Let’s look at other parameters of the request:

<figure><img src="../../.gitbook/assets/image (542).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (543).png" alt=""><figcaption></figcaption></figure>

* **Rate** — the rate at the time the request was created.
* The action window is displayed when using the paid [Trading Actions module](https://premium.gitbook.io/main/osnovnye-nastroiki/modul-torgovye-deistviya) and is intended for initiating trading actions based on the request.

<figure><img src="../../.gitbook/assets/image (547).png" alt="" width="221"><figcaption></figcaption></figure>

* **Creation Date** — the date and time the request was created.
* **Modification Date** — the date and time of any changes made to the request (if applicable).

<figure><img src="../../.gitbook/assets/image (544).png" alt=""><figcaption></figcaption></figure>

* **Giving** — the currency the customer is giving.
* **Amount (with fees)** — the amount considering the [exchange point fees](https://premium.gitbook.io/main/osnovnye-nastroiki/valyuty-i-napravleniya/sozdanie-novogo-napravleniya-obmena#vkladka-komissii-obmennogo-punkta) (if fees are applied).
* **Amount (with fees)** — the amount considering both the exchange point fees and the [payment system fees](https://premium.gitbook.io/main/osnovnye-nastroiki/valyuty-i-napravleniya/sozdanie-novogo-napravleniya-obmena#vkladka-komissii-platezhnykh-sistem) (if fees are applied).

<figure><img src="../../.gitbook/assets/image (545).png" alt=""><figcaption></figcaption></figure>

* **Receiving** — the currency the customer is receiving.
* **Amount (with fees)** — the amount considering the [exchange point fees](https://premium.gitbook.io/main/osnovnye-nastroiki/valyuty-i-napravleniya/sozdanie-novogo-napravleniya-obmena#vkladka-komissii-obmennogo-punkta) (if fees are applied).
* **Amount (with fees)** — the amount considering both the exchange point fees and the [payment system fees](https://premium.gitbook.io/main/osnovnye-nastroiki/valyuty-i-napravleniya/sozdanie-novogo-napravleniya-obmena#vkladka-komissii-platezhnykh-sistem) (if fees are applied).
* **To Account** — the account specified by the customer when creating the request.

<figure><img src="../../.gitbook/assets/image (546).png" alt=""><figcaption></figcaption></figure>

* **Email** — the customer's email provided during the request creation.
* **IP Address** — the customer's IP address.
* **User Agent** — the string that the customer's browser sends to the server when requesting a web page, containing information about their operating system, browser and its version, as well as other data such as device type and language. The web server uses this information to provide an optimized version of the web page for the customer's device and browser.