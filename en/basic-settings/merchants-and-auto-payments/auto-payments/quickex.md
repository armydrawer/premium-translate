# Quickex

{% hint style="danger" %}
<mark style="color:red;">Before setting up auto payouts, please read the</mark> [<mark style="color:blue;">risk warning</mark>](https://premium.gitbook.io/main/en/basic-settings/merchants-and-auto-payments/auto-payments/risk-warning)<mark style="color:blue;">!</mark>
{% endhint %}

{% hint style="info" %}
If you need to update the module on the server, please refer to the [instructions](https://premium.gitbook.io/main/en/en/basic-settings/faq/updating-script-files-on-the-server/how-to-update-files-on-the-server#merchant-and-auto-payout-modules).
{% endhint %}

## Merchant Account Settings <a href="#nastroiki-v-lichnom-kabinete-merchanta" id="nastroiki-v-lichnom-kabinete-merchanta"></a>

{% hint style="warning" %}
Please note that the auto payout module is technical and **does not process** the actual payout. The Quickex receiving module initiates the payout immediately after receiving funds from the client, while the auto payout module confirms the payout to change the application status to "**Completed**."

It is **always necessary** to use the Quickex auto payout module in conjunction with the [receiving module](https://premium.gitbook.io/main/en/basic-settings/merchants-and-auto-payments/merchants/quickex).

Additionally, keep in mind that payouts are **always** made at the service's exchange rate. Therefore, it is highly recommended to use the [parser](https://premium.gitbook.io/main/en/basic-settings/valyuty-i-napravleniya-obmena/kursy-valyut/parser-kursov-valyut-parsery-2.0) for Quickex's exchange rate in the direction where Quickex is used, and to enable [application recalculation based on the exchange rate](https://premium.gitbook.io/main/en/basic-settings/valyuty-i-napravleniya-obmena/sozdanie-novogo-napravleniya#pereschet-po-kursu-obmena) to ensure that the actual payout amount matches the amount in the application.
{% endhint %}

## Module Settings <a href="#nastroiki-modulya" id="nastroiki-modulya"></a>

In the admin panel, create a new merchant in the "**Auto Payouts**" section by clicking on "**Add Auto Payout**."

Select Quickex from the dropdown menu in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (29)_eng.png" alt="" width="389"><figcaption></figcaption></figure>

You do not need to fill in the authorization fields.

<figure><img src="https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252Fhcpgo0esYP63gs8hEYlt%252Fimage_eng.png%3Falt%3Dmedia%26token%3D601c0074-951c-408a-b11c-7856129e1e3d&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=1fde9588&#x26;sv=2" alt="" width="563"><figcaption></figcaption></figure>

**Domain —** This field should only be filled out if your Quickex manager has specifically instructed you to do so (in all other cases, leave this field blank).

## Continuing the Setup

Next, proceed to configure the merchant by following the [general setup instructions](https://premium.gitbook.io/main/en/basic-settings/merchants-and-auto-payments/auto-payments/obshie-nastroiki-merchantov-avtovyplat).