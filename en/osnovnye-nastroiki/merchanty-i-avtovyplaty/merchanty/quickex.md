# Quickex

{% hint style="info" %}
If you need to update the module on your server, please follow the [instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-merchantov).
{% endhint %}

{% hint style="warning" %}
The Quickex module should be used **only** for cryptocurrency-to-cryptocurrency exchange directions.

Please note that to operate a merchant for Quickex receiving, you must also install the [Quickex Auto-Payout module](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/quickex) for the same exchange direction. The receiving module processes the payout immediately after receiving funds from the client, while the auto-payout module confirms the payout, which updates the request status to "**Completed request**."

The Quickex receiving module **must always** be used together with the [auto-payout module](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/quickex). Using any other auto-payout module in the same exchange direction will result in **double payouts**.

Also, keep in mind that payouts are **always** made at the service’s own exchange rate. Therefore, it is highly recommended to use the [Quickex rate parser](https://premium.gitbook.io/main/osnovnye-nastroiki/valyuty-i-napravleniya-obmena/kursy-valyut/parser-kursov-valyut-parsery-2.0) for the exchange direction where Quickex is enabled, and to enable [request recalculation based on the exchange rate](https://premium.gitbook.io/main/osnovnye-nastroiki/valyuty-i-napravleniya-obmena/sozdanie-novogo-napravleniya#pereschet-po-kursu-obmena) to ensure the actual payout amount matches the amount specified in the request.
{% endhint %}

## Merchant Account Setup

Register an account on the [Quickex service](https://quickex.io/).

## Module Configuration

In the admin panel, create a new merchant by going to "**Merchants**" -> "**Add Merchant**."

Select Quickex from the dropdown menu in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (2134).png" alt="" width="398"><figcaption></figcaption></figure>

Fill in the required fields (except for "**Domain**").

<figure><img src="../../../.gitbook/assets/image (27).png" alt="" width="422"><figcaption></figcaption></figure>

**Domain —** fill in this field **only if** your Quickex manager has instructed you to do so.  
<mark style="color:green;">In all other cases, leave this field blank.</mark>

Here is a natural, fluent English translation of the provided text:

---

**Partner ID** — the ID assigned to you by the merchant’s representative to track partner applications.

**Markup (%)** — the percentage by which the Quickex rate used for exchange requests involving the connected merchant will be **increased** (example: markup 2%, base rate: 1 to 102. Rate after applying markup: 1 to 104.04).  
**Please enter only a positive value in this field!**

{% hint style="warning" %}
To compensate for the specified markup, add a coefficient with the same value but a negative sign in the "**Parsers 2.0**" ➔ "**Rates**" section for the Quickex rate used in the exchange direction with this merchant.

Example:  
If you entered a 2% markup in the "**Markup**" field, use the formula `[shortcode]*0.98` for the side opposite to 1 in the rate.

![](<../../../.gitbook/assets/image (2179).png>)
{% endhint %}

## Special Fields

<figure><img src="../../../.gitbook/assets/image (2136).png" alt="" width="374"><figcaption></figcaption></figure>

**"Give/Receive" Currency** — select the currencies whose details will be displayed in the application (the "**Give**" currency) and which will be paid out to the client (the "**Receive**" currency).

If you select "**Automatic**," the currency XML code specified in its settings will be used.

{% hint style="warning" %}
For the pair of receive-pay modules to work correctly for the "**Receive**" currency in the exchange direction using Quickex, the mandatory "**To Account**" field must be active and filled out by the client in the application form.
{% endhint %}

## Continuing Setup

Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).

---

If you need any adjustments or a more formal/informal tone, just let me know!