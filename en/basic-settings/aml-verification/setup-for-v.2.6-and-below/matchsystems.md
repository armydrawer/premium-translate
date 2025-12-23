# Matchsystems

## **Authorization**

Download the script distribution for updating your version (2.5 or 2.6) from the link [premiumexchanger.com/uscript/](http://premiumexchanger.com/uscript/) and upload the folder `wp-content/plugins/premiumbox/moduls/matchsystems` to the server at the same path (using the <mark style="color:$success;">**website user**</mark>, not as <mark style="color:red;">**root**</mark>!).

After installing the module, activate it in the "**Modules**" section, then navigate to "**Modules**" ➔ "**Matchsystems**" in the sidebar.

<figure><img src="../../../.gitbook/assets/изображение (25).png" alt=""><figcaption></figcaption></figure>

**Domain** — leave this field empty.

**API Key** — the key provided to you by a service representative.

## Module Settings

* **Critical Risk Level** is important for automatic mode. If the check of outgoing or incoming client addresses shows a risk level above the critical threshold (recommended — 50%), the admin panel will not allow the creation of such a request.

On this page, you can also manually check any address or TxID that is not associated with requests.

<figure><img src="../../../.gitbook/assets/изображение (1) (1).png" alt=""><figcaption></figcaption></figure>

## **Manual Request Verification**

In the "**Requests**" section, you can manually check the risk of an address:

* for requests that have a merchant account and transaction (based on the transaction)
* for requests that have a "**Sending**" wallet
* for requests that have a "**Receiving**" wallet

To manually check the risk in a request, click on the "**Check**" link.

By clicking on the risk assessment (50% in the screenshot), you can see the components of the risk score.

## **Setting Up Automatic Mode**

Automatic mode is enabled for exchange directions. Let's demonstrate this with the example of the Bitcoin BTC to Ethereum ETH direction.

In the exchange direction settings, find the "**Matchsystems**" tab and configure the checks for accounts/addresses and/or incoming transactions.

<figure><img src="../../../.gitbook/assets/Screenshot_19 (3).png" alt=""><figcaption></figcaption></figure>

If you want to automatically check the outgoing address (client's payout address) in the request, set the "**Check Sending Account**" field to "**Yes**," and in the **"Exchange Amount 'from'"** field, specify the minimum amount for which the check should be performed in the currency of the address.

For example, if you set 0.005 for this direction, it means that the outgoing address of the request will be checked for requests of 0.005 BTC and above. If the client's address has a risk level above the critical threshold (see point 1), then such a request cannot be created.

If you want to check the incoming address in the request, set the "**Check Sending Account**" field to "**Yes**" and specify the minimum amount for the check in the **"Exchange Amount 'from'"** field.

You can also automatically check incoming transactions.

We recommend checking TxID and outgoing addresses for amounts greater than 10 USD for directions involving BTC, ETH, and USDT.

## **Displaying AML Risk to Users**

If you want to display the AML risk to your users to facilitate communication in case of disputes, we recommend enabling the display of verification results on the request page.

To do this, in the "**Exchange Directions**" - "**Currency Exchange Templates**" section, add the shortcodes below to the relevant templates for display in the request and save the changes.

<figure><img src="../../../.gitbook/assets/изображение (115).png" alt=""><figcaption></figcaption></figure>
