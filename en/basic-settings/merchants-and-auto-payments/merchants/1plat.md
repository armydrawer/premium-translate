# 1Plat

{% hint style="info" %}
If you need to update the module on the server, please refer to the [instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-merchantov).
{% endhint %}

{% hint style="warning" %}
For discussions regarding terms and connection, please contact a service representative.

**Disclaimer**: When connecting your website to any service, please assess the potential risks of collaboration on your own.
{% endhint %}

{% hint style="warning" %}
Please note that when using the 1Plat payment module, the actual payment amount is always rounded to zero decimal places on the service's side.
{% endhint %}

Register on the [1Plat](https://1plat.money/user/reg) service and log in to your personal account. Create a new store.

<figure><img src="../../../.gitbook/assets/изображение (2).png" alt="" width="563"><figcaption></figcaption></figure>

Fill in the details in the new window and save them.

<figure><img src="../../../.gitbook/assets/изображение.png" alt="" width="424"><figcaption></figcaption></figure>

## Module Settings

In the admin panel, create a new merchant in the "**Merchants**" ➔ "**Add Merchant**" section.

Select 1Plat from the dropdown list in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/изображение (200).png" alt="" width="331"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/изображение (202).png" alt="" width="413"><figcaption></figcaption></figure>

**Domain** — leave this field empty.

**Store ID** — your store's ID on the 1Plat service.

<figure><img src="../../../.gitbook/assets/изображение (195).png" alt=""><figcaption></figcaption></figure>

**Secret Key** — the key copied from the "**Store ➔ Settings**" section in your 1Plat personal account.

<figure><img src="../../../.gitbook/assets/изображение (196).png" alt=""><figcaption></figcaption></figure>

## Special Fields

<figure><img src="../../../.gitbook/assets/изображение (203).png" alt="" width="299"><figcaption></figcaption></figure>

**Merchant Type** (the selected option is tied to the module and cannot be changed later):

* **Payment Link** — returns a payment link in the request, this option works in conjunction with the selected payment method.
* **Requisites** — returns the details for transferring funds in the request via the shortcode \[to\_account].

<figure><img src="../../../.gitbook/assets/изображение (204).png" alt="" width="390"><figcaption></figcaption></figure>

**Payment Method** — choose an appropriate method from the list or manually specify your option in the "**Add**" field (please confirm acceptable options with your 1Plat manager).

This method only works with the selected merchant type "**Payment Link**":

**qr** — generates a QR code.

This method only works with the selected merchant type "**Requisites**":

**alfa** — provides Alfa-Bank details.

**card** — provides a card number from any bank.

**mobile** — provides a phone number.

**sbp** — provides a phone number for payment via SBP.

{% hint style="info" %}
For the option to work, be sure to enable the field for the client to enter a phone number in the exchange form when creating an application

<img src="../../../.gitbook/assets/изображение (205).png" alt="" data-size="original">
{% endhint %}

{% hint style="danger" %}
Please note that a separate copy of the merchant module must be created for each payment method.
{% endhint %}

To operate the module for receiving payments without using a [cron job](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-sozdat-zadanie-cron-na-servere), specify the link from the module settings.

<figure><img src="../../../.gitbook/assets/изображение (199).png" alt=""><figcaption></figcaption></figure>

In your 1Plat personal account, go to "**Store ➔ Settings ➔ Callback**":

<figure><img src="../../../.gitbook/assets/изображение (198).png" alt="" width="563"><figcaption></figcaption></figure>

## Continuing the Setup

Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).
