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

Account details may not be provided immediately, so it is recommended to select the "**Waiting for details status**" option in the module settings.

<img src="../../../.gitbook/assets/изображение (202).png" alt="" data-size="original">
{% endhint %}

Register on the Loderunner service with the help of a [service representative](https://t.me/roinotgoall). Obtain an API key from the representative to work with Premium Exchanger.

## Module Settings

In the admin panel, create a new merchant in the "**Merchants**" ➔ "**Add Merchant**" section.

Select Loderunner from the dropdown menu in the "**Module**" field, enter a name for the module, and click "**Save**".

<figure><img src="../../../.gitbook/assets/изображение (191).png" alt=""><figcaption></figcaption></figure>

Fill in the specified authorization fields.

<figure><img src="../../../.gitbook/assets/изображение (198).png" alt=""><figcaption></figcaption></figure>

**Domain** — leave this field empty.

**API Key** — the key provided to you by the Loderunner representative.

## Special Fields

{% hint style="warning" %}
When receiving funds using the Loderunner merchant, it is **necessary** to add additional fields to the exchange form for the client to fill out when creating a request.

To do this, create and add [additional fields](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/valyuty-i-napravleniya/dobavlenie-novoi-valyuty#vkladka-dop.-polya) to the relevant currencies for receiving funds through Loderunner.

Make sure to specify a variable in the "**Unique ID**" field (use lowercase letters) and set the field as mandatory.

**1. Additional field for** <mark style="color:$warning;">currency</mark> **for cardholder name (optional)**

* **Unique ID**: `give_cardholder`
* **Processing priority (any option can be selected)**:
  1. `give_cardholder` (priority field)
  2. Automatic generation from the client's full name (`last_name + first_name + second_name`) — standard fields "**Last Name**", "**First Name**", "**Middle Name**" for the exchange direction (not currency!)
  3. After this, the fields will appear in the exchange form and will be mandatory for the client to fill out when creating a request.

**2. Additional field for** <mark style="color:$warning;">currency</mark> **for card number (optional)**

* **Unique ID**: `give_account`
* **Processing priority (any option can be selected)**:
  1. `give_account` (priority field)
  2. The "**From Account**" field from the currency settings "**I Give**"

**3. Additional field for** <mark style="color:$warning;">exchange direction</mark> **for phone number (optional)**

* **Unique ID**: `give_phone`
* **Processing priority (any option can be selected)**:
  1. `give_phone` (priority field)
  2. Standard field "**Phone**" for the exchange direction (not currency!)**.**

**4. Additional field for** <mark style="color:$warning;">exchange direction</mark> **for Telegram account (optional)**

* **Unique ID**: `give_tg` / `dir_tg`
{% endhint %}

## Continue Configuration

Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).<br>
