# BitOK

## Connecting to the Service

{% hint style="warning" %}
To connect to the service, please contact the [manager](https://t.me/premiumexchanger_business) — they will create a chat with you and representatives from the AML service to discuss connection terms, rates, and other questions.
{% endhint %}

Once you have access to the service, fund your account to perform client detail checks on your exchange.

Log into your personal account and go to the "[**API Keys**](https://kyt.bitok.org/api-keys)" section. Create a new key by clicking the "**Create Key**" button. In the pop-up window, specify a desired name for the key and the IP address of your server (optional).

Click "**Create**" and copy the generated keys into a text file.

In the admin panel of the script, under the "**Modules**" -> "**BitOK**" section, fill in the fields for module authorization:

{% tabs %}
{% tab title="2.5" %}
<figure><img src="../../../.gitbook/assets/image (1755)_eng.png" alt=""><figcaption></figcaption></figure>

**API Key** — The **API Key** generated in the BitOK personal account.

**API Secret** — The **API Secret** generated in the BitOK personal account.

**Waiting time for verification result (sec, max 25-30 sec)** — The time to wait for a response from the service after sending the details (we recommend setting a value between 15 and 28). If a wallet is being checked when creating a request, the specified time in seconds will increase the request creation time after the client clicks the "**Create Request**" button.

**Risk if API is not working (in auto payout)** — Specify the desired risk value (from 0 to 100) that will apply if no response is received from the API service. This value should be higher than the value in the "**Critical risk level for hash**" field.
{% endtab %}

{% tab title="2.6" %}
**API Key** — The **API Key** generated in the BitOK personal account.

**API Secret** — The **API Secret** generated in the BitOK personal account.

**Waiting time for verification result (sec, max 25-30 sec)** — The time to wait for a response from the service after sending the details (we recommend setting a value between 15 and 28). If a wallet is being checked when creating a request, the specified time in seconds will increase the request creation time after the client clicks the "**Create Request**" button.

**Request status if risk is exceeded** — The automatic change of the request status to the selected option from the dropdown list if the risk is exceeded (this option is relevant when checking an address or hash in an already created request).

**Risk if API is not working** — Specify the desired risk value (from 0 to 100) that will apply if no response is received from the API service. This value should be higher than the values in the "**Critical risk level for address**" and "**Critical risk level for hash**" fields.
{% endtab %}
{% endtabs %}

## Module Configuration

{% hint style="warning" %}
Please note that the risk level in the module is set for all exchange directions where it will be used, regardless of the currency. Individual settings for each exchange direction are not provided.
{% endhint %}

In the "**Modules**" -> "**BitOK**" section, you will find fields to configure the risk level at which the module will trigger. Depending on the exchange direction settings:

* **For wallet** — prohibit the creation of requests with the specified wallet.
* **For incoming transaction hash** — prohibit auto payout (when using the connected auto payout module).

### Settings for Address Verification

**Critical risk level for address** — <mark style="color:red;">**mandatory**</mark> specify a value (from 0 to 100) above which the module will report a risk for the request in the "Requests" section (we recommend consulting with the BitOK manager about configuring the risk level before setting up this section).

**Other parameters** — setting risk levels for various categories (no need to fill in, as category settings are managed on the BitOK service side).

<div><figure><img src="../../../.gitbook/assets/image (1733)_eng.png" alt="" width="305"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/image (1732)_eng.png" alt="" width="293"><figcaption></figcaption></figure></div>

### Settings for Incoming Transaction Hash Verification

**Critical risk level for hash** — <mark style="color:red;">**mandatory**</mark> specify a value (from 0 to 100) above which the module will report a risk for the request in the "Requests" section (we recommend consulting with the BitOK manager about configuring the risk level before setting up this section).

**Other parameters** — setting risk levels for various categories (no need to fill in, as category settings are managed on the BitOK service side).

<div><figure><img src="../../../.gitbook/assets/image (1737)_eng.png" alt="" width="314"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/image (1736)_eng.png" alt="" width="293"><figcaption></figcaption></figure></div>

### Manual Checks

In this section, you can also perform manual checks of addresses and hashes.

To check an address, enter its value in the "**Address**" field, select the correct currency for that address, and click the "**Check**" button.

To check a hash, enter the wallet address **for receiving funds** related to the transaction in the "**Address**" field, select the correct currency for that address, and enter the hash in the "**TxID**" field, then click the "**Check**" button.

<figure><img src="../../../.gitbook/assets/image (1744)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

The results of the checks will be displayed at the top of the module settings page, as well as in the "**Modules**" -> "**Bitok logs**" section.

<figure><img src="../../../.gitbook/assets/image (1745)_eng.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (1747)_eng.png" alt="" width="421"><figcaption></figcaption></figure>

## Module Configuration for Exchange Direction

{% hint style="warning" %}
An error like the one shown in the screenshot below means that you have no available checks — you need to purchase a new check package from the BitOK service.
{% endhint %}

You can use the module for checking addresses and hashes without interfering with the request, as well as for prohibiting the creation of requests or payouts based on them.

Open the settings for the exchange direction where you want to use the checks and go to the "**Bitok**" tab.

### Version 2.5

<figure><img src="../../../.gitbook/assets/image (1741)_eng.png" alt="" width="533"><figcaption></figcaption></figure>

Checking accounts "**Giving**" and "**Receiving**":

<div><figure><img src="../../../.gitbook/assets/image (1738)_eng.png" alt="" width="253"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/image (1739)_eng.png" alt="" width="242"><figcaption></figcaption></figure></div>

* **No** — no checks will be performed.
*   **Yes** — checks will be performed for informational purposes only, without prohibiting request creation.

    <figure><img src="../../../.gitbook/assets/image (1748)_eng.png" alt=""><figcaption></figcaption></figure>
*   **Yes and prohibit request creation** — checks will be performed to prohibit request creation if the specified risk level is exceeded.

    <figure><img src="../../../.gitbook/assets/image (1748)_eng.png" alt=""><figcaption></figcaption></figure>
* **Exchange amount "from"** — specify the amount from the request above which the address check will be performed. If the amount is below the specified value, the check will not be performed.\
  \
  The value should be specified in the currency for which the address will be checked (for example, for checking a USDT address, specify 1000; for BTC — 0.015, etc., but all values are at your discretion).

TxID Check:

<figure><img src="../../../.gitbook/assets/image (1740)_eng.png" alt="" width="206"><figcaption></figcaption></figure>

* **No** — no checks will be performed.
*   **Yes** — checks will be performed for informational purposes only, without prohibiting payouts.\\

    <figure><img src="../../../.gitbook/assets/image (1748)_eng.png" alt=""><figcaption></figcaption></figure>
*   **Yes and stop payout** — checks will be performed to prohibit payouts for the request if the specified risk level is exceeded (this is relevant only if auto payout is enabled for the exchange direction).\
    When the request changes to the status "**Auto payout error**" due to exceeding the risk level, you can verify the module's activation by going to the "**Merchants**" -> "**Auto payout log**" section, where the following entry will be displayed:\\

    <figure><img src="../../../.gitbook/assets/image (1748)_eng.png" alt=""><figcaption></figcaption></figure>
* **Exchange amount "from"** — specify the amount from the request above which the hash check will be performed. If the amount is below the specified value, the check will not be performed.\
  The value should be specified in the currency for the "**Giving**" side.

### Version 2.6

Checking accounts "**Giving**" and "**Receiving**":

* **No** — no checks will be performed.
* **Yes, during request creation** — checks will be performed to prohibit request creation if the specified risk level is exceeded.

Here’s a naturalistic English translation of the provided text:

***

* **Yes, at the time of payment** — the account will be checked after the payment is received from the client (only if the merchant module for accepting payments is enabled in the exchange direction).
* **Yes, during auto payout** — the account will be checked before the funds are paid out to the client (only if the auto payout module is enabled in the exchange direction).
* **Risk Exceedance:**\
  • **None** — Checks will be conducted for informational purposes only.\
  • **Error** — An error will be displayed if the risk exceeds the limits set in the module settings.
* **Exchange amount "from"** — specify the amount from the request above which the address check will be performed. If the amount is below this specified value, no check will be conducted.\
  The value should be in the currency for which the address will be checked (for example, for checking a USDT address, specify 1000; for BTC, specify 0.015, etc., but all values are at your discretion).

TxID Check:

* **No** — no check will be performed.
* **Yes, at the time of payment** —
* **Yes, during auto payout** —
* **Yes, and stop payout** — checks will be conducted to prevent the payout on the request if the specified risk level is exceeded (this is relevant only if auto payout is enabled in the exchange direction).\
  If the request changes to the status "**Auto payout error**" due to exceeding the risk level, you can verify the module's activation by going to the "**Merchants**" -> "**Auto payout log**" section, where the following entry will be displayed:
* **Exchange amount "from"** — specify the amount from the request above which the hash check will be performed. If the amount is below this specified value, no check will be conducted.\
  The value should be in the currency for the "**I give**" side.

***

Let me know if you need any further assistance!
