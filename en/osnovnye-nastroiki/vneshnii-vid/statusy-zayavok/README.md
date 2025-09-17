# Application Statuses

The **Applications** section displays exchange requests and their statuses.

<figure><img src="../../../.gitbook/assets/изображение (189).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/изображение (41).png" alt=""><figcaption></figcaption></figure>

In this section, you will see a list of all applications along with their IDs. Applications that have been paid by the user are marked with the statuses "**Paid Application**," "**Application Under Review**," or "**User Marked Application as Paid**."

For semi-automatic exchanges, you need to verify whether the corresponding amount has been transferred to your wallet. Once confirmed, transfer the specified amount to the user's wallet as indicated in the application details.&#x20;

{% hint style="info" %}
Please note that for each application, the amounts to be transferred to the client are displayed both with and without the commission. Typically, you should transfer the amount that includes the commission. However, some payment systems charge the commission to the recipient (i.e., the client). In such cases, you should transfer the amount without the commission.
{% endhint %}

Next, select the application you have processed, choose "**Completed Application**" in the "**Actions**" field, and click the "**Apply**" button. The user will be notified that the exchange has been processed.

For automatic exchanges, the system will automatically transfer the funds to the client for applications with the status "**Paid Application**."

Applications with the status "**Application Under Review**" will be processed automatically based on the settings for automatic exchanges.

Applications with the status "**User Marked Application as Paid**" must be processed manually.

The status "**Erroneous Application**" can be used in cases of errors, such as when the client provides incorrect payment details. In automatic exchange mode, this status may also appear if there are issues with the automatic payout for the application.

The status "**Application Under Review**" can also be used when the information in the application requires additional verification by the site administrator. This status is automatically assigned when payment is made via a merchant and the wallet number used for payment does not match the wallet number specified when the application was created. This verification can be disabled in the settings for each merchant.

If needed, you can create your own custom status in the "**Application Statuses**" section located in the console menu.