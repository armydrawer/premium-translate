# AI-pay

{% hint style="info" %}
If you need to update the module on the server, please refer to the [instructions](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat).
{% endhint %}

## Merchant Account Settings

{% hint style="warning" %}
To discuss the terms of service, please contact a [service representative](https://t.me/AI_pay_kirill).

**Disclaimer**: When connecting your website to any service, please assess the potential risks of collaboration on your own.
{% endhint %}

Register on the AI-pay service through a [service representative](https://t.me/AI_pay_kirill) and request API keys to connect to Premium Exchanger.

## Module Settings

In the admin panel, create a new merchant in the "**Merchants**" ➔ "**Add Merchant**" section.

Select AI-pay from the dropdown menu in the "**Module**" field, enter a name for the module, and click "**Save**."

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1)_eng.png" alt="" width="338"><figcaption></figcaption></figure>

**Domain** — leave this field empty.

**API UID** — the identifier provided to you earlier by the AI-pay representative.

**API Key** — the API key provided to you earlier by the AI-pay representative.

## Special Fields

<figure><img src="../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1)_eng.png" alt=""><figcaption></figcaption></figure>

**Payment Method** — select the appropriate method for receiving funds from the client:

**Card** — provide bank card details.

**Account** — provide the bank account number.

**Phone** — provide a phone number for receiving funds via SBP.

{% hint style="warning" %}
When receiving funds using the AI-pay merchant, it is **necessary** to add additional fields to the exchange form for the client to fill out when creating a request.

To do this, create and add [additional fields](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/valyuty-i-napravleniya/dobavlenie-novoi-valyuty#vkladka-dop.-polya) to the relevant currencies for receiving funds through AI-pay.

Make sure to specify a variable in the "**Unique ID**" field (use lowercase letters) and make the field mandatory.

**1. Field for Cardholder Name (when using the "Card" or "Account" method)**

* **Unique ID**: `give_cardholder`/`cardholder`

<img src="https://premium.gitbook.io/main/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FyBUMmdMiMlEvL4OlAoxr%252Fimage_eng.png%3Falt%3Dmedia%26token%3D9669cfff-79cc-49fb-a222-50ecccb3fa5e&#x26;width=300&#x26;dpr=4&#x26;quality=100&#x26;sign=50a9f19f&#x26;sv=2" alt="" data-size="original">

* **Purpose**: Full name of the card/account holder.
*   **Processing Priority (any option can be selected)**:

    1. `give_cardholder` or `cardholder` (priority field)
    2. Automatically generated from the client's full name (`last_name + first_name + second_name`) — standard fields "**Last Name**," "**First Name**," "**Middle Name**" for the exchange direction (not currency!)
    3. After this, the field will appear in the exchange form and will be mandatory for the client to fill out when creating a request.

    ![](https://premium.gitbook.io/main/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FcoBFe70zmN1JtepEFM68%252Fimage_eng.png%3Falt%3Dmedia%26token%3Da5a19b16-bc6f-425d-89ed-bb07c7065e00\&width=300\&dpr=4\&quality=100\&sign=d8ed43c6\&sv=2)

**2. Field for Phone Number (when using the "Phone" method)**

* **Unique ID**: `give_phone`/`phone`
* **Purpose**: Client's phone number.
* **Processing Priority (any option can be selected)**:
  1. `give_phone` or `phone` (priority field)
  2. `user_phone` from the main request data — standard field "**Phone**" for the exchange direction (not currency!)
{% endhint %}

## Continue Configuration

Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).
