# Payeer

## Merchant Account Settings

1. Register or log in to your [Payeer](https://payeer.com/) account.
2. Complete the account verification process in the "**Profile and Verification**" section to use the API.
3. Go to the "**API**" section and click the "**Add**" button. Fill in the required fields and click "**Add Merchant**."

<figure><img src="../../../.gitbook/assets/image (1535)_eng.png" alt=""><figcaption></figcaption></figure>

Complete the domain verification process.

<figure><img src="../../../.gitbook/assets/image (954)_eng.png" alt="" width="524"><figcaption></figcaption></figure>

Fill out the form that appears.

<figure><img src="../../../.gitbook/assets/image (843)_eng.png" alt="" width="459"><figcaption></figcaption></figure>

* **Successful Payment URL (SUCCESS URL)** — `https://YOUR_DOMAIN/merchant-payeer_success.html`
* **Failed Payment URL (FAIL URL)** — `https://YOUR_DOMAIN/merchant-payeer_fail.html`
* **Return URL (RETURN URL)** — `https://YOUR_DOMAIN/merchant-payeer_status.html`

Replace **`YOUR_DOMAIN`** with the name of your exchange point's domain. If you have added a hash for the **Return URL (RETURN URL)** in the merchant module settings, include the URL with the hash.

<figure><img src="../../../.gitbook/assets/image (1536)_eng.png" alt=""><figcaption></figcaption></figure>

Submit your store for moderation so that it can start accepting payments.

## Module Settings

In the admin panel, go to the "**Merchants**" -> "**Merchants**" section, click the "**Add**" button, and select Payeer.

<figure><img src="../../../.gitbook/assets/image (1537)_eng.png" alt="" width="466"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (1538)_eng.png" alt="" width="450"><figcaption></figcaption></figure>

**Secret Key** — the key provided in your Payeer account when creating the store.

**Store ID** — the store ID from your Payeer account.

## Continuing the Setup

Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/main/en/en/basic-settings/merchants-and-auto-payments/merchants/general-merchant-settings).