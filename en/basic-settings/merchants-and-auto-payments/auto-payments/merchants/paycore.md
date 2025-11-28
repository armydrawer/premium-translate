# Paycore

{% hint style="info" %}
If you need to update the module on the server, please refer to the [instructions](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat).
{% endhint %}

## Merchant Account Settings

{% hint style="warning" %}
To discuss terms and setup, please contact a [service representative](https://t.me/Paycore_pw).

**Disclaimer**: When connecting your website to any service, please assess the potential risks of collaboration on your own.
{% endhint %}

After receiving your login credentials from a [service representative](https://t.me/Paycore_pw), log in to the [PayCore Dashboard](https://paycore.pw/admin) and complete the verification process. Once verified, request an API key from the service representative for integration.

## Module Settings

In the admin panel, create a new merchant by navigating to "**Merchants**" ➔ "**Add Merchant**."

Select Paycore from the dropdown menu in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (2268).png" alt=""><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (2269).png" alt=""><figcaption></figcaption></figure>

**Domain** — leave this field empty.

**API Key** — enter the API key provided to you by the Paycore representative.

{% hint style="warning" %}
Please note that for the Paycore module to function correctly for receiving payments, you must activate the "**From Account**" field in the currency settings that will be used with Paycore. The client will fill in this field with **their phone number** (the number should start with +7), and this number will be sent to the merchant.

![](<../../../.gitbook/assets/image (2270).png>)
{% endhint %}

## Continuing the Setup

Next, proceed to configure the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).