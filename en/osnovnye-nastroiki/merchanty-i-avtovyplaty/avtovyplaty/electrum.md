# Electrum

{% hint style="danger" %}
<mark style="color:red;">Before setting up auto payouts, please read the</mark> [<mark style="color:blue;">risk warning</mark>](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/preduprezhdenie-o-riskakh)<mark style="color:blue;">!</mark>
{% endhint %}

{% hint style="info" %}
If you need to update the module on the server, please refer to the [instructions](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat).
{% endhint %}

{% hint style="warning" %}
It is **recommended** to use [different Electrum wallets](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/modul-electrum/ustanovka-i-nastroika-electrum/sozdanie-dopolnitelnogo-koshelka) for receiving funds and for auto payouts.
{% endhint %}

## Installation and Setup of the Module

Install Electrum on the server following the [instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/modul-electrum/ustanovka-i-nastroika-electrum).

Make sure to save the wallet password, the port number for connection, the server address (optional), and the login and password for wallet access in a text file.

<figure><img src="../../../.gitbook/assets/image (1443).png" alt=""><figcaption></figcaption></figure>

## **Module Settings**

In the admin panel, create a new merchant in the "**Auto Payouts**" section by clicking "**Add Auto Payout**."

Select Electrum from the dropdown menu in the "**Module**" field, provide a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (1447).png" alt="" width="509"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (1448).png" alt=""><figcaption></figcaption></figure>

* **Number of confirmations for a payment to be considered completed** — leave this field empty to use the default value set by Electrum.
* **Login** — enter the information from the "**User for connection**" field.
* **Password** — enter the information from the "**User password for connection**" field.
* **API server** — enter the information from the "**API server**" field.

{% hint style="warning" %}
The "**API Server**" field should only be filled in if the Electrum module is installed on a different server than the one where the Premium Exchanger script is located.

If the Electrum module is installed on the same server as the Premium Exchanger script, leave this field empty.
{% endhint %}

* **API port** — enter the information from the "**Port for connection**" field.
* **Wallet password** — enter the password for your wallet that you set when creating the wallet (if no password was set, leave this field empty).

## Special Fields

In the auto payout module settings, you will find the following options:

<figure><img src="../../../.gitbook/assets/image (768).png" alt=""><figcaption></figcaption></figure>

1. Mass payouts:

* “**No**” — mass payouts are not used, and requests will be processed sequentially.
* “**Yes + instant payout by button**” — mass payouts will be enabled, and you can also make an instant single payout by clicking the “Transfer” button in the "Requests" section of the admin panel.
* “**Yes + add request to payout queue**” — mass payouts will be enabled, and when you click the “Transfer” button in the "Requests" section of the admin panel, requests will be added to the mass payout queue.

2. Commission priority — choose one of the available network fee options.

{% hint style="info" %}
The current fee for sending a payment is automatically requested from the [Mempool.space](https://mempool.space/api/v1/fees/recommended) service just before each fund payout.
{% endhint %}

3. **Minimum and maximum fee size (in bytes)** — limits for the minimum and maximum network fee size. It is recommended to set these to avoid using abnormal values.

&nbsp;        _Recommended values: min. = 3 and max. = 100_.

4. **Minimum number of requests for mass payout** — the minimum number of requests in the queue required to trigger a mass payout. If the required number is not met, the payout will not occur.

&nbsp;        _Recommended value = 20_.

5. **Waiting time before mass payout (in minutes)** — the time during which paid requests will accumulate before the mass payout. The countdown starts from the first paid request in the queue.

&nbsp;        _Recommended value = 5_.

6. **CRON (mass payments)** — a link for setting up a cron job that needs to be [added to the task scheduler on the server](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-sozdat-zadanie-cron-na-servere). This task checks for available requests for payout and initiates the payout if there are any.

&nbsp;        _Recommended execution time - once every minute_.

### Recommended Settings for the Above Parameters:

<figure><img src="../../../.gitbook/assets/image (1449).png" alt=""><figcaption></figcaption></figure>

With these settings, mass payouts will occur after 5 minutes if 20 paid requests are accumulated. If 5 minutes pass and there are not 20 requests, the mass payout will still occur, but with the number of requests currently in the queue.

## Continuing the Setup

Next, proceed to configure the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-merchantov-avtovyplat).