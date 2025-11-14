# Error Diagnostics

In the "**Trading Actions -> Orders**" section, all executed trading actions are recorded. If the action name is highlighted in <mark style="color:green;">green</mark>, it means the action was successfully completed. If it is highlighted in <mark style="color:red;">red</mark>, this indicates an error in the trading action (the action was not executed).

<figure><img src="../../../ru/.gitbook/assets/image (612) (1).png" alt=""><figcaption></figcaption></figure>

If a trading action is highlighted in <mark style="color:red;">red</mark>, you can click on the "**action link**" to retry the action. If the action is successfully completed, the color will change to <mark style="color:green;">green</mark>. Otherwise, the text will remain <mark style="color:red;">red</mark>. Clicking the link for an action that is already <mark style="color:green;">successfully completed</mark> will have no effect.

If the error persists, you should review the logs in the "**Trading Actions -> Script Logs**" section to identify specific errors returned by the exchange's API. Most commonly, errors are related to insufficient funds in the account or an invalid currency pair on the exchange.

<figure><img src="../../.gitbook/assets/%D0%9B%D0%BE%D0%B3%D0%B8%20%D1%81%D0%BA%D1%80%D0%B8%D0%BF%D1%82%D0%BE%D0%B2%20%E2%80%B9%202%20Premium%20Exchanger%202%20%E2%80%94%20WordPress%20-%20Google%20Chrome_230512172527_eng.png" alt=""><figcaption><p>Trading Action Logs</p></figcaption></figure>

{% hint style="warning" %}
To troubleshoot trading actions with technical support, please prepare the following information:

* Screenshots or a text file of the "**Logs**" and "**Script Logs**" sections
* Screenshots of the full settings for the specific trading action (found in the "**Trading Actions**" section)
* A screenshot of the expanded "**Info**" button for the order in the "**Orders**" section, where the action was performed

<img src="../../../ru/.gitbook/assets/image (613) (1).png" alt="" data-size="original">

* Screenshots of the auto-payout module settings used for the exchange direction
* Information on which type of amount is considered the payout amount (as specified in the auto-payout settings)
{% endhint %}
