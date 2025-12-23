# Configuration in v.2.7

## etting Up the AML Module

Make sure the module is activated in the "**Modules**" section, or activate it if it isn't.

<figure><img src="../../.gitbook/assets/изображение (5).png" alt=""><figcaption></figcaption></figure>

Add one of the four supported services in the "**AML**" ➔ "**Add**" section.

{% hint style="warning" %}
Remember to top up your balance with the chosen service to be able to check addresses and transactions!
{% endhint %}

<figure><img src="../../.gitbook/assets/изображение (7).png" alt=""><figcaption></figcaption></figure>

In the new window, fill in the authorization details in the "**Module Settings**" section:

{% tabs %}
{% tab title="AML Bot" %}
<figure><img src="../../.gitbook/assets/изображение (5) (1).png" alt=""><figcaption></figcaption></figure>

**Connecting to the Service**

Register on the [AMLBot](https://web.amlbot.com/signup?) service, log in to your personal account, and generate an ID and key for module authorization.

<figure><img src="../../.gitbook/assets/image (192).png" alt=""><figcaption></figcaption></figure>

Enter the generated keys in the corresponding fields in the module settings and save the data.
{% endtab %}

{% tab title="BitOk" %}
<figure><img src="../../.gitbook/assets/изображение (2) (1).png" alt=""><figcaption></figcaption></figure>

**Connecting to the Service**

To connect to the service, contact the [manager](https://t.me/premiumexchanger_business) — they will create a chat with you and representatives from the AML service to discuss connection terms, rates, and other questions.

After gaining access to the service, top up your account to perform client verification checks on your exchange.

Go to your personal account, in the "[**API Keys**](https://kyt.bitok.org/api-keys)" section. Create a new key by clicking the "**Create Key**" button, and in the pop-up window, specify a desired name for the key and your server's IP address (optional).

<figure><img src="https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FgIzth95zoCr0EOsUo9oj%252Fimage.png%3Falt%3Dmedia%26token%3D32a05d2f-48ec-47cf-aa8d-70cc487756e1&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=87b578bc&#x26;sv=2" alt="" width="563"><figcaption></figcaption></figure>

Click "**Create**" and copy the generated keys into a text file.

<figure><img src="https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FYOk96z3uNPDpR60IPc69%252Fimage.png%3Falt%3Dmedia%26token%3D3ab0171e-90d8-4ca9-ae24-abf3eeaa3421&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=348e2df1&#x26;sv=2" alt="" width="563"><figcaption></figcaption></figure>

Enter the generated keys in the corresponding fields in the module settings and save the data.
{% endtab %}

{% tab title="CoinKyt" %}
<figure><img src="../../.gitbook/assets/изображение (1) (1).png" alt=""><figcaption></figcaption></figure>

**Connecting to the Service**

To connect to the service, contact the [manager](https://t.me/premiumexchanger_business) — they will create a chat with you and representatives from the AML service to discuss connection terms, rates, and other questions.

Log into your personal account and generate a new key by clicking the "**Generate**" button in the "**API**" section. Copy the generated key to your clipboard or a text file.

<figure><img src="https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FHkttfrUnvNLrOw6Chvhx%252Fimage.png%3Falt%3Dmedia%26token%3D6a543cea-2f74-4014-b383-8c12eebd0132&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=4c5ecb43&#x26;sv=2" alt="" width="563"><figcaption></figcaption></figure>

Enter the key in the corresponding field in the module settings and save the data.
{% endtab %}

{% tab title="GetBlock" %}
<figure><img src="../../.gitbook/assets/изображение (3) (1).png" alt=""><figcaption></figcaption></figure>

**Connecting to the Service**

To obtain an API key, send an email to [info@getblock.net](mailto:info@getblock.net). Enter the key received from the service representative in the corresponding field in the module settings and save the data.
{% endtab %}

{% tab title="Matchsystems" %}
<figure><img src="../../.gitbook/assets/изображение (4) (1).png" alt=""><figcaption></figcaption></figure>

**Connecting to the Service**

An API key will be issued by the Matchsystems manager after the terms of service and payment are agreed upon.

Enter the key received from the service representative in the corresponding field in the module settings and save the data.
{% endtab %}
{% endtabs %}

## General Settings

<figure><img src="../../.gitbook/assets/изображение (8).png" alt=""><figcaption></figcaption></figure>

**Risk if API doesn't work** — the desired risk value (from 0 to 100) that will be assigned to the verification result if no response is received from the API service. The value <mark style="color:red;">**must be**</mark> higher than the value set in the "**Critical Risk Level for Address/TxID**" fields.

<figure><img src="../../.gitbook/assets/изображение (9).png" alt="" width="302"><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/изображение (10).png" alt="" width="294"><figcaption></figcaption></figure>

**Critical Risk Level for Address/TxID** — <mark style="color:red;">**must**</mark> specify a value (from 0 to 100) above which the module will report a risk for applications in the "**Orders**" section (before configuring this section, we recommend consulting the manager of the chosen AML service regarding risk level settings).

<figure><img src="../../.gitbook/assets/изображение (11).png" alt=""><figcaption></figcaption></figure>

**Waiting Time for Verification Result (sec, max 25-30 sec)** — the time to wait for a response from the service after sending data for verification (it is recommended to set a value between 15 and 28).

**Script Timeout (sec)** — the time during which the site waits for a response from the AML service. If no response is received within the specified time, the site will continue its operation without an answer. If the time is not set or is equal to 0, the standard timeout of 20 seconds applies. There is no universal timeout value as it depends on the specific service's speed.

<figure><img src="../../.gitbook/assets/изображение (12).png" alt=""><figcaption></figcaption></figure>

**Disable Logs** — turning off logs for checks (not recommended).

**Verification Categories** — setting risk levels for various categories. Request assistance from the service you are connecting to for fine-tuning the categories (note that each module has its own set of categories for configuration).

<figure><img src="../../.gitbook/assets/изображение (13).png" alt=""><figcaption></figcaption></figure>

## Manual Checks

The AML module allows for manual checks of addresses, hashes, and transactions. To perform a check, go to the settings of the configured service, enter the data for verification, and click the "**Check**" button.

{% hint style="info" %}
TxID is a unique transaction identifier generated **before** the transaction is included in the blockchain. It is usually a hash of the transaction data (e.g., inputs, outputs, signatures) but before the transaction is included in a block.

* **What is it used for?**\
  TxID allows for quick identification of a transaction in the blockchain. It is like an "order number" in a system.
* **Example:**\
  When you send cryptocurrency, the TxID is what you see immediately after creating the transaction. It helps track the status of the transaction until it is confirmed.

A transaction hash is a unique identifier that is generated **after** the transaction is included in a block. It is calculated based on the transaction data and additional information (e.g., block number, time, and other parameters).

* **What is it used for?**\
  The transaction hash is used to verify the integrity of data in the blockchain. It ensures that the transaction has not been altered after being included in a block.
* **Example:**\
  The transaction hash can be compared to a "fingerprint" of the transaction after it is confirmed. It is unique and depends on all the data associated with the transaction in the block.

**Analogy**

Imagine you are sending a letter:

* **TxID** — is the tracking number you receive immediately after handing the letter to the post office. It helps track the letter until it is delivered.
* **Transaction Hash** — is the unique stamp on the envelope that is applied after the letter is delivered and registered. It confirms that the letter was indeed delivered and has not been altered.

Thus, TxID and transaction hash are two stages of transaction identification: before and after it is included in the blockchain.
{% endhint %}

{% tabs %}
{% tab title="AML Bot" %}
<figure><img src="../../.gitbook/assets/изображение (17).png" alt=""><figcaption></figcaption></figure>

**Address Check** — check the wallet address. Enter the address and select the desired currency.

**Transaction Check** — check the transaction. Enter the wallet address of the <mark style="color:green;">**recipient**</mark>**,** select the desired currency, enter the TxID, and choose the type of transaction (deposit or withdrawal).

**UID Check** — check the unique identifier from the transaction verification request response.

<figure><img src="../../.gitbook/assets/image (99).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="BitOk" %}
<figure><img src="../../.gitbook/assets/изображение (16).png" alt=""><figcaption></figcaption></figure>

**Address Check** — check the wallet address. Enter the address and select the desired currency.

**Transaction Check** — check the transaction. Enter the wallet address of the <mark style="color:green;">**recipient**</mark>**,** select the desired currency, and enter the TxID.
{% endtab %}

{% tab title="CoinKyt" %}
<figure><img src="../../.gitbook/assets/изображение (15).png" alt=""><figcaption></figcaption></figure>

**Address Check** — check the wallet address. Enter the address and select the desired currency.

**Transaction Check** — check the transaction. Enter the wallet address of the <mark style="color:green;">**recipient**</mark>**,** select the desired currency, and enter the TxID.
{% endtab %}

{% tab title="GetBlock" %}
<figure><img src="../../.gitbook/assets/изображение (14).png" alt=""><figcaption></figcaption></figure>

**Address Verification** — This feature allows you to check a wallet address. Please enter the address and select the desired currency.

**Hash Verification** — This feature allows you to verify a transaction. Please provide the TxID and select the appropriate currency.
{% endtab %}

{% tab title="Matchsystems" %}
<figure><img src="../../.gitbook/assets/изображение (18).png" alt=""><figcaption></figcaption></figure>

**Address Check** — check the wallet address. Enter the address of wallet&#x20;

**Transaction Check** — check the transaction. Select the desired currency and enter the TxID
{% endtab %}
{% endtabs %}

## Logging

In the "**AML**" ➔ "**Logs**" section, you will find the results of the verifications as well as any errors encountered while using the services.

<figure><img src="../../.gitbook/assets/изображение (19).png" alt="" width="563"><figcaption></figcaption></figure>

## Module Configuration for Exchange Direction

You can use the module for both address and hash verification without interfering with the request, as well as to prohibit the creation of requests or the disbursement of funds.

Open the settings for the exchange direction where you want to use the verifications and navigate to the "**AML**" tab. Select the previously configured AML service and set the specified options.

<figure><img src="../../.gitbook/assets/изображение (20).png" alt=""><figcaption></figcaption></figure>

**Verification of "Send" and "Receive" Accounts:**

<figure><img src="../../.gitbook/assets/изображение (21).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/изображение (22).png" alt=""><figcaption></figcaption></figure>

* **No** — No verification will be performed.
* **Yes, during request creation** — Verification will be conducted to prevent the creation of a request if the specified risk level is exceeded.

![Request Creation Verification](https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FrCkAUosTHwbhajPIQwjp%252Fbrave_nG8qmZEGwR.png%3Falt%3Dmedia%26token%3Dd2063fa4-97fa-4736-97d5-bd3fd8220467\&width=768\&dpr=4\&quality=100\&sign=93fefc8d\&sv=2)

* **Yes, at payment** — The account verification will be performed when accepting a payment made by the client (only if the exchange direction has the merchant module for receiving funds enabled).
* **Yes, during auto-disbursement** — The account verification will be performed before disbursing funds to the client (only if the exchange direction has the auto-disbursement module enabled).
* **Risk Exceedance:**\
  • **Nothing** — Verifications will be conducted for informational purposes only.\
  • **Error** — If the risk level specified in the module settings is exceeded, an error will be displayed to the client when creating a request or attempting an auto-disbursement (depending on the settings).
* **Exchange Amount "From"** — Specify the amount from the request, above which the address or transaction verification will be performed. If the amount in the request is below this specified value, no verification will be conducted.

{% hint style="warning" %}
The value should be specified in the currency for which the address will be verified (for example, for verifying a USDT address, specify 1000; for BTC, specify 0.015, etc. — you can set the minimum amounts for which verifications will be performed at your discretion).
{% endhint %}

**TxID Verification:**

<figure><img src="../../.gitbook/assets/изображение (23).png" alt=""><figcaption></figcaption></figure>

* **No** — The TxID verification for incoming payments will not be performed.
* **Yes, at payment** — The TxID verification for incoming payments will be performed when accepting a payment made by the client (only if the exchange direction has the merchant module for receiving funds enabled).
* **Yes, during auto-disbursement** — The TxID verification for incoming payments will be performed before disbursing funds to the client (only if the exchange direction has the auto-disbursement module enabled).

<figure><img src="../../.gitbook/assets/изображение (24).png" alt=""><figcaption></figcaption></figure>

* **Exchange Amount "From"** — Specify the amount from the request, above which the hash verification will be performed. If the amount is below this specified value, no verification will be conducted (the amount value is specified in the currency for the "**Send**" side).
