# AMLBot

{% hint style="info" %}
To use the service, you need to purchase a [plan](https://amlbot.com/ru/api-integration) that is at least Standard

($500 for 1,000 checks or $3,600 for 12,000 checks per year)

![](<../../../.gitbook/assets/image (1238)_eng.png>)\
![](<../../../.gitbook/assets/image (1167)_eng (1).png>)
{% endhint %}

## **AMLBot Module Settings**

You can download the script distribution for updates or a separate folder at wp-content/plugins/premiumbox/moduls/amlbot from [premiumexchanger.com/uscript/](http://premiumexchanger.com/uscript/).

After installing the module, go to the "**Modules**" section and select "**AML Bot**".

<figure><img src="../../../.gitbook/assets/Screenshot_12 (1) (1).png" alt=""><figcaption></figcaption></figure>

In this module settings section, you need to enter your ID and key. You can obtain your ID and key after registering on the [AMLBot website](https://web.amlbot.com/account).

* The **Critical Risk Level** is important for the automatic mode. If the check of an outgoing or incoming address shows a risk higher than the critical level (recommended — 50%), the admin panel will not allow the creation of such a request.

<figure><img src="../../../.gitbook/assets/Screenshot_14 (1) (1).png" alt=""><figcaption></figcaption></figure>

On this page, you can manually check any address or TxID that is not related to requests.

<figure><img src="../../../.gitbook/assets/Screenshot_15 (2) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/Screenshot_16 (4) (1).png" alt=""><figcaption></figcaption></figure>

## **Manual Request Checks**

In the "**Requests**" section, you can manually check the risk of an address:

* for requests that have a merchant account and a transaction (based on the transaction)
* for requests that have a "Sending" wallet
* for requests that have a "Receiving" wallet

To manually check the risk in a request, click on the "**Check**" link.

<figure><img src="../../../.gitbook/assets/Screenshot_17 (3) (1).png" alt=""><figcaption></figcaption></figure>

By clicking on the risk score (20% in the screenshot), you can see the components of the risk assessment.

<figure><img src="../../../.gitbook/assets/Screenshot_18 (2) (1).png" alt=""><figcaption></figcaption></figure>

## **Setting Up Automatic Mode**

Automatic mode is enabled in the exchange directions. Let's demonstrate this using the example of the Bitcoin BTC to Ethereum ETH exchange. In the exchange direction, find the "**AML Bot**" tab.

<figure><img src="../../../.gitbook/assets/Screenshot_19 (3) (1).png" alt=""><figcaption></figcaption></figure>

If you want to automatically check the outgoing address (the client's payout address) in the request, set the "**Check Sending Account**" field to "**Yes**," and in the **"Exchange Amount 'from'"** field, specify the minimum amount for the check in the currency of the address.

For example, if you set 0.005 for this direction, it means that the outgoing address will be checked for requests of 0.005 BTC and above. If the client's address has a risk higher than critical (see point 1), such a request cannot be created.

If you want to check the incoming address in the request, set the "**Check Sending Account**" field to "**Yes**" and specify the minimum amount for the check in the **"Exchange Amount 'from'"** field.

You can also automatically check incoming transactions.

We recommend checking TxID and outgoing addresses for amounts greater than $10 for directions involving BTC, ETH, and USDT.

## **Displaying AML Risk to Users of the Exchange**

If you want to display the AML risk to your users to facilitate communication in case of disputes, we recommend enabling the display on the request page.

<figure><img src="../../../.gitbook/assets/Screenshot_20 (1) (1).png" alt=""><figcaption></figcaption></figure>

To do this, in the "**Exchange Directions**" section, under the "**User Information**" tab, set the tag **\[AML Risk]** in the fields **"Request Status 'Paid Request'"** and **"Request Status 'Completed Request'"**.

<figure><img src="../../../.gitbook/assets/image (1116)_eng.png" alt=""><figcaption></figcaption></figure>
