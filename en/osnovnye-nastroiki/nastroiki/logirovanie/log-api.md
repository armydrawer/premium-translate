# API Logs

In this section ("**API**" -> "**Logs**"), you can view the logs generated while using the Premium Exchanger API.

<figure><img src="../../../.gitbook/assets/image (1136)_eng.png" alt=""><figcaption></figcaption></figure>

The logs received from the API can vary significantly in content, but the [log structure remains consistent](#user-content-fn-1)[^1] and includes the following parameters:

**Date** — the date and time the log was received

**Data**:

* **headers** — the log headers, which contain information about the transaction
* **post_data** — the body of the log, which contains information about the transaction

**API Login** — the login obtained from the "**API Keys**" section

**API Key** — the key obtained from the "**API Keys**" section

**Action** — the method used to request the API

**IP Address** — the address from which the API request was made

For easier searching of specific data, you can use filters based on five criteria:

<figure><img src="../../../.gitbook/assets/image (1065)_eng.png" alt=""><figcaption></figcaption></figure>

* **API Login** — display only logs associated with this login
* **API Key** — display only logs associated with this key
* **Source** — display only logs from this address
* **Start Date** — do not display logs received before the specified date
* **End Date** — do not display logs received after the specified date

[^1]: Some parameters may occasionally be missing from the logs if the API does not return them.