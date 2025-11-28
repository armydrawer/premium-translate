# Converting Reserves When Using a Merchant

Let's assume you are using Binance's auto payout feature to distribute BTC. Your Binance account holds reserves in USDT, and you need to convert the USDT reserve into the current BTC reserve.

1.  In the control panel, navigate to "**Merchants" → "Auto Payouts"** and go to the settings for the Binance module. At the bottom of the module settings page, find the active link labeled "**Currency Reserve Shortcode**" and click on it. Copy the shortcode for "**Binance (binance) — USDT**."

    <figure><img src="../../../../.gitbook/assets/Screenshot_34 (3) (1).png" alt=""><figcaption></figcaption></figure>
2. In the website control panel, go to "**Parsers 2.0" → "Source Rates"** and copy the shortcode for BTC=>USDT.
3. Proceed to edit the BTC currency. In the currency settings under the "**Reserves**" tab, select the option "**By Formula**" for the "**Currency Reserve**" parameter.
4.  To obtain the current reserve in BTC, you need to divide the USDT reserve by the **BTC -> USDT** rate. In the field labeled "**Reserve Formula**" that appears below, enter the following formula in the currency settings:

    <figure><img src="../../../../.gitbook/assets/image (1274)_eng.png" alt="" width="344"><figcaption></figcaption></figure>

    Here, **\[binance\_usdt]** is the shortcode you copied from the Binance auto payout module settings, and **\[parser\_binance\_btcusdt]** is the shortcode you copied from the "**Parsers 2.0**" section, with the **parser\_** prefix added.

You can set up a convertible reserve for other currencies in a similar manner.
