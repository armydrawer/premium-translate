# Application Statuses

In the "**Applications**" section, you can view the exchange requests and their statuses.

<figure><img src="../../../../ru/.gitbook/assets/image (189) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image%20(41)_eng.png" alt=""><figcaption></figcaption></figure>

In this section, you will see a list of all applications along with their IDs. Applications that have been paid by the user will show statuses such as "**Paid Application**," "**Application Under Review**," and "**User Marked Application as Paid**."

For semi-automatic exchanges, you should check whether the corresponding amount has been transferred to your wallet. After that, you need to transfer the specified amount to the user's wallet. This amount is also indicated in the application details.

{% hint style="info" %}
Please note that for each application, the amounts to be transferred to the client are displayed both with and without fees. Generally, you should transfer the amount that includes the fee. Some payment systems charge a fee to the recipient of the payment, i.e., the client, in which case you should send the amount without the fee.
{% endhint %}

Next, select the application you have processed, choose "**Completed Application**" from the "**Actions**" dropdown, and click the "**Apply**" button. The user will be notified about the processing of this exchange.

In the case of automatic exchanges, the system will automatically transfer the funds to the client for applications with the status "**Paid Application**."

Applications with the status "**Application Under Review**" will be processed automatically based on the settings for automatic exchanges.

Applications marked as "**User Marked Application as Paid**" need to be processed manually.

You can use the status "**Error Application**" in case of a mistake, for example, if the client provided incorrect details. In automatic operation mode, this status may appear if there are issues with the automatic payout of funds for the application.

The status "**Application Under Review**" can be used when the information for this application requires additional verification by the site administrator. This status is also automatically set when payment is made using a merchant if the wallet number from which the payment was made does not match the wallet number provided when creating the application. This verification can be disabled in the settings of each merchant.

If necessary, you can create your own status in the "**Application Statuses**" section found in the console menu.
