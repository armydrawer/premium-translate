# CoinKyt

## Connecting to the Service

{% hint style="warning" %}
To connect to the service, please contact the [manager](https://t.me/premiumexchanger_business) — they will create a chat with you and representatives from the AML service to discuss connection terms, rates, and other questions.
{% endhint %}

Log in to the [CoinKyt](https://explorer.coinkyt.com/authorization) service.

Go to your personal account and generate a new key by clicking the "**Generate**" button in the "**API**" section. Copy the generated key to your clipboard or a text file.

In the script's admin panel, under the "**Modules**" -> "**CoinKyt**" section, fill in the fields for module authorization:

**API Key** — The **API key** generated in your CoinKyt personal account.

**Waiting time for verification result (sec, max 25-30 sec)** — The time to wait for a response from the service after sending the details (we recommend setting a value between 15 and 28).

**Application status if risk is exceeded** — The status to which the application will change if the risk set in the settings is exceeded.

**Risk if API is not working** — The desired risk value (from 0 to 100) that will be assigned to the verification result if no response is received from the API service. This value should be higher than the value in the "**Critical risk level for address/hash**" fields.

## Module Configuration

{% hint style="warning" %}
Please note that the risk level in the module is configured for all exchange directions where it will be used, regardless of the currency. Individual settings for each currency are not provided.
{% endhint %}

In the "**Modules**" -> "**CoinKyt**" section, you will find fields to set the risk level at which the module will trigger. Depending on the exchange direction settings:

* **For wallet** — prohibits creating an application with the specified client wallet.
* **For incoming transaction hash** — prohibits automatic payouts (when using the connected automatic payout module).

### Settings for Address Verification

**Critical risk level for address** — <mark style="color:red;">**mandatory**</mark> specify a value (from 0 to 100), exceeding which the module will report a risk for the application in the "**Applications**" section (before configuring this section, we recommend consulting with the CoinKyt manager regarding risk level settings).

**Other parameters** — setting risk levels for various categories (before configuring this section, we recommend consulting with the CoinKyt manager regarding risk level settings).

### Settings for Incoming Transaction Hash Verification

**Critical risk level for hash** — <mark style="color:red;">**mandatory**</mark> specify a value (from 0 to 100), exceeding which the module will report a risk for the application in the "**Applications**" section (before configuring this section, we recommend consulting with the CoinKyt manager regarding risk level settings).

**Other parameters** — setting risk levels for various categories (before configuring this section, we recommend consulting with the CoinKyt manager regarding risk level settings).

### Manual Checks

In this section, you can manually check addresses and hashes.

**To check an address**, enter its value in the "**Address**" field, select the correct currency for this address, and click the "**Check**" button.

<figure><img src="../../../.gitbook/assets/image (1852)_eng.png" alt=""><figcaption><p>Available currencies for checking</p></figcaption></figure>

**To check a transaction**, enter its identifier in the "**TxID**" field, select the correct currency, and click the "**Check**" button.

The results of the checks will be displayed at the top of the module settings page, as well as in the "**Modules**" -> "**CoinKyt logs**" section.

## Module Configuration for Exchange Direction

You can use the module for checking addresses and hashes without interfering with the application, as well as for prohibiting the creation of applications or payouts based on them.

Open the settings for the exchange direction where you want to use the checks and go to the "**CoinKyt**" tab.

Checking accounts "**Giving**" and "**Receiving**":

* **No** — no checks will be performed.
* **Yes, during application creation** — checks will be performed to prohibit application creation if the specified risk level is exceeded.
* **Yes, at payment** — the account check will be performed when receiving a payment made by the client (only if the merchant module for receiving funds is connected in the exchange direction).
* **Yes, during automatic payout** — the account check will be performed before paying out funds to the client (only if the automatic payout module is connected in the exchange direction).
* **Risk Exceeded:**\
  • **Nothing** — checks will be performed for informational purposes only.\
  • **Error** — if the risk specified in the module settings is exceeded, an error will be displayed to the client when creating an application or attempting an automatic payout (depending on the settings).
* **Exchange amount "from"** — the minimum amount from the application, above which the address or transaction check will be performed. If the amount is below the specified value, the check will not be performed.

{% hint style="warning" %}
The value is specified in the currency for which the address will be checked (for example, for checking a USDT address, specify 1000; for BTC — 0.015, etc. — all values are at your discretion).
{% endhint %}

TxID Check:

* **No** — the TxID check for incoming payments will not be performed.
* **Yes, at payment** — the TxID check for incoming payments will be performed when receiving a payment made by the client (only if the merchant module for receiving funds is connected in the exchange direction).
* **Yes, during automatic payout** — the TxID check for incoming payments will be performed before paying out funds to the client (only if the automatic payout module is connected in the exchange direction).

<figure><img src="../../../.gitbook/assets/image (1853)_eng.png" alt="" width="469"><figcaption></figcaption></figure>

* **Exchange amount "from"** — specify the amount from the application, above which the hash check will be performed. If the amount is below the specified value, the check will not be performed (the amount value is specified in the currency for the "**Giving**" side).
