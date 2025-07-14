# Bitbanker

{% hint style="info" %}
If you need to update the module on your server, please follow the [instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-merchantov).
{% endhint %}

{% hint style="success" %}
For any questions related to the service, please contact support via the chat on the [Bitbanker website](https://bitbanker.org).
{% endhint %}

## Merchant Account Settings

[Register](https://app.bitbanker.org/auth/register) on the service and log in to your merchant account. Then go to the **API** section.

<figure><img src="../../../.gitbook/assets/image (2007).png" alt="" width="222"><figcaption></figcaption></figure>

Copy the displayed API Key to your clipboard or save it in a text file.

<figure><img src="../../../.gitbook/assets/image (2006).png" alt="" width="549"><figcaption></figcaption></figure>

To enable callback functionality for updating the status of requests, enter the URL from your merchant module settings into the **API** section, and add all merchant IP addresses that send callbacks to your firewall whitelist (request the list of IP addresses directly from the merchant).

<figure><img src="../../../.gitbook/assets/image (203).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (202).png" alt="" width="563"><figcaption></figcaption></figure>

## Module Settings

In the admin panel, create a new merchant by going to **Merchants** -> **Add Merchant**.

Select **Bitbanker** from the dropdown menu in the **Module** field, enter a name for the module, and click **Save**.

<figure><img src="../../../.gitbook/assets/image (232).png" alt="" width="417"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (233).png" alt="" width="464"><figcaption></figcaption></figure>

**API Key** — the API Key you copied earlier from the merchant account.

## Special Fields

<figure><img src="../../../.gitbook/assets/image (234).png" alt="" width="563"><figcaption></figcaption></figure>

**Network** — select the appropriate network for receiving funds from the client.

{% hint style="warning" %}
For each payment method you use, you need to create a separate copy of the merchant module, select the corresponding network in it, and then connect this copy on the **Merchants and Payouts** tab in the exchange direction settings, where the currency in the **Give** field matches the selected network.
{% endhint %}

## Continuing Setup

Next, continue configuring the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).