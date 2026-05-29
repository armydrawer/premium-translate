# Merchant001

{% hint style="info" %}
If you need to update the module on the server, please refer to the [instructions](https://premium.gitbook.io/main/en/en/basic-settings/faq/updating-script-files-on-the-server/how-to-update-files-on-the-server#merchant-and-auto-payout-modules).
{% endhint %}

{% hint style="info" %}
To display the **cardholder's full name and the name of the bank that issued the card** in the client's application, add the shortcode \[dest\_tag] in the instructions within the merchant settings.

<img src="../../../.gitbook/assets/image (1627)_eng.png" alt="" data-size="original">
{% endhint %}

## Merchant Account Settings

{% hint style="warning" %}
For discussions regarding terms and connections, please contact a [service representative](https://t.me/merch001online).

**Disclaimer**: When connecting your website to any service, please assess the potential risks of collaboration on your own.
{% endhint %}

Register on the Merchant001 service and go to your personal account. Create a new token in the ["**API**" - "**Settings**" section](https://app.merchant001.io/merchant/api) - the token will be automatically copied to the clipboard.

<figure><img src="../../../.gitbook/assets/image (1717)_eng.png" alt=""><figcaption></figcaption></figure>

## Module Settings

In the admin panel, create a new merchant in the "**Merchants**" section by selecting "**Add Merchant**."

Choose Merchant001 from the dropdown list in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (385).png" alt="" width="374"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (398).png" alt="" width="378"><figcaption></figcaption></figure>

**Token** — the domain generated in the Merchant001 account after API access is created.

**Access Code** — a technical field that does not need to be filled in.

## Special Fields

**Merchant type:**

<figure><img src="../../../.gitbook/assets/image (418).png" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
The merchant type is assigned to the custom module without the ability to change it after the first order created using this module.

In order to use a different type of merchant, you need to create a separate copy by selecting a different type and connect it in the desired exchange direction.
{% endhint %}

* **Requisites** - details from the merchant will be displayed in the application itself

<figure><img src="../../../.gitbook/assets/image (403).png" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
When choosing this type of issuing details, the time for creating orders may increase to 20 seconds due to the selection of details on the merchant’s side
{% endhint %}

* **Payment link** - the application will display the “**Proceed to payment**” button, when clicked, the client will be taken to the merchant’s payment page, where details will be displayed or details will be selected and then displayed.

**Payment method:**

<figure><img src="../../../.gitbook/assets/image (410).png" alt=""><figcaption></figcaption></figure>

* **ALL** – details of any format specified below will be issued
* **\[RUB] НСПК (QR-код)** - QR code for payment through NSPK
* **\[RUB] Универсальный QR с чеком** - individual entrepreneur in a bank with auto-filling of details via QR

{% hint style="info" %}
The list of available systems and currencies in the dropdown is determined by your token specified in the module settings for authorization.

If the systems or currencies you need, as shown in the screenshot above, do not appear in the list, please contact merchant support to have them enabled.
{% endhint %}

## Continuing the Setup

Next, proceed with the merchant setup by following the [general setup instructions](https://premium.gitbook.io/main/en/en/basic-settings/merchants-and-auto-payments/merchants/general-merchant-settings).
