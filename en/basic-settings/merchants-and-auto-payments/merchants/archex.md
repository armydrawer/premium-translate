# ArchEx

{% hint style="info" %}
If you need to update a module on the server, please refer to the [instructions](https://premium.gitbook.io/main/en/basic-settings/faq/updating-script-files-on-the-server/how-to-update-files-on-the-server#merchant-and-auto-payout-modules).
{% endhint %}

## Merchant Account Settings

{% hint style="warning" %}
To obtain the h2h key required for module authorization, please contact a [service representative](https://t.me/archex_headsupport) (after registering with the service, let them know you need the h2h key for the Premium Exchanger script).

**Disclaimer**: When connecting your website to any service, please assess the potential risks of collaboration on your own.
{% endhint %}

[Register for the service](https://dash.archex.io/signin/) and log in to your account. Create a new project.

<figure><img src="../../../.gitbook/assets/image (2036)_eng.png" alt=""><figcaption></figcaption></figure>

Fill in the required information and select "Merchant" from the "Module" dropdown menu.

<figure><img src="../../../.gitbook/assets/image (2037)_eng.png" alt=""><figcaption></figcaption></figure>

In your profile settings, copy the API token (this is the **Profile API Token**).

<figure><img src="../../../.gitbook/assets/image (2041)_eng.png" alt=""><figcaption></figcaption></figure>

Go to the project settings. To enable the callback for changing the application status, specify the URL from the merchant module settings in the project settings and add all IP addresses from which the merchant sends callbacks to your firewall whitelist (request the list of addresses directly from the merchant).

Copy the API token from this same page (this is the **Project API Token**).

<figure><img src="../../../.gitbook/assets/image (2040)_eng.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (2038)_eng.png" alt=""><figcaption></figcaption></figure>

Select the methods you plan to use.

<figure><img src="../../../.gitbook/assets/image (2039)_eng.png" alt=""><figcaption></figcaption></figure>

## Module Settings

In the admin panel, create a new merchant in the "**Merchants**" section by clicking "**Add Merchant**."

Select ArchEx from the dropdown menu in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (2034)_eng.png" alt="" width="464"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (2033)_eng.png" alt="" width="458"><figcaption></figcaption></figure>

**Profile API Token** — the API token you copied earlier from the merchant account.

**Project API Token** — the API token you copied earlier from the merchant account.

**Host2Host Key** — the key provided to you by a [merchant representative](https://t.me/archex_headsupport).

## Special Fields

<figure><img src="../../../.gitbook/assets/image (2035)_eng.png" alt="" width="389"><figcaption></figcaption></figure>

**Payment Method** — choose the appropriate method for receiving funds from the client.

{% hint style="warning" %}
For each payment method you use, you need to create a separate copy of the merchant module, selecting the corresponding method, and then connect this copy on the "**Merchants and Payouts**" tab in the exchange direction settings, where the currency in "**I Give**" will be the appropriate currency.
{% endhint %}

## Continuing the Setup

Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/main/en/basic-settings/merchants-and-auto-payments/merchants/general-merchant-settings).