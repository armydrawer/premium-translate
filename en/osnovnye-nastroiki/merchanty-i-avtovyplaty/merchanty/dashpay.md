# DashPay

{% hint style="info" %}
If you need to update the module on your server, please follow the [instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-merchantov).
{% endhint %}

{% hint style="warning" %}
To discuss terms and connection details, please contact the [service representative](https://t.me/adamdashpay).

**Disclaimer:** When connecting your website to any service, please independently assess the potential risks involved in the partnership.
{% endhint %}

## Merchant Account Settings

Register on the [DashPay](https://dashpayment.pro/) service. Log in to your personal account, go to the "**Profile**" section ➔ "**Merchants**," and create a new merchant.

<figure><img src="../../../.gitbook/assets/image (131).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Copy the URLs for all "**Redirect URL**" fields later in the settings of the created merchant module and paste them into the corresponding fields (pay close attention to the end of each URL!). Save these settings.

<img src="../../../.gitbook/assets/image (140).png" alt="" data-size="original">

![](<../../../.gitbook/assets/image (141).png>)
{% endhint %}

Copy the "**Basic Token**" for the created merchant to your clipboard or save it in a text file.

<figure><img src="../../../.gitbook/assets/image (138).png" alt=""><figcaption></figcaption></figure>

Go to the "**Main Settings**" tab, click the "Update" button, and copy the generated API token.

<figure><img src="../../../.gitbook/assets/image (136).png" alt="" width="563"><figcaption></figcaption></figure>

## Module Settings

In the admin panel, create a new merchant under "**Merchants**" ➔ "**Add Merchant**."

Select DashPay from the dropdown menu in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (142).png" alt="" width="416"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (133).png" alt="" width="422"><figcaption></figcaption></figure>

**API Token** — the API token you copied earlier from the merchant’s personal account

**Basic Token** — the Basic token you copied earlier from the merchant’s personal account

## Special Fields

**Merchant Type:**

<figure><img src="../../../.gitbook/assets/image (144).png" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
The merchant type is permanently assigned to the configured module and cannot be changed after the first transaction request using this module.
{% endhint %}

To use a different type of merchant, you need to create a separate copy by selecting another type and connect it in the desired exchange direction.  
{% endhint %}

* **Requisites** — the merchant’s details will be displayed in the request.

<figure><img src="../../../.gitbook/assets/image (147).png" alt="" width="563"><figcaption></figcaption></figure>

{% hint style="warning" %}
When choosing this type of requisites delivery, the request creation time may increase up to 20 seconds due to the requisites being selected on the merchant’s side.
{% endhint %}

* **Payment link** — the request will show a "**Proceed to Payment**" button. When clicked, the client will be redirected to the merchant’s payment page, where the requisites will be displayed or selected.

<figure><img src="../../../.gitbook/assets/image (148).png" alt="" width="563"><figcaption></figcaption></figure>

**Payment method:**

<figure><img src="../../../.gitbook/assets/image (145).png" alt="" width="360"><figcaption></figcaption></figure>

* **card_number** — bank card number for receiving ruble payments  
* **payment_account_number** — bank account number for receiving ruble payments  
* **phone_number** — phone number for receiving ruble payments via the SBP (System of Fast Payments)

## Continuing the setup

Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).