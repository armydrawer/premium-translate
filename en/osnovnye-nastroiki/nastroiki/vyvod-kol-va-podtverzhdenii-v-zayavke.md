# Displaying the Number of Confirmations in the Application

{% hint style="info" %}
To select the shortcode in the shortcode panel, you need to activate the "**Transaction Confirmation Counter (Crypto)**" module in the "**Modules**" section.
{% endhint %}

{% hint style="warning" %}
Please note that for the number of confirmations to be displayed, the merchant must provide this information via API. In 90% of cases, this does not happen due to a lack of data from the merchant.
{% endhint %}

If a merchant is used for accepting cryptocurrencies, the number of transaction confirmations can be displayed to the user on the application page. To do this, go to the "**Exchange Directions**" section, edit the exchange direction, and select the "**User Information**" tab.

Locate the text field labeled "**Application Status**" with the value "**new application**." Above this text field, you will see a panel with shortcodes. The shortcode responsible for displaying the number of confirmations is "**Number of Confirmations**." Place your cursor in the text field where you want to display the number of confirmations, then click on the shortcode "**Number of Confirmations**." The text field will show the code in square brackets **\[confirm\_count]**, which will be converted on the application page into the actual number of confirmations.

Repeat the above procedure for the text field labeled "**Application Status: waiting for confirmation from the merchant**."

<figure><img src="../../.gitbook/assets/Screenshot_42 (1).png" alt=""><figcaption></figcaption></figure>