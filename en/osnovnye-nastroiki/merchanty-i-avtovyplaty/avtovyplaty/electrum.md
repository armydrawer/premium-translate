# Electrum

{% hint style="danger" %}
<mark style="color:red;">Before setting up auto payouts, be sure to read</mark> [<mark style="color:blue;">the risk warning</mark>](https://premiumexchanger.com/wiki/preduprezhdenie-auto/)<mark style="color:blue;">!</mark>
{% endhint %}

{% hint style="info" %}
If you need to update the module on your server, please follow this [guide](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-avtovyplat).
{% endhint %}

{% hint style="warning" %}
It is **recommended** to use [separate Electrum wallets](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/modul-electrum/ustanovka-i-nastroika-electrum/sozdanie-dopolnitelnogo-koshelka) for receiving funds and for auto payouts.
{% endhint %}

## Module Installation and Setup

Install Electrum on your server by following the [installation guide](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/modul-electrum/ustanovka-i-nastroika-electrum).

Make sure to save the wallet password, connection port number, server address (optional), and the login credentials for wallet access in a text file.

<figure><img src="../../../.gitbook/assets/image (1443).png" alt=""><figcaption></figcaption></figure>

## **Module Settings**

In the admin panel, create a new merchant under "**Auto Payouts**" -> "**Add Auto Payout**."

Select Electrum from the "**Module**" dropdown, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (1447).png" alt="" width="509"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (1448).png" alt=""><figcaption></figcaption></figure>

* **Number of confirmations required to consider a payment complete** — leave this field empty to use Electrum’s default value
* **Login** — enter the value from the "**User for connection**" field
* **Password** — enter the value from the "**User password for connection**" field
* **API Server** — enter the value from the "**API server**" field

{% hint style="warning" %}
The "**API Server**" field should only be filled if the Electrum module is installed on a different server than the one running the Premium Exchanger script.

If Electrum is installed on the same server as Premium Exchanger, leave this field empty.
{% endhint %}

* **API Port** — enter the value from the "**Connection port**" field
* **Wallet Password** — the password you set when creating the wallet (leave empty if no password was set)

## Special Fields

The auto payout module settings include the following options:



Here is a natural English translation of the provided text:

---

1. Bulk Payments:

* "**No**" — bulk payments are not used; requests will be paid out one by one.
* "**Yes + instant payment by button**" — bulk payment of requests will be enabled, and you can also make an instant single payment by clicking the “Pay” button in the "Requests" section of the admin panel.
* "**Yes + add request to payment queue**" — bulk payment of requests will be enabled, and when you click the “Pay” button in the "Requests" section of the admin panel, the requests will be added to the bulk payment queue.

2. Commission Priority — select one of the available network fee options.

{% hint style="info" %}
The current fee amount for sending a payment is automatically requested from the [Mempool.space](https://mempool.space/api/v1/fees/recommended) service immediately before each payout.
{% endhint %}

3. **Minimum and Maximum Fee Size (in bytes)** — limits for the minimum and maximum network fee size. We strongly recommend setting these limits to avoid using abnormal values.

 _Recommended values: min = 3, max = 100._

4. **Minimum Number of Requests for Bulk Payment** — the minimum number of requests in the queue required to trigger a bulk payment. If the queue does not contain enough requests, the bulk payment will not be executed.

 _Recommended value: 20._

5. **Waiting Time Before Bulk Payment (in minutes)** — the time during which paid requests will accumulate before the bulk payment is processed. The timer starts from the first paid request in the queue.

 _Recommended value: 5._

6. **CRON (mass payments)** — the URL for setting up a cron job, which should be [added to the server’s task scheduler](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-sozdat-zadanie-cron-na-servere). This task checks for available requests to pay and initiates the payment if any requests are found.

 _Recommended run frequency: once every 1 minute._

---

Let me know if you need it adapted for a specific audience or style!

### Recommended settings for the parameters described above:

<figure><img src="../../../.gitbook/assets/image (1449).png" alt=""><figcaption></figcaption></figure>

With these settings, a bulk payout will be triggered after 5 minutes if 20 paid requests have been accumulated. If 5 minutes pass without reaching 20 requests, the bulk payout will still be processed with however many requests are currently in the queue.

## Continuing the setup

Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-merchantov-avtovyplat).