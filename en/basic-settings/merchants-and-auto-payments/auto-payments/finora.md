# Finora

{% hint style="danger" %}
Before setting up automatic payouts, please read the [risk warning!](https://premium.gitbook.io/main/en/basic-settings/merchants-and-auto-payments/auto-payments/risk-warning)
{% endhint %}

{% hint style="info" %}
If you need to update the module on the server, please refer to the [instructions](https://premium.gitbook.io/main/en/basic-settings/faq/updating-script-files-on-the-server/how-to-update-files-on-the-server#merchant-and-auto-payout-modules).

<mark style="color:red;">Please note that when updating the module, you need to reconfigure it according to the instructions below, because after updating the files, all fields and settings of the module will be reset to the default state.</mark>
{% endhint %}

{% hint style="warning" %}
For discussions regarding terms and connections, please contact a service representative.

**Disclaimer**: When connecting your website to any service, please assess the potential risks of collaboration on your own.
{% endhint %}

{% hint style="warning" %}
Please note that when using the Finora automatic payout module, the actual payout amount is always rounded to two decimal places on the service side.
{% endhint %}

## Module Settings

In the admin panel, create a new merchant in the "**Merchants**" ➔ "**Add Automatic Payout**" section.

Select Finora from the dropdown list in the "**Module**" field, provide a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/изображение (67).png" alt=""><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/изображение (71).png" alt=""><figcaption></figcaption></figure>

**Login (Personal Account)** — your login for the Finora personal account

**OTP Key (Personal Account)** — the OTP key issued to you by your Finora manager

**Login (SSO Payout)** — the login issued to you by your Finora manager

**OTP Key (SSO Payout)** — the OTP key issued to you by your Finora manager

**Private Key** — the private key from your Finora personal account (issued according to the instructions below)

{% hint style="warning" %}
Before you start working, you need to generate a public key (**Public Key**), which should be saved in the payment system's personal account (**Security - Your Public Key**), and the private key (**Private Key**) should be entered in the module settings in the "**Private Key**" field.

![](<../../../.gitbook/assets/изображение (89).png>)

For convenience, a pair of keys is automatically generated for working with the merchant (the **Sodium** service/extension must be running on the server for the key generator to work correctly). Copy these keys from the automatic payout module settings and paste them into the corresponding fields as per the instructions above.

<img src="../../../.gitbook/assets/изображение (94).png" alt="" data-size="original">
{% endhint %}

## Special Fields

<figure><img src="../../../.gitbook/assets/изображение (98).png" alt=""><figcaption></figcaption></figure>

**Payment Method** — select the appropriate method from the list.

{% hint style="info" %}
### Additional Fields for the Application

To correctly transmit recipient data to the payment system, you need to add additional fields in the exchange directions.

To do this, create and add additional fields for the corresponding currencies for payouts. Be sure to specify a variable in the "Unique ID" field (in lowercase) and make the field mandatory.

**1. Additional Field for Recipient's Full Name**

*   **Unique ID:** `get_cardholder/cardholder`&#x20;

    <figure><img src="../../../.gitbook/assets/изображение (191).png" alt="" width="498"><figcaption></figcaption></figure>
* **Purpose:** Full name of the payment recipient (Full Name)
* **Processing Priority:**
  * `get_cardholder` or `cardholder` (priority field)
  * Automatically generated from the client's personal data (Full Name from Personal Data)

**2. Additional Field for Card Number**

* **Unique ID:** `get_account/account`
* **Purpose:** Recipient's card number
* **Processing Priority:**
  * `get_account` or `account` (priority field)
  * "To Account" field from currency settings

**3. Additional Field for Phone Number**

* **Unique ID:** `get_phone/phone`
* **Purpose:** Recipient's phone number (must include the prefix "+")
* **Processing Priority:**
  * `get_phone` or `phone` (priority field)
  * "To Account" field from currency settings

**4. Additional Field for Bank Name**

* **Unique ID:** `get_bankname/bankname`
* **Purpose:** Name of the recipient's bank (the list of available banks should be confirmed in the payment system's support chat)
* **Processing Priority:**
  * `get_bankname` or `bankname` (priority field)
  * Currency from the exchange direction

After adding these fields, they will appear in the exchange form and will be mandatory for the client to fill out when creating a payout request.

**3. Choosing the Payment Method**

In the module settings, you can choose how the payout details will be determined.

* **Automatically:** The system will determine the type of details based on the entered data:
  * **Phone:** if the value starts with "+" and contains between 10 and 15 characters.
  * **Card:** if the value contains between 12 and 19 characters.
* **Card:** Forcefully use the value from the card number fields (`get_account/account` or "To Account") for the payout.
* **Phone:** Forcefully use the value from the phone number fields (`get_phone/phone` or "To Account") for the payout.
{% endhint %}

To operate the automatic payout module without using a [cron job](https://premium.gitbook.io/main/en/basic-settings/faq/how-to-create-a-cron-job-on-a-server), specify the link from the module settings

<figure><img src="../../../.gitbook/assets/изображение (163).png" alt=""><figcaption></figcaption></figure>

in the Finora personal account in the **PayOut Webhook** field:

<figure><img src="../../../.gitbook/assets/изображение (152).png" alt=""><figcaption></figcaption></figure>

## Continuing the Setup <a href="#prodolzhenie-nastroiki" id="prodolzhenie-nastroiki"></a>

Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/main/en/basic-settings/merchants-and-auto-payments/auto-payments/general-auto-payment-settings).
