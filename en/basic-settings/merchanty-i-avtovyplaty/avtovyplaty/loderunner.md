# Loderunner

{% hint style="danger" %}
<mark style="color:red;">Before setting up auto payouts, please read the</mark> [<mark style="color:blue;">risk warning!</mark>](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplat/avtovyplat/preduprezhdenie-o-riskakh)
{% endhint %}

{% hint style="info" %}
If you need to update the module on the server, please refer to the [instructions](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat)
{% endhint %}

## Merchant Account Settings

{% hint style="warning" %}
To discuss working conditions, please contact a [service representative](https://t.me/oleg6781).

**Disclaimer**: When connecting your website to any service, please assess the potential risks of collaboration on your own.
{% endhint %}

Register on the Loderunner service through a [service representative](https://t.me/oleg6781) and request an API key to connect to Premium Exchanger.

## Module Settings

In the admin panel, create a new merchant in the "**Merchants**" section ➔ "**Add Auto Payout**."

Select Loderunner from the dropdown menu in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (2218)_eng.png" alt="" width="395"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (2219)_eng.png" alt="" width="432"><figcaption></figcaption></figure>

**Domain** — leave this field empty.

**API Key** — the API key provided to you earlier by the Loderunner representative.

## Special Fields

<figure><img src="../../../.gitbook/assets/image (2220)_eng.png" alt="" width="278"><figcaption></figcaption></figure>

**Statistics** — enable or disable the transmission of additional data about the request for calculations in the personal account.

### [Additional Fields](https://premium.gitbook.io/main/osnovnye-nastroiki/valyuty-i-napravleniya-obmena/dopolnitelnye-polya)

<mark style="color:red;">**It is necessary**</mark> to also transmit client data to the merchant through additional fields created for the currency "**Receiving**." To do this, create additional fields and check them in the currency settings. When the client fills out these fields in the exchange form while creating a request, the data will be transmitted to the merchant.

Specify the name from the list below in the "**Unique ID**" field (the other fields can be filled out at your discretion) for each additional field.

<figure><img src="https://premium.gitbook.io/main/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FAUKYMBIlttlhEVWigqYZ%252Fimage_eng.png%3Falt%3Dmedia%26token%3D164622ad-c56b-4d07-ad97-9a918effd5eb&#x26;width=300&#x26;dpr=4&#x26;quality=100&#x26;sign=bd108799&#x26;sv=2" alt="" width="375"><figcaption></figcaption></figure>

IDs for additional fields (suitable values for the "**Unique ID**" field are indicated with `/`):

* **Bank Name:** `get_bankname`/`bankname`
* **Card Number:** activate the "**Show 'To Account' Field**" option.

<figure><img src="../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

* **Cardholder's Full Name:** `get_cardholder`/`cardholder`
* **Phone for SBP:** `get_phone`/`phone`/activate the "**Show 'To Account' Field**" option.
* Telegram for contact (<mark style="color:orange;">**additional field in the exchange direction, not in the currency!**</mark>): `dir_tg`/`get_tg`/`tg`

Activation of created additional fields for the "Receiving" currency (the unique ID from the corresponding field in the settings of each additional field is indicated in parentheses).

<figure><img src="https://premium.gitbook.io/main/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FM842FBd18fqWCI8EaduC%252Fimage_eng.png%3Falt%3Dmedia%26token%3D6aeff3a7-4ae6-47eb-9b88-25d17c9e146b&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=9c12e4cd&#x26;sv=2" alt="" width="563"><figcaption></figcaption></figure>

Exchange Form

<figure><img src="https://premium.gitbook.io/main/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252F3U0WTMvGp9dlw5dzwyqJ%252Fimage_eng.png%3Falt%3Dmedia%26token%3Dee980067-efa0-407c-ad97-c1d6406cb4e4&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=26bdeb64&#x26;sv=2" alt="" width="375"><figcaption><p>Display of additional fields in the exchange form on the website</p></figcaption></figure>

## Continuing the Setup

Next, proceed to configure the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).