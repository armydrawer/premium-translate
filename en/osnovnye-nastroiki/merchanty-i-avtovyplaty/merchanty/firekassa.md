# FireKassa Card/Link

{% hint style="info" %}
If you need to update the module on the server, please refer to the [instructions](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat).
{% endhint %}

## Settings in the Merchant's Personal Account

Register on the [Vanilapay](https://web.vanilapay.com/) website (for transactions in RUB) or on the [Gamepay](https://web.gampay.cc/) website (for transactions in UAH).

Log into your personal account, go to the "**Sites**" section -> "**List of Sites**" and add a new site.

<figure><img src="../../../.gitbook/assets/image (749)_eng.png" alt=""><figcaption></figcaption></figure>

Fill in the required fields, except for "**Notification URL**" and "**Payout Notification URL**," then click "**Add**."

<figure><img src="../../../.gitbook/assets/image (750)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

In the window that opens, go to the "**API**" tab.

<figure><img src="../../../.gitbook/assets/image (751)_eng.png" alt=""><figcaption></figcaption></figure>

Update the **API Bearer Token** and **API Sign Token** by clicking **"Edit"** on each line one by one.

<figure><img src="../../../.gitbook/assets/image (752)_eng.png" alt=""><figcaption></figcaption></figure>

Copy the keys and save them in a text file.

## Module Settings

In the admin panel, create a new merchant in the "**Merchants**" -> "**Add Merchant**" section.

*   **FireKassa Card** — if you want the wallet/card number to be displayed directly on your website.

    <figure><img src="../../../.gitbook/assets/image (753)_eng.png" alt=""><figcaption><p>FireKassa Card</p></figcaption></figure>
*   **FireKassa Link** — if you want the user to be redirected to the payment system's website for payment.

    <figure><img src="../../../.gitbook/assets/image (754)_eng.png" alt=""><figcaption><p>FireKassa Link</p></figcaption></figure>

{% hint style="info" %}
Both payment format options have limits set by the merchant, which should be confirmed with FireKassa's technical support.
{% endhint %}

Select the appropriate module from the dropdown list in the "**Module**" field, enter a name for the module, and click "**Save**."

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (1421)_eng.png" alt=""><figcaption></figcaption></figure>

**API URL** — specify the URL of the service you will be working with:\
• **https://admin.gampay.cc** — for transactions in UAH (alternative URL - **https://web.gampay.cc)**\
• **https://admin.vanilapay.com** — for transactions in RUB (alternative URL - **https://web.vanilapay.com)**

**API Key** — **API Bearer Token** from your FireKassa personal account

**Secret Key** — **API Sign Token** from your FireKassa personal account

### Continuing the Setup

Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).

## Special Fields

**Type (FireKassa Card):**

<figure><img src="../../../.gitbook/assets/image (649)_eng.png" alt=""><figcaption></figcaption></figure>

* **Type** — select the bank for receiving funds (RUB, UAH)

{% hint style="warning" %}
The list of banks and payment systems for this option is loaded via API from the merchant. If a type is missing, please contact the merchant to have it included.
{% endhint %}

### **Meeting FireKassa Requirements**

The merchant's requirement is to collect the customer's phone number, which they must enter in the exchange form. To do this, in the settings for the direction (under the "**Additional Fields**" tab), check the box next to the "**Phone**" field (make sure this field is marked as required — a <mark style="color:red;">red asterisk</mark> should appear next to it in the exchange form).

<figure><img src="../../../.gitbook/assets/изображение (43)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

After this, the phone number input field will be displayed in the exchange form for this direction.

<figure><img src="../../../.gitbook/assets/image (63)_eng.png" alt="" width="349"><figcaption></figcaption></figure>