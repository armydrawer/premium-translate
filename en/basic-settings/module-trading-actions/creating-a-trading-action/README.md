# Creating a Trading Action

When creating a trading action, you define specific operational logic that will be executed by a script. The trading actions you create can be used across multiple directions simultaneously.

{% hint style="danger" %}
Improperly configured trading operations can negatively impact your financial results, so be cautious when setting them up.

Always perform test exchanges yourself before granting access to all clients.

It’s important to remember that trading operations will be executed at the **current market rate of the connected exchange**.
{% endhint %}

{% hint style="warning" %}
When trading cryptocurrencies, it’s recommended to keep a small reserve of each currency in your balance. This helps avoid issues related to rounding calculations and transferring funds between accounts. Additionally, having a reserve can be useful in case of sudden changes in withdrawal fees.

For example, when purchasing BTC on Garantex, you should leave a small amount in your balance, even if it’s minimal—such as 0.01 BTC.

This is because the order book may contain BTC split across multiple trades, and Garantex has a minimum trade size requirement.

When buying in parts at market price, if the final purchase is smaller than the minimum trade size, it will be rounded up or down. As a result, you may end up with a small surplus or shortage of BTC, though this happens rarely.
{% endhint %}

{% hint style="danger" %}
Please note that the configured trading action will be triggered **only** if the exchange direction where the action is used has a **merchant connected for receiving funds**. Manually changing the status of an application will not trigger the trading action.
{% endhint %}

***

### Steps to Create a Trading Action

1. **Fill in the following fields:**
   * **Title** — This is the name of the action, which will appear in the general table of trading actions.
   * **Module** — Select the exchange where you want to perform trading operations.
   * **Status** — Indicate whether this action is active or not, i.e., whether it will be triggered.

<figure><img src="../../../.gitbook/assets/image (2062)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

2. Click the "**Save**" button to save the trading action you’ve created.
3. Fill in the fields with the API keys for the connected exchange. Ensure that the keys you use have permissions to perform trading operations on the selected exchange.

<figure><img src="../../../.gitbook/assets/%D0%94%D0%BE%D0%B1%D0%B0%D0%B2%D0%B8%D1%82%D1%8C%20%D0%B4%D0%B5%D0%B9%D1%81%D1%82%D0%B2%D0%B8%D0%B5%20%E2%80%B9%202%20Premium%20Exchanger%202%20%E2%80%94%20WordPress%20-%20Google%20Chrome_230512161400_eng.png" alt="" width="563"><figcaption><p>API Key Settings</p></figcaption></figure>

4. Next, configure the general parameters of the trading action:

{% hint style="warning" %}
If multiple steps are activated within a trading action, they will be executed sequentially (from top to bottom).

If multiple trading actions are used simultaneously, all active steps in the highest-priority trading action will be executed first, followed by the second-priority action (with its own active steps).

<img src="../../../../ru/.gitbook/assets/image (573) (1).png" alt="" data-size="original">
{% endhint %}

* **Execution Order** — If multiple trading actions can be triggered in one exchange direction, **set their execution order**. If there’s only one trading action in the direction, this field can be left blank. Actions are executed in descending order of priority (e.g., if there are several actions, the one with priority 3 will execute first, followed by priority 2, and then priority 1).\
  If there’s only one trading action in the exchange direction, the execution order doesn’t matter, as the single action will be executed automatically when its configured conditions are met. In this case, you can leave the execution order blank or assign any number.
* **Trigger Status** — Select the application status that will trigger the trading action. Typically, the status "**After 'Paid Application' status**" is used.
* **Exchange Directions** — Choose the exchange directions where the trading action will be triggered.
* **Error Margin (%)** — This setting is relevant **only** for Binance and applies to **buying** operations. The recommended value is 0.15%.

<figure><img src="../../../.gitbook/assets/%D0%94%D0%BE%D0%B1%D0%B0%D0%B2%D0%B8%D1%82%D1%8C%20%D0%B4%D0%B5%D0%B9%D1%81%D1%82%D0%B2%D0%B8%D0%B5%20%E2%80%B9%202%20Premium%20Exchanger%202%20%E2%80%94%20WordPress%20-%20Google%20Chrome_230512164107_eng.png" alt="" width="563"><figcaption><p>General Trading Action Settings</p></figcaption></figure>

5. Next, go to the settings of the corresponding exchange and complete the necessary configurations. Below are instructions for setting up some popular exchanges:
   * [Garantex](broken-reference/)
   * [Binance](binance.md)
6. To create another trading action, repeat the process starting with selecting the exchange where you want to perform operations. Then, fill in the required settings according to the chosen exchange’s requirements. Be sure to double-check all fields before saving the settings.
7. After saving the settings, **it is recommended** to conduct test exchanges to ensure the trading actions are functioning correctly.
