# Bitconce Card/Link

{% hint style="info" %}
If you need to update the module on the server, please refer to the [instructions](https://premium.gitbook.io/main/en/basic-settings/faq/kak-obnovit-faily-na-servere#moduli-merchantov).
{% endhint %}

<details>

<summary><mark style="background-color:red;">Replacing the Outdated Bitconce Module in the Admin Panel</mark></summary>

The **Bitconce** module has been split into two separate modules for handling different currencies:

• **Bitconce Card** — provides account details on the application page (banks for accepting KZT, QIWI, ЮMoney, and other systems)

• **Bitconce Link** — redirects to the merchant's payment page (only banks for RUB currency)

If you previously used the **Bitconce** module, depending on the currency you were using (RUB or others), replace it with one of the new modules in the settings of the already created module copy in the "**Merchants**" section (the old module will no longer be supported - <mark style="color:red;">it must also be removed from the server</mark>) and click "**Save**" (see screenshot).

When setting up a merchant from scratch, simply select the appropriate module from the list (if the new modules are not listed, you will need to upload them to the server manually following the [instructions](https://premium.gitbook.io/main/en/basic-settings/faq/kak-obnovit-faily-na-servere#moduli-merchantov)).

_Please note that the new modules are incompatible with the old module - if you decide to use the new modules, the old module (Bitconce) must be removed from the server. If you choose to continue using the old module (it will work until the merchant-side methods are disabled), nothing will change for you, and you do not need to upload the new modules to the server._

<img src="../../../.gitbook/assets/image (631)_eng.png" alt="" data-size="original">\
After replacing the module, configure the new module according to the standard instructions, and adjust the user instruction text in the module settings if you replaced the module with **Bitconce Link** (the shortcode \[to\_account] can also be removed from the instructions — instead of providing account details in the application, a "**Proceed to Payment**" button will be displayed).\
![](<../../../.gitbook/assets/image (624)_eng.png>)

</details>

{% hint style="warning" %}
To use [ЮMoney](https://yoomoney.ru/) for receiving funds, you need to request a separate token from Bitconce and create a separate copy of the merchant module for receiving ЮMoney.

In this case, the bank selection in the "**Bank**" field will not matter (choose any item from the list) — the module copy will only work with ЮMoney.

<img src="../../../.gitbook/assets/image (628)_eng.png" alt="" data-size="original">
{% endhint %}

## Settings in the Merchant's Personal Account

Register or log in to the [Bitconce](https://bitconce.top/) system.

Go to the "**API**" section:

<figure><img src="../../../.gitbook/assets/изображение (92)_eng.png" alt="" width="341"><figcaption></figcaption></figure>

To obtain a token in the "**API Token**" block, click the "Create" button:

<figure><img src="../../../.gitbook/assets/изображение (100)_eng.png" alt=""><figcaption></figcaption></figure>

## Module Settings

In the admin panel, create a new merchant in the "**Merchants**" -> "**Add Merchant**" section.

Select a module from the dropdown list. There are two separate modules for Bitconce to work with different currencies:

* **Bitconce Card** — if you want the wallet/card number to be provided directly on your site.

<figure><img src="../../../.gitbook/assets/image (627)_eng.png" alt="" width="496"><figcaption></figcaption></figure>

* **Bitconce Link** — if you want the user to be redirected to the payment system's site (works only with RUB).

<figure><img src="../../../.gitbook/assets/image (626)_eng.png" alt="" width="503"><figcaption></figcaption></figure>

{% hint style="warning" %}
If the specified modules are not in the dropdown list, upload the modules to the server following the [instructions](https://premium.gitbook.io/main/en/basic-settings/faq/kak-obnovit-faily-na-servere#moduli-merchantov).
{% endhint %}

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (1437)_eng.png" alt=""><figcaption></figcaption></figure>

**Token** — the token obtained in your Bitconce personal account.

## Special Fields

<figure><img src="../../../.gitbook/assets/image (1436)_eng.png" alt="" width="354"><figcaption></figcaption></figure>

* **Bank** — select the bank whose details will be provided in the application.

{% tabs %}
{% tab title="Bitconce Card" %}
The list of available banks in the dropdown is determined by your token specified in the module settings for authorization.

If the banks you need, as shown in the screenshot below, do not appear in the list, please contact merchant support to have them included.

<figure><img src="../../../.gitbook/assets/image (629)_eng.png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Bitconce Link (RUB)" %}
The list of available banks in the dropdown is determined by your token specified in the module settings for authorization.

If the banks you need, as shown in the screenshot below, do not appear in the list, please contact merchant support to have them included.

<figure><img src="../../../.gitbook/assets/image (628)_eng.png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

* **SBP** — transfer of funds by phone number, which will be provided in the application (works only in the Bitconce Link module)\
  • **Yes**\
  • **No**
* **Show another bank's card if the requested one is not available** — provide alternative payment details (any bank from the list for the same currency) if there are no available details for the selected bank\
  • **Yes**\
  • **No**

## Continuing the Setup

Next, proceed to configure the merchant by following the [general setup instructions](https://premium.gitbook.io/main/en/en/basic-settings/merchants-and-auto-payments/merchants/general-merchant-settings).