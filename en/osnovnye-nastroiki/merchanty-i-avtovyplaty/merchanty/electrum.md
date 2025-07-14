# Electrum

{% hint style="info" %}
If you need to update the module on your server, please follow the [instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-merchantov).
{% endhint %}

{% hint style="danger" %}
Electrum allows transactions to be canceled and replaced, which can lead to losses for the exchanger if the settings described below are not configured in your exchanger, and a fraudster tries to exploit this Electrum feature. If you are using the module to work with Electrum, it is **essential** to apply the following settings.

When using merchants to receive funds, you must [recalculate the order amount](https://premium.gitbook.io/main/osnovnye-nastroiki/valyuty-i-napravleniya/sozdanie-novogo-napravleniya-obmena#pereschet-po-summe-oplaty) at least for the "**Paid order**" status in the exchange direction settings.

![](<../../../.gitbook/assets/image (329).png>)

Additionally, you need to configure automatic switching of orders to the "**Under Review**" status if the actual payment amount is less than the original amount (this option is available in the merchant module settings for receiving funds under the "**Merchants**" section).

<img src="../../../.gitbook/assets/image (328).png" alt="" data-size="original">
{% endhint %}

{% hint style="warning" %}
For receiving funds and automatic payouts, it is **recommended** to use [separate Electrum wallets](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/modul-electrum/ustanovka-i-nastroika-electrum/sozdanie-dopolnitelnogo-koshelka). This allows you to create independent wallets for BTC deposits and withdrawals.

This measure is necessary to prevent withdrawing "tainted" BTC. If you use the same wallet for both receiving and sending funds, there is a risk that "tainted" BTC will be sent out along with clean funds.
{% endhint %}

## Module Installation and Setup

Install Electrum on your server by following the [installation guide](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/modul-electrum/ustanovka-i-nastroika-electrum).

Be sure to save the port number for connection, server address (optional), login, and password for wallet access in a text file.

<figure><img src="../../../.gitbook/assets/image (1443).png" alt=""><figcaption></figcaption></figure>

## Module Settings

In the admin panel, create a new merchant by going to "**Merchants**" -> "**Add Merchant**."

Select Electrum from the dropdown menu in the "**Module**" field, enter a name for the module, and click "**Save**."

Fill in the specified authorization fields.

* **Number of payment confirmations required to consider the payment complete** — leave this field empty to use the default value employed by Electrum.
* **Login** — enter the data from the "**User for connection**" field.
* **Password** — enter the data from the "**User password for connection**" field.
* **API server** — fill in this field only if the Electrum module is installed on a different server than the one running the Premium Exchanger script. Specify the IP address in the format `111.111.111.111` (without including the `http/https` protocol).

{% hint style="warning" %}
If the Electrum module is installed on the same server as the Premium Exchanger script, leave this field empty.
{% endhint %}

* **API port** — enter the data from the "**Connection port**" field.

## Continuing the setup

Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).