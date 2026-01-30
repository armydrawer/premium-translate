# Finora

{% hint style="info" %}
If you need to update the module on the server, please refer to the [instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-merchantov).
{% endhint %}

{% hint style="warning" %}
For discussions regarding terms and connections, please contact a [service representative](https://t.me/Exe_PMx).

**Disclaimer**: When connecting your website to any service, please assess the potential risks of collaboration on your own.
{% endhint %}

{% hint style="warning" %}
Please note that when using the Finora payment module, the actual payout amount is always rounded to four decimal places on the service's side.
{% endhint %}

## Module Settings

In the admin panel, create a new merchant in the "**Merchants**" section ➔ "**Add Merchant**."

Select Finora from the dropdown list in the "**Module**" field, provide a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="345"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (251).png" alt="" width="421"><figcaption></figcaption></figure>

**API Key** — This is the key provided to you by your Finora manager for a specific payment method (please confirm this information with your manager).

## Special Fields

<figure><img src="../../../.gitbook/assets/изображение (1) (1).png" alt=""><figcaption></figcaption></figure>

**Merchant Type** (the selected option is fixed to the module and cannot be changed later):

* **Payment Link** — returns a link for payment via QR code in the request; this option works in conjunction with the selected payment method.
* **Requisites** — returns a card or phone number for transferring funds directly in the request using the shortcode \[to\_account].

<figure><img src="../../../.gitbook/assets/изображение (192).png" alt=""><figcaption></figcaption></figure>

**Payment Method** — select the appropriate method from the list or manually enter your option in the "**Add**" field (please confirm acceptable options with your Finora manager).

<figure><img src="../../../.gitbook/assets/изображение (188).png" alt=""><figcaption></figcaption></figure>

**Bank** — select the appropriate bank from the list or manually enter your option in the "**Add**" field (please confirm acceptable options with your Finora manager).

{% hint style="danger" %}
Choose a specific bank only if you previously selected the **Payment Link** format; if you are using the **Requisites** format, leave the default option (no bank selected).
{% endhint %}

<figure><img src="../../../.gitbook/assets/изображение (191).png" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
Please note that if you select a specific bank in the module settings, your client will need to make payments using a card from that bank (payments made with cards from other banks may not be credited, including through appeals).
{% endhint %}

{% hint style="danger" %}
Please be aware that a separate copy of the merchant module must be created for each payment method.
{% endhint %}

To operate the module for receiving funds without using a [cron job](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-sozdat-zadanie-cron-na-servere), enter the link from the module settings

<figure><img src="https://premium.gitbook.io/main/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252F6nSFLEEezB9OcBzt8DhE%252F%25D0%25B8%25D0%25B7%25D0%25BE%25D0%25B1%25D1%2580%25D0%25B0%25D0%25B6%25D0%25B5%25D0%25BD%25D0%25B8%25D0%25B5.png%3Falt%3Dmedia%26token%3D0c2df531-cd7a-4ff8-9fdc-dcf940e9eb68&#x26;width=768&#x26;dpr=3&#x26;quality=100&#x26;sign=d422910b&#x26;sv=2" alt=""><figcaption></figcaption></figure>

in the Finora personal account in the **PayIn Webhook** field:

<figure><img src="../../../.gitbook/assets/изображение (2).png" alt=""><figcaption></figcaption></figure>

## Continuing the Setup

Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).<br>