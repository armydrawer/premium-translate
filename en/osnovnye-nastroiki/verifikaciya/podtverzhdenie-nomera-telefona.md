# Phone Number Verification

The "**Phone Verification Before Creating a Request**" module allows you to verify a customer's phone number when they submit a request. Make sure the module is enabled in the "**Modules**" section, or activate it if necessary.

<figure><img src="../../.gitbook/assets/image (170).png" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
To use this module, [SMS notifications](https://premium.gitbook.io/main/osnovnye-nastroiki/uvedomleniya-administratoram-i-klientam/uvedomleniya-po-sms) must also be configured.
{% endhint %}

In the "**Modules**" -> "**Phone Verification Before Creating a Request**" section, configure the module:

<figure><img src="../../.gitbook/assets/image (171).png" alt="" width="373"><figcaption></figcaption></figure>

**Code Type:**\
**• Numbers**\
**• Letters**

**Send SMS to:**\
**• All users** — the code will be sent to all exchange clients\
**• Guests** — the code will be sent only to guests

**Timeout (sec.)** — the time to wait for a response from the server

**Verification Parameter** — the parameter used to verify the client\
**• "Giving" Account**\
**• "Receiving" Account**\
**• Phone**

**Text** — specify the desired text for the SMS and be sure to include the shortcode \[code] in the message.

In the exchange direction settings, enable SMS code verification and select the verification parameter (if "**Default**" is chosen, the parameter from the general module settings will be used).

<figure><img src="../../.gitbook/assets/image (172).png" alt=""><figcaption></figcaption></figure>