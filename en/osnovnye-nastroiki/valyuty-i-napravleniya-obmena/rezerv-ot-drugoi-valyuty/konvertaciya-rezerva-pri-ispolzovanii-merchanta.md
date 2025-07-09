# Converting Reserves When Using a Merchant

Suppose you are using Binance auto-payouts to pay out BTC. On your Binance account, the reserve is held in USDT. You need to convert the USDT reserve value into the current BTC reserve.

1. In the admin panel, go to **"Merchants" → "Auto Payouts"** and open the settings for the Binance module. At the bottom of the module settings page, find the active link labeled **"Currency Reserve Shortcode"** and click on it. Copy the shortcode for **"Binance (binance) — USDT"**.

<figure><img src="../../../../.gitbook/assets/Screenshot_34 (3).png" alt=""><figcaption></figcaption></figure>

2. In the admin panel, navigate to **"Parsers 2.0" → "Source Rates"** and copy the shortcode for **BTC=>USDT**.

<figure><img src="../../../../.gitbook/assets/Screenshot_35.png" alt="" width="563"><figcaption></figcaption></figure>

3. Go to edit the BTC currency settings. On the **"Reserves"** tab, set the **"Currency Reserve"** option to **"By formula"**.

4. To get the current BTC reserve, you need to divide the USDT reserve by the BTC→USDT exchange rate. Enter the following formula in the **"Reserve formula"** field that appears below:

<figure><img src="../../../../.gitbook/assets/image (1274).png" alt="" width="344"><figcaption></figcaption></figure>

Here, **\[binance_usdt]** is the shortcode you copied from the Binance auto-payout module settings, and **\[parser_binance_btcusdt]** is the shortcode you copied from the **"Parsers 2.0"** section, with the prefix **parser_** added.

You can configure convertible reserves for other currencies in the same way.