# Quixfer

{% hint style="info" %}
If you need to update the module on the server, please refer to the [instructions](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat).
{% endhint %}

## Settings in the Merchant's Personal Account

{% hint style="warning" %}
To discuss working conditions, please contact a [service representative](https://t.me/quixfer).

**Disclaimer**: When connecting your website to any service, please assess the potential risks of collaboration on your own.
{% endhint %}

[Register](https://quixfer.cc/#contacts) on the Quixfer service, log in to your personal account, and navigate to the "**Settings**" ➔ "**Security**" section.

<figure><img src="../../../.gitbook/assets/image (4) (1) (1) (1) (1).png" alt="" width="375"><figcaption></figcaption></figure>

Generate your API keys and save them in a text file.

<figure><img src="../../../.gitbook/assets/image (5) (1) (1) (1).png" alt="" width="375"><figcaption></figcaption></figure>

## Module Settings

In the admin panel, create a new merchant in the "**Merchants**" ➔ "**Add Merchant**" section.

Select Quixfer from the dropdown list in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="486"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="460"><figcaption></figcaption></figure>

**Domain** — leave this field empty.

**API Key** — Public Key from your Quixfer personal account, copied earlier.

**Secret Key** — Private Key from your Quixfer personal account, copied earlier.

## Special Fields

<figure><img src="../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

**Payment Method** — select the necessary payment method for receiving funds, or choose "**Automatically**" — in this case, the details will be requested according to the XML code of the currency from the exchange direction where the module is connected (the list of methods will only be displayed after entering the correct API keys for module authorization).

### Additional Fields

To correctly receive the details for the currency being accepted through Quixfer, you must add **mandatory** additional fields to the exchange form. A hint regarding the required fields for each payment method will be displayed below the "**Payment Method**" field.

<figure><img src="../../../.gitbook/assets/image (5) (1) (1).png" alt=""><figcaption></figcaption></figure>

Create and add an [additional field](https://premium.gitbook.io/main/osnovnye-nastroiki/valyuty-i-napravleniya-obmena/dopolnitelnye-polya) for the relevant currencies to receive funds via Quixfer. Be sure to specify a value in the "**Unique ID**" field according to the table above (use lowercase letters) and make the field mandatory.

<figure><img src="https://premium.gitbook.io/main/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FyBUMmdMiMlEvL4OlAoxr%252Fimage.png%3Falt%3Dmedia%26token%3D9669cfff-79cc-49fb-a222-50ecccb3fa5e&#x26;width=300&#x26;dpr=4&#x26;quality=100&#x26;sign=50a9f19f&#x26;sv=2" alt="" width="375"><figcaption></figcaption></figure>

After this, the field will appear in the exchange form and will be mandatory for clients when creating a request.

<figure><img src="https://premium.gitbook.io/main/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FcoBFe70zmN1JtepEFM68%252Fimage.png%3Falt%3Dmedia%26token%3Da5a19b16-bc6f-425d-89ed-bb07c7065e00&#x26;width=300&#x26;dpr=4&#x26;quality=100&#x26;sign=d8ed43c6&#x26;sv=2" alt="" width="375"><figcaption></figcaption></figure>

Example of filling out for the currency T-Bank RUB (highlighted names from the "Unique ID" fields):

<figure><img src="../../../.gitbook/assets/image (2205).png" alt="" width="375"><figcaption></figcaption></figure>

Example of filling out for the currency Bank transfer GEL (Georgian Lari):

<figure><img src="../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="375"><figcaption></figcaption></figure>

## Continuing the Setup

Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).