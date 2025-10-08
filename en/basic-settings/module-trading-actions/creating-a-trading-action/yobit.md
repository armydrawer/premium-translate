# Yobit

{% hint style="warning" %}
Please note that you can set up actions for step-by-step exchanges between two currencies using intermediary currencies. Most commonly, if a direct pair **Currency 1** -> **Currency 2** is unavailable on the exchange, the conversion is done via the stablecoin USDT (TRC20) (**Currency 1** -> **USDT** -> **Currency 2**). However, you can also use alternative routes.

To set up a step-by-step exchange, you need to:

* Create two trading actions: **Sell** (**Currency 1** -> **USDT**) and **Buy** (**USDT** -> **Currency 2**).
* Select the same exchange directions and statuses for triggering in the "**Addition Settings**" block within the action settings.
* Set the execution order of the actions: 1 for the **Sell** action and 2 for the **Buy** action.
{% endhint %}

Go to the "**Trading Actions -> Add Action**" section, enter a name for the trading action in the "**Title**" field, select "Yobit" from the dropdown menu in the "**Module**" field, leave the status as "**Active Action**," and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (607)_eng.png" alt="" width="392"><figcaption></figcaption></figure>

{% hint style="info" %}
[General instructions for configuring trading action parameters](https://premium.gitbook.io/main/en/basic-settings/modul-torgovye-deistviya/sozdanie-torgovogo-deistviya/parametry-torgovykh-deistvii)
{% endhint %}

Within the module, you can create one of two actions: "**Sell**" or "**Buy**."

<div><figure><img src="../../../.gitbook/assets/image (608)_eng.png" alt="" width="485"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/image (610)_eng.png" alt="" width="472"><figcaption></figcaption></figure></div>

{% hint style="info" %}
The "**Sell**" action is suitable when you want to convert the currency received from a client’s request into a stablecoin like USDT (or another currency you find appropriate).

The "**Buy**" action is suitable when you don’t want to maintain a reserve of the payout currency in your exchange accounts and instead plan to purchase the currency for payout only when a client submits a request to buy that currency from your exchange. In this case, you need to use the [Yobit auto-payout module](https://premium.gitbook.io/main/en/basic-settings/merchants-and-auto-payments/auto-payments/yobit) to pay out the currency immediately after purchasing it.
{% endhint %}

To ensure the action is executed correctly, it’s important to select the currencies you plan to work with in the "**Currency Code**" and "**Trading Currency Code**" fields.

The current list of currency pairs is displayed in the [JSON file](https://yobit.net/tapipe/info) on the merchant’s website, under the "**defi**" block.

<figure><img src="../../../.gitbook/assets/image (611)_eng.png" alt="" width="363"><figcaption></figcaption></figure>

{% hint style="danger" %}
If you select currencies that do not form a pair from the list above, the trading action will inevitably result in an error when attempting to execute.
{% endhint %}