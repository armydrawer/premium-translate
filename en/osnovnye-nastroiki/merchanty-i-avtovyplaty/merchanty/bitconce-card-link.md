Certainly! Here's a natural, fluent English translation of the provided text:

---

# Bitconce Card/Link

{% hint style="info" %}
If you need to update the module on your server, please follow the [instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-merchantov).
{% endhint %}

<details>

<summary><mark style="background-color:red;">Replacing the outdated Bitconce module in the admin panel</mark></summary>

The **Bitconce** module has been split into two separate modules to support different currencies:

• **Bitconce Card** — provides payment details on the application page (banks for accepting KZT, QIWI, YooMoney, and other systems)

• **Bitconce Link** — redirects to the merchant’s payment page (banks only for RUB currency)

If you were previously using the **Bitconce** module, you need to replace it with one of the new modules depending on the currency you use (RUB or other currencies). Do this by selecting the appropriate new module in the settings of the existing module copy under the "**Merchants**" section (the old module will no longer be supported — <mark style="color:red;">it must also be removed from the server</mark>). Then click "**Save**" (see screenshot).

When setting up a merchant from scratch, simply choose the appropriate module from the list. If the new modules are not visible in the list, you will need to upload them to the server manually following the [instructions](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-merchantov).

_Note that the new modules are not compatible with the old one. If you decide to switch to the new modules, the old Bitconce module must be removed from the server. If you choose to continue using the old module (which will work until the merchant-side methods are disabled), nothing will change for you and you do not need to upload the new modules to the server._

<img src="../../../.gitbook/assets/image (631).png" alt="" data-size="original">\
After replacing the module, configure the new module according to the standard instructions. Also, update the user instructions text in the module settings if you switched to **Bitconce Link** (you can remove the shortcode \[to_account] from the instructions — instead of showing payment details on the application page, a "**Proceed to Payment**" button will be displayed).\
![](<../../../.gitbook/assets/image (624).png>)

</details>

---

Let me know if you need it adapted for a specific audience or style!

Here is a natural, fluent English translation of the provided text:

---

{% hint style="warning" %}
To use [YooMoney](https://yoomoney.ru/) for receiving payments, you need to request a separate token from Bitconce and create a separate copy of the merchant module specifically for YooMoney payments.

In this case, the bank selection in the "**Bank**" field will not matter (you can select any option from the list) — the module copy will work exclusively with YooMoney.

<img src="../../../.gitbook/assets/image (628).png" alt="" data-size="original">
{% endhint %}

## Settings in the Merchant Dashboard

Register or log in to your account at [Bitconce](https://bitconce.top/).

Go to the "**API**" section:

<figure><img src="../../../.gitbook/assets/изображение (92).png" alt="" width="341"><figcaption></figcaption></figure>

To get your token, click the "Create" button in the "**API Token**" block:

<figure><img src="../../../.gitbook/assets/изображение (100).png" alt=""><figcaption></figcaption></figure>

## Module Configuration

In the admin panel, create a new merchant under "**Merchants**" -> "**Add Merchant**."

Select the module from the dropdown list. Bitconce offers two separate modules for handling different currencies:

* **Bitconce Card** — use this if you want the wallet/card number to be displayed directly on your website.

<figure><img src="../../../.gitbook/assets/image (627).png" alt="" width="496"><figcaption></figcaption></figure>

* **Bitconce Link** — use this if you want the user to be redirected to the payment system’s website to complete the payment (works only with RUB).

<figure><img src="../../../.gitbook/assets/image (626).png" alt="" width="503"><figcaption></figcaption></figure>

{% hint style="warning" %}
If the modules mentioned above do not appear in the dropdown list, upload the modules to your server following the [instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-merchantov).
{% endhint %}

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (1437).png" alt=""><figcaption></figcaption></figure>

**Token** — the token you obtained from your Bitconce dashboard

## Special Fields

<figure><img src="../../../.gitbook/assets/image (1436).png" alt="" width="354"><figcaption></figcaption></figure>

* **Bank** — select the bank whose details will be provided in the payment request

{% tabs %}
{% tab title="Bitconce Card" %}
The list of available banks in the dropdown is determined by the token you entered in the module settings for authorization.

If the banks you need (as shown in the screenshot below) do not appear in the list, please contact merchant support to have them enabled.

<figure><img src="../../../.gitbook/assets/image (629).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

---

If you need any further adjustments or a more formal tone, just let me know!

{% tab title="Bitconce Link (RUB)" %}
The list of available banks in the dropdown menu is determined by the token you provided in the module settings for authorization.

If the banks you need, as shown in the screenshot below, do not appear in the list, please contact the merchant support team to have them enabled.

<figure><img src="../../../.gitbook/assets/image (628).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

* **SBP** — transfer funds using a phone number provided in the application (works only in the Bitconce Link module)\
  • **Yes**\
  • **No**
* **Show a card from another bank if the requested one is unavailable** — select alternative payment details (any bank from the list with the same currency) if there are no available details for the chosen bank\
  • **Yes**\
  • **No**

## Continuing the setup

Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).