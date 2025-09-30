# Firekassa

{% hint style="danger" %}
<mark style="color:red;">Before setting up automatic payouts, please read the</mark> [<mark style="color:blue;">risk warning</mark>](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/preduprezhdenie-o-riskakh)<mark style="color:blue;">!</mark>
{% endhint %}

{% hint style="info" %}
If you need to update the module on the server, please refer to the [instructions](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat).
{% endhint %}

{% hint style="danger" %}
The module only works with banks (payouts to cards) - currently, there is no support for payouts to Qiwi, YuMoney, or via phone number.
{% endhint %}

## Merchant Account Settings

Register on the [Vanilapay](https://web.vanilapay.com/) website (for RUB transactions) or on the [Gamepay](https://web.gampay.cc/) website (for UAH transactions).

Log into your account, go to the "**Sites**" section -> "**List of Sites**" and add a new site.

<figure><img src="../../../.gitbook/assets/image (749)_eng.png" alt=""><figcaption></figcaption></figure>

Fill in the required fields, except for "**Notification URL**" and "**Payout Notification URL**," then click "**Add**."

<figure><img src="../../../.gitbook/assets/image (750)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

In the window that opens, go to the "**API**" tab.

<figure><img src="../../../.gitbook/assets/image (751)_eng.png" alt=""><figcaption></figcaption></figure>

Update the **API Bearer Token** and **API Sign Token** by clicking **"Edit"** on each line one by one.

<figure><img src="../../../.gitbook/assets/image (752)_eng.png" alt=""><figcaption></figcaption></figure>

Copy the keys and save them in a text file.

## **Module Settings**

In the admin panel, create a new merchant in the "**Automatic Payouts**" -> "**Add Automatic Payout**" section.

Select Firekassa from the dropdown menu in the "**Module**" field, provide a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (746)_eng.png" alt=""><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (1429)_eng.png" alt=""><figcaption></figcaption></figure>

**API URL** — specify the URL of the service you will be working with:\
• **https://admin.gampay.cc** — for UAH transactions (alternative URL - **https://web.gampay.cc**)\
• **https://admin.vanilapay.com** — for RUB transactions (alternative URL - **https://web.vanilapay.com**)

**API Key** — **API Bearer Token** from your Firekassa account

**Secret Key** — **API Sign Token** from your Firekassa account

## Special Fields

**Type**:

<figure><img src="../../../.gitbook/assets/image (648)_eng.png" alt=""><figcaption></figcaption></figure>

* **Type** — select the bank for fund payouts (RUB, UAH)

{% hint style="warning" %}
The list of banks and payment systems for this option is loaded via API from the merchant — if a type is missing, please contact the merchant to have it included.
{% endhint %}

## Continuing the Setup

Next, configure the automatic payout by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-merchantov-avtovyplat).