# Evo Pay

{% hint style="info" %}
If you need to update the module on your server, please follow the [instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-merchantov).
{% endhint %}

## Merchant Account Settings

{% hint style="warning" %}
To discuss terms and set up the connection, please contact a service representative ([https://t.me/evopayceo](https://t.me/evopayceo) or [https://t.me/tethermckenna](https://t.me/tethermckenna)).

**Disclaimer:** When integrating your website with any service, please carefully assess the potential risks involved in the partnership.
{% endhint %}

Log in to your [EVO personal account](https://evo-pay.net/login). Go to the "**Settings**" section and create an API key by clicking the "**Create API KEY**" button.

<figure><img src="../../../.gitbook/assets/image (51).png" alt=""><figcaption></figcaption></figure>

Copy the generated key (without the `API KEY:` prefix) to your clipboard or save it in a text file.

<figure><img src="../../../.gitbook/assets/image (55).png" alt="" width="324"><figcaption></figcaption></figure>

Next, open the module settings in the Premium Exchanger admin panel.

To enable webhook notifications for status updates on requests, enter the URL from the merchant module settings in your EVO personal account. Additionally, whitelist all the merchant’s IP addresses that send webhooks in your firewall (request the list of IP addresses directly from the merchant).

<figure><img src="../../../.gitbook/assets/image (56).png" alt=""><figcaption></figcaption></figure>

To update request statuses without using a Cron job, add a webhook in your EVO personal account, select the "**Order**" method, and paste the previously copied webhook URL. Save your changes.

<figure><img src="../../../.gitbook/assets/image (2119).png" alt=""><figcaption></figcaption></figure>

## Module Settings

In the admin panel, create a new merchant by going to "**Merchants**" ➔ "**Add Merchant**."

Select Evo from the dropdown menu in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (58).png" alt="" width="422"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (57).png" alt="" width="424"><figcaption></figcaption></figure>

**Domain** — leave this field empty

**API Key** — paste the API key you copied earlier from the merchant account

## Special Fields

<figure><img src="../../../.gitbook/assets/image (59).png" alt="" width="455"><figcaption></figcaption></figure>

**Payment Method** — select the appropriate method for receiving funds from the client (by default, two methods are available: `BANK_CARD` — to obtain bank card details, and `SBP` — to get a phone number for topping up via the Faster Payments System).

<figure><img src="../../../.gitbook/assets/image (60).png" alt="" width="318"><figcaption></figcaption></figure>

If you select "**All**," the merchant will provide any available payment details, regardless of the method.

**Add** — add your own payment methods (not used without instructions from the merchant).

{% hint style="warning" %}
For each payment method you use, you need to create a separate copy of the merchant module, select the corresponding method in it, and then connect this copy on the "**Merchants and Payouts**" tab in the exchange direction settings, where the "**Give**" currency matches the appropriate currency.
{% endhint %}

**Recalculate the request if the payment amount changes** — this option works similarly to the [main option for recalculating the request amount](https://premium.gitbook.io/main/osnovnye-nastroiki/valyuty-i-napravleniya-obmena/sozdanie-novogo-napravleniya#pereschet-po-summe-oplaty).

{% hint style="warning" %}
If a request is made for 5,000 rubles, the merchant may require a payment within the range of 4,999.50 to 5,000.50 rubles (allowing a deviation of up to 100 rubles). The merchant may either require a different amount or accept the originally specified sum.

Therefore, if the client sees an amount of 5,000 rubles, the merchant might not automatically confirm the payment if the actual amount paid differs slightly (by a few rubles or kopecks).

This new option integrates with the request recalculation module. When the necessary conditions are met and a discrepancy in amounts is detected, the recalculation process will start automatically.

The new amount and recalculation are based on the value selected in the "**Expected amount to be credited**" parameter.

![](<../../../.gitbook/assets/image (53).png>)

If the recalculation feature is enabled in the merchant settings, the system will handle discrepancies automatically, and no further action is required.


However, if recalculation is disabled, the new amount will be recorded in the corresponding field. In this case, it is necessary to display this specific field to the client so they can see the current amount to be transferred. Otherwise, the client will see the amount specified in the application, which depends on the shortcode used.  
{% endhint %}

**Operation Status** — shows the module connection status ("<mark style="color:green;">**OK**</mark>" – module connected, "<mark style="color:red;">**ERROR**</mark>" – authorization error in the module, a valid API key must be provided)

## Continuing the Setup

Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).