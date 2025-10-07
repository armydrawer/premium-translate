# Bitbanker

{% hint style="info" %}
If you need to update a module on the server, please refer to the [instructions](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat).
{% endhint %}

{% hint style="success" %}
For any questions related to the service, please contact support via the chat on the [Bitbanker](https://bitbanker.org) website.
{% endhint %}

## Merchant Account Settings

[Register](https://app.bitbanker.org/auth/register) for the service and log in to your merchant account. Navigate to the API section.

<figure><img src="../../../.gitbook/assets/image (2007)_eng.png" alt="" width="222"><figcaption></figcaption></figure>

Copy the provided API Key to your clipboard or a text file.

<figure><img src="../../../.gitbook/assets/image (2006)_eng.png" alt="" width="549"><figcaption></figcaption></figure>

To enable the callback for changing the application status, specify the URL from the merchant module settings in the "**API**" section and add all the merchant's IP addresses that send callbacks to your firewall's whitelist (request the list of addresses directly from the merchant).

<figure><img src="../../../.gitbook/assets/image (203)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (202)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

## Module Settings

In the admin panel, create a new merchant in the "**Merchants**" -> "**Add Merchant**" section.

Select Bitbanker from the dropdown list in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (232)_eng.png" alt="" width="417"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (233)_eng.png" alt="" width="464"><figcaption></figcaption></figure>

**API Key** — The API Key you copied earlier from the merchant account.

## Special Fields

<figure><img src="../../../.gitbook/assets/image (234)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

**Network** — Choose the appropriate network for receiving funds from the customer.

{% hint style="warning" %}
For each payment method used, you need to create a separate copy of the merchant module, selecting the corresponding network, and then connect this copy in the "**Merchants and Payments**" tab in the exchange direction settings, where the currency in "**I Give**" will be the appropriate currency.
{% endhint %}

## Continuing Configuration

Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).