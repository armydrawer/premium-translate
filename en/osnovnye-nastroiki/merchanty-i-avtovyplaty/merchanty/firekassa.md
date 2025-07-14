# FireKassa Card/Link

{% hint style="info" %}
If you need to update the module on your server, please follow the [instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-merchantov).
{% endhint %}

## Merchant Account Settings

Register on [Vanilapay](https://web.vanilapay.com/) (for RUB transactions) or on [Gamepay](https://web.gampay.cc/) (for UAH transactions).

Log in to your account, go to the "**Sites**" section -> "**Site List**," and add a new site.

<figure><img src="../../../.gitbook/assets/image (749).png" alt=""><figcaption></figcaption></figure>

Fill in the required fields, except for "**Notification URL**" and "**Payout Notification URL**," then click "**Add**."

<figure><img src="../../../.gitbook/assets/image (750).png" alt="" width="563"><figcaption></figcaption></figure>

In the window that opens, switch to the "**API**" tab.

<figure><img src="../../../.gitbook/assets/image (751).png" alt=""><figcaption></figcaption></figure>

Update the **API Bearer Token** and **API Sign Token** by clicking "**Edit**" next to each field one at a time.

<figure src="../../../.gitbook/assets/image (752).png" alt=""><figcaption></figcaption></figure>

Copy the keys and save them in a text file for safekeeping.

## Module Configuration

In the admin panel, create a new merchant under "**Merchants**" -> "**Add Merchant**."

* **FireKassa Card** — choose this if you want the wallet/card number to be displayed directly on your website.

    <figure><img src="../../../.gitbook/assets/image (753).png" alt=""><figcaption><p>FireKassa Card</p></figcaption></figure>

* **FireKassa Link** — choose this if you want users to be redirected to the payment system’s website to complete the payment.

    <figure><img src="../../../.gitbook/assets/image (754).png" alt=""><figcaption><p>FireKassa Link</p></figcaption></figure>

{% hint style="info" %}
Both payment formats have merchant-side limits. Please check these limits with FireKassa technical support.
{% endhint %}

Select the appropriate module from the dropdown menu in the "**Module**" field, enter a name for the module, and click "**Save**."

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (1421).png" alt=""><figcaption></figcaption></figure>

**API URL** — specify the service URL you will be working with:  
• **https://admin.gampay.cc** — for UAH transactions (alternative URL: **https://web.gampay.cc**)  
• **https://admin.vanilapay.com** — for RUB transactions (alternative URL: **https://web.vanilapay.com**)  

**API Key** — the **API Bearer Token** from your FireKassa account

**Secret Key** — the **API Sign Token** from your FireKassa account

### Continuing Configuration



Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).

## Special Fields

**Type (Firekassa Card):**

<figure><img src="../../../.gitbook/assets/image (649).png" alt=""><figcaption></figcaption></figure>

* **Type** — select the bank for receiving funds (RUB, UAH)

{% hint style="warning" %}
The list of banks and payment systems for this option is loaded via the merchant’s API — if a certain type is missing, please contact the merchant to have it enabled.
{% endhint %}

### **Meeting Firekassa’s Requirements**

The merchant requires the customer’s phone number to be submitted, which the customer must enter in the exchange form. To enable this, go to the direction settings (tab "**Additional Fields**") and check the box next to "**Phone**" (make sure this field is marked as required — a <mark style="color:red;">red asterisk</mark> should appear next to it in the exchange form).

<figure><img src="../../../.gitbook/assets/изображение (43).png" alt="" width="563"><figcaption></figcaption></figure>

After that, the phone number input field will be displayed in the exchange form for this direction.

<figure><img src="../../../.gitbook/assets/изображение (63).png" alt="" width="349"><figcaption></figcaption></figure>