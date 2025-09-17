# Reserve from Another Currency

You can use the reserve of one currency to transfer its value in real-time. To do this, go to the settings of the currency that will act as the source, and in the field "**Link reserve to currency reserve ID**," specify the IDs of the currencies that will receive the reserve value of this currency.

&#x20;

<figure><img src="../../../../.gitbook/assets/изображение (171).png" alt=""><figcaption></figcaption></figure>

Currency IDs are listed in the first column of the "Currencies" section.

<figure><img src="../../../../.gitbook/assets/изображение (25).png" alt=""><figcaption></figcaption></figure>

In the "receiving" currency, specify the ID of the "transmitting" currency with the prefix **rc:**.

<figure><img src="../../../../.gitbook/assets/изображение (60).png" alt=""><figcaption></figcaption></figure>

After completing these steps, whenever the reserve of the "primary" currency changes, all currencies linked to this reserve will synchronize and adopt the new value as the reserve of the "primary" currency changes.

{% hint style="info" %}
To link reserves between exchange directions, use **`rd`** (currency direction IDs) instead of **`rc`** in formulas.\
![](<../../../../.gitbook/assets/image (1863).png>)
{% endhint %}