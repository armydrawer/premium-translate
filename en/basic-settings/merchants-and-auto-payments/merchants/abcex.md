# ABCEx

{% hint style="info" %}
If you need to update the module on the server, please refer to the [instructions](https://premium.gitbook.io/main/en/en/basic-settings/faq/updating-script-files-on-the-server/how-to-update-files-on-the-server#merchant-and-auto-payout-modules).
{% endhint %}

## Merchant Account Settings

Register on the [ABCEx](https://abcex.io/) exchange. Complete the KYC process and enable 2FA in your account under the "**Profile**" section.

<figure><img src="../../../.gitbook/assets/image (229)_eng.png" alt=""><figcaption></figcaption></figure>

## Module Settings

In the admin panel, create a new merchant in the "**Merchants**" -> "**Add Merchant**" section.

Select ABCEx from the dropdown menu in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (227)_eng.png" alt="" width="459"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (228)_eng.png" alt=""><figcaption></figcaption></figure>

**API Key** — This is the key sent to you by your ABCEx manager after completing KYC. To request your API key, contact [https://t.me/ABCEX_management](https://t.me/ABCEX_management).

## Special Fields

<figure><img src="../../../.gitbook/assets/image (230)_eng.png" alt="" width="376"><figcaption></figcaption></figure>

**Wallet** — Select the currency you wish to receive from clients (currently, only USDT is available).

**Network** — Choose the appropriate network for the currency: ETH (ERC20) or TRX (TRC20).

## Continuing the Setup

Next, proceed with the merchant setup by following the [general setup instructions](https://premium.gitbook.io/main/en/en/basic-settings/merchants-and-auto-payments/merchants/general-merchant-settings).