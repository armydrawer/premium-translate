### Section: "Requests"

The "Requests" section in the admin panel is designed for managing purchase and sale requests for currency exchange. In this section, you can view and manage all the requests submitted by clients on your website.

For each request, you can review client information such as their name, email, phone number, cryptocurrency name, exchange amount, exchange rate, and other details. You can also update the request status, reject or approve it, and send a comment to the client, which will be displayed in the request.

<figure><img src="../../.gitbook/assets/image (1611).png" alt=""><figcaption></figcaption></figure>

Let’s take a closer look at the parameters of a specific request.

<figure><img src="../../.gitbook/assets/image (1612).png" alt=""><figcaption></figcaption></figure>

#### Information Above the Request Window:

* **Checkbox** — Use this to select a specific request if you want to change its status (you can also select multiple requests at once) or delete it.

You can also add the client’s details from the request to the blacklist by selecting the "Add to Blacklist" option. This will add all the client’s details (email, account/card/wallet number from the "Send" and/or "Receive" fields, IP address, Skype) to the "Blacklist" section.

<div><figure><img src="../../.gitbook/assets/image (1619).png" alt="" width="425"><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/image (1621).png" alt="" width="381"><figcaption></figcaption></figure></div>

* **Request ID** — A unique identifier automatically assigned to the request by the system.

{% hint style="info" %}
You can modify the starting ID by enabling the "**Set Initial Request ID**" module in the "**Modules**" section. After changing the initial ID, all subsequent requests will start from the specified number.

![](<../../.gitbook/assets/image (1613).png>)
{% endhint %}

* **Country Flag Icon** — Indicates the language version of the website where the client created the request.
* **Country Code** — The client’s country, determined by their IP address. If "N/A" is displayed instead of a country code, it means the client’s country could not be identified via their IP address (this may occur when the client uses [IPv6](https://en.wikipedia.org/wiki/IPv6)).

<figure><img src="../../.gitbook/assets/image (1614).png" alt="" width="396"><figcaption></figcaption></figure>

* **Client Name** — The nickname chosen by the client during registration on the website.

Notifications for the operator may also appear above the request window:

<figure><img src="../../.gitbook/assets/image (549).png" alt="" width="404"><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (548).png" alt="" width="323"><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (551).png" alt="" width="400"><figcaption></figcaption></figure>

#### Filters and Buttons Below the Request Window:

<figure><img src="../../.gitbook/assets/image (552).png" alt=""><figcaption></figcaption></figure>

* **Info** — Clicking this button reveals additional details about the request.

<figure><img src="../../.gitbook/assets/image (553).png" alt="" width="563"><figcaption></figcaption></figure>

* **Similar** — Filters and displays only the requests with the same email, Skype, or phone number as the selected request (filtering by client).
* **By "Send" Account** — Filters and displays only the requests with the same "Send" account as the selected request.
* **By "Receive" Account** — Filters and displays only the requests with the same "Receive" account as the selected request.
* **By Email** — Filters and displays only the requests with the same email as the selected request.
* **By IP** — Filters and displays only the requests with the same IP address as the selected request.
* **Edit** — Allows manual editing of the request parameters.

<figure><img src="../../.gitbook/assets/image (554).png" alt="" width="355"><figcaption></figcaption></figure>

* **Recalculate Amount** — Recalculates the amount for the request (useful if the client paid less than the specified amount and automatic recalculation is not enabled).
* **Recalculate Rate** — Recalculates the exchange rate for the request (useful if automatic rate recalculation is not enabled).
* **Transfer** — For requests involving an exchange direction with an auto-payout module enabled, this button allows manual initiation of the auto-payout.

<figure><img src="../../.gitbook/assets/image (1615).png" alt="" width="563"><figcaption></figcaption></figure>

If a merchant is connected for payment processing, the request will display the merchant’s payment details, payment tag, merchant transaction ID (for cryptocurrency exchanges), and the actual payment amount (the amount transferred by the client).

<figure><img src="../../.gitbook/assets/image (1616).png" alt="" width="411"><figcaption></figcaption></figure>

If auto-payout is enabled, the request will display the auto-payout transaction ID (for cryptocurrency exchanges), the payout TXID (for verifying the payment via a blockchain explorer, e.g., [Blockchair](https://blockchair.com/)), and the actual payout amount (the amount transferred to the client).

<figure><img src="../../.gitbook/assets/image (1618).png" alt="" width="469"><figcaption></figcaption></figure>

If [AML verification](https://premium.gitbook.io/main/osnovnye-nastroiki/proverka-aml) is enabled for cryptocurrency exchanges, the request will display the likelihood of receiving "tainted" currency and a "**Check**" button for manually initiating the verification.

<figure><img src="../../.gitbook/assets/image (1617).png" alt="" width="450"><figcaption></figcaption></figure>

#### Additional Request Parameters:

<figure><img src="../../.gitbook/assets/image (542).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (543).png" alt=""><figcaption></figcaption></figure>

* **Rate** — The exchange rate at the time the request was created.
* **Action Window** — Available when using the paid [“Trading Actions” module](https://premium.gitbook.io/main/osnovnye-nastroiki/modul-torgovye-deistviya), this is used to initiate trading actions for the request.

<figure><img src="../../.gitbook/assets/image (547).png" alt="" width="221"><figcaption></figcaption></figure>

* **Creation Date** — The date and time the request was created.
* **Modification Date** — The date and time any changes were made to the request (if applicable).

<figure><img src="../../.gitbook/assets/image (544).png" alt=""><figcaption></figcaption></figure>

* **Send** — The currency the client is sending.
* **Amount (with additional fees)** — The amount including [exchange service fees](https://premium.gitbook.io/main/osnovnye-nastroiki/valyuty-i-napravleniya/sozdanie-novogo-napravleniya-obmena#vkladka-komissii-obmennogo-punkta) (if applicable).
* **Amount (with additional fees)** — The amount including both exchange service fees and [payment system fees](https://premium.gitbook.io/main/osnovnye-nastroiki/valyuty-i-napravleniya/sozdanie-novogo-napravleniya-obmena#vkladka-komissii-platezhnykh-sistem) (if applicable).

<figure><img src="../../.gitbook/assets/image (545).png" alt=""><figcaption></figcaption></figure>

* **Receive** — The currency the client is receiving.
* **Amount (with additional fees)** — The amount including [exchange service fees](https://premium.gitbook.io/main/osnovnye-nastroiki/valyuty-i-napravleniya/sozdanie-novogo-napravleniya-obmena#vkladka-komissii-obmennogo-punkta) (if applicable).
* **Amount (with additional fees)** — The amount including both exchange service fees and [payment system fees](https://premium.gitbook.io/main/osnovnye-nastroiki/valyuty-i-napravleniya/sozdanie-novogo-napravleniya-obmena#vkladka-komissii-platezhnykh-sistem) (if applicable).
* **To Account** — The account specified by the client when creating the request.

<figure><img src="../../.gitbook/assets/image (546).png" alt=""><figcaption></figcaption></figure>

* **Email** — The client’s email address provided during request creation.
* **IP Address** — The client’s IP address.
* **User Agent** — A string sent by the client’s browser to the server when requesting a web page. It contains information about the client’s operating system, browser, browser version, and other details such as device type and language. The web server uses this information to deliver an optimized version of the web page for the client’s device and browser.