# Phone Number Verification

The "**Phone Verification Before Request Submission**" module allows you to verify a client’s phone number when they create a request. Make sure the module is enabled in the "**Modules**" section, or activate it if necessary.

<figure><img src="../../.gitbook/assets/image (170).png" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
For the module to work properly, [SMS notifications](https://premium.gitbook.io/main/osnovnye-nastroiki/uvedomleniya-administratoram-i-klientam/uvedomleniya-po-sms) must also be configured.
{% endhint %}

In the "**Modules**" -> "**Phone Verification Before Request Submission**" section, configure the module settings:

<figure><img src="../../.gitbook/assets/image (171).png" alt="" width="373"><figcaption></figcaption></figure>

**Code type:**\
**• Numbers**\
**• Letters**

**Send SMS to:**\
**• All users** — the code will be sent to all exchange clients\
**• Guests** — the code will be sent only to guests

**Timeout (sec.)** — the time to wait for a server response

**Verification parameter** — the parameter used to verify the client:\
**• "Giving" account**\
**• "Receiving" account**\
**• Phone number**

**Text** — enter the desired SMS text and be sure to include the shortcode \[code] in the message

In the exchange direction settings, enable SMS code verification and select the verification parameter (if "**Default**" is selected, the parameter from the module’s general settings will be used).

<figure><img src="../../.gitbook/assets/image (172).png" alt=""><figcaption></figcaption></figure>