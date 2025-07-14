# PandaPay

{% hint style="info" %}
If you need to update the module on your server, please follow the [instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-merchantov).
{% endhint %}

## Settings in the Merchant Dashboard

{% hint style="warning" %}
To discuss terms and set up your connection, please contact a [service representative](https://t.me/PandaPaySup).

**Disclaimer:** When connecting your website to any service, please independently assess any potential risks involved in the partnership.
{% endhint %}

After receiving your login credentials from the service representative, log in to your [PandaPay dashboard](https://pandapay24.com/). Then, go to the "**Settings**" section.

<figure><img src="../../../.gitbook/assets/image (122).png" alt="" width="563"><figcaption></figcaption></figure>

Enter the Callback URL in the designated field.

<figure><img src="../../../.gitbook/assets/image (120).png" alt="" width="563"><figcaption></figcaption></figure>

{% hint style="success" %}
To update the status of requests, make sure to specify the current Callback URL in your merchant dashboard — you can find this URL in the module settings under the "**Webhook**" field.

![](<../../../.gitbook/assets/image (121).png>)
{% endhint %}

Generate new access keys and copy them to your clipboard or save them in a text file.

<figure><img src="../../../.gitbook/assets/image (119).png" alt="" width="563"><figcaption></figcaption></figure>

## Module Settings

In the admin panel, create a new merchant by navigating to "**Merchants**" ➔ "**Add Merchant**."

Select PandaPay from the dropdown menu in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (2092).png" alt="" width="445"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (2093).png" alt="" width="458"><figcaption></figcaption></figure>

**API Key** — the API key copied from your merchant dashboard

**Secret Key** — the secret key copied from your merchant dashboard

## Special Fields

<figure><img src="../../../.gitbook/assets/image (2094).png" alt="" width="456"><figcaption></figcaption></figure>

**Allowed Countries** — the list of countries where the system will search for payment details.

- **If "ANY" is selected**, the search will include all countries.  
- **If one or more specific countries are selected**, the search will be limited to those countries only.  
- **If no countries are selected**, the search will be based on the currency code of the "**Giving**" side in the exchange direction.

**Payment Method** — the method used to search for payment details:

<figure><img src="../../../.gitbook/assets/image (2097).png" alt="" width="354"><figcaption></figcaption></figure>

* **accountNumber** — bank account number  
* **card** — bank card number  
* **crossBorderTransfer** — cross-border money transfer  
* **SBP** — phone number for transfers via SBP  

{% hint style="info" %}
The "**Add**" buttons allow you to add new methods without updating the module on the server itself (use these options **only** if the merchant representative has informed you that it is necessary).  
{% endhint %}

## Continuing the setup

Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).