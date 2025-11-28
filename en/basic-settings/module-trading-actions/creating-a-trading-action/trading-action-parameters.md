# Trading Action Parameters

{% hint style="info" %}
The set of parameters and steps in the trading actions module varies across different exchanges. If a parameter or an entire step described below is missing in the trading action you are configuring, this is completely normal — you can skip that section in the instructions.

**The screenshots below are based on working with Binance.**
{% endhint %}

## Authorization in the Module

<figure><img src="../../../.gitbook/assets/image (692) (1).png" alt=""><figcaption></figcaption></figure>

**API Key** — the key generated in your Binance account.

**Secret Key** — the secret key generated in your Binance account.

It is recommended to issue a separate key with the necessary permissions for trading actions, especially if you are already using Binance for merchant services and/or auto-payouts.

The permissions required for all module functions are highlighted below.

<figure><img src="../../../.gitbook/assets/image (693) (1).png" alt=""><figcaption></figcaption></figure>

## General Parameters:

<figure><img src="../../../.gitbook/assets/image (700) (1).png" alt="" width="563"><figcaption></figcaption></figure>

**Execution Order** — specifies the order in which actions are executed (if multiple trading actions are used for the same exchange directions). Enter values from [1 to 10](#user-content-fn-1)[^1] for each trading action involved. Leave the field empty if you are using only one action.

<figure><img src="../../../.gitbook/assets/image (614) (1).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (615) (1).png" alt="" width="563"><figcaption></figcaption></figure>

**Assign Actions** — select the application status at which the action will be executed. Only one option can be selected.

{% hint style="info" %}
We recommend using the "After status "**Paid Application**" option for "**Buy**" and "**Sell**" actions.
{% endhint %}

**Exchange Directions** — select the exchange directions for which trading actions will be executed when processing applications. You can select multiple directions with the same currency in either the "**Give**" or "**Receive**" fields simultaneously.

**Error Margin (%)** — specify the error margin percentage (only a number) for the application amount to be used in the action. Typically, a value between 0.1 and 0.5 is used (the optimal value is 0.15).

<figure><img src="../../../.gitbook/assets/image (616) (1).png" alt="" width="307"><figcaption></figcaption></figure>

## Step: "Borrow"

<figure><img src="../../../.gitbook/assets/image (696) (1).png" alt="" width="515"><figcaption></figcaption></figure>

**Enabled:**\
• **Yes**\
• **No**

**Currency Code** — specify the currency code to <mark style="color:yellow;">**borrow**</mark> in this step.

**Network** — specify the network for the currency from the "**Currency Code**" field (optional, only if the currency has a network).

**Trading Currency Code** — specify the currency code you need to provide to the exchange as collateral for borrowing the selected currency (field "**Currency Code**").

**Amount** — select the type of amount from the application to be used in this step.\
![](<../../../.gitbook/assets/image (702) (1).png>)

{% hint style="danger" %}
Choose the amount from the "**Give**" or "**Receive**" side depending on the currency involved in the action (the side of the currency pair must match the currency specified in the "**Currency Code**" field).

If the exchange direction does not have merchants connected for receiving/auto-payouts, the payment/payout amount will be 0. If the trading action amount is set to "**Payment Amount**" or "**Payout Amount**" in such cases, the trading action will fail because it will attempt to execute with an amount of 0.

If you encounter a trading action error related to this, edit the amount in the application (go to the "**Applications**" section, click "**Edit**",<br>

enter the correct amount in the required field, save the changes, and manually restart the trading action by clicking the "**Action Link**" in the "**Trading Actions**" -> "**Applications**" section. The trading action will then execute successfully.
{% endhint %}

**If the amount is incorrect:**\
• **Error** — the step will not be executed (recommended).\
• **Proceed** — the step will be executed despite the mismatch.

**Min. Amount** — the minimum amount for this trading step (specified in the currency being used).

**Max. Amount** — the maximum amount for this trading step (specified in the currency being used).

**Add Withdrawal Fee** — select "**No**"\
• **Yes**\
• **No**

**Add Trading Fee** — select "**No**"\
• **Yes**\
• **No**

**Transfer to Spot Account** — transfer the borrowed amount to the spot account.\
• **Yes**\
• **No**

## Step: "Repay Debt"

<figure><img src="../../../.gitbook/assets/image (697) (1).png" alt="" width="506"><figcaption></figcaption></figure>

**Enabled:**\
• **Yes**\
• **No**

**If the amount is incorrect:**\
• **Error** — the step will not be executed (recommended).\
• **Proceed** — the step will be executed despite the mismatch.

**Transfer to Margin Account** — transfer to the margin account to repay the debt.\
• **Yes**\
• **No**

**Currency Code** — specify the currency code to <mark style="color:orange;">**repay the debt**</mark> in this step.

{% hint style="warning" %}
The currency code must match:

* The payment currency code from the client’s application if "**Payment Amount**" or any "**Give/Giving**" option is selected in the "**Amount**" field.
* The payout currency code from the application if "**Payout Amount**" or any "**Receive/Receiving**" option is selected in the "**Amount**" field.
{% endhint %}

**Amount** — select the type of amount from the application to be used in this step.\
![](<../../../.gitbook/assets/image (702) (1).png>)

{% hint style="warning" %}
Choose the amount from the "**Give**" or "**Receive**" side depending on the currency involved in the action (the side of the currency pair must match the currency specified in the "**Currency Code**" field).
{% endhint %}

**Min. Amount** — the minimum amount for this trading step (specified in the currency being used).

**Max. Amount** — the maximum amount for this trading step (specified in the currency being used).

## Step: "Sell"

<figure><img src="../../../.gitbook/assets/image (695) (1).png" alt="" width="518"><figcaption></figcaption></figure>

**Enabled:**\
• **Yes**\
• **No**

**If the amount is incorrect:**\
• **Error** — the step will not be executed (recommended).\
• **Proceed** — the step will be executed despite the mismatch.

**Trading Account** — the account from which the currency will be sold.\
• **Spot** — spot account.\
• **Margin** — margin account.

**Borrow** — if your account lacks sufficient funds, you can borrow from the exchange (only available if the margin account is selected in the previous parameter). You can then repay the debt manually or using the "**Repay Debt**" step.\
• **No** — no borrowing will occur.\
• **Full Amount** — borrow the full amount from the application.\
• **Required Amount** — borrow only the missing amount.

**Transfer to Account** — transfer funds to the selected account.\
• **Spot** — spot account.\
• **Margin** — margin account.

**Currency Code** — specify the currency code to <mark style="color:red;">**sell**</mark> in this step to purchase the currency specified in the "**Trading Currency Code**" field.

{% hint style="warning" %}
The currency code must match:

* The payment currency code from the client’s application if "**Payment Amount**" or any "**Give/Giving**" option is selected in the "**Amount**" field.
* The payout currency code from the application if "**Payout Amount**" or any "**Receive/Receiving**" option is selected in the "**Amount**" field.
{% endhint %}

**Network** — specify the network for the currency from the "**Currency Code**" field (optional, only if the currency has a network). If the currency does not have a network, leave the field empty.

**Trading Currency Code** — specify the currency code to <mark style="color:green;">**buy**</mark> in this step (usually USDT).

**Amount** — select the type of amount from the application to be used in this action (when selling the incoming currency from the client, choose one of the "**Give/Giving Amount**" options or the "**Payment Amount**" option).\
![](<../../../.gitbook/assets/image (702) (1).png>)

Here’s a naturalistic English translation of the provided text:

***

{% hint style="warning" %}
Select the amount from either the "**Give**" or "**Receive**" side, depending on which currency you plan to work with (the side of the currency pair must match the currency you specify in the "**Currency Code**" field).
{% endhint %}

**Min. Amount** — the minimum amount for this trading step (specified in the currency being used for the operation). If the amount in the request is lower than the specified minimum, the step will not be executed.

**Max. Amount** — the maximum amount for this trading step (specified in the currency being used for the operation). If the amount in the request exceeds the specified maximum, the step will not be executed.

**Add withdrawal fee** — for the "**Sell**" action, select "**No**"\
• **Yes**\
• **No**

**Add trading fee** — for the "**Sell**" action, select "**No**"\
• **Yes**\
• **No**

***

## Step: "Buy"

<figure><img src="../../../.gitbook/assets/image (698) (1).png" alt="" width="504"><figcaption></figcaption></figure>

**Enabled:**\
• **No** — the step is not used\
• **Full Amount** — purchase the full amount from the request\
• **Required Amount** — purchase only the missing amount (the balance of the selected currency in your merchant account will be taken into account)

**If the amount doesn’t match:**\
• **Error** — the step will not be executed (recommended)\
• **Proceed** — the step will be executed even if the amount doesn’t match

**Trading Account** — the account where the purchased currency will be credited\
• **Spot** — spot account\
• **Margin** — margin account

**Borrow Funds** — if your account lacks sufficient funds, you can borrow from the exchange (only if the margin account (Margin) is selected in the previous parameter) and repay the debt manually or using the "**Repay Debt**" step\
• **No** — no borrowing will occur\
• **Full Amount** — borrow the full amount from the request\
• **Required Amount** — borrow only the missing amount

**Borrowing Currency** — select the currency to borrow\
• **Currency Code** — the currency specified in the "**Currency Code**" field for this step\
• **Trading Currency Code** — the currency specified in the "**Trading Currency Code**" field for this step

**Transfer to Account** — transfer funds to the selected account\
• **No** — no transfer will occur\
• **Spot** — spot account\
• **Margin** — margin account

**Currency Code** — specify the code of the currency you want to <mark style="color:green;">**buy**</mark> in this step

{% hint style="warning" %}
The currency code must match:

* the payment currency code from the client’s request if "**Payment Amount**" or any of the "**Give**" options is selected in the "**Amount**" field
* the payout currency code from the request if "**Payout Amount**" or any of the "**Receive**" options is selected in the "**Amount**" field
{% endhint %}

**Network** — specify the network for the currency in the "**Currency Code**" field (optional, only required if the currency has a network)

**Trading Currency Code** — specify the code of the currency you want to <mark style="color:red;">**sell**</mark> in this step to purchase the currency specified in the "**Currency Code**" field

**Amount** — select the type of amount from the request to be passed to this step\
![](<../../../.gitbook/assets/image (702) (1).png>)

{% hint style="warning" %}
Select the amount from either the "**Give**" or "**Receive**" side, depending on which currency you plan to work with (the side of the currency pair must match the currency you specify in the "**Currency Code**" field).
{% endhint %}

**Min. Amount** — the minimum amount for this trading step (specified in the currency being used for the operation). If the amount in the request is lower than the specified minimum, the step will not be executed.

**Max. Amount** — the maximum amount for this trading step (specified in the currency being used for the operation). If the amount in the request exceeds the specified maximum, the step will not be executed.

**Add withdrawal fee** —\
• **Yes** — select "**Yes**" if the newly purchased currency is to be paid out via the [Binance auto-payout module](https://premium.gitbook.io/main/en/basic-settings/merchants-and-auto-payments/auto-payments/binance)\
• **No**

**Add trading fee** — select "**Yes**"\
• **Yes**\
• **No**

***

## Step: "Transfer to Account"

<figure><img src="../../../.gitbook/assets/image (699) (1).png" alt="" width="509"><figcaption></figcaption></figure>

**Enabled:**\
• **Yes**\
• **No**

**Transfer to Account:**\
• **Spot -> Margin** — transfer from the spot account to the margin account\
• **Margin -> Spot** — transfer from the margin account to the spot account

**Currency Code** — specify the code of the currency you want to <mark style="color:blue;">**transfer**</mark> between accounts in this step

**Network** — specify the network for the currency in the "**Currency Code**" field (optional, only required if the currency has a network)

**Trading Currency Code** — specify the code of the currency to be transferred in the opposite direction

**Amount** — select the type of amount from the request to be passed to this step\
![](<../../../.gitbook/assets/image (702) (1).png>)

**Add withdrawal fee** — select "**No**"\
• **Yes**\
• **No**

**Add trading fee** — select "**No**"\
• **Yes**\
• **No**

***

## **Proxy Settings**

If your server’s IP address does not have access to the exchange you plan to work with, purchase a proxy and enter its details in the specified section.

<figure><img src="../../../.gitbook/assets/image (1411)_eng.png" alt="" width="446"><figcaption></figcaption></figure>

* **IP Address** — the proxy server’s IP address
* **Port** — the proxy server’s port
* **Login** — your login credentials for the proxy server
* **Password** — your password for the proxy server
* **Disable Proxy Tunnel** — disable this option if the above fields are filled\
  • **No**\
  • **Yes**

***

Let me know if you need further clarification!

[^1]: 1 - highest priority

    2 - second priority, and so on
