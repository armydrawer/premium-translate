# Transaction Hash and Link

When using automatic payouts for cryptocurrency, you have the option to display the transaction hash on the application page for the user.

To do this, go to the "**Exchange Directions**" section, edit the direction, and select the "**User Information**" tab.

Next, find the text field labeled "**Application Status**" with the option "**completed application**." Above the text field, there is a panel with shortcodes. The shortcode responsible for displaying the transaction hash is "**Automatic Payout Transaction ID**." Place your cursor in the field where you want to display the number of confirmations, then click on the shortcode "**Automatic Payout Transaction ID**." The text field will show the code in square brackets **\[bid\_trans\_out]**, which will be converted into the transaction hash on the application page for the user.

<figure><img src="../../.gitbook/assets/Screenshot_43.png" alt=""><figcaption></figcaption></figure>

You can also make the transaction hash an active link. For example, the code for an active link to a Bitcoin transaction hash looks like this — copy the code and place it in the text field for "**Application Status**" with the option "**completed application**":

`Link to transaction: https://www.blockchain.com/ru/btc/tx/[bid_trans_out]`

<figure><img src="../../.gitbook/assets/Screenshot_44.png" alt=""><figcaption></figcaption></figure>

Please note that the transaction hash will not appear on the application page immediately — it takes some time for the payment gateway to process the application and provide the hash.