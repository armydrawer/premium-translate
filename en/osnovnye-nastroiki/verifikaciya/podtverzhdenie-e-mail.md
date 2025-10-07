# Email Confirmation

In version 2.6 of the script, a module for confirming the client's email before registration on the site and before creating a request has been introduced.

## Email Confirmation Before Registration

To use this option, activate the new module in the "**Modules**" section.

<figure><img src="../../.gitbook/assets/image (1865)_eng.png" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
To ensure the module works, you also need to activate the template "**Email Confirmation Before Registration**" in the "**Messages**" -> "**Email Templates**" section (this is a mandatory requirement).

![](<../../.gitbook/assets/image (1877)_eng.png>)
{% endhint %}

General settings for the module can be found in the "**Modules**" -> "**Email Confirmation Before Registration**" section.

<figure><img src="../../.gitbook/assets/image (1867)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

**Code Type** — the format of the code that will be sent to the client after clicking the "**Register**" button:

* **Letters** — the code will consist only of Latin letters
* **Numbers** — the code will consist only of digits

**Timeout (sec.)** — the waiting time

Once the module is activated and the template "**Email Confirmation Before Registration**" is enabled in the "**Messages**" -> "**Email Templates**" section (this is a mandatory requirement), after clicking the "**Register**" button, a new user will receive an email with a confirmation code sent to the email address they provided. This code must be entered in the corresponding field to complete the registration.

<figure><img src="../../.gitbook/assets/image (1864)_eng.png" alt="" width="354"><figcaption></figcaption></figure>

After entering the correct code and clicking the "**Register**" button again, the user will receive a notification of successful registration and will be immediately logged into their personal account.

<figure><img src="../../.gitbook/assets/image (1868)_eng.png" alt="" width="283"><figcaption></figcaption></figure>

## Email Confirmation Before Creating a Request

To use this option, activate the new module in the "**Modules**" section.

<figure><img src="../../.gitbook/assets/image (1870)_eng.png" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
To ensure the module works, you also need to enable the "**Email Verification**" option in the settings of the selected exchange directions under the "**Verification**" tab.

<img src="../../.gitbook/assets/image (1873)_eng.png" alt="" data-size="original">

Additionally, activate the template "**Email Confirmation Before Creating a Request**" in the "**Messages**" -> "**Email Templates**" section (these are mandatory requirements).

![](<../../.gitbook/assets/image (1875)_eng.png>)
{% endhint %}

General settings for the module can be found in the "**Modules**" -> "**Email Confirmation Before Creating a Request**" section.

<figure><img src="../../.gitbook/assets/image (1872)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

**Code Type** — the format of the code that will be sent to the client after clicking the "**Register**" button:

* **Letters** — the code will consist only of Latin letters
* **Numbers** — the code will consist only of digits

Send email for:

* **All Users** — email confirmation will be requested from both registered users and guests
* **Guests** — email confirmation will only be requested from guests (if a request is created by a user with an unverified parameter for verification, confirmation will not be required for them)

**Timeout (sec.)** — the waiting time

**Verification Parameter** — the parameter that the user will need to confirm:

* **Account Sending**
* **Account Receiving**
* **Email**

Once the module is activated, the "**Email Verification**" option is enabled, and the template "**Email Confirmation Before Creating a Request**" is activated, after clicking the "**Continue**" button, the user will receive an email with a confirmation code sent to the email address they provided. This code must be entered in the corresponding field in the form on the site to create a request.

<figure><img src="../../.gitbook/assets/image (1874)_eng.png" alt="" width="358"><figcaption></figcaption></figure>

After entering the correct code and clicking the "**Continue**" button again, the user will receive a notification of successful request creation.