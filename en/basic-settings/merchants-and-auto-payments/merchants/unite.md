# Unite

{% hint style="info" %}
If you need to update a module on the server, please refer to the [instructions](https://premium.gitbook.io/main/en/basic-settings/faq/updating-script-files-on-the-server/how-to-update-files-on-the-server#merchant-and-auto-payout-modules).
{% endhint %}

## Merchant Account Settings

{% hint style="warning" %}
To discuss working conditions, please contact a [service representative](https://t.me/Unite_Plat).

**Disclaimer**: When connecting your website to any service, please assess the potential risks of collaboration on your own.
{% endhint %}

Register on the [Unite service](https://unitekass.org/#contacts) and log in to your merchant account. Create a new project in the "**Projects**" section. Fill in the required fields in the pop-up window, submit your application for review, and wait for the status to change from "**Under Moderation**" to "**Active**."

Once your project is activated, go to its settings and copy the highlighted keys.

## Module Settings

In the admin panel, create a new merchant in the "**Merchants**" ➔ "**Add Merchant**" section.

Select Unite from the drop-down list in the "**Module**" field, provide a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (428).png" alt=""><figcaption></figcaption></figure>

Fill in the specified authorization fields.

<figure><img src="../../../.gitbook/assets/image (433).png" alt=""><figcaption></figcaption></figure>

**Domain** — leave this field empty.

**Key ID** — the ID provided to you earlier by the Unite representative.

**Private Key** — the key provided to you earlier by the Unite representative.

## Special Fields

**Merchant Type:**

<figure><img src="../../../.gitbook/assets/image (434).png" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
The merchant type is assigned to the configured module and cannot be changed after the first application is created using this module.

To use a different merchant type, you must create a separate copy, selecting a different type and connecting it in the desired exchange direction.
{% endhint %}

* **Requisites** — the merchant's details will be displayed in the application itself.

<figure><img src="../../../.gitbook/assets/image (382).png" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
Choosing this type of details may increase the application creation time by up to 20 seconds due to the merchant's details being retrieved.
{% endhint %}

* **Payment Link** — a "**Proceed to Payment**" button will appear in the application, which, when clicked, will take the client to the merchant's payment page, where the details will be displayed or retrieved and then shown:

<div><figure><img src="../../../.gitbook/assets/image (438).png" alt=""><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/image (437).png" alt=""><figcaption></figcaption></figure></div>

When using the **Payment Link** method, the client will need to attach a receipt after completing the payment:

<figure><img src="../../../.gitbook/assets/image (436).png" alt=""><figcaption></figcaption></figure>

After uploading the receipt, the client must wait for it to be processed:

<figure><img src="../../../.gitbook/assets/image (435).png" alt=""><figcaption></figcaption></figure>

**Payment Method:**

{% tabs %}
{% tab title="When selecting "Requisites"" %}
<figure><img src="../../../.gitbook/assets/image (439).png" alt=""><figcaption></figcaption></figure>

* **Card** — bank card number
* **SBP** — phone number linked to SBP
{% endtab %}

{% tab title="When selecting "Payment Link"" %}
<figure><img src="../../../.gitbook/assets/image (440).png" alt=""><figcaption></figcaption></figure>

* **Any** — details of any format specified below will be provided
* **Card** — bank card number
* **SBP** — phone number linked to SBP
* **TPay** — details for payment via [T-Pay service](https://www.tbank.ru/t-pay/online/)
{% endtab %}
{% endtabs %}

## Continuing the Setup

Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/main/en/basic-settings/merchants-and-auto-payments/merchants/general-merchant-settings).
