# MoneyGo

{% hint style="info" %}
If you need to update the module on the server, please refer to the [instructions](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat).
{% endhint %}

## Merchant Account Settings

Register for the [MoneyGo](https://money-go.com/ru/register) service. After registering, request API access from your MoneyGo manager or submit a request for API access to work with the module via the [feedback form](https://money-go.com/ru/helpdesk) (under the "**Contacts**" section on the website), selecting "**Collaboration**" and filling out the required fields.

<figure><img src="../../../.gitbook/assets/image (2011)_eng.png" alt=""><figcaption></figcaption></figure>

## Module Settings

In the admin panel, create a new merchant in the "**Merchants**" -> "**Add Merchant**" section.

Select MoneyGo from the dropdown menu in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (224)_eng.png" alt="" width="455"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (2113)_eng.png" alt="" width="454"><figcaption></figcaption></figure>

**Client ID** — The **Client ID** provided to you by your MoneyGo manager.

**Client Secret** — The client secret key (**Secret**) provided to you by your MoneyGo manager.

**Form Secret Key** — The merchant key (**Token for the form**) provided to you by your MoneyGo manager.

**U-wallet** — The USD wallet from your MoneyGo account.

<figure><img src="../../../.gitbook/assets/image (226)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

**E-, R-wallet** — These fields should remain empty.

{% hint style="warning" %}
For the module to function correctly for the currency "**I Give**" in the exchange direction where MoneyGo is used to receive funds, the mandatory field "**From Account**" must be filled out. This field will be completed by the client in the application creation form (indicating their wallet in the MoneyGo system).

![](<../../../.gitbook/assets/image (231)_eng.png>)
{% endhint %}

## Continuing the Setup

Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/main/en/basic-settings/merchants-and-auto-payments/merchants/general-merchant-settings).