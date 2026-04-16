# Loderunner

{% hint style="info" %}
If you need to update the module on the server, please refer to the [instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-merchantov).
{% endhint %}

{% hint style="warning" %}
For discussions regarding terms and connections, please contact a [service representative](https://t.me/roinotgoall).

**Disclaimer**: When connecting your website to any service, please assess the potential risks of collaboration on your own.
{% endhint %}

{% hint style="warning" %}
Please note that when using the Loderunner module for receiving payments, the actual payment amount is always rounded to two decimal places on the service's side.

Account details may not be provided immediately, so it is recommended to select the "**Waiting for merchant details**" option in the module settings.

![](<../../../.gitbook/assets/изображение (1).png>)
{% endhint %}

Register on the Loderunner service with the help of a [service representative](https://t.me/roinotgoall). Obtain an API key from the representative to work with Premium Exchanger.

## Module Settings

In the admin panel, create a new merchant in the "**Merchants**" ➔ "**Add Merchant**" section.

Select Loderunner from the dropdown menu in the "**Module**" field, enter a name for the module, and click "**Save**".

<figure><img src="../../../.gitbook/assets/изображение (239).png" alt=""><figcaption></figcaption></figure>

Fill in the specified authorization fields.

<figure><img src="../../../.gitbook/assets/изображение (240).png" alt=""><figcaption></figcaption></figure>

**Domain** — leave this field empty.

**API Key** — the key provided to you by the Loderunner representative.

## Special Fields

{% hint style="warning" %}
When receiving funds using the Loderunner merchant, it is **necessary** to add additional fields to the exchange form for the client to fill out when creating a request.

To do this, create and add [additional fields](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/valyuty-i-napravleniya/dobavlenie-novoi-valyuty#vkladka-dop.-polya) to the relevant currencies for receiving funds through Loderunner.

Make sure to specify a variable in the "**Unique ID**" field (use lowercase letters) and set the field as mandatory.

**1. Additional field for** <mark style="color:$warning;">currency</mark> **for cardholder name (optional)**

* **Unique ID**: `give_cardholder`

<img src="https://premium.gitbook.io/main/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FyBUMmdMiMlEvL4OlAoxr%252Fimage.png%3Falt%3Dmedia%26token%3D9669cfff-79cc-49fb-a222-50ecccb3fa5e&#x26;width=300&#x26;dpr=4&#x26;quality=100&#x26;sign=50a9f19f&#x26;sv=2" alt="" data-size="original">

*   **Processing priority (any option can be selected)**:

    1. `give_cardholder` (priority field)
    2. Automatic generation from the client's full name (`last_name + first_name + second_name`) — standard fields "**Last Name**", "**First Name**", "**Middle Name**" for the exchange direction (not currency!)
    3. After this, the fields will appear in the exchange form and will be mandatory for the client to fill out when creating a request.

    ![](https://premium.gitbook.io/main/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FcoBFe70zmN1JtepEFM68%252Fimage.png%3Falt%3Dmedia%26token%3Da5a19b16-bc6f-425d-89ed-bb07c7065e00&width=300&dpr=4&quality=100&sign=d8ed43c6&sv=2)

**2. Additional field for** <mark style="color:$warning;">currency</mark> **for card number (optional)**

* **Unique ID**: `give_account`
* **Processing priority (any option can be selected)**:
  1. `give_account` (priority field)
  2. The "**From Account**" field from the currency settings "**I Give**"

![](<../../../.gitbook/assets/изображение (2).png>)

**3. Additional field for** <mark style="color:$warning;">exchange direction</mark> **for phone number (optional)**

* **Unique ID**: `give_phone`
* **Processing priority (any option can be selected)**:
  1. `give_phone` (priority field)
  2. Standard field "**Phone**" for the exchange direction (not currency!)**.**&#x20;

**4. Additional field for** <mark style="color:$warning;">exchange direction</mark> **for Telegram account (optional)**

* **Unique ID**: `give_tg` / `dir_tg`
{% endhint %}

## Continue Configuration

Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).<br>