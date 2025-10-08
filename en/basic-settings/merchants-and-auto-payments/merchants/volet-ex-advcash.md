# Volet (formerly Advcash)

{% hint style="info" %}
If you need to update the module on your server, please refer to the [instructions](https://premium.gitbook.io/main/en/basic-settings/faq/updating-script-files-on-the-server/how-to-update-files-on-the-server#merchant-and-auto-payout-modules).
{% endhint %}

## Merchant Account Settings

Register in the [Volet](https://account.volet.com/register) system and verify your account to work with the API.

{% hint style="warning" %}
To receive funds into your merchant accounts, it is sufficient to create an **SCI (Shopping Cart Interface)** following the instructions below. If you also want to withdraw funds from your merchant accounts, you will need to create a new **API (Application Programming Interface)** as well.
{% endhint %}

1. Go to the "**For Developers**" section and click the "**Create New SCI**" button.

<figure><img src="../../../.gitbook/assets/image (1425)_eng.png" alt="" width="267"><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (1422)_eng.png" alt=""><figcaption></figcaption></figure>

Select the payment systems you want to work with and click "**Continue**."

<figure><img src="../../../.gitbook/assets/image (677)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

Fill out the form that appears and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (678)_eng.png" alt="" width="550"><figcaption></figcaption></figure>

**Successful Transaction Page** — `https://your_domain/merchant-advcash_success.html`

**Failed Transaction Page** — `https://your_domain/merchant-advcash_fail.html`

**Status Page** — `https://your_domain/merchant-advcash_status.html`

Replace "**your_domain**" with the name of your exchange point's domain.

{% hint style="warning" %}
For all fields, select the POST method.
{% endhint %}

2. Create a new API for merchant operations.

Go to the "**For Developers**" section and click the "**Create New API**" button.

<figure><img src="../../../.gitbook/assets/image (1425)_eng.png" alt="" width="267"><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (1422)_eng.png" alt=""><figcaption></figcaption></figure>

Fill out the form that appears and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (679)_eng.png" alt="" width="498"><figcaption></figcaption></figure>

## Module Settings

In the admin panel, create a new merchant in the "**Merchants**" -> "**Add Merchant**" section.

Select AdvCash from the dropdown list in the "**Module**" field, provide a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (1424)_eng.png" alt=""><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (1423)_eng.png" alt=""><figcaption></figcaption></figure>

**Account Owner Email** — **the email displayed in the SCI**, as specified in your AdvCash account.

**SCI Name** — **the name of the SCI**, as specified in your AdvCash account.

**SCI Password** — **the password for the SCI**, as specified in your AdvCash account.

**API Name** — **the name of the API**, as specified in your AdvCash account (this is filled in the auto-payment module; you can leave it blank in the funds reception module).

**API Password** — **the password for the API**, as specified in your AdvCash account (this is filled in the auto-payment module; you can leave it blank in the funds reception module).

## Continuing the Setup

Next, proceed to configure the merchant by following the [general setup instructions](https://premium.gitbook.io/main/en/basic-settings/merchants-and-auto-payments/merchants/general-merchant-settings).