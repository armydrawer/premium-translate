# Binance

## Module Authorization

<figure><img src="../../../.gitbook/assets/image (692).png" alt="" width="453"><figcaption></figcaption></figure>

**API Key** — the key generated in your Binance account dashboard.

**Secret Key** — the secret key generated in your Binance account dashboard.

For trading operations, it is recommended to create a separate API key with the necessary permissions, especially if you are already using Binance as a merchant and/or for automatic payouts.

The permissions required for all module functions are highlighted below.

<figure><img src="../../../.gitbook/assets/image (693).png" alt=""><figcaption></figcaption></figure>

## General Settings:

<figure><img src="../../../.gitbook/assets/image (700).png" alt="" width="563"><figcaption></figcaption></figure>

**Execution Order** — the order in which actions will be performed (if multiple trading actions are set for the same exchange directions). Enter a value from [1 to 10](#user-content-fn-1)[^1] for each trading action involved. Leave this field empty if you are using only one action.

<figure><img src="../../../.gitbook/assets/image (614).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (615).png" alt="" width="563"><figcaption></figcaption></figure>

**Assign Actions** — select the order status upon reaching which the action will be executed. Only one option should be selected.

{% hint style="info" %}
We recommend using the status "After 'Paid Order'" for the actions "Buy" and "Sell".
{% endhint %}

**Exchange Directions** — select the exchange directions for which trading actions will be performed when processing orders. You can select multiple directions that share the same currency in either the "Giving" or "Receiving" fields simultaneously.

**Tolerance Percentage (%)** — specify the tolerance percentage (numbers only) for the order amount on which the action will be based. Typically, values between 0.1 and 0.5 are used (the optimal value is 0.15).

<figure><img src="../../../.gitbook/assets/image (616).png" alt="" width="307"><figcaption></figcaption></figure>

## Step: "Borrow"

<figure><img src="../../../.gitbook/assets/image (696).png" alt="" width="515"><figcaption></figcaption></figure>

**Enabled:**\
• **Yes** \
• **No**

**Currency Code** — specify the currency code you want to **borrow** during this step.

**Network** — specify the network for the currency from the "Currency Code" field (optional; fill in only if the currency supports networks).

**Trading Currency Code** — specify the currency code that you need to lend to the exchange as a deposit in order for the exchange to lend you the selected currency (field "**Currency Code**").

**Amount** — select the type of amount from the order that will be passed to this step.  
![](<../../../.gitbook/assets/image (702).png>)

{% hint style="warning" %}
Choose the amount from either the "**Giving**" or "**Receiving**" side depending on which currency you plan to work with (the currency side must match the currency you specify in the "**Currency Code**" field).

The fields "**Payment Amount**" and "**Payout Amount**" are recorded by the merchant module for payment acceptance/automatic payout and only work if these values are not empty (i.e., a payment or payout was made through a merchant connected in the direction).

If no merchants are connected for payment acceptance/automatic payout in the exchange direction, the payment/payout values will be zero. If you select "**Payment Amount**" or "**Payout Amount**" as the amount for the trading step under these conditions, the trading step will fail because it will attempt to execute with an amount of zero.

If you have already encountered a trading error related to this issue, edit the relevant amount in the order (go to "**Orders**", click "**Edit**",  
![](<../../../.gitbook/assets/image (376).png>)  

enter the correct amount in the appropriate field, save the changes, and manually trigger the trading step by clicking the "**Action Link**" in the "**Trading Actions**" -> "**Orders**" section). The trading step will then be executed successfully.
{% endhint %}

**If the amount does not match:**  
• **Error** — the step will not be executed (recommended)  
• **Continue** — the step will be executed despite the amount mismatch

**Min. Amount** — the minimum amount for this trading step (specified in the currency used for the operation)

**Max. Amount** — the maximum amount for this trading step (specified in the currency used for the operation)

Here is a natural English translation of the provided text:

---

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

**If the amount doesn’t match:**  
• **Error** — the step will not be executed (recommended)  
• **Continue** — the step will be executed despite the amount mismatch

**Transfer to Margin account** — transfer to the margin account as debt repayment  
• **Yes**  
• **No**

**Currency code** — specify the currency code for the debt repayment in this step

{% hint style="warning" %}
The currency code must match:

* the client’s payment currency code from the order if "**Amount**" is set to "**Payment amount**" or any "**Give**" options  
* the payout currency code from the order if "**Amount**" is set to "**Payout amount**" or any "**Receive**" options  
{% endhint %}

**Amount** — select the amount type from the order that will be passed to this step  
![](<../../../.gitbook/assets/image (702).png>)

{% hint style="warning" %}
Choose the amount from the "**Give**" or "**Receive**" side depending on which currency will be used in this step (the currency side must match the currency you specify in the "**Currency code**" field)  
{% endhint %}

**Min. amount** — minimum amount for this trading step (specified in the currency used for the operation)

**Max. amount** — maximum amount for this trading step (specified in the currency used for the operation)

## Step: "Sell"

<figure><img src="../../../.gitbook/assets/image (695).png" alt="" width="518"><figcaption></figcaption></figure>

**Enabled:**  
• **Yes**  
• **No**

**If the amount doesn’t match:**  
• **Error** — the step will not be executed (recommended)  
• **Continue** — the step will be executed despite the amount mismatch

**Trading account** — the account from which the currency will be sold  
• **Spot** — spot account  
• **Margin** — margin account

---

If you need the translation adapted for a specific audience or style, please let me know!

**Borrowing** — if your account balance is insufficient or zero, you can borrow funds from the exchange (only if a margin account is selected in the previous setting), then repay the debt manually or by using the "**Repay Debt**" step.  
• **No** — no borrowing will occur  
• **Full amount** — purchase the full amount specified in the order  
• **Required amount** — purchase only the shortfall amount

**Transfer to account** — transfer funds to the selected account  
• **Spot** — spot account  
• **Margin** — margin account

**Currency code** — specify the currency code to be <mark style="color:red;">**sold**</mark> in this step to buy the currency indicated in "**Trading currency code**"

{% hint style="warning" %}
The currency code must match:

* the client’s payment currency code from the order if "**Amount**" is set to "**Payment amount**" or any of the "**Giving**" options  
* the payout currency code from the order if "**Amount**" is set to "**Payout amount**" or any of the "**Receiving**" options  
{% endhint %}

**Network** — specify the network for the currency from "**Currency code**" (optional; only fill in if the currency has a network). Leave blank if the currency has no network.

**Trading currency code** — specify the currency code to be <mark style="color:green;">**bought**</mark> in this step (usually USDT)

**Amount** — select the amount type from the order that will be used in this action (when selling the client’s incoming currency, choose one of the "**Giving**" options or the "**Payment amount**" option)  
![](<../../../.gitbook/assets/image (702).png>)

{% hint style="warning" %}
Choose the amount from the "**Giving**" or "**Receiving**" side depending on which currency the action involves (the currency side must match the currency you specify in the "**Currency code**" field).  
{% endhint %}

**Min. amount** — the minimum amount for this trading step (specified in the currency being transacted). If the amount from the order is less than this minimum, the step will not be executed.

**Max Amount** — the maximum amount allowed for this trading step (specified in the currency used for the operations). If the amount in the order exceeds this maximum, the step will not be executed.

**Add Withdrawal Fee** — for the "**Sell**" action, select "**No**"  
• **Yes**  
• **No**

**Add Trading Fee** — for the "**Sell**" action, select "**No**"  
• **Yes**  
• **No**

## Step: "Buy"

<figure><img src="../../../.gitbook/assets/image (698).png" alt="" width="504"><figcaption></figcaption></figure>

**Enabled:**  
• **No** — step is not used  
• **Full Amount** — buy the full amount specified in the order  
• **Required Amount** — buy only the missing amount (the balance of the selected currency in your merchant account will be taken into account)

**If the amount does not match:**  
• **Error** — the step will not be executed (recommended)  
• **Continue** — the step will be executed despite the amount mismatch

**Trading Account** — the account to which the currency will be purchased  
• **Spot** — spot account  
• **Margin** — margin account

**Borrow Funds** — if your account balance is insufficient or empty, you can borrow from the exchange (only if the margin account is selected in the previous option), then repay the debt manually or using the "**Repay Debt**" step  
• **No** — no borrowing will occur  
• **Full Amount** — borrow the full amount specified in the order  
• **Required Amount** — borrow only the missing amount

**Borrowing Currency** — select the currency to borrow  
• **Currency Code** — the currency from the "**Currency Code**" field in this step  
• **Trading Currency Code** — the currency from the "**Trading Currency Code**" field in this step

**Transfer to Account** — transfer funds to the selected account  
• **No** — no transfer  
• **Spot** — spot account  
• **Margin** — margin account

**Currency Code** — specify the code of the currency to be **bought** in this step

{% hint style="warning" %}
The currency code must match:

Here is a natural English translation of the provided text:

---

* Use the payment currency code from the client’s order if the "**Amount**" field is set to "**Payment Amount**" or any of the "**Giving**" options  
* Use the payout currency code from the order if the "**Amount**" field is set to "**Payout Amount**" or any of the "**Receiving**" options  

{% endhint %}

**Network** — specify the network for the currency indicated in the "**Currency Code**" field (optional; only required if the currency supports a network)

**Trading Currency Code** — specify the currency code that needs to be <mark style="color:red;">**sold**</mark> in this step in order to purchase the currency from the "**Currency Code**" field

**Amount** — select the type of amount from the order that will be used in this step  
![](<../../../.gitbook/assets/image (702).png>)

{% hint style="warning" %}
Choose the amount from the "**Giving**" or "**Receiving**" side depending on which currency you plan to work with (the side of the currency pair must match the currency you specify in the "**Currency Code**" field)  
{% endhint %}

**Min. Amount** — the minimum amount for this trading step (specified in the currency being purchased in this step — see "**Currency Code**"). If the amount from the order is less than this minimum, the step will not be executed.

**Max. Amount** — the maximum amount for this trading step (specified in the currency being purchased in this step — see "**Currency Code**"). If the amount from the order exceeds this maximum, the step will not be executed.

**Add withdrawal fee:**  
• **Yes** — select "**Yes**" if the freshly purchased currency is to be paid out via the [Binance auto-payout module](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/binance)  
• **No**

**Add trading fee** — select "**Yes**"  
• **Yes**  
• **No**

## **Step: "Transfer to Account"**

<figure><img src="../../../.gitbook/assets/image (699).png" alt="" width="509"><figcaption></figcaption></figure>

**Enabled:**  
• **Yes**  
• **No**

**Transfer to account:**  
• **Spot -> Margin** — transfer from spot account to margin account  
• **Margin -> Spot** — transfer from margin account to spot account

---

If you need any further adjustments or clarifications, feel free to ask!

**Currency Code** — specify the currency code to be **transferred** between accounts in this step.

**Network** — specify the network for the currency from the "**Currency Code**" field (optional; only required if the currency supports networks).

**Trading Currency Code** — specify the currency code that will be transferred in the opposite direction.

**Amount** — select the type of amount from the request that will be passed to this step.  
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
* **Login** — your login for proxy server access  
* **Password** — your password for proxy server access  
* **Disable Proxy Tunnel** — disable this option if the fields above are filled in  
  • **No**  
  • **Yes**

[^1]: 1 - highest priority  
2 - second action by priority, and so on