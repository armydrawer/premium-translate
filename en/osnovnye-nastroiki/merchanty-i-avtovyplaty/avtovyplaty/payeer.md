# Payeer

{% hint style="danger" %}
<mark style="color:red;">Before setting up automatic payouts, be sure to read</mark> [<mark style="color:blue;">the risk warning</mark>](https://premiumexchanger.com/wiki/preduprezhdenie-auto/)<mark style="color:blue;">!</mark>
{% endhint %}

{% hint style="info" %}
If you need to update the module on your server, please follow this [guide](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-avtovyplat).
{% endhint %}

{% hint style="danger" %}
Because Payeer always rounds transaction fees up, your clients may receive amounts that are either slightly higher or lower than the stated sum. The discrepancy can be up to a few tenths.
{% endhint %}

## Merchant Account Settings

1. Register or log in to your account at [Payeer](https://payeer.com/).
2. Complete account verification in the "**Profile and Verification**" section to enable API access.
3. Complete the domain verification process.

<figure><img src="../../../.gitbook/assets/image (954).png" alt="" width="524"><figcaption></figcaption></figure>

4. Go to "**API**" -> "**Mass Payouts**" and click "**Add**". Fill in the required fields and click "**Add API**".

* **Name** — a custom name for the service in your merchant dashboard  
* **Secret Key** — the key used for API authorization  
* **IP Address** — the IP address of your server

<figure><img src="../../../.gitbook/assets/image (1542).png" alt="" width="563"><figcaption></figcaption></figure>

## Module Settings

In the admin panel, go to "**Merchants**" -> "**Auto Payouts**", click "**Add**", and select Payeer.

<figure><img src="../../../.gitbook/assets/image (1539).png" alt="" width="490"><figcaption></figcaption></figure>

Fill in the authorization fields as shown.

<figure><img src="../../../.gitbook/assets/image (1540).png" alt="" width="446"><figcaption></figcaption></figure>

**Wallet Number** — the wallet number from your Payeer account

**API ID** — your API ID from the Payeer dashboard

**API Key** — the secret key from your Payeer account

## Continuing Setup

Next, complete the merchant setup by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).