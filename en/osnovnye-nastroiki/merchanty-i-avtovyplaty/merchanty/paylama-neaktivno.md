# Paylama (Inactive)

{% hint style="info" %}
If you need to update the module on your server, please follow the [instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-merchantov).
{% endhint %}

## Settings in the Merchant Dashboard

Register on the [Paylama website](https://paylama.io/) and log in to your merchant dashboard.

Go to the "**API Management**" section and click the "**Create API**" button.

<figure><img src="../../../.gitbook/assets/image (1591).png" alt="" width="563"><figcaption></figcaption></figure>

Enter a name of your choice for the new API access, specify your server’s IP address (this is required), and click "**Create**."

<figure><img src="../../../.gitbook/assets/image (1585).png" alt="" width="563"><figcaption></figcaption></figure>

Copy the generated keys and save them in a text file.

<figure><img src="../../../.gitbook/assets/image (1593).png" alt="" width="563"><figcaption></figcaption></figure>

## Module Configuration

In your admin panel, create a new merchant by going to "**Merchants**" -> "**Add Merchant**."

Select **Paylama Card** from the "**Module**" dropdown, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (1586).png" alt="" width="443"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (1588).png" alt="" width="422"><figcaption></figcaption></figure>

**API Key** — the APIKey generated in your Paylama dashboard

## Special Fields

<figure><img src="../../../.gitbook/assets/image (1589).png" alt=""><figcaption></figcaption></figure>

**Type:**  
• **P2P** — the phone number for SBP (Fast Payment System) top-ups will be provided in the request  
• **FPS** — the card number of the selected bank (see below) will be provided in the request

<figure><img src="../../../.gitbook/assets/image (1590).png" alt=""><figcaption></figcaption></figure>

**Type** — select from the list the currency you plan to accept from clients and the bank whose card numbers will be issued in requests

## Continuing Setup

Next, complete the merchant setup by following the [general merchant configuration guide](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).