# "Requests" Section

The "Requests" section in the admin panel is designed for managing currency buy and sell requests. Here, you can view and handle all the requests submitted by clients on your website.

For each request, you can see client details such as their name, email, phone number, cryptocurrency name, exchange amount, currency rate, and other relevant information. You can also change the request status, reject or approve the request, and send comments to the client, which will be visible within the request.

<figure><img src="../../.gitbook/assets/image (1611).png" alt=""><figcaption></figcaption></figure>

Let’s take a closer look at the parameters of a specific request.

<figure><img src="../../.gitbook/assets/image (1612).png" alt=""><figcaption></figcaption></figure>

Information above the request window:

* **Checkbox** — check this box if you want to change the status of a particular request (you can also select multiple requests at once) or delete it.

You can also add the client’s details from the request to the blacklist by selecting "Add to Blacklist." This will add all the client’s details (email, account/card/wallet numbers from the "Giving" and/or "Receiving" fields, IP address, Skype) to the "Blacklist" section.

<div><figure><img src="../../.gitbook/assets/image (1619).png" alt="" width="425"><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/image (1621).png" alt="" width="381"><figcaption></figcaption></figure></div>

* **Request ID** — the unique identifier automatically assigned to the request by the script.

{% hint style="info" %}
You can change the starting ID number by enabling the "**Set Initial Request ID**" module in the "**Modules**" section. After changing the initial ID, all subsequently created requests will be numbered starting from the specified value.

![](<../../.gitbook/assets/image (1613).png>)
{% endhint %}

* **Flag icon** — indicates the language version of the site where the client submitted the request.
* **Country code** — the client’s country (determined by IP address). If "N/A" appears instead of a country code, it means the client’s country could not be identified by IP (this often happens when the client uses [IPv6](https://en.wikipedia.org/wiki/IPv6)).

<figure><img src="../../.gitbook/assets/image (1614).png" alt="" width="396"><figcaption></figcaption></figure>

* **Client name** — the nickname the client chose when registering on the site.

Various notifications for the operator may appear above the request window:

<figure><img src="../../.gitbook/assets/image (549).png" alt="" width="404"><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (548).png" alt="" width="323"><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (551).png" alt="" width="400"><figcaption></figcaption></figure>

Below the request window, different filters and buttons will be displayed:

<figure><img src="../../.gitbook/assets/image (552).png" alt=""><figcaption></figcaption></figure>

* **Info** — clicking this button expands additional information about the request

<figure><img src="../../.gitbook/assets/image (553).png" alt="" width="563"><figcaption></figcaption></figure>

* **Similar** — filters the main request list to show only requests with the same email, Skype, and phone number as the request under which the button was clicked (client-based filtering)
* **By "Giving" Account** — filters to show only requests with the same "Giving" account as the request under which the button was clicked
* **By "Receiving" Account** — filters to show only requests with the same "Receiving" account as the request under which the button was clicked
* **By Email** — filters to show only requests with the same email as the request under which the button was clicked
* **By IP** — filters to show only requests with the same IP address as the request under which the button was clicked
* **Edit** — manually edit the request parameters

<figure><img src="../../.gitbook/assets/image (554).png" alt="" width="355"><figcaption></figcaption></figure>

* **Recalculate Amount** — recalculates the amount for the request (useful if the client paid less than the amount specified in the request and [automatic amount recalculation](https://premium.gitbook.io/main/osnovnye-nastroiki/valyuty-i-napravleniya/sozdanie-novogo-napravleniya-obmena#pereschet-po-summe-oplaty) is not enabled)
* **Recalculate Rate** — recalculates the exchange rate for the request (useful if [automatic exchange rate recalculation](https://premium.gitbook.io/main/osnovnye-nastroiki/valyuty-i-napravleniya/sozdanie-novogo-napravleniya-obmena#pereschet-po-kursu-obmena) is not enabled)
* **Transfer** — for exchange requests with the auto-payout module enabled and payout by button activated, a button will appear to manually trigger the connected auto-payout

<figure><img src="../../.gitbook/assets/image (1615).png" alt="" width="563"><figcaption></figcaption></figure>

When a merchant is connected, the payment details in the order will display the merchant’s information used by the client to make the payment, the purpose tag, the merchant’s transaction ID (for cryptocurrency exchanges), and the actual payment amount (the amount transferred by the client).

<figure><img src="../../.gitbook/assets/image (1616).png" alt="" width="411"><figcaption></figcaption></figure>

When auto-payout is enabled, the order will show the auto-payout transaction ID (for cryptocurrency exchanges), the payout TXID (for verifying the payment via a blockchain explorer such as [Blockchair](https://blockchair.com/)), and the actual payout amount (the amount transferred to the client).

<figure><img src="../../.gitbook/assets/image (1618).png" alt="" width="469"><figcaption></figcaption></figure>

When [AML verification](https://premium.gitbook.io/main/osnovnye-nastroiki/proverka-aml) is enabled during cryptocurrency exchanges, the order will display the probability that the currency is “dirty” along with a "**Check**" button to manually initiate the verification.

<figure><img src="../../.gitbook/assets/image (1617).png" alt="" width="450"><figcaption></figcaption></figure>

Let’s review other order parameters:

<figure><img src="../../.gitbook/assets/image (542).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (543).png" alt=""><figcaption></figcaption></figure>

* **Rate** — the exchange rate at the time the order was created  
* The action panel appears when using the paid [“Trading Actions” module](https://premium.gitbook.io/main/osnovnye-nastroiki/modul-torgovye-deistviya) and is intended to trigger trading actions on the order

<figure><img src="../../.gitbook/assets/image (547).png" alt="" width="221"><figcaption></figcaption></figure>

* **Creation Date** — the date and time when the order was created  
* **Modification Date** — the date and time of any changes made to the order (if applicable)

<figure><img src="../../.gitbook/assets/image (544).png" alt=""><figcaption></figcaption></figure>

* **You Give** — the currency the client is sending  
* **Amount (incl. extra fees)** — the amount including the [exchange point’s fees](https://premium.gitbook.io/main/osnovnye-nastroiki/valyuty-i-napravleniya/sozdanie-novogo-napravleniya-obmena#vkladka-komissii-obmennogo-punkta) (if any fees are applied)  
* **Amount (incl. extra fees)** — the amount including both the exchange point’s fees and the [payment system’s fees](https://premium.gitbook.io/main/osnovnye-nastroiki/valyuty-i-napravleniya/sozdanie-novogo-napravleniya-obmena#vkladka-komissii-platezhnykh-sistem) (if any fees are applied)

<figure><img src="../../.gitbook/assets/image (545).png" alt=""><figcaption></figcaption></figure>

Here is a natural English translation of the provided text:

* **You receive** — the currency amount the client will receive  
* **Amount (incl. exch. fees)** — the amount including the exchange point’s fees (if any fees are applied)  
* **Amount (incl. exch. & payment fees)** — the amount including both the exchange point’s fees and the payment system’s fees (if any fees are applied)  
* **To account** — the account specified by the client when creating the request  

<figure><img src="../../.gitbook/assets/image (546).png" alt=""><figcaption></figcaption></figure>

* **E-mail** — the client’s e-mail address provided when creating the request  
* **IP address** — the client’s IP address  
* **User agent** — a string sent by the client’s browser to the server when requesting a web page. It contains information about the client’s operating system, browser and its version, as well as other details such as device type and language. The web server uses this information to deliver an optimized version of the web page tailored to the client’s device and browser.