# Evo Pay

{% hint style="info" %}
If you need to update the module on the server, please refer to the [instructions](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat).
{% endhint %}

## Merchant Account Settings

{% hint style="warning" %}
To discuss terms and connection, please contact a service representative ([https://t.me/evopayceo](https://t.me/evopayceo) or [https://t.me/tethermckenna](https://t.me/tethermckenna)).

**Disclaimer**: When connecting your website to any service, please assess the potential risks of collaboration on your own.
{% endhint %}

Log in to your [EVO account](https://evo-pay.net/login). Go to the "**Settings**" section and create an API key by clicking the "**Create API KEY**" button.

<figure><img src="../../../.gitbook/assets/image (51).png" alt=""><figcaption></figcaption></figure>

Copy the generated key (without `API KEY:`) to your clipboard or a text file.

<figure><img src="../../../.gitbook/assets/image (55).png" alt="" width="324"><figcaption></figcaption></figure>

Navigate to the module settings in the Premium Exchanger admin panel.

To enable the webhook for status changes of requests, specify the URL from the merchant module settings in your EVO account. Additionally, add all IP addresses from which the merchant sends webhooks to your firewall's whitelist (you can request the list of IP addresses directly from the merchant).

<figure><img src="../../../.gitbook/assets/image (56).png" alt=""><figcaption></figcaption></figure>

To update request statuses without using a Cron job, add the webhook in your EVO account, select the "**Order**" method, and paste the previously copied webhook URL. Save the changes.

<figure><img src="../../../.gitbook/assets/image (2119).png" alt=""><figcaption></figcaption></figure>

## Module Settings

In the admin panel, create a new merchant in the "**Merchants**" ➔ "**Add Merchant**" section.

Select Evo from the dropdown list in the "**Module**" field, enter a name for the module, and click "**Save**".

<figure><img src="../../../.gitbook/assets/image (58).png" alt="" width="422"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (57).png" alt="" width="424"><figcaption></figcaption></figure>

**Domain** — leave this field empty.

**API Key** — the API key you copied earlier from the merchant account.

## Special Fields

<figure><img src="../../../.gitbook/assets/image (59).png" alt="" width="455"><figcaption></figcaption></figure>

**Payment Method** — choose the appropriate method for receiving funds from the client (by default, two methods are available: `BANK_CARD` — for receiving bank card details and `SBP` — for obtaining a phone number for top-ups via SBP).

<figure><img src="../../../.gitbook/assets/image (60).png" alt="" width="318"><figcaption></figcaption></figure>

When selecting "**All**," the merchant will be provided with any available details, regardless of the method.

**Add** — to add your own payment methods (not used without instructions from the merchant).

{% hint style="warning" %}
For each payment method used, a separate copy of the merchant module must be created, selecting the corresponding method, and then this copy should be connected in the "**Merchants and Payments**" tab in the exchange direction settings, where the currency in "**I Give**" will be the appropriate currency.
{% endhint %}

**Recalculate Request if Payment Amount Changes** — this option works similarly to the [main option for recalculating the amount for a request](https://premium.gitbook.io/main/osnovnye-nastroiki/valyuty-i-napravleniya-obmena/sozdanie-novogo-napravleniya#pereschet-po-summе-oplaty).

{% hint style="warning" %}
If a request is specified for an amount of 5000 rubles, the merchant may require a payment within the range of 4999.50–5000.50 rubles (possible deviation — up to 100 rubles). The merchant can either require a different amount or accept the originally specified amount.

Thus, if the client sees an amount of 5000 rubles, the merchant may not automatically confirm the payment if the actual amount paid differs slightly (by a few rubles or kopecks).

This new option integrates with the request recalculation module. If the necessary conditions are met and discrepancies in amounts are detected, the recalculation process will be automatically initiated.

The new amount and recalculation are based on the selected value in the "**Expected Amount to be Credited**" parameter.

![](<../../../.gitbook/assets/image (53).png>)

If the recalculation function is enabled in the merchant settings, the system will automatically handle discrepancies without additional intervention.

However, if recalculation is disabled, the new amount will be recorded in the corresponding field. In this case, it is necessary to display this field to the client so they can see the actual amount for the transfer. Otherwise, the client will see the amount specified in the request, which depends on the shortcode used.
{% endhint %}

**Status** — displays the connection status of the module ("<mark style="color:green;">**OK**</mark>" - module connected, "<mark style="color:red;">**ERROR**</mark>" - error during module authorization, a valid API key is required).

## Continuing the Setup

Next, proceed to configure the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).