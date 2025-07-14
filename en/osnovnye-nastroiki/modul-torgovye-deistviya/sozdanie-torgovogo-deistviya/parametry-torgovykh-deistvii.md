# Trading Action Parameters

{% hint style="info" %}
The set of parameters and steps in the trading actions module varies between different exchanges. If a parameter or an entire step described below is missing in the trading action you are configuring, this is normal — you can simply skip that part of the instructions.

**The screenshots below show the interface when working with the Binance exchange.**
{% endhint %}

## Authorization in the Module

<figure><img src="../../../.gitbook/assets/image (692).png" alt=""><figcaption></figcaption></figure>

**API Key** — the key generated in your Binance account dashboard

**Secret Key** — the secret key generated in your Binance account dashboard

For trading actions, it is recommended to create a separate API key with the necessary permissions, especially if you are already using Binance as a merchant and/or for automatic payouts.

The permissions required to use all the module’s features are highlighted below.

<figure><img src="../../../.gitbook/assets/image (693).png" alt=""><figcaption></figcaption></figure>

## General Parameters:

<figure><img src="../../../.gitbook/assets/image (700).png" alt="" width="563"><figcaption></figcaption></figure>

**Execution Order** — defines the order in which actions will be performed (if multiple trading actions are set up for the same exchange directions). Enter a value from [1 to 10](#user-content-fn-1)[^1] for each active trading action. Leave this field empty if you are using only one action.

<figure><img src="../../../.gitbook/assets/image (614).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (615).png" alt="" width="563"><figcaption></figcaption></figure>

**Assign Actions** — select the order status upon reaching which the action will be executed. Only one option should be selected.

{% hint style="info" %}
We recommend using the status "After 'Paid Order'" for the actions "Buy" and "Sell".
{% endhint %}

**Exchange Directions** — select the exchange directions for which trading actions will be performed when processing orders. You can select multiple directions involving the same currency either in the "Giving" or "Receiving" fields simultaneously.

**Tolerance Percentage (%)** — specify the tolerance percentage (numbers only) for the order amount on which the action will be based. Typically, a value between 0.1 and 0.5 is used (the optimal value is 0.15).

Here is a naturalistic English translation of the provided text:

---

## Step: "Borrow"

**Enabled:**  
• **Yes**  
• **No**

**Currency Code** — specify the currency code that needs to be **borrowed** in this step.

**Network** — specify the network for the currency from the "**Currency Code**" field (optional, only if the currency has a network).

**Trading Currency Code** — specify the currency code that you need to lend to the exchange as a deposit in order for the exchange to lend you the currency selected in the "**Currency Code**" field.

**Amount** — select the type of amount from the order that will be passed to this step.  
![](../../../.gitbook/assets/image%20(702).png)

{% hint style="danger" %}
Choose the amount from either the "**Give**" or "**Receive**" side depending on which currency you plan to work with (the side of the currency pair must match the currency you specify in the "**Currency Code**" field).

The fields "**Payment Amount**" and "**Payout Amount**" are recorded by the merchant module for receiving/auto-payout and only work if these values are not empty (i.e., a payment/payout was made through a merchant connected in the direction).

If merchants for receiving/auto-payout are not connected in the exchange direction, the payment/payout values will be zero. If you select "**Payment Amount**" or "**Payout Amount**" as the amount for the trading action under these conditions, the trading action will fail because it will attempt to execute with an amount of zero.

If you have already encountered an error related to this issue, edit the relevant amount in the order (go to the "**Orders**" section, click "**Edit**",  
![](../../../.gitbook/assets/image%20(376).png)  

enter the correct amount in the appropriate field, save the changes, and manually trigger the trading action by clicking the "**Action Link**" in the "**Trading Actions**" -> "**Orders**" section). The trading action will then be executed successfully.
{% endhint %}

---

Let me know if you need any further adjustments!

Here is a natural, fluent English translation of the provided text:

---

**If the amount does not match:**  
• **Error** — the step will not be executed (recommended)  
• **Continue** — the step will be executed despite the amount mismatch

**Min. amount** — the minimum amount for this trading step (specified in the currency used for the operations)

**Max. amount** — the maximum amount for this trading step (specified in the currency used for the operations)

**Add withdrawal fee** — select "**No**"  
• **Yes**  
• **No**

**Add trading fee** — select "**No**"  
• **Yes**  
• **No**

**Transfer to Spot account** — transfer the borrowed amount to the spot account  
• **Yes**  
• **No**

## Step: "Repay Debt"

<figure><img src="../../../.gitbook/assets/image (697).png" alt="" width="506"><figcaption></figcaption></figure>

**Enabled:**  
• **Yes**  
• **No**

**If the amount does not match:**  
• **Error** — the step will not be executed (recommended)  
• **Continue** — the step will be executed despite the amount mismatch

**Transfer to Margin account** — transfer funds to the margin account to repay the debt  
• **Yes**  
• **No**

**Currency code** — specify the currency code for the debt repayment in this step

{% hint style="warning" %}
The currency code must match:

* the client’s payment currency code from the order if "**Amount**" is set to "**Payment amount**" or any of the "**Giving**" options  
* the payout currency code from the order if "**Amount**" is set to "**Payout amount**" or any of the "**Receiving**" options  
{% endhint %}

**Amount** — select the amount type from the order that will be passed to this step  
![](<../../../.gitbook/assets/image (702).png>)

{% hint style="warning" %}
Choose the amount from the "**Giving**" or "**Receiving**" side depending on which currency the actions will be performed with (the currency side must match the currency you specify in the "**Currency code**" field)  
{% endhint %}

**Min. amount** — the minimum amount for this trading step (specified in the currency used for the operations)

**Max. amount** — the maximum amount for this trading step (specified in the currency used for the operations)

---

If you need the translation adapted for a specific audience or style, please let me know!

## Step: "Sell"

<figure><img src="../../../.gitbook/assets/image (695).png" alt="" width="518"><figcaption></figcaption></figure>

**Enabled:**  
• **Yes**  
• **No**

**If the amount does not match:**  
• **Error** — the step will not be executed (recommended)  
• **Continue** — the step will be executed despite the amount mismatch

**Trading account** — the account from which the currency will be sold  
• **Spot** — spot account  
• **Margin** — margin account

**Borrow funds** — if your account has insufficient or no funds, you can borrow from the exchange (only available if the margin account is selected in the previous setting), then repay the loan manually or using the "**Repay Debt**" step  
• **No** — no borrowing will occur  
• **Full amount** — purchase the full amount specified in the order  
• **Required amount** — purchase only the shortfall amount

**Transfer to account** — transfer funds to the selected account  
• **Spot** — spot account  
• **Margin** — margin account

**Currency code** — specify the code of the currency to be <mark style="color:red;">**sold**</mark> in this step in order to buy the currency specified in "**Trading currency code**"

{% hint style="warning" %}
The currency code must match:

* the payment currency code from the client’s order if "**Amount**" is set to "**Payment amount**" or any of the "**Give/Give away**" options  
* the payout currency code from the order if "**Amount**" is set to "**Payout amount**" or any of the "**Receive/Receive**" options  
{% endhint %}

**Network** — specify the network for the currency from "**Currency code**" (optional; only if the currency has a network). Leave blank if the currency has no network.

**Trading currency code** — specify the code of the currency to be <mark style="color:green;">**bought**</mark> in this step (usually USDT)

**Amount** — select the type of amount from the order that will be passed to the chosen action (when selling the currency received from the client, choose one of the "**Amount Give/Give away ...**" options or the "**Payment amount**" option)  
![](<../../../.gitbook/assets/image (702).png>)

{% hint style="warning" %}
Select the amount from either the "**Giving**" or "**Receiving**" side depending on which currency you plan to use (the side of the currency pair must match the currency you specify in the "**Currency Code**" field).
{% endhint %}

**Min. amount** — the minimum amount for this trading step (specified in the currency being used for the operation). If the order amount is less than this minimum, the step will not be executed.

**Max. amount** — the maximum amount for this trading step (specified in the currency being used for the operation). If the order amount exceeds this maximum, the step will not be executed.

**Add withdrawal fee** — for the "**Sell**" action, select "**No**"\
• **Yes**\
• **No**

**Add trading fee** — for the "**Sell**" action, select "**No**"\
• **Yes**\
• **No**

## Step "Buy"

<figure><img src="../../../.gitbook/assets/image (698).png" alt="" width="504"><figcaption></figcaption></figure>

**Enabled:**\
• **No** — step is not used\
• **Full amount** — buy the full amount from the order\
• **Required amount** — buy only the missing amount (your merchant account balance in the selected currency will be taken into account)

**If the amount doesn’t match:**\
• **Error** — the step will not be executed (recommended)\
• **Continue** — the step will be executed despite the amount mismatch

**Trading account** — the account where the currency will be purchased\
• **Spot** — spot account\
• **Margin** — margin account

**Borrow funds** — if your account balance is insufficient or zero, you can borrow from the exchange (only if the margin account is selected in the previous option), then repay the loan manually or using the "**Repay Debt**" step\
• **No** — no borrowing will occur\
• **Full amount** — borrow the full amount from the order\
• **Required amount** — borrow only the missing amount

**Borrowing Currency** — the choice of currency to borrow  
• **Currency Code** — the currency from the "**Currency Code**" field in this step  
• **Trading Currency Code** — the currency from the "**Trading Currency Code**" field in this step  

**Transfer to Account** — transfer of funds to the selected account  
• **None** — transfer is not used  
• **Spot** — spot account  
• **Margin** — margin account  

**Currency Code** — specify the currency code of the currency to be **bought** in this step  

{% hint style="warning" %}
The currency code must match:  

* the payment currency code from the client’s request if "**Amount**" is set to "**Payment Amount**" or any of the "**Giving**" options  
* the payout currency code from the request if "**Amount**" is set to "**Payout Amount**" or any of the "**Receiving**" options  
{% endhint %}

**Network** — specify the network for the currency indicated in "**Currency Code**" (optional; only required if the currency has an associated network)  

**Trading Currency Code** — specify the currency code of the currency to be **sold** in this step in order to buy the currency specified in "**Currency Code**"  

**Amount** — select the type of amount from the request that will be passed to this step  
![](<../../../.gitbook/assets/image (702).png>)  

{% hint style="warning" %}
Choose the amount from the "**Giving**" or "**Receiving**" side depending on which currency the operation involves (the currency side in the pair must match the currency you specify in the "**Currency Code**" field)  
{% endhint %}

**Min. Amount** — the minimum amount for this trading step (specified in the currency being transacted). If the amount from the request is below this minimum, the step will not be executed.  

**Max. Amount** — the maximum amount for this trading step (specified in the currency being transacted). If the amount from the request exceeds this maximum, the step will not be executed.

**Add Withdrawal Fee** —  
• **Yes** — select "**Yes**" if you plan to pay out newly purchased currency for the order via the [Binance Auto-Payout Module](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/binance)  
• **No**

**Add Trading Fee** — select "**Yes**"  
• **Yes**  
• **No**

## **"Transfer Between Accounts" Step**

<figure><img src="../../../.gitbook/assets/image (699).png" alt="" width="509"><figcaption></figcaption></figure>

**Enabled:**  
• **Yes**  
• **No**

**Transfer Between Accounts:**  
• **Spot -> Margin** — transfer from spot account to margin account  
• **Margin -> Spot** — transfer from margin account to spot account

**Currency Code** — specify the currency code to be **transferred** between accounts in this step

**Network** — specify the network for the currency from the "**Currency Code**" field (optional; only required if the currency supports networks)

**Trading Currency Code** — specify the currency code that will be transferred in the opposite direction

**Amount** — select the type of amount from the order that will be passed to this step  
![](<../../../.gitbook/assets/image (702).png>)

**Add Withdrawal Fee** — select "**No**"  
• **Yes**  
• **No**

**Add Trading Fee** — select "**No**"  
• **Yes**  
• **No**

## **Proxy Settings**

If your server’s IP address cannot access the exchange you plan to work with, purchase a proxy and enter its details in the section below.

<figure><img src="../../../.gitbook/assets/image (1411).png" alt="" width="446"><figcaption></figcaption></figure>

* **IP Address** — proxy server address  
* **Port** — proxy server port  
* **Username** — your login for proxy server access  
* **Password** — your password for proxy server access  
* **Disable Proxy Tunnel** — disable this option if the fields above are filled in  
  • **No**  
  • **Yes**

[^1]: 1 - highest priority  
    2 - second priority action, and so on