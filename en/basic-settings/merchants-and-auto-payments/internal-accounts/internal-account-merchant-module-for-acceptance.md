# Internal Account (Merchant Module for Acceptance)

In the exchange point control panel, go to the "**Modules" → "Modules"** section and activate the "**Internal Account**" module (`iac` — current module, `domacc` — outdated).

In the "**Merchants"** -> "**Merchants**" section, click the "**Add**" button. In the new window, select the "**Internal Account**" module from the dropdown list.

<figure><img src="../../../.gitbook/assets/image (1092)_eng.png" alt=""><figcaption></figcaption></figure>

Configure the module according to the [general settings for merchant modules](https://premium.gitbook.io/main/en/en/basic-settings/merchants-and-auto-payments/merchants/general-merchant-settings):

In the control panel, go to the "**Exchange Directions**" section and create a new direction or edit an existing one that uses currency for the internal account. Switch to the "**Merchants and Payments**" tab and select "**Internal Account**" for the "**Merchant**" parameter.

{% hint style="warning" %}
Please note that a single copy of the "**Internal Account**" acceptance module can be used for all internal currencies — since there are no specific settings for the currency in the module, it will work with all currencies that are allowed for internal use.
{% endhint %}
