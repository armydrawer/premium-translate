# Creating a Trading Action

When you create a trading action, you embed specific operational logic that is executed by a script. These trading actions can be used simultaneously across multiple directions.

{% hint style="danger" %}
Incorrectly configured trading operations can negatively impact your financial results, so please be careful when setting them up.

Always perform test exchanges yourself before making the feature available to all clients.

Keep in mind that trading operations will be executed at the **current market rate of the connected exchange**.
{% endhint %}

{% hint style="warning" %}
When trading cryptocurrencies, it’s recommended to keep a small reserve of each coin in your balance. This helps avoid issues related to rounding calculations and transferring funds between accounts. Additionally, having a reserve can be useful in case of sudden changes in withdrawal fees.

\
For example, when buying BTC on Garantex, you should maintain a small balance—even as little as 0.01 BTC.

This is because the order book may contain BTC from multiple trades, and Garantex enforces a minimum trade size.

When buying in parts at market price, if the last purchase falls below the minimum trade size, it will be rounded up or down. As a result, you might end up with slightly more or less BTC than expected, though this rarely happens.
{% endhint %}

{% hint style="danger" %}
Please note that a configured trading action will run **only** if the exchange direction where the action is used has a **merchant enabled to receive funds** (manually changing the request status will not trigger the trading action).
{% endhint %}

1. To create a trading action, you need to fill out the following fields:

* **Title** — this is the name of the action that will be displayed in the main table of trading actions.  
* **Module** — select the exchange where you want to perform trading operations.  
* **Status** — specify whether this action is active or not, i.e., whether it will be triggered.

<figure><img src="../../../.gitbook/assets/image (2062).png" alt="" width="563"><figcaption></figcaption></figure>

3. Click the "**Save**" button to save the trading action you created.  
4. Fill in the fields with the API keys for the connected exchange. Please note that the keys you use must have permission to execute trading operations on the selected exchange.

<figure><img src="../../../.gitbook/assets/Добавить действие ‹ 2 Premium Exchanger 2 — WordPress - Google Chrome_230512161400.png" alt="" width="563"><figcaption><p>API Key Settings</p></figcaption></figure>

5. Next, configure the general parameters of the trading action:

{% hint style="warning" %}
When multiple steps are activated within a trading action, they will be executed sequentially from top to bottom.

If several trading actions are used simultaneously, all active steps in the highest-priority action will be executed first, followed by the next action in order of priority (with its own active steps).

![](<../../../.gitbook/assets/image (1516).png>)
{% endhint %}

Here is a natural English translation of the provided text:

---

**Execution Order** — If multiple trading actions can be triggered in the same exchange direction, **set the order in which they should be executed**. If there is only one trading action in that direction, this field can be left blank. Actions are executed in descending order of their assigned number (for example, if there are several actions, the one with number 3 will be executed first, then number 2, and finally number 1).

If only one trading action is assigned to an exchange direction, the execution order number does not matter, since the single trading action will be executed automatically once its configured conditions are met. In this case, you can leave the execution order field empty or enter any number.

**Assign Actions** — Select the order status upon which the trading action will be triggered. The most commonly used status is "**After the status 'Paid Order'**."

**Exchange Directions** — Choose the exchange directions in which the trading action will be triggered.

**Error Margin (%)** — This setting applies **only** to the Binance exchange and relates to executing **buy** trades. The recommended value is 0.15%.

---

<figure><img src="../../../.gitbook/assets/Добавить действие ‹ 2 Premium Exchanger 2 — WordPress - Google Chrome_230512164107.png" alt="" width="563"><figcaption><p>General settings for a trading action</p></figcaption></figure>

6. Next, you need to go to the settings of the corresponding exchange and configure the necessary options. Below are instructions for setting up some popular exchanges:  
   * [Garantex](garantex-skoro.md)  
   * [Binance](binance.md)  
7. To create the next trading action, repeat the process starting with selecting the exchange where you want to perform transactions. Then fill in the required settings according to the chosen exchange’s requirements. Be sure to double-check that all fields are filled out correctly before saving the settings.  
8. After saving the settings, we **recommend** running test trades to ensure that the trading actions work correctly.