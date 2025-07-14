# Yobit

{% hint style="warning" %}
Please note that you can set up actions for stepwise exchanges from one currency to another through intermediate currencies. Most often, when a direct trading pair **currency 1** -> **currency 2** is not available on the exchange, the exchange is done via the stablecoin USDT (TRC20) (**currency 1** -> **USDT** -> **currency 2**), but you can also use alternative routes.

To set up a stepwise exchange, you need to:

* Create 2 trading actions: **Sell** (**currency 1** -> **USDT**) and **Buy** (**USDT** -> **currency 2**)
* Select the same exchange directions and trigger statuses in the "**Addition Settings**" block within the action settings
* Set the execution order of the actions: 1 — for the **Sell** action, 2 — for the **Buy** action
{% endhint %}

Go to "**Trading Actions -> Add Action**", enter a name for the trading action in the "**Title**" field, select Yobit from the "**Module**" dropdown menu, leave the status as "**Active Action**", and click "**Save**".

<figure><img src="../../../.gitbook/assets/image (607).png" alt="" width="392"><figcaption></figcaption></figure>

{% hint style="info" %}
[General guide on configuring trading action parameters](https://premium.gitbook.io/main/osnovnye-nastroiki/modul-torgovye-deistviya/sozdanie-torgovogo-deistviya/parametry-torgovykh-deistvii)
{% endhint %}

Within the module, you can create one of two actions — "**Sell**" or "**Buy**".

<div><figure><img src="../../../.gitbook/assets/image (608).png" alt="" width="485"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/image (610).png" alt="" width="472"><figcaption></figcaption></figure></div>

{% hint style="info" %}
The "**Sell**" action is suitable when you want to convert the currency received from the client’s order into the stablecoin USDT (or another currency you find appropriate).

The "**Buy**" action is suitable when you do not want to keep a reserve of the payout currency on your exchange accounts and plan to purchase the currency for payout only when a client places an order to buy that currency from your exchange. In this case, you should use the [Yobit auto-payout module](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/yobit) to pay out the currency immediately after purchase.
{% endhint %}

To ensure the action is performed correctly, it is important to select the currencies you intend to work with in the "**Currency Code**" and "**Trading Currency Code**" fields.

The current list of currency pairs can be found in the [JSON file](https://yobit.net/tapipe/info) on the merchant’s website, under the "**defi**" section.

<figure><img src="../../../.gitbook/assets/image (611).png" alt="" width="363"><figcaption></figcaption></figure>

{% hint style="danger" %}
Selecting currencies that do not form a pair listed above will cause the trading action to fail with an error upon execution.
{% endhint %}