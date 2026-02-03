# 1Plat

{% hint style="danger" %}
Before setting up automatic payouts, please read the [risk warning!](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/preduprezhdenie-o-riskakh)
{% endhint %}

{% hint style="info" %}
If you need to update the module on the server, please refer to the [instructions](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat).
{% endhint %}

{% hint style="warning" %}
For discussions regarding terms and connection, please contact a service representative.

**Disclaimer**: When connecting your website to any service, please assess the potential risks of collaboration on your own.
{% endhint %}

{% hint style="warning" %}
Please note that when using the Finora automatic payout module, the actual payout amount is always rounded to two decimal places on the service side.
{% endhint %}

Register on the [1Plat](https://1plat.money/user/reg) service and log into your personal account. Create a new store.

<figure><img src="https://premium.gitbook.io/main/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FDcA3ojce9SPst39S6liy%252Fimage.png%3Falt%3Dmedia%26token%3D87c1b7d6-0980-4944-b0ff-bf2f840fbea6&#x26;width=768&#x26;dpr=3&#x26;quality=100&#x26;sign=12a57ed4&#x26;sv=2" alt="" width="563"><figcaption></figcaption></figure>

Fill in the required information in the new window and save it.

<figure><img src="https://premium.gitbook.io/main/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FEG8wFY7cWtrWH0caX989%252Fimage.png%3Falt%3Dmedia%26token%3D8f60df99-964e-4da2-9a7b-154381ad686b&#x26;width=768&#x26;dpr=3&#x26;quality=100&#x26;sign=32ccf277&#x26;sv=2" alt="" width="375"><figcaption></figcaption></figure>

## Module Settings

In the admin panel, create a new merchant in the "**Merchants**" ➔ "**Add Automatic Payout**" section.

<figure><img src="../../../.gitbook/assets/изображение.png" alt=""><figcaption></figcaption></figure>

Select 1Plat from the dropdown menu in the "**Module**" field, enter a name for the module, and click "**Save**."

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/изображение (1).png" alt=""><figcaption></figcaption></figure>

**Domain** — leave this field empty.

**Store ID** — the ID of your store on the 1Plat service.

<figure><img src="https://premium.gitbook.io/main/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FoaEmf9GDZTuqqZYhsAXi%252Fimage.png%3Falt%3Dmedia%26token%3D1739707a-d872-4f63-8ce9-a8b6501ea37f&#x26;width=768&#x26;dpr=3&#x26;quality=100&#x26;sign=766ba424&#x26;sv=2" alt=""><figcaption></figcaption></figure>

**Secret Key** — the key copied from the "**Store - Settings**" section in your 1Plat personal account.

<figure><img src="https://premium.gitbook.io/main/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252F6hB0yytf4B1hUvSkA3Nf%252Fimage.png%3Falt%3Dmedia%26token%3D532a4bc3-73b8-4d4d-a213-c848cdc35c15&#x26;width=768&#x26;dpr=3&#x26;quality=100&#x26;sign=120443ba&#x26;sv=2" alt=""><figcaption></figcaption></figure>

## Special Fields

<figure><img src="../../../.gitbook/assets/изображение (4).png" alt=""><figcaption></figcaption></figure>

**Payment Method** — select an appropriate method from the list or manually enter your option in the "**Add**" field (for acceptable options, please check with your 1Plat manager).

{% hint style="danger" %}
When selecting "**Sbp**," be sure to choose a bank in the next field!
{% endhint %}

<figure><img src="../../../.gitbook/assets/изображение (3).png" alt=""><figcaption></figcaption></figure>

**Bank** — select an appropriate bank from the list or manually enter your option in the "**Bank**" field (for acceptable options, please check with your 1Plat manager).

{% hint style="info" %}
## Additional Fields for the Application

When processing payouts using the 1Plat automatic payout feature, **additional fields** must be added to the exchange form for the client to fill out when creating an application.

To do this, create and add [additional fields](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/valyuty-i-napravleniya/dobavlenie-novoi-valyuty#vkladka-dop.-polya) to the relevant currencies for payouts through 1Plat.

Make sure to specify a variable in the "**Unique ID**" field (use lowercase letters) and make the field mandatory.

**1. Field for Cardholder Name (when using the "Card" method)**

* **Unique ID**: `get_cardholder`/`cardholder`

<img src="../../../.gitbook/assets/image (2235).png" alt="" data-size="original">

* **Purpose**: Full name of the card/account holder
* **Processing Priority (any option can be selected)**:

    1. `get_cardholder` or `cardholder` (priority field)
    2. Automatically generated from the client's full name (`last_name + first_name + second_name`) — standard fields "**Last Name**," "**First Name**," "**Middle Name**" for the exchange direction (not currency!)
    3. After this, the field will appear in the exchange form and will be mandatory for the client to fill out when creating an application.

    <figure><img src="../../../.gitbook/assets/image (2236).png" alt="" width="434"><figcaption></figcaption></figure>

**2. Field for Phone Number (when using the "Phone" method)**

* **Unique ID**: `get_phone`/`phone`
* **Purpose**: Client's phone number
* **Processing Priority (any option can be selected)**:
  1. `get_phone` or `phone` (priority field)
  2. `user_phone` from the main application data — standard field "**Phone**" for the exchange direction (not currency!)

**3. Field for Bank Name (when using the "Card" or "Account" method) — optional**

* **Unique ID**: `get_bankname`/`bankname`
* **Purpose**: Client's bank name
* **Processing Priority (any option can be selected)**:
  1. `get_bankname` or `bankname` (priority field)
  2. **Automatic Value:** User's phone from the application (`user_phone`), or from the `account_get` field (if the phone is specified as a detail)
{% endhint %}

To operate the module for receiving funds without using a [cron job](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-sozdat-zadanie-cron-na-servere), specify the link from the module settings.

<figure><img src="../../../.gitbook/assets/изображение (5).png" alt=""><figcaption></figcaption></figure>

In your 1Plat personal account, go to "**Store - Settings - Callback for Withdrawals**":

<figure><img src="../../../.gitbook/assets/изображение (6).png" alt=""><figcaption></figcaption></figure>

## Continue Configuration <a href="#prodolzhenie-nastroiki" id="prodolzhenie-nastroiki"></a>

Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-merchantov-avtovyplat).