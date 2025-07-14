# Volet (formerly AdvCash)

{% hint style="info" %}
If you need to update the module on your server, please follow the [instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-merchantov).
{% endhint %}

## Merchant Account Setup

Register an account with [Volet](https://account.volet.com/register) and verify it to enable API access.

{% hint style="warning" %}
To receive funds into your merchant accounts, simply create an **SCI (Shopping Cart Interface)** following the instructions below. If you also want to make payouts from your merchant accounts, you will need to create a separate **API (Application Programming Interface)** as well.
{% endhint %}

1. Go to the "**For Developers**" section and click "**Create New SCI**".

<figure><img src="../../../.gitbook/assets/image (1425).png" alt="" width="267"><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (1422).png" alt=""><figcaption></figcaption></figure>

Select the payment systems you want to work with and click "**Continue**".

<figure><img src="../../../.gitbook/assets/image (677).png" alt="" width="563"><figcaption></figcaption></figure>

Fill out the form that appears and click "**Save**".

<figure><img src="../../../.gitbook/assets/image (678).png" alt="" width="550"><figcaption></figcaption></figure>

**Successful transaction page:** `https://your_domain/merchant-advcash_success.html`

**Failed transaction page:** `https://your_domain/merchant-advcash_fail.html`

**Status page:** `https://your_domain/merchant-advcash_status.html`

Replace "**your_domain**" with the domain name of your exchange site.

{% hint style="warning" %}
Use the POST method for all URLs.
{% endhint %}

2. Create a new API for merchant operations.

Go to the "**For Developers**" section and click "**Create New API**".

<figure><img src="../../../.gitbook/assets/image (1425).png" alt="" width="267"><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (1422).png" alt=""><figcaption></figcaption></figure>

Fill out the form and click "**Save**".

<figure><img src="../../../.gitbook/assets/image (679).png" alt="" width="498"><figcaption></figcaption></figure>

## Module Configuration

In the admin panel, create a new merchant under "**Merchants**" -> "**Add Merchant**."

Select AdvCash from the "**Module**" dropdown, enter a name for the module, and click "**Save**".

<figure><img src="../../../.gitbook/assets/image (1424).png" alt=""><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (1423).png" alt=""><figcaption></figcaption></figure>

**Account owner’s email** — the email address displayed in the SCI, as specified in your AdvCash account.

**SCI Name** — the **SCI name** as specified in your AdvCash personal account

**SCI Password** — the **SCI password** as specified in your AdvCash personal account

**API Name** — the **API name** as specified in your AdvCash personal account (to be entered in the auto-payout module; can be left blank in the funds acceptance module)

**API Password** — the **API password** as specified in your AdvCash personal account (to be entered in the auto-payout module; can be left blank in the funds acceptance module)

## Continuing the Setup

Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).