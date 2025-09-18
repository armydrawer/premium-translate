# Error Diagnostics

In the "**Trading Actions -> Orders**" section, all executed trading actions are recorded. If the action name is highlighted in <mark style="color:green;">green</mark>, it means the action was successfully completed. If it is highlighted in <mark style="color:red;">red</mark>, this indicates an error in the trading action (the action was not executed).

<figure><img src="../../.gitbook/assets/image (612).png" alt=""><figcaption></figcaption></figure>

If a trading action is highlighted in <mark style="color:red;">red</mark>, you can click on the "**action link**" to retry the action. If the action is successfully completed, the color will change to <mark style="color:green;">green</mark>. Otherwise, the text will remain <mark style="color:red;">red</mark>. Clicking the link for an action that is already <mark style="color:green;">successfully completed</mark> will have no effect.

If the error persists, you should review the logs in the "**Trading Actions -> Script Logs**" section to identify specific errors returned by the exchange's API. Most commonly, errors are related to insufficient funds in the account or an invalid currency pair on the exchange.

<figure><img src="../../.gitbook/assets/Логи скриптов ‹ 2 Premium Exchanger 2 — WordPress - Google Chrome_230512172527.png" alt=""><figcaption><p>Trading Action Logs</p></figcaption></figure>

{% hint style="warning" %}
To troubleshoot trading actions with technical support, please prepare the following information:

* Screenshots or a text file of the "**Logs**" and "**Script Logs**" sections
* Screenshots of the full settings for the specific trading action (found in the "**Trading Actions**" section)
* A screenshot of the expanded "**Info**" button for the order in the "**Orders**" section, where the action was performed

![](<../../.gitbook/assets/image (613).png>)

* Screenshots of the auto-payout module settings used for the exchange direction
* Information on which type of amount is considered the payout amount (as specified in the auto-payout settings)
{% endhint %}