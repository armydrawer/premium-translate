# MoneyGo

{% hint style="info" %}
If you need to update the module on your server, please follow the [instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-merchantov).
{% endhint %}

## Settings in the Merchant Dashboard

Register for an account at [MoneyGo](https://money-go.com/ru/register). After registering, request API access from your MoneyGo manager or submit a request for API access to work with the module via the [contact form](https://money-go.com/ru/helpdesk) (under the "**Contacts**" section on the website). Select "**Cooperation**" and fill in the required fields.

<figure><img src="../../../.gitbook/assets/image (2011).png" alt=""><figcaption></figcaption></figure>

## Module Configuration

In the admin panel, create a new merchant by going to "**Merchants**" -> "**Add Merchant**."

Select MoneyGo from the dropdown menu in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (224).png" alt="" width="455"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (2113).png" alt="" width="454"><figcaption></figcaption></figure>

- **Client ID** — the Client ID provided to you by your MoneyGo manager  
- **Client Secret** — the Client Secret key provided to you by your MoneyGo manager  
- **Form Secret Key** — the merchant’s secret key (**Token for the form**) provided by your MoneyGo manager  
- **U-wallet** — the USD wallet from your MoneyGo personal account

<figure><img src="../../../.gitbook/assets/image (226).png" alt="" width="563"><figcaption></figcaption></figure>

- **E- and R-wallet fields** — leave these fields empty

{% hint style="warning" %}
For the module to work correctly, the "**From Account**" field must be enabled and mandatory for the "**Giving**" currency in the exchange direction where MoneyGo is used to receive funds. This field will be filled in by the client when submitting the request form (the client must specify their wallet in the MoneyGo system).

![](<../../../.gitbook/assets/image (231).png>)
{% endhint %}

## Continuing Setup

Next, complete the merchant setup by following the [general configuration instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).