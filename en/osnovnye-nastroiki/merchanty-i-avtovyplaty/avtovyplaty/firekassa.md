# Firekassa

{% hint style="danger" %}
<mark style="color:red;">Before setting up auto payouts, be sure to read</mark> [<mark style="color:blue;">the risk warning</mark>](https://premiumexchanger.com/wiki/preduprezhdenie-auto/)<mark style="color:blue;">!</mark>
{% endhint %}

{% hint style="info" %}
If you need to update the module on your server, please follow this [instruction](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-avtovyplat).
{% endhint %}

{% hint style="danger" %}
This module works only with banks (payouts to bank cards) — payouts via Qiwi, YooMoney, or phone number are currently not supported.
{% endhint %}

## Merchant Account Settings

Register on [Vanilapay](https://web.vanilapay.com/) if you are working with RUB, or on [Gamepay](https://web.gampay.cc/) if you are working with UAH.

Log in to your account, go to the "**Sites**" section -> "**Site List**," and add a new site.

<figure><img src="../../../.gitbook/assets/image (749).png" alt=""><figcaption></figcaption></figure>

Fill in the required fields, except for "**Notification URL**" and "**Payout Notification URL**," then click "**Add**."

<figure><img src="../../../.gitbook/assets/image (750).png" alt="" width="563"><figcaption></figcaption></figure>

In the window that opens, go to the "**API**" tab.

<figure><img src="../../../.gitbook/assets/image (751).png" alt=""><figcaption></figcaption></figure>

Update the **API Bearer Token** and **API Sign Token** by clicking **"Edit"** next to each field one at a time.

<figure><img src="../../../.gitbook/assets/image (752).png" alt=""><figcaption></figcaption></figure>

Copy these keys and save them in a text file.

## **Module Settings**

In the admin panel, create a new merchant under "**Auto Payouts**" -> "**Add Auto Payout**."

Select Firekassa from the dropdown menu in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (746).png" alt=""><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (1429).png" alt=""><figcaption></figcaption></figure>

**API URL** — specify the service URL you will be working with:  
• **https://admin.gampay.cc** — for UAH (alternative URL: **https://web.gampay.cc**)  
• **https://admin.vanilapay.com** — for RUB (alternative URL: **https://web.vanilapay.com**)  

**API Key** — the **API Bearer Token** from your Firekassa account

**Secret Key** — the **API Sign Token** from your Firekassa account

## Special Fields

**Type**:

<figure><img src="../../../.gitbook/assets/image (648).png" alt=""><figcaption></figcaption></figure>

* **Type** — select the bank for payouts (RUB or UAH)

{% hint style="warning" %}
The list of banks and payment systems for this option is loaded via the merchant's API — if a certain type is missing, please contact the merchant to have it enabled.
{% endhint %}

## Continuing the Setup

Next, configure the auto-payout by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-merchantov-avtovyplat).