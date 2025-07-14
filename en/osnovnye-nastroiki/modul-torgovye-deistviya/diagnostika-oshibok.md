# Error Diagnostics

All executed trading actions are recorded in the "**Trading Actions** -> **Orders**" section. If the action name is highlighted in <mark style="color:green;">green</mark>, it means the action was completed successfully. If it is highlighted in <mark style="color:red;">red</mark>, this indicates an error occurred and the action was not completed.

<figure><img src="../../.gitbook/assets/image (612).png" alt=""><figcaption></figcaption></figure>

If a trading action is marked in <mark style="color:red;">red</mark>, you can click the "**action link**" to retry the action. If the retry is successful, the color will change to <mark style="color:green;">green</mark>. Otherwise, the text will remain <mark style="color:red;">red</mark>. Clicking the link when the action is already <mark style="color:green;">successfully completed</mark> will have no effect.

If the error persists, check the log in the "**Trading Actions** -> **Script Logs**" section for specific error messages returned by the exchange API. Most errors are related to insufficient account funds or a non-existent currency pair on the exchange.

<figure><img src="../../.gitbook/assets/Логи скриптов ‹ 2 Premium Exchanger 2 — WordPress - Google Chrome_230512172527.png" alt=""><figcaption><p>Trading Action Logs</p></figcaption></figure>

{% hint style="warning" %}
When contacting technical support for help diagnosing trading actions, please prepare the following information:

* Screenshots or text files of the "**Logs**" and "**Script Logs**" sections  
* Screenshots of the full settings for the specific trading action (found in the "**Trading Actions**" section)  
* A screenshot of the expanded "**Info**" view of the order from the "**Orders**" section for which the action was performed  

![](<../../.gitbook/assets/image (613).png>)

* Screenshots of the auto-payout module settings used in the exchange direction  
* What type of amount is considered the payout amount? (as specified in the auto-payout settings)  
{% endhint %}