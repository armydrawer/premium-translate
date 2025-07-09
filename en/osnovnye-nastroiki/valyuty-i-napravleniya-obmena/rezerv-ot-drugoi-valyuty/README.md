# Reserve from Another Currency

You can use the reserve of one currency to update the reserve value of another currency in real-time. To do this, in the settings of the currency that will act as the source, enter the IDs of the currencies that should receive this reserve value in the field "**Link reserve with currency reserve ID**."

&#x20;

<figure><img src="../../../../.gitbook/assets/изображение (171).png" alt=""><figcaption></figcaption></figure>

Currency IDs are listed in the first column of the "Currencies" section.

<figure><img src="../../../../.gitbook/assets/изображение (25).png" alt=""><figcaption></figcaption></figure>

In the receiving currency’s settings, specify the ID of the sending currency, prefixed with **rc:**.

<figure><img src="../../../../.gitbook/assets/изображение (60).png" alt=""><figcaption></figcaption></figure>

After completing these steps, whenever the reserve of the "main" currency changes, all currencies linked to this reserve will synchronize and update their reserve values accordingly.

{% hint style="info" %}
To link reserves between exchange directions, use **rd** (currency direction IDs) instead of **`rc`** in formulas.\
![](<../../../../.gitbook/assets/image (1863).png>)
{% endhint %}