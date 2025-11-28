# GoldEx

{% hint style="danger" %}
<mark style="color:red;">Before setting up auto payouts, please read the</mark> [<mark style="color:blue;">risk warning!</mark>](https://premium.gitbook.io/main/en/basic-settings/merchants-and-auto-payments/auto-payments/risk-warning)
{% endhint %}

{% hint style="info" %}
If you need to update the module on the server, please refer to the [instructions](https://premium.gitbook.io/main/en/en/basic-settings/faq/updating-script-files-on-the-server/how-to-update-files-on-the-server#merchant-and-auto-payout-modules)
{% endhint %}

## Merchant Account Settings <a href="#nastroiki-v-lichnom-kabinete-merchanta" id="nastroiki-v-lichnom-kabinete-merchanta"></a>

After gaining access to your personal account, log in and navigate to the "**Preferences**" section.

Copy the token displayed on the page to your clipboard.

## Module Settings

In the admin panel, create a new merchant in the "**Auto Payouts**" -> "**Add Auto Payout**" section.

Select GoldEx from the dropdown menu in the "**Module**" field, provide a name for the module, and click "**Save**."

Fill in the required authorization fields.

**Token** — the token you previously copied from the merchant's personal account (in the "**Preferences**" section).

## Special Fields

<figure><img src="../../../.gitbook/assets/image (2139) (1).png" alt="" width="483"><figcaption></figcaption></figure>

**Payment Method** — select the appropriate payment method.

{% hint style="warning" %}
For each payment method used, you must create a separate copy of the auto payout module, selecting the corresponding method, and then connect this copy in the "**Merchants and Payouts**" tab in the exchange direction settings.

Also, please note that it is **mandatory** to create a separate copy of the GoldEx module for each range of amounts from the dropdown list above and set the corresponding amount range in each version of the module,\
![](<../../../.gitbook/assets/image (2138) (1).png>)\
so that among several connected copies of the module with different amount ranges in the same direction, the correct copy is automatically selected based on the amount in the request.
{% endhint %}

You can pass client data to the merchant through additional fields created for the currency "**Receiving**." To do this, create additional fields and check them in the currency settings. When the client fills out these fields in the exchange form while creating a request, the data will be sent to the merchant.

{% hint style="info" %}
Field Names:

* `get_cardholder` or `cardholder` — Cardholder's full name
* `get_bankname` or `bankname` — Bank name
* `get_iban` or `iban` — Bank IBAN
* `get_phone` or `phone` — Phone number
* `get_inn` or `inn` — Tax Identification Number (TIN)
* `get_revTagWiseTag` or `revTagWiseTag` — Identifiers for [Revolut](https://help.revolut.com/ru-EE/help/transfers/internal-transfers/username-payments/revtags/)/[Wise](https://wise.com/ru/help/articles/6DtiR7Ugdp7hfoKJHfRfvJ/%D1%87%D1%82%D0%BE-%D1%82%D0%B0%D0%BA%D0%BE%D0%B5-wisetag-%D0%B8-%D0%BA%D0%B0%D0%BA-%D0%B5%D0%B3%D0%BE-%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D1%8C)

Enter the name from the list above in the "**Unique ID**" field (the other fields can be filled out at your discretion).

<img src="../../../.gitbook/assets/image (2004)_eng.png" alt="" data-size="original">
{% endhint %}

## Continuing the Setup

Next, proceed with the module setup by following the [general setup instructions](https://premium.gitbook.io/main/en/basic-settings/merchants-and-auto-payments/auto-payments/obshie-nastroiki-merchantov-avtovyplat).
