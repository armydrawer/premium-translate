# Email Confirmation

In script version 2.6, a new module was introduced to confirm the client’s email before site registration and before submitting a request.

## Email Confirmation Before Registration

To enable this feature, activate the new module in the "**Modules**" section.

<figure><img src="../../.gitbook/assets/image (1865).png" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
For the module to work, you also need to activate the "**Email Confirmation Before Registration**" template in "**Messages**" -> "**Email Templates**" (this is mandatory).

![](<../../.gitbook/assets/image (1877).png>)
{% endhint %}

General settings for the module can be found under "**Modules**" -> "**Email Confirmation Before Registration**".

<figure><img src="../../.gitbook/assets/image (1867).png" alt="" width="563"><figcaption></figcaption></figure>

**Code Type** — the format of the code sent to the client after clicking the "**Register**" button:

* **Letters** — the code will consist only of Latin letters
* **Numbers** — the code will consist only of digits

**Timeout (sec.)** — waiting time

Once the module is activated and the "**Email Confirmation Before Registration**" template is enabled in "**Messages**" -> "**Email Templates**" (this is mandatory), when a new user clicks the "**Register**" button, a confirmation code will be sent to the email address they provided. The user must enter this code in the designated field to complete the registration.

<figure><img src="../../.gitbook/assets/image (1864).png" alt="" width="354"><figcaption></figcaption></figure>

After entering the correct code and clicking the "**Register**" button again, the user will receive a notification confirming successful registration and will be immediately logged into their personal account.

<figure><img src="../../.gitbook/assets/image (1868).png" alt="" width="283"><figcaption></figcaption></figure>

## Email Confirmation Before Submitting a Request

To enable this feature, activate the new module in the "**Modules**" section.

<figure><img src="../../.gitbook/assets/image (1870).png" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
For the module to function, you also need to enable the "**Email Verification**" option in the settings of the selected exchange directions under the "**Verification**" tab.

<img src="../../.gitbook/assets/image (1873).png" alt="" data-size="original">
{% endhint %}

Please activate the "**Email Confirmation Before Creating a Request**" template in the "**Messages**" -> "**Email Templates**" section (this is a mandatory requirement).

![](<../../.gitbook/assets/image (1875).png>)

General module settings can be found under "**Modules**" -> "**Email Confirmation Before Registration**".

<figure><img src="../../.gitbook/assets/image (1872).png" alt="" width="563"><figcaption></figcaption></figure>

**Code Type** — the format of the code that will be sent to the client after clicking the "**Register**" button:

* **Letters** — the code will consist of Latin letters only
* **Numbers** — the code will consist of digits only

Send email confirmation to:

* **All users** — email confirmation will be requested from both registered users and guests
* **Guests** — email confirmation will be requested only from guests (if a user with an unverified parameter creates a request, confirmation will not be required for them)

**Timeout (seconds)** — waiting time

**Verification Parameter** — the parameter the user will need to verify:

* **Account to Give**
* **Account to Receive**
* **Email**

When the module is activated, the "**Email Verification**" option is enabled, and the "**Email Confirmation Before Creating a Request**" template is active, after clicking the "**Continue**" button, the user will receive an email with a confirmation code sent to the email address they provided. This code must be entered into the corresponding field on the website form to create the request.

<figure><img src="../../.gitbook/assets/image (1874).png" alt="" width="358"><figcaption></figcaption></figure>

After entering the correct code and clicking the "**Continue**" button again, the user will receive a notification confirming the successful creation of the request.