# Payeer

{% hint style="danger" %}
<mark style="color:red;">Before setting up auto payouts, please read the</mark> [<mark style="color:blue;">risk warning</mark>](https://premium.gitbook.io/main/en/basic-settings/merchants-and-auto-payments/auto-payments/risk-warning)<mark style="color:blue;">!</mark>
{% endhint %}

{% hint style="info" %}
If you need to update the module on your server, please refer to the [instructions](https://premium.gitbook.io/main/en/en/basic-settings/faq/updating-script-files-on-the-server/how-to-update-files-on-the-server#merchant-and-auto-payout-modules).
{% endhint %}

{% hint style="danger" %}
Please note that Payeer always rounds transaction fees up, which means your clients may receive amounts that are either higher or lower than expected. The discrepancy can be up to tenths of a unit.
{% endhint %}

## Settings in the Merchant's Personal Account

1. Register or log in to the [Payeer](https://payeer.com/) system.
2. Complete the account verification in the "**Profile and Verification**" section to use the API.
3. Confirm your domain.

<figure><img src="../../../.gitbook/assets/image (954) (1).png" alt="" width="524"><figcaption></figcaption></figure>

4. Go to the "**API" -> "Mass Payouts**" section and click the "**Add**" button. Fill in the required fields and click "**Add API**".

* **Name** — the name of the service in the merchant's personal account, any name you choose
* **Secret Key** — the key that will be used for API authorization
* **IP Address** — the IP address of your server

<figure><img src="../../../.gitbook/assets/image (599) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## Module Settings

In the admin panel, go to the "**Merchants**" -> "**Auto Payouts**" section, click the "**Add**" button, and select Payeer.

<figure><img src="../../../.gitbook/assets/image (596) (1).png" alt="" width="490"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (597) (1).png" alt="" width="446"><figcaption></figcaption></figure>

**Wallet Number** — the wallet specified in your Payeer personal account

**API ID** — the ID from your Payeer personal account

**API Key** — the secret key from your Payeer personal account

## Continuing the Setup

Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/main/en/en/basic-settings/merchants-and-auto-payments/merchants/general-merchant-settings).
