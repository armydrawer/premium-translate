# Ivanpay

{% hint style="info" %}
If you need to update the module on your server, please follow the [instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-merchantov).
{% endhint %}

## Merchant Account Settings

{% hint style="warning" %}
To discuss terms and setup, please contact the [service representative](https://t.me/IvanPay_pro).

**Disclaimer:** When connecting your website to any service, please independently assess any potential risks involved in the partnership.
{% endhint %}

Register for an account at [IvanPay](https://ivanpay.com/).

<figure><img src="../../../.gitbook/assets/image (214).png" alt=""><figcaption></figcaption></figure>

In your merchant account dashboard, copy the information from the "**Your API Address**" field, as well as the API key provided to you by the service representative.

<figure><img src="../../../.gitbook/assets/image (215).png" alt=""><figcaption></figcaption></figure>

## Module Configuration

In the admin panel, create a new merchant by going to "**Merchants**" -> "**Add Merchant**."

Select Ivanpay from the dropdown menu under the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/Arc_mcpyS7Mdvy.png" alt="" width="417"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (292).png" alt="" width="421"><figcaption></figcaption></figure>

**Domain** — the merchant domain you previously copied from the "**Your API Address**" field in your merchant account.

**API Key** — the API key provided to you by your Ivanpay manager.

## Special Fields

<figure><img src="../../../.gitbook/assets/image (1939).png" alt="" width="199"><figcaption></figcaption></figure>

**Payment Method** — select the desired payment method for receiving funds.

{% hint style="warning" %}
Please note a particular feature of the Ivanpay service — **whenever possible**, a card from the bank you selected in the module settings will be issued. However, if no cards from the chosen bank are available, a card from another bank currently supported by the service will be issued instead (the payment method itself remains unchanged and stays as the original — CARD or SBP).
{% endhint %}

{% hint style="warning" %}
When accepting payments through the Ivanpay merchant, it is **mandatory** to add an extra field to your exchange form that the client must fill out when creating a request.
{% endhint %}

To do this, create and add an [additional field](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/valyuty-i-napravleniya/dobavlenie-novoi-valyuty#vkladka-dop.-polya) to the relevant currencies for receiving payments via Ivanpay. Be sure to enter "**Unique ID**" as **`give_cardholder`** (use lowercase letters) and make this field mandatory.

![](<../../../.gitbook/assets/image (322).png>)

After that, the field will appear in the exchange form and will be required for clients to fill out when creating a request.

![](<../../../.gitbook/assets/image (1879).png>)

## Continuing the setup

Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).