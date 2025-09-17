# Setting a Manual Reserve for a New Currency

{% hint style="info" %}
If you are using the auto-payout module, you can retrieve the reserve for this payment system directly from the wallet in real time. In this case, when creating the currency, select the corresponding wallet for the "**Currency Reserve**" parameter. If you do this, the steps described below are not necessary.
{% endhint %}

If you want to set the currency reserve manually, navigate to the "**Reserve Adjustment**" section in the sidebar. Click the "**Add**" button located above the table of existing currencies.

<figure><img src="../../../.gitbook/assets/image (1027).png" alt=""><figcaption></figcaption></figure>

In the pop-up window, you will need to fill in the fields "**Comment**," "**Amount**," and "**Currency**":

<figure><img src="../../../.gitbook/assets/image (1010).png" alt=""><figcaption></figcaption></figure>

* **Comment -** Add a note or description for this transaction (optional).
* **Amount -** Specify the amount by which you want to increase the reserve for this currency.
* **Currency -** Select the currency name from the dropdown list for which you are setting the reserve.

Click the "**Save**" button to apply the changes.

Please note: If, for any reason unrelated to exchange operations on the website, the currency reserve increases or decreases, you will need to manually update the data for that currency. Repeat the steps above to adjust the currency reserve, and in the "Amount" field, enter the amount by which the reserve has changed. Use a negative sign ("-") if the reserve has decreased. For example, if the reserve has decreased by 500 units, enter "-500" in the "Amount" field. Click the "**Save**" button to save the changes.

{% hint style="info" %}
The currency reserve amount is automatically updated after an exchange is completed. The manual reserve adjustment feature is intended for cases where you need to add or withdraw funds from the balance used by your exchange service.
{% endhint %}