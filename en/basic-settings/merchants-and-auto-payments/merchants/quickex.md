# Quickex

{% hint style="info" %}
If you need to update a module on the server, please refer to the [instructions](https://premium.gitbook.io/main/en/en/basic-settings/faq/updating-script-files-on-the-server/how-to-update-files-on-the-server#merchant-and-auto-payout-modules).
{% endhint %}

{% hint style="warning" %}
The Quickex module should only be used for transactions in the **cryptocurrency to cryptocurrency** direction.

Please note that in order for the merchant to accept Quickex payments, you must also install the [Quickex auto-payment module](https://premium.gitbook.io/main/en/basic-settings/merchants-and-auto-payments/auto-payments/quickex) in the same exchange direction. The receiving module processes payments immediately after funds are received from the client, while the auto-payment module confirms the payment to change the status of the request to "**Completed Request**."

It is **always necessary** to use the Quickex receiving module in conjunction with the [auto-payment module](https://premium.gitbook.io/main/en/basic-settings/merchants-and-auto-payments/auto-payments/quickex) (if another auto-payment module is connected in the exchange direction, **double payments will occur**).

Additionally, keep in mind that payments are **always** made at the service's exchange rate, so it is highly recommended to use the [Quickex parser](https://premium.gitbook.io/main/en/basic-settings/valyuty-i-napravleniya-obmena/kursy-valyut/parser-kursov-valyut-parsery-2.0) for the exchange rate in the direction where Quickex is connected, and to enable [request recalculation based on the exchange rate](https://premium.gitbook.io/main/en/basic-settings/valyuty-i-napravleniya-obmena/sozdanie-novogo-napravleniya#pereschet-po-kursu-obmena) to ensure that the actual payout amount matches the amount in the request.
{% endhint %}

## Merchant Account Settings

Register on the [Quickex](https://quickex.io/) service.

## Module Settings

In the admin panel, create a new merchant in the "**Merchants**" section ➔ "**Add Merchant**."

Select Quickex from the dropdown menu in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (2134) (1).png" alt="" width="398"><figcaption></figcaption></figure>

Fill in the required fields (except for the "**Domain**").

<figure><img src="../../../.gitbook/assets/image (2225) (1).png" alt="" width="490"><figcaption></figcaption></figure>

**Domain —** this field should be filled **only if** your Quickex manager has instructed you to do so (<mark style="color:green;">in all other cases, leave this field blank</mark>).

**Partner ID** — the ID provided to you by the merchant representative for tracking partner requests.

**Markup (%)** — the percentage by which the Quickex exchange rate used for requests in the connected merchant's exchange direction will be <mark style="color:green;">**increased**</mark>.

{% hint style="success" %}
Example: if the base rate for BTC/USDT is 1 to 102,000, and the markup is 2%, the final rate for the user will be 1 to 104,040 for the purchase request.
{% endhint %}

**Only enter a positive value in this field!**

{% hint style="warning" %}
<mark style="color:red;">**Important!**</mark> To compensate for the specified markup, add a coefficient with the same value but in the opposite direction in the "**Parsers 2.0**" ➔ "**Rates**" section for the Quickex rate that will be used in the exchange direction with this merchant.

Example:\
If you specified a markup of 2% in the "**Markup**" field, use the formula `[shortcode]*0.98` for the opposite side.

<img src="../../../.gitbook/assets/image (2226) (1).png" alt="" data-size="original">

If the rate is reversed, use parentheses and divide one by the shortcode: `1/([shortcode]*0.98)`

<img src="../../../.gitbook/assets/image (2227) (1).png" alt="" data-size="original">

**If the coefficient is not included in the formula, the rate displayed to the end user will be 1 = 1, and the user will effectively receive an exchange rate that is 2% lower than stated, as the "Markup" field indicates 2% — this will lead to negative feedback from users.**

In the second screenshot of the instructions (in the merchant module settings), a markup of 2% is set.

The base rate for ETH/USDT is 4,336.78 - for 1 ETH, we receive 4,336.78 USDT. However, we need to reduce this rate for the end user, as a markup of 2% is set. We apply the coefficient of 0.98 for ETH/USDT in the formula. The final rate that the user will see is 4250.05 USDT for 1 ETH.

For the reverse rate, the formula should be written for the outgoing rate and will look like `1/([quickex_usdttrc20eth]*0.98)` — note that the shortcodes differ: `ethusdttrc20` and `usdttrc20eth`

<mark style="color:red;">**Important!**</mark> **Do not forget about the parentheses; otherwise, the formula will not work correctly.**
{% endhint %}

## Special Fields

<figure><img src="../../../.gitbook/assets/image (2136) (1).png" alt="" width="374"><figcaption></figcaption></figure>

**Currency "You Give/You Receive"** — select the currencies for which the details will be displayed in the request (the currency "**You Give**") and which will be paid to the client ("**You Receive**").

When selecting the "**Automatically**" option, the XML code for the currency specified in its settings will be used.

{% hint style="warning" %}
For the proper functioning of the receiving and payment modules for the currency "**You Receive**" in the exchange direction where Quickex is used, the mandatory field "**To Account**" must be active and filled out by the client in the request creation form.
{% endhint %}

## Accounting for Withdrawal Network Fees

In the current integration of Quickex and Premium Exchanger, there is no way to automatically account for withdrawal network fees. To avoid discrepancies in the rate, you need to specify an additional fee in the settings for each exchange direction.

In the "**Exchange Directions**" section — select the desired direction — go to the "**Exchange Point Fees**" tab — in the "**Additional Recipient Fee**" field, specify the withdrawal fee for the asset "**You Receive**."

<figure><img src="../../../.gitbook/assets/image (2228) (1).png" alt="" width="563"><figcaption></figcaption></figure>

After this, in the exchange form on the website, an additional field "**With Fee**" will be added to the "**You Receive**" rate, where the rate will be displayed correctly, taking into account the network fee.

For convenience, in the "**Exchange Directions**" — "**Basic Settings**," you can add the direction to a group of directions. This will simplify the process if you need to change the network fee in the bulk editor.

<figure><img src="../../../.gitbook/assets/image (2231) (1).png" alt="" width="563"><figcaption></figcaption></figure>

The bulk editor can be found in the "**Exchange Directions**" — "**Bulk Editor for User Information**." In the "**Field**" dropdown, select “**Exchange Point Fees**,” and also choose the necessary group of directions. After that, all relevant fields will be displayed.

<figure><img src="../../../.gitbook/assets/image (2230) (1).png" alt="" width="563"><figcaption></figcaption></figure>

You can view the network fees for Quickex assets in the [table](https://docs.google.com/spreadsheets/d/1MD3ULwbrcBlJOjM8RO7AZTwPk-Y0TPqGTPigJc_WyoY/edit?gid=0#gid=0).

## Continuing Setup

Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/main/en/en/basic-settings/merchants-and-auto-payments/merchants/general-merchant-settings).
