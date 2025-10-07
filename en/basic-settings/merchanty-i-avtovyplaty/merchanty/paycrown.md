# PayCrown

{% hint style="info" %}
If you need to update a module on the server, please refer to the [instructions](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat).
{% endhint %}

## Merchant Account Settings

{% hint style="warning" %}
To discuss working conditions, please contact a [service representative](https://t.me/paycrown_chief).

**Disclaimer**: When connecting your website to any service, please assess the potential risks of collaboration on your own.
{% endhint %}

Register for the PayCrown service through a [service representative](https://t.me/paycrown_chief) and request API keys to connect to the Premium Exchanger.

## Module Settings

In the admin panel, create a new merchant in the "**Merchants**" section by selecting "**Add Merchant**."

Choose PayCrown from the dropdown menu in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1)_eng.png" alt="" width="422"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (3) (1) (1) (1) (1)_eng.png" alt="" width="439"><figcaption></figcaption></figure>

**Domain** — leave this field empty.

**Merchant ID** — the ID provided to you by the PayCrown representative.

**API Key** — the public key provided to you by the PayCrown representative.

**Secret Key** — the secret key provided to you by the PayCrown representative.

## Special Fields

<figure><img src="../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1)_eng.png" alt="" width="439"><figcaption></figcaption></figure>

**Payment Method** — the method for issuing payment details:

* **C2C** — this method is temporarily not in use.
* **Invoice** — provides a RUB card number.
* **SBP** — provides a phone number for payment via SBP.

## Continuing the Setup

Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).