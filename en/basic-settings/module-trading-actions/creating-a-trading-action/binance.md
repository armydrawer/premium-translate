# Binance

## Authorization in the Module

<figure><img src="../../../../ru/.gitbook/assets/image (692) (1).png" alt="" width="453"><figcaption></figcaption></figure>

**API Key** — a key generated in your Binance personal account.

**Secret Key** — a secret key generated in your Binance personal account.

For trading actions, it is recommended to generate a separate key with the necessary permissions, especially if you are already using Binance as a merchant and/or for auto-payouts.

The permissions required to work with all module functions are highlighted below.

<figure><img src="../../../../ru/.gitbook/assets/image (693) (1).png" alt=""><figcaption></figcaption></figure>

## General Parameters:

<figure><img src="../../../../ru/.gitbook/assets/image (700) (1).png" alt="" width="563"><figcaption></figcaption></figure>

**Execution Order** — the order in which actions are performed (if multiple trading actions are involved for the same exchange directions). Specify values from [1 to 10](#user-content-fn-1)[^1] for each trading action involved. Leave the field empty if you are using only one action.

<figure><img src="../../../../ru/.gitbook/assets/image (614) (1).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../../ru/.gitbook/assets/image (615) (1).png" alt="" width="563"><figcaption></figcaption></figure>

**Assign Actions** — select the status of the request upon reaching which the action will be executed. Only one option should be selected.

{% hint style="info" %}
We recommend using the "After status **Paid Request**" option for the "**Buy**" and "**Sell**" actions.
{% endhint %}

**Exchange Directions** — select the exchange directions for which trading actions will be performed when working with requests. You can select multiple directions with the same currency in the "**Give**" or "**Receive**" fields simultaneously.

**Error Margin (%)** — specify the error margin percentage (numbers only) for the amount in the request that the action will be based on. Typically, values range from 0.1 to 0.5 (the optimal value is 0.15).

<figure><img src="../../../../ru/.gitbook/assets/image (616) (1).png" alt="" width="307"><figcaption></figcaption></figure>

## Step "Borrow Funds"

<figure><img src="../../../../ru/.gitbook/assets/image (696) (1).png" alt="" width="515"><figcaption></figcaption></figure>

**Enabled:**\
• **Yes**\
• **No**

**Currency Code** — specify the currency code to <mark style="color:yellow;">**borrow**</mark> in this step.

**Network** — specify the network for the currency from the "**Currency Code**" field (optional, only required if the currency has a network).

**Trading Currency Code** — specify the currency code you need to lend to the exchange as a deposit for borrowing the selected currency (from the "**Currency Code**" field).

**Amount** — select the type of amount from the request that will be passed to this step.\
![](<../../../../ru/.gitbook/assets/image (702) (1).png>)

{% hint style="warning" %}
Choose the amount from the "**Give**" or "**Receive**" side depending on the currency you plan to work with (the currency pair side must match the currency specified in the "**Currency Code**" field).

If the "**Payment Amount**" or "**Payout Amount**" fields are empty (e.g., no payment/payout was made via the connected merchant in the exchange direction), the values will default to 0. If the trading action amount is set to "**Payment Amount**" or "**Payout Amount**" and a trading action is triggered, an error will occur because the amount will be 0.

If you encounter a trading action error due to this, edit the amount in the request (go to the "**Requests**" section, click "**Edit**",\
![](../../../.gitbook/assets/image%20\(376\)_eng.png)

enter the correct amount in the relevant field, save the changes, and manually trigger the trading action by clicking the "**Action Link**" in the "**Trading Actions**" -> "**Requests**" section. The trading action will then be executed.
{% endhint %}

**If the amount is incorrect:**\
• **Error** — the step will not be executed (recommended).\
• **Proceed** — the step will be executed despite the amount mismatch.

**Min. Amount** — the minimum amount for this trading step (specified in the currency being operated on).

**Max. Amount** — the maximum amount for this trading step (specified in the currency being operated on).

**Add Withdrawal Fee** — select "**No**".\
• **Yes**\
• **No**

**Add Trading Fee** — select "**No**".\
• **Yes**\
• **No**

**Transfer to Spot Account** — transfer the borrowed amount to the spot account.\
• **Yes**\
• **No**

## Step "Repay Debt"

<figure><img src="../../../../ru/.gitbook/assets/image (697) (1).png" alt="" width="506"><figcaption></figcaption></figure>

**Enabled:**\
• **Yes**\
• **No**

**If the amount is incorrect:**\
• **Error** — the step will not be executed (recommended).\
• **Proceed** — the step will be executed despite the amount mismatch.

**Transfer to Margin Account** — transfer funds to the margin account to repay the debt.\
• **Yes**\
• **No**

**Currency Code** — specify the currency code to <mark style="color:orange;">**repay the debt**</mark> in this step.

{% hint style="warning" %}
The currency code must match:

* The payment currency code from the client’s request if "**Payment Amount**" or any "**Give/Giving**" option is selected in the "**Amount**" field.
* The payout currency code from the client’s request if "**Payout Amount**" or any "**Receive/Receiving**" option is selected in the "**Amount**" field.
{% endhint %}

**Amount** — select the type of amount from the request that will be passed to this step.\
![](<../../../../ru/.gitbook/assets/image (702) (1).png>)

{% hint style="warning" %}
Choose the amount from the "**Give**" or "**Receive**" side depending on the currency you plan to work with (the currency pair side must match the currency specified in the "**Currency Code**" field).
{% endhint %}

**Min. Amount** — the minimum amount for this trading step (specified in the currency being operated on).

**Max. Amount** — the maximum amount for this trading step (specified in the currency being operated on).

## Step "Sell"

<figure><img src="../../../../ru/.gitbook/assets/image (695) (1).png" alt="" width="518"><figcaption></figcaption></figure>

**Enabled:**\
• **Yes**\
• **No**

**If the amount is incorrect:**\
• **Error** — the step will not be executed (recommended).\
• **Proceed** — the step will be executed despite the amount mismatch.

**Trading Account** — the account from which the currency will be sold.\
• **Spot** — spot account.\
• **Margin** — margin account.

**Borrow Funds** — if your account lacks sufficient funds, you can borrow from the exchange (only applicable if the margin account is selected in the previous parameter). You can then repay the debt manually or via the "**Repay Debt**" step.\
• **No** — no borrowing will occur.\
• **Full Amount** — borrow the full amount from the request.\
• **Required Amount** — borrow only the missing amount.

**Transfer to Account** — transfer funds to the selected account.\
• **Spot** — spot account.\
• **Margin** — margin account.

**Currency Code** — specify the currency code to <mark style="color:red;">**sell**</mark> in this step to purchase the currency specified in the "**Trading Currency Code**" field.

{% hint style="warning" %}
The currency code must match:

* The payment currency code from the client’s request if "**Payment Amount**" or any "**Give/Giving**" option is selected in the "**Amount**" field.
* The payout currency code from the client’s request if "**Payout Amount**" or any "**Receive/Receiving**" option is selected in the "**Amount**" field.
{% endhint %}

**Network** — specify the network for the currency from the "**Currency Code**" field (optional, only required if the currency has a network). If the currency does not have a network, leave the field empty.

**Trading Currency Code** — specify the currency code to <mark style="color:green;">**buy**</mark> in this step (usually USDT).

**Amount** — select the type of amount from the request that will be passed to this action (when selling the incoming currency from the client, choose one of the "**Give/Giving Amount**" options or the "**Payment Amount**" option).\
![](<../../../../ru/.gitbook/assets/image (702) (1).png>)

{% hint style="warning" %}
Choose the amount from the "**Give**" or "**Receive**" side depending on the currency you plan to work with (the currency pair side must match the currency specified in the "**Currency Code**" field).
{% endhint %}

**Min. Amount** — the minimum amount for this trading step (specified in the currency being operated on). If the amount from the request is below the specified minimum, the step will not be executed.

### Maximum Amount

The **Maximum Amount** is the highest permissible sum for this trading step (specified in the currency used for operations). If the amount in the request exceeds the specified maximum, the step will not be executed.

### Add Withdrawal Fee

For the **Sell** action, select **No**:\
• **Yes**\
• **No**

### Add Trading Fee

For the **Sell** action, select **No**:\
• **Yes**\
• **No**

***

## Step: "Buy"

<figure><img src="../../../../ru/.gitbook/assets/image (698) (1).png" alt="" width="504"><figcaption></figcaption></figure>

### Enabled:

• **No** — the step is not used\
• **Full Amount** — purchase the full amount from the request\
• **Required Amount** — purchase only the missing amount (the balance of the selected currency in your merchant account will be taken into account)

### If the Amount is Not Suitable:

• **Error** — the step will not be executed (recommended)\
• **Proceed** — the step will be executed even if the amount does not match

### Trading Account

The account where the currency will be purchased:\
• **Spot** — spot account\
• **Margin** — margin account

### Borrow Funds

If your account lacks sufficient funds, you can borrow from the exchange (only if the **Margin** account is selected in the previous parameter). The debt can be repaid manually or using the "**Repay Debt**" step:\
• **No** — no borrowing will occur\
• **Full Amount** — borrow the full amount from the request\
• **Required Amount** — borrow only the missing amount

### Borrowing Currency

Choose the currency to borrow:\
• **Currency Code** — the currency specified in the "**Currency Code**" field for this step\
• **Trading Currency Code** — the currency specified in the "**Trading Currency Code**" field for this step

### Transfer to Account

Transfer funds to the selected account:\
• **No** — no transfer will occur\
• **Spot** — transfer to the spot account\
• **Margin** — transfer to the margin account

### Currency Code

Specify the code of the currency you want to <mark style="color:green;">**buy**</mark> in this step.

{% hint style="warning" %}
The currency code must match:

* The payment currency code from the client’s request if the "**Amount**" field is set to "**Payment Amount**" or any of the "**Give/Giving**" options.
* The payout currency code from the request if the "**Amount**" field is set to "**Payout Amount**" or any of the "**Receive/Receiving**" options.
{% endhint %}

### Network

Specify the network for the currency in the "**Currency Code**" field (optional, only if the currency has an associated network).

### Trading Currency Code

Specify the code of the currency you want to <mark style="color:red;">**sell**</mark> in this step to purchase the currency specified in the "**Currency Code**" field.

### Amount

Select the type of amount from the request to be passed to this step:\
![](<../../../../ru/.gitbook/assets/image (702) (1).png>)

{% hint style="warning" %}
Choose the amount from the "**Giving**" or "**Receiving**" side, depending on the currency you plan to work with. The currency side in the pair must match the currency specified in the "**Currency Code**" field.
{% endhint %}

### Minimum Amount

The minimum permissible amount for this trading step (specified in the currency being purchased in this step, as per the "**Currency Code**" field). If the amount in the request is below this minimum, the step will not be executed.

### Maximum Amount

The maximum permissible amount for this trading step (specified in the currency being purchased in this step, as per the "**Currency Code**" field). If the amount in the request exceeds this maximum, the step will not be executed.

### Add Withdrawal Fee

• **Yes** — select **Yes** if the newly purchased currency is to be paid out via the [Binance Auto-Payout Module](https://premium.gitbook.io/main/en/basic-settings/merchants-and-auto-payments/auto-payments/binance).\
• **No**

### Add Trading Fee

Select **Yes**:\
• **Yes**\
• **No**

***

## Step: "Transfer to Account"

<figure><img src="../../../../ru/.gitbook/assets/image (699) (1).png" alt="" width="509"><figcaption></figcaption></figure>

### Enabled:

• **Yes**\
• **No**

### Transfer to Account:

• **Spot -> Margin** — transfer from the spot account to the margin account\
• **Margin -> Spot** — transfer from the margin account to the spot account

### Currency Code

Specify the code of the currency to <mark style="color:blue;">**transfer**</mark> between accounts in this step.

### Network

Specify the network for the currency in the "**Currency Code**" field (optional, only if the currency has an associated network).

### Trading Currency Code

Specify the code of the currency to be transferred in the opposite direction.

### Amount

Select the type of amount from the request to be passed to this step:\
![](<../../../../ru/.gitbook/assets/image (702) (1).png>)

### Add Withdrawal Fee

Select **No**:\
• **Yes**\
• **No**

### Add Trading Fee

Select **No**:\
• **Yes**\
• **No**

***

## Proxy Settings

If your server’s IP address does not have access to the exchange you plan to work with, purchase a proxy and enter its details in the specified block.

<figure><img src="../../../.gitbook/assets/image (1411)_eng.png" alt="" width="446"><figcaption></figcaption></figure>

* **IP Address** — the proxy server’s address
* **Port** — the proxy server’s port
* **Login** — your login credentials for the proxy server
* **Password** — your password for the proxy server
* **Disable Proxy Tunnel** — disable this option if the above fields are filled:\
  • **No**\
  • **Yes**

[^1]: 1 - highest priority\
    2 - second priority, and so on.
