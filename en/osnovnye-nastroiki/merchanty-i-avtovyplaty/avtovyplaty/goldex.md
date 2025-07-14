# GoldEx

{% hint style="danger" %}
<mark style="color:red;">Before setting up auto payouts, be sure to read</mark> [<mark style="color:blue;">the risk warning!</mark>](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/preduprezhdenie-o-riskakh)
{% endhint %}

{% hint style="info" %}
If you need to update the module on your server, please follow this [instruction](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-avtovyplat)
{% endhint %}

## Merchant Account Settings <a href="#merchant-account-settings" id="merchant-account-settings"></a>

After gaining access to your merchant account, log in and go to the "**Preferences**" section.

<figure><img src="../../../.gitbook/assets/image (242).png" alt="" width="411"><figcaption></figcaption></figure>

Copy the token displayed on the page to your clipboard.

<figure><img src="../../../.gitbook/assets/image (241).png" alt=""><figcaption></figcaption></figure>

## Module Settings

In the admin panel, create a new merchant under "**Auto Payouts**" -> "**Add Auto Payout**."

Select GoldEx from the "**Module**" dropdown menu, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (235).png" alt="" width="433"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (236).png" alt="" width="466"><figcaption></figcaption></figure>

**Token** — paste the token you previously copied from the merchant account (under "**Preferences**").

## Special Fields

<figure><img src="../../../.gitbook/assets/image (2139).png" alt="" width="483"><figcaption></figcaption></figure>

**Payment Method** — select the appropriate payment method.

{% hint style="warning" %}
You must create a separate copy of the auto payout module for each payment method you use. In each copy, select the corresponding payment method, then connect that copy on the "**Merchants and Payouts**" tab in the exchange direction settings.

Also, please note that you **must** create a separate copy of the GoldEx module for each payment amount range selected from the dropdown above, and set the corresponding amount range in each module version, \
![](<../../../.gitbook/assets/image (2138).png>)\
so that when multiple copies of the module with different amount ranges are connected under one exchange direction, the system automatically selects the correct module copy based on the payout amount.
{% endhint %}

You can pass client data to the merchant through additional fields created for the "**Receiving**" currency. To do this, create the extra fields and check the corresponding boxes in the currency settings. When the client fills out these fields in the exchange form while creating a request, the data will be sent to the merchant.

<figure><img src="../../../.gitbook/assets/image (243).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Field names:

* `get_cardholder` or `cardholder`
* `get_bankname` or `bankname`
* `get_iban` or `iban`
* `get_phone` or `phone`

Use one of the names from the list above in the "**Unique ID**" field (you can fill out the other fields as you see fit).

![](<../../../.gitbook/assets/image (2004).png>)
{% endhint %}

<figure><img src="../../../.gitbook/assets/image (244).png" alt=""><figcaption><p>Additional fields settings (the unique ID from the corresponding field settings is shown in parentheses)</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (246).png" alt="" width="533"><figcaption><p>Exchange form</p></figcaption></figure>

## Continuing the setup

Next, proceed with configuring the module by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-merchantov-avtovyplat).