# Paylama (Inactive)

{% hint style="info" %}
If you need to update the module on the server, please refer to the [instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-merchantov).
{% endhint %}

## Merchant Account Settings

Register on the [Paylama](https://paylama.io/) website and log into your account.

Go to the "**API Management**" section and click the "**Create API**" button.

<figure><img src="../../../.gitbook/assets/image (1591)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

Enter a name for the access you are creating, provide your server's IP address (required), and click the "**Create**" button.

<figure><img src="../../../.gitbook/assets/image (1585)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

Copy the generated keys and save them in a text file.

<figure><img src="../../../.gitbook/assets/image (1593)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

## Module Settings

In the admin panel, create a new merchant in the "**Merchants**" -> "**Add Merchant**" section.

Select "Paylama Card" from the dropdown list in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (1586)_eng.png" alt="" width="443"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (1588)_eng.png" alt="" width="422"><figcaption></figcaption></figure>

**API Key** — The APIKey generated in your Paylama account.

## Special Fields

<figure><img src="../../../.gitbook/assets/image (1589)_eng.png" alt=""><figcaption></figcaption></figure>

**Type:**\
• **P2P** — Provides a phone number for replenishment via SBP in the request\
• **FPS** — Provides a card number from the selected bank in the request

<figure><img src="../../../.gitbook/assets/image (1590)_eng.png" alt=""><figcaption></figcaption></figure>

**Type** — Select the currency you plan to accept from clients and the bank whose card numbers will be issued in requests.

## Continuing the Setup

Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).