# Configuration in v.2.7

## AML Module Setup

Make sure the module is activated in the "**Modules**" section, or activate it if it isn't.

<figure><img src="../../.gitbook/assets/image (2047)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

Add one of the four supported services in the "**AML**" -> "**Add**" section.

{% hint style="warning" %}
Don't forget to top up your balance with the chosen service to be able to check addresses and transactions!
{% endhint %}

<figure><img src="../../.gitbook/assets/image (2046)_eng.png" alt="" width="484"><figcaption></figcaption></figure>

In the new window, fill in the authorization details in the "**Module Settings**" section:

{% tabs %}
{% tab title="AML Bot" %}
<figure><img src="../../.gitbook/assets/image (188) (1).png" alt="" width="462"><figcaption></figcaption></figure>

**Connecting to the Service**

Register on the [AMLBot](https://web.amlbot.com/signup?) service, log into your personal account, and generate an ID and key for module authorization.

<figure><img src="../../.gitbook/assets/image (192) (1).png" alt=""><figcaption></figcaption></figure>

Enter these keys in the corresponding fields in the module settings and save the data.
{% endtab %}

{% tab title="BitOk" %}
<figure><img src="../../.gitbook/assets/image (189) (1).png" alt="" width="461"><figcaption></figcaption></figure>

**Connecting to the Service**

To connect to the service, contact the [manager](https://t.me/premiumexchanger_business) — they will create a chat with you and representatives from the AML service to discuss connection terms, rates, and other questions.

After gaining access to the service, top up your account to perform checks on client details on your exchange.

Go to your personal account, in the "[**API Keys**](https://kyt.bitok.org/api-keys)" section. Create a new key by clicking the "**Create Key**" button, and in the pop-up window, specify a desired name for the key and your server's IP address (optional).

<figure><img src="https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FgIzth95zoCr0EOsUo9oj%252Fimage_eng.png%3Falt%3Dmedia%26token%3D32a05d2f-48ec-47cf-aa8d-70cc487756e1&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=87b578bc&#x26;sv=2" alt="" width="563"><figcaption></figcaption></figure>

Click "**Create**" and copy the generated keys into a text file.

<figure><img src="https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FYOk96z3uNPDpR60IPc69%252Fimage_eng.png%3Falt%3Dmedia%26token%3D3ab0171e-90d8-4ca9-ae24-abf3eeaa3421&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=348e2df1&#x26;sv=2" alt="" width="563"><figcaption></figcaption></figure>

Enter these keys in the corresponding fields in the module settings and save the data.
{% endtab %}

{% tab title="CoinKyt" %}
<figure><img src="../../.gitbook/assets/image (190) (1).png" alt="" width="461"><figcaption></figcaption></figure>

**Connecting to the Service**

To connect to the service, contact the [manager](https://t.me/premiumexchanger_business) — they will create a chat with you and representatives from the AML service to discuss connection terms, rates, and other questions.

Log into your personal account and generate a new key by clicking the "**Generate**" button in the "**API**" section. Copy the generated key to your clipboard or a text file.

<figure><img src="https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FHkttfrUnvNLrOw6Chvhx%252Fimage_eng.png%3Falt%3Dmedia%26token%3D6a543cea-2f74-4014-b383-8c12eebd0132&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=4c5ecb43&#x26;sv=2" alt="" width="563"><figcaption></figcaption></figure>

Enter this key in the corresponding field in the module settings and save the data.
{% endtab %}

{% tab title="GetBlock" %}
<figure><img src="../../.gitbook/assets/image (191) (1).png" alt="" width="457"><figcaption></figcaption></figure>

**Connecting to the Service**

To obtain an API key, send an email to [info@getblock.net](mailto:info@getblock.net). Enter the key received from the service representative in the corresponding field in the module settings and save the data.
{% endtab %}
{% endtabs %}

## General Settings

<figure><img src="../../.gitbook/assets/image (178) (1).png" alt="" width="329"><figcaption></figcaption></figure>

**Risk if API is not working** — the desired risk value (from 0 to 100) that will be assigned to the check result if no response is received from the service API. The value <mark style="color:red;">**must be**</mark> higher than the value set in the "**Critical risk level for address/hash**" fields.

<div><figure><img src="../../.gitbook/assets/image (179) (1).png" alt="" width="325"><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/image (180) (1).png" alt="" width="326"><figcaption></figcaption></figure></div>

**Critical risk level for address/hash** — <mark style="color:red;">**mandatory**</mark> to specify a value (from 0 to 100), above which the module will report a risk for requests in the "**Requests**" section (before configuring this section, we recommend consulting with the manager of the chosen AML service regarding risk level settings).

<figure><img src="../../.gitbook/assets/image (183) (1).png" alt="" width="322"><figcaption></figcaption></figure>

**Waiting time for check result (sec, max 25-30 sec)** — the time to wait for a response from the service after sending data for verification (it is recommended to set a value between 15 and 28).

**Script timeout (sec)** — the time during which the site waits for a response from the AML service. If no response is received within the specified time, the site will continue its operation without an answer. If the time is not set or is equal to 0, the standard timeout of 20 seconds applies. There is no universal timeout value, as it depends on the speed of the specific service.

<figure><img src="../../.gitbook/assets/image (182) (1).png" alt="" width="281"><figcaption></figcaption></figure>

**Disable logs** — turning off logs for checks (not recommended).

**Check categories** — setting risk levels for various categories. Consult with the service you are connecting to for assistance with fine-tuning categories (note that each module has its own set of categories for configuration).

<figure><img src="../../.gitbook/assets/image (187) (1).png" alt="" width="322"><figcaption></figcaption></figure>

## Manual Checks

The AML module allows for manual checks of addresses, hashes, and transactions. To perform a check, go to the settings of the configured service, enter the data for verification, and click the "**Check**" button.

{% hint style="info" %}
TxID is a unique transaction identifier generated **before** the transaction is included in the blockchain. It is usually a hash of the transaction data (e.g., inputs, outputs, signatures) but is created before the transaction is included in a block.

* **What is it used for?**\
  TxID allows for quick identification of a transaction in the blockchain. It's like an "order number" in a system.
* **Example:**\
  When you send cryptocurrency, the TxID is what you see immediately after creating the transaction. It helps track the status of the transaction until it is confirmed.

A transaction hash is a unique identifier that is generated **after** the transaction is included in a block. It is calculated based on the transaction data and additional information (e.g., block number, time, and other parameters).

* **What is it used for?**\
  The transaction hash is used to verify the integrity of data in the blockchain. It ensures that the transaction has not been altered after being included in a block.
* **Example:**\
  The transaction hash can be compared to a "fingerprint" of the transaction after it is confirmed. It is unique and depends on all the data associated with the transaction in the block.

**Analogy**

Imagine you are sending a letter:

* **TxID** — this is the tracking number you receive immediately after handing the letter to the post office. It helps track the letter until it is delivered.
* **Transaction hash** — this is the unique stamp on the envelope that is placed after the letter is delivered and registered. It confirms that the letter was indeed delivered and has not been altered.

Thus, TxID and transaction hash are two stages of transaction identification: before and after it is included in the blockchain.
{% endhint %}

{% tabs %}
{% tab title="AML Bot" %}
<figure><img src="../../.gitbook/assets/image (173) (1).png" alt="" width="466"><figcaption></figcaption></figure>

**Address Check** — check a wallet address. Enter the address and select the desired currency.

**Transaction Check** — check a transaction. Enter the wallet address of the <mark style="color:green;">**recipient**</mark>**,** select the desired currency, enter the TxID, and choose the type of transaction (deposit or withdrawal).

**UID Check** — check the unique identifier from the response to the transaction check request.
{% endtab %}

{% tab title="BitOk" %}
<figure><img src="../../.gitbook/assets/image (174) (1).png" alt="" width="472"><figcaption></figcaption></figure>

**Address Check** — check a wallet address. Enter the address and select the desired currency.

**Transaction Check** — check a transaction. Enter the wallet address of the <mark style="color:green;">**recipient**</mark>**,** select the desired currency, and enter the TxID.
{% endtab %}

{% tab title="CoinKyt" %}
<figure><img src="../../.gitbook/assets/image (175) (1).png" alt="" width="473"><figcaption></figcaption></figure>

**Address Check** — check a wallet address. Enter the address and select the desired currency.

**Transaction Check** — check a transaction. Enter the TxID and select the desired currency.
{% endtab %}

{% tab title="GetBlock" %}
<figure><img src="../../.gitbook/assets/image (176) (1).png" alt="" width="452"><figcaption></figcaption></figure>

**Address Check** — This feature allows you to verify a wallet address. Enter the address and select the desired currency.

**Transaction Check** — This feature enables you to verify a transaction. Provide the recipient's wallet address, select the currency, enter the TxID, and choose the type of transaction (deposit or withdrawal).

**Hash Check** — This allows you to verify the hash from the response to the transaction check request.

<figure><img src="../../.gitbook/assets/image (100) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

The results of the checks will be displayed at the top of the page:

<figure><img src="../../.gitbook/assets/image (177) (1).png" alt=""><figcaption></figcaption></figure>

## Logging

In the "**AML**" -> "**Logs**" section, you will find the results of the checks as well as any errors encountered while using the services.

<figure><img src="../../.gitbook/assets/image (2048)_eng.png" alt=""><figcaption></figcaption></figure>

## Module Configuration for Exchange Direction

You can use the module to check addresses and hashes without interfering with the request, or to block the creation of requests or prevent payouts.

Open the settings for the exchange direction where you want to implement the checks and navigate to the "**AML**" tab. Select the previously configured AML service and adjust the specified options.

<figure><img src="../../.gitbook/assets/image (184) (1).png" alt=""><figcaption></figcaption></figure>

Checking the accounts for "**Sending**" and "**Receiving**":

![](https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252F7R3KdtN6GGnYeNXhmRma%252Fimage_eng.png%3Falt%3Dmedia%26token%3D63493485-ecb6-47e6-9f1b-2401b3502abe\&width=768\&dpr=4\&quality=100\&sign=ab6174df\&sv=2) ![](https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FD3WNc4TbMfIAV3uhgBab%252Fimage_eng.png%3Falt%3Dmedia%26token%3D5547117b-2df9-437b-8601-e31e26f6930e\&width=768\&dpr=4\&quality=100\&sign=2384dec3\&sv=2)

* **No** — No checks will be performed.
*   **Yes, during request creation** — Checks will be conducted to prevent the creation of a request if the specified risk level is exceeded.

    <figure><img src="https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FrCkAUosTHwbhajPIQwjp%252Fbrave_nG8qmZEGwR_eng.png%3Falt%3Dmedia%26token%3Dd2063fa4-97fa-4736-97d5-bd3fd8220467&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=93fefc8d&#x26;sv=2" alt="" width="563"><figcaption></figcaption></figure>
* **Yes, during payment** — The account check will be performed when receiving a payment made by the client (only if the exchange direction has the merchant module for receiving funds enabled).

<figure><img src="../../.gitbook/assets/image (185) (1).png" alt=""><figcaption></figcaption></figure>

* **Yes, during auto-payout** — The account check will be performed before funds are paid out to the client (only if the exchange direction has the auto-payout module enabled).
* **Risk Exceeded:**\
  • **Nothing** — Checks will be performed for informational purposes only.\
  • **Error** — If the risk level specified in the module settings is exceeded, the client will see an error when creating a request or attempting an auto-payout (depending on the settings).
* **Exchange Amount "from"** — Specify the amount from the request, above which the address or transaction check will be performed. If the amount in the request is below this specified value, the check will not be conducted.

{% hint style="warning" %}
The value should be specified in the currency for which the address will be checked (for example, for checking a USDT address, enter 1000; for BTC, enter 0.015, etc. — you can set the minimum amounts for which checks will be performed at your discretion).
{% endhint %}

TxID Check:

![](https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FGKXGBpd9faaSHOJsRBJG%252Fimage_eng.png%3Falt%3Dmedia%26token%3D3016e6fb-ec81-4428-89c1-4b840b798573\&width=768\&dpr=4\&quality=100\&sign=7c6d03ba\&sv=2)

* **No** — The TxID check for incoming payments will not be performed.
* **Yes, during payment** — The TxID check for incoming payments will be conducted when receiving a payment made by the client (only if the exchange direction has the merchant module for receiving funds enabled).
* **Yes, during auto-payout** — The TxID check for incoming payments will be performed before funds are paid out to the client (only if the exchange direction has the auto-payout module enabled).

<figure><img src="../../.gitbook/assets/image (186) (1).png" alt="" width="563"><figcaption></figcaption></figure>

* **Exchange Amount "from"** — Specify the amount from the request, above which the hash check will be performed. If the amount is below this specified value, the check will not be conducted (the amount value is specified in the currency for the "**Sending**" side).
