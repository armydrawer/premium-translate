# Application Statuses

In the "**Applications**" section, you can view exchange requests and their statuses.

<figure><img src="../../../.gitbook/assets/изображение (189).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/изображение (41).png" alt=""><figcaption></figcaption></figure>

In this section, you will see a list of all requests along with their IDs. Requests that have been paid by the user will show statuses such as "**Paid Request**," "**Request Under Review**," and "**User Marked Request as Paid**."

In the case of semi-automatic exchanges, you should verify that the corresponding amount has been transferred to your wallet. After that, transfer the specified amount to the user's wallet. This amount is also indicated in the request information.

{% hint style="info" %}
Please note that for each request, the amounts to be transferred to the client are displayed both with and without fees. Generally, you should transfer the amount that includes the fee. Some payment systems charge the recipient of the payment (i.e., the client), in which case you should send the amount without the fee.
{% endhint %}

Next, select the request you have processed, choose "**Completed Request**" from the "**Actions**" dropdown, and click the "**Apply**" button. The user will be notified about the processing of this exchange.

In the case of automatic exchanges, the system will automatically transfer the funds to the client for requests with the status "**Paid Request**."

Requests with the status "**Request Under Review**" will be processed automatically based on the settings for automatic exchanges.

Requests marked as "**User Marked Request as Paid**" need to be processed manually.

The status "**Error in Request**" can be used in case of an error, for example, if the client provided incorrect details. In automatic operation mode, this status may appear if there are issues with the automatic payout of funds for the request.

The status "**Request Under Review**" can be used when the information for a particular request requires additional verification by the site administrator. This status is also set automatically when payment is made using a merchant—if the wallet number from which the payment was made does not match the wallet number provided when creating the request. This verification can be disabled in the settings of each merchant.

If necessary, you can create your own status in the "**Application Statuses**" section found in the console menu.

## Standard Application Statuses:

* **When the user navigates to the payment page** — the page where the client sees the details for transferring funds
* **Request Pending Verification** — waiting for the operator to confirm the client's verification
* **Request Cancelled by User** — the client has cancelled the request themselves
* **Deleted Request** — the request has been deleted
* **User Marked Request as Paid** — the client marked the request as paid by clicking the "**I Paid**" button in the request
* **New Request** — a newly created request
* **Waiting for Merchant Confirmation** — payment from the client is being processed on the merchant's side
* **Partially Paid** — a partial payment for the request has been received from the client
* **Paid Request** — the request has been fully paid
* **Request Under Review** — the request is under review (details do not match, underpayment/overpayment, etc.)
* **Waiting for AML Verification** — an automatic AML check is being conducted
* **AML Check Failed** — the details or transaction hash did not pass the AML check
* **Waiting for Details from Merchant** — the details for the request are being gathered on the merchant's side
* **Merchant Error** — the merchant was unable to provide details for the request
* **Error in Request** — the request was not created
* **Auto-Payout Error** — status for manual transfer by the operator when payout for the request is not possible
* **Auto-Payout Error (Payment System API)** — error in fund payout on the merchant's side (insufficient funds, incorrect settings for the auto-payout module, etc.)
* **Waiting for Confirmation from Auto-Payout Module** — the payout from the exchanger has been completed, awaiting payment confirmation on the merchant's side
* **Partial Payout** — a partial payout has been made for the request
* **Completed Request** — the request has been fully completed