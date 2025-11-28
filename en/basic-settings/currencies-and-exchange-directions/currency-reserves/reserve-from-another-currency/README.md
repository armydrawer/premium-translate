# Reserve from Another Currency

You can use the reserve of one currency to transfer its value in real-time. To do this, in the settings of the currency that will be considered the source, enter the IDs of the currencies that will receive the reserve value of this currency in the field "**Link Reserve to Currency Reserve ID**."

The currency IDs are listed in the first column of the "Currencies" section.

In the "receiving" currency, specify the ID of the "sending" currency with the prefix **rc:**

After completing these steps, whenever the reserve of the "main" currency changes, all currencies that use this reserve value will synchronize and adopt the new value as the reserve of the "main" currency changes.

{% hint style="info" %}
To link reserves between exchange directions, use **`rd`** (Currency Direction IDs) instead of **`rc`** for formulas.\
![](<../../../../.gitbook/assets/image (1863)_eng.png>)
{% endhint %}
