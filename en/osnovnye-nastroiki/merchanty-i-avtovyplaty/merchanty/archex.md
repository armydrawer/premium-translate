# ArchEx

{% hint style="info" %}
If you need to update the module on your server, please follow the [instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-merchantov).
{% endhint %}

## Merchant Account Settings

{% hint style="warning" %}
To obtain the h2h key required for module authorization, please contact a [service representative](https://t.me/archex_headsupport) (after registering on the service, message them that you need the h2h key for the Premium Exchanger script).

**Disclaimer:** When connecting your website to any service, please carefully assess the potential risks involved in the partnership.
{% endhint %}

[Register on the service](https://dash.archex.io/signin/) and log in to your merchant account. Create a new project.

<figure><img src="../../../.gitbook/assets/image (2036).png" alt=""><figcaption></figcaption></figure>

Fill in the required information and select "**Merchant**" from the "**Module**" dropdown menu.

<figure><img src="../../../.gitbook/assets/image (2037).png" alt=""><figcaption></figcaption></figure>

In your profile settings, copy the API token (this is your **Profile API Token**).

<figure><img src="../../../.gitbook/assets/image (2041).png" alt=""><figcaption></figcaption></figure>

Go to the project settings. To enable callback functionality for updating application statuses, enter the URL from the merchant module settings into the project settings, and whitelist all merchant IP addresses that send callbacks (request the list of IP addresses directly from the merchant).

Copy the API token from this page as well (this is your **Project API Token**).

<figure><img src="../../../.gitbook/assets/image (2040).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (2038).png" alt=""><figcaption></figcaption></figure>

Select the payment methods you plan to use.

<figure><img src="../../../.gitbook/assets/image (2039).png" alt=""><figcaption></figcaption></figure>

## Module Settings

In the admin panel, create a new merchant under "**Merchants**" -> "**Add Merchant**."

Choose ArchEx from the "**Module**" dropdown, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (2034).png" alt="" width="464"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure src="../../../.gitbook/assets/image (2033).png" alt="" width="458"><figcaption></figcaption></figure>

- **Profile API Token** — the profile API token you copied earlier from the merchant account  
- **Project API Token** — the project API token you copied earlier from the merchant account

**Host2Host Key** — a key issued to you by a [merchant representative](https://t.me/archex_headsupport).

## Special Fields

<figure><img src="../../../.gitbook/assets/image (2035).png" alt="" width="389"><figcaption></figcaption></figure>

**Payment Method** — select the appropriate method for receiving funds from the client.

{% hint style="warning" %}
For each payment method you use, you need to create a separate copy of the merchant module, select the corresponding payment method in it, and then connect this copy on the "**Merchants and Payouts**" tab in the exchange direction settings, where the "**Give**" currency matches the appropriate currency.
{% endhint %}

## Continuing Setup

Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).