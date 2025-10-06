# Electrum

{% hint style="info" %}
If you need to update the module on the server, please refer to the [instructions](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat).
{% endhint %}

{% hint style="danger" %}
Electrum allows for the cancellation and substitution of transactions, which can lead to the loss of funds for the exchange if the settings mentioned below are not configured in your exchange and a fraudster attempts to exploit this feature of Electrum. If you are using a module to work with Electrum, **make sure** to perform the following configuration.

When using merchants to receive funds, it is necessary to [recalculate the payment amount](https://premium.gitbook.io/main/osnovnye-nastroiki/valyuty-i-napravleniya/sozdanie-novogo-napravleniya-obmena#pereschet-po-summe-oplaty) at least for the status "**Paid Request**" in the exchange direction settings.

![](<../../../.gitbook/assets/image (329)_eng.png>)

You must also configure the automatic transition of requests to the status "**Under Review**" if the actual payment amount is less than the original (this option is found in the merchant module settings for receiving funds under the "**Merchants**" section).

<img src="../../../.gitbook/assets/image (328)_eng.png" alt="" data-size="original">
{% endhint %}

{% hint style="warning" %}
For receiving funds and for auto payouts, it is **recommended** to use [different Electrum wallets](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/modul-electrum/ustanovka-i-nastroika-electrum/sozdanie-dopolnitelnogo-koshelka) — this will create independent channels for receiving and withdrawing BTC.

This measure is necessary to prevent the withdrawal of "dirty" BTC. If you receive and pay everything to one wallet, there is a risk that "dirty" BTC will be withdrawn along with clean funds.
{% endhint %}

## Installation and Configuration of the Module

Install Electrum on the server following the [instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/modul-electrum/ustanovka-i-nastroika-electrum).

Make sure to save the port number for connection, server address (optional), username, and password for wallet access in a text file.

<figure><img src="../../../.gitbook/assets/image (1443)_eng.png" alt=""><figcaption></figcaption></figure>

## Module Settings

In the admin panel, create a new merchant in the "**Merchants**" -> "**Add Merchant**" section.

Select Electrum from the dropdown list in the "**Module**" field, provide a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (1444)_eng.png" alt=""><figcaption></figcaption></figure>

Fill in the specified authorization fields.

<figure><img src="../../../.gitbook/assets/image (1446)_eng.png" alt=""><figcaption></figcaption></figure>

* **Number of confirmations for a payment to be considered completed** — leave this field empty to use the default value that Electrum employs.
* **Login** — enter the information from the "**User for Connection**" line.
* **Password** — enter the information from the "**User Password for Connection**" line.
* **Api server** — fill this field only if the Electrum module is installed on a server different from the one where the Premium Exchanger script is installed. Enter the IP address in the format `111.111.111.111` (without specifying the `http/https` protocol).

{% hint style="warning" %}
If the Electrum module is installed on the same server as the Premium Exchanger script, leave this field empty.
{% endhint %}

* **Api port** — enter the information from the "**Port for Connection**" line.

## Continuing the Configuration

Next, proceed to configure the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).