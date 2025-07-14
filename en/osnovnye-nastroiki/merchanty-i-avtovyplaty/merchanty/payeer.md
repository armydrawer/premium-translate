# Payeer

## Merchant Account Settings

1. Register or log in to your account at [Payeer](https://payeer.com/).
2. Complete account verification in the "**Profile and Verification**" section to enable API access.
3. Go to the "**API**" section and click "**Add**". Fill in the required fields and click "**Add Merchant**".

<figure><img src="../../../.gitbook/assets/image (1535).png" alt=""><figcaption></figcaption></figure>

Complete the domain verification process.

<figure><img src="../../../.gitbook/assets/image (954).png" alt="" width="524"><figcaption></figcaption></figure>

Fill out the form that appears.

<figure><img src="../../../.gitbook/assets/image (843).png" alt="" width="459"><figcaption></figcaption></figure>

* **Success URL** — `https://YOUR_DOMAIN/merchant-payeer_success.html`
* **Fail URL** — `https://YOUR_DOMAIN/merchant-payeer_fail.html`
* **Return URL (Handler URL)** — `https://YOUR_DOMAIN/merchant-payeer_status.html`

Replace **`YOUR_DOMAIN`** with the domain name of your exchange service. If you added a hash to the **Return URL** in the merchant module settings, be sure to include the URL with the hash.

<figure><img src="../../../.gitbook/assets/image (1536).png" alt=""><figcaption></figcaption></figure>

Submit your store for moderation so it can start accepting payments.

## Module Settings

In the admin panel, go to "**Merchants**" -> "**Merchants**", click "**Add**", and select Payeer.

<figure><img src="../../../.gitbook/assets/image (1537).png" alt="" width="466"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure src="../../../.gitbook/assets/image (1538).png" alt="" width="450"><figcaption></figcaption></figure>

**Secret Key** — the key provided in your Payeer account when creating the store

**Store ID** — the store ID from your Payeer account

## Continuing Setup

Next, continue configuring the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).