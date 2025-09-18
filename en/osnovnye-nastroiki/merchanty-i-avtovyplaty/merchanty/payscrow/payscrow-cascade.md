# Payscrow Cascade

{% hint style="info" %}
If you need to update the module on the server, please refer to the [instructions](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat).
{% endhint %}

{% hint style="info" %}
To display the cardholder's full name (as issued by the merchant) in the client's application, add the shortcode \[dest\_tag] in the instructions within the merchant settings.

![](<../../../../.gitbook/assets/image (1627).png>)
{% endhint %}

## Merchant Account Settings

{% hint style="warning" %}
For discussions regarding terms and connections, please contact a [service representative](https://t.me/Payscrow).

**Disclaimer**: When connecting your website to any service, please assess the potential risks of collaboration on your own.
{% endhint %}

Register and log in to your merchant account. In the "**Terminals**" ➔ "**API Settings**" section, copy the API key for authorization in the merchant module.

<figure><img src="../../../../.gitbook/assets/image (2163).png" alt=""><figcaption></figcaption></figure>

In the "**Order Status for Purchase**" field, enter the URL from the auto-payment module settings (Webhook URL).

<figure><img src="../../../../.gitbook/assets/image (2165).png" alt=""><figcaption></figcaption></figure>

## Module Settings

In the admin panel, create a new merchant in the "**Merchants**" ➔ "**Add Merchant**" section.

Select "Payscrow Cascade" from the dropdown menu in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../../.gitbook/assets/image (2166).png" alt="" width="499"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../../.gitbook/assets/image (2167).png" alt="" width="442"><figcaption></figcaption></figure>

**Domain** — leave this field empty.

**API Key** — enter the API key you copied earlier from the Payscrow account.

## Special Fields

<figure><img src="../../../../.gitbook/assets/image (2168).png" alt="" width="416"><figcaption></figcaption></figure>

Merchant Type:

* **Payment link** — a "**Proceed to Payment**" button will appear in the application, which, when clicked, will take the client to the merchant's payment page, where the payment details will be displayed or selected.
* **Requisites** — the merchant's details will be displayed in the application.

{% hint style="warning" %}
The merchant type is fixed to the configured module and cannot be changed after the first application is created using this module.

![](https://premium.gitbook.io/main/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FzcRcd0cY32xbgh1lhGx6%252Fimage.png%3Falt%3Dmedia%26token%3Df1f65b44-fd81-4597-98d5-b705a410977f&width=300&dpr=4&quality=100&sign=57a702c3&sv=2)![](https://premium.gitbook.io/main/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FVQqDVFVlJ7dwBTiSb2Rf%252Fimage.png%3Falt%3Dmedia%26token%3D16a4d0bc-48dc-4280-8e0a-8733cdb18f94&width=300&dpr=4&quality=100&sign=7c7aa62c&sv=2)&#x20;

To use a different merchant type, you must create a separate copy, selecting a different type and connecting it in the desired exchange direction.
{% endhint %}

**Payment Method** — available formats for providing details to clients:

* **\[BankAccount, RUB] Sberbank Account** — provides the Sberbank account number.
* **\[BankCard, RUB] Any Russian Bank** — provides the card number of any bank.\
  • **\[BankCard, RUB] {bank_name}** — provides the card number of the specified bank.
* **\[SBP, RUB] SBP** — provides a phone number for payment.\
  • **\[SBP, RUB] SBP {bank_name}** — provides a phone number for payment linked to the card of the selected bank.
* **\[TransBankCard, RUB]** — provides the card number of any cross-border bank.\
  • **\[TransBankCard, RUB] {bank_name}** — provides the card number of the specified cross-border bank.
* **\[TransSBP, RUB] SBP** — provides a phone number for payment.\
  • **\[TransSBP, RUB] SBP {bank_name}** — provides a phone number for payment linked to the card of the specified cross-border bank.

## Continuing the Setup

Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).