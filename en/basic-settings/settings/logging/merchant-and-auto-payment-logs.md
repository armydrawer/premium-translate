# Merchant and Auto-Payment Logs

In this section ("**Merchants**" ➔ "**Merchant Logs**" and "**Merchants**" ➔ "**Auto-Payment Logs**"), you can view the logs received from merchants when creating requests that utilize these merchants.

{% hint style="warning" %}
If the section does not appear in the sidebar, please enable the modules in the "**Modules**" section:

<img src="../../../.gitbook/assets/image (1148)_eng.png" alt="" data-size="original"><img src="../../../.gitbook/assets/image (2116)_eng.png" alt="" data-size="original">
{% endhint %}

<figure><img src="../../../.gitbook/assets/image (1143)_eng.png" alt=""><figcaption><p>Merchant Logs</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (1170)_eng (1).png" alt=""><figcaption><p>Auto-Payment Logs</p></figcaption></figure>

Logs received from merchants and auto-payments can vary significantly in content due to differences in the development of each service. However, the log structure remains consistent and includes the following parameters:

**Date** — the date and time the log was received

**Data**:

* **url** — the address from which the log was received from the merchant
* **headers** — the log headers, containing information about the transaction
* **post\_data** — the body of the log, containing transaction information sent to the merchant
* **result** — contains information about the actions performed, their results, and any errors received from the merchant

**Merchant/Auto-Payment** — the name of the merchant/auto-payment module that sent the log

**IP Address** — the IP address from which the log entry was received

**Request ID** — the ID of the client's request

For easier searching of specific data, you can use filters based on four criteria:

<figure><img src="../../../.gitbook/assets/image (889) (1).png" alt=""><figcaption></figcaption></figure>

* **Merchant** — display only logs from the specified merchant
* **IP Address** — display only logs that came from the specified IP address
* **Start Date** — do not display logs received before the specified date and time
* **End Date** — do not display logs received after the specified date and time

<figure><img src="../../../.gitbook/assets/image (2118)_eng.png" alt="" width="369"><figcaption></figcaption></figure>
