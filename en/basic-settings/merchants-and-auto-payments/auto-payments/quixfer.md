# Quixfer

{% hint style="danger" %}
<mark style="color:red;">Before setting up automatic payouts, please read the</mark> [<mark style="color:blue;">risk warning</mark>](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/preduprezhdenie-o-riskakh)<mark style="color:blue;">!</mark>
{% endhint %}

{% hint style="info" %}
If you need to update the module on the server, please refer to the [instructions](https://premium.gitbook.io/main/en/basic-settings/faq/updating-script-files-on-the-server/how-to-update-files-on-the-server#merchant-and-auto-payout-modules).
{% endhint %}

## Merchant Account Settings

{% hint style="warning" %}
To discuss the terms of service, please contact a [service representative](https://t.me/quixfer).

**Disclaimer**: When connecting your website to any service, please assess the potential risks of collaboration on your own.
{% endhint %}

[Register](https://quixfer.cc/#contacts) on the Quixfer service, log into your account, and navigate to the "**Settings**" ➔ "**Security**" section.

<figure><img src="../../../.gitbook/assets/image (4) (1) (1) (1) (1)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

Generate your API keys and save them in a text file.

<figure><img src="../../../.gitbook/assets/image (5) (1) (1) (1)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

## Module Settings

In the admin panel, create a new merchant in the "**Automatic Payouts**" ➔ "**Add Automatic Payout**" section.

Select Quixfer from the dropdown menu in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1)_eng.png" alt="" width="472"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1)_eng.png" alt="" width="460"><figcaption></figcaption></figure>

**Domain** — leave this field empty.

**API Key** — Public Key from your Quixfer account, copied earlier.

**Secret Key** — Private Key from your Quixfer account, copied earlier.

## Special Fields

<figure><img src="../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

**Payment Method** — select the desired method for fund payouts or choose "**Automatically**" — in this case, the payout will be made according to the XML code of the currency from the exchange direction where the module is connected (the list of methods will only be displayed after entering the correct API keys for module authorization).

## Additional Fields <a href="#dopolnitelnye-polya" id="dopolnitelnye-polya"></a>

To correctly receive the details for the currency being accepted with Quixfer, you need to add **mandatory** additional fields to the exchange form. A hint regarding the required fields for each payment method will be displayed below the "**Payment Method**" field.

<figure><img src="../../../.gitbook/assets/image (4) (1) (1) (1)_eng.png" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
Hovering over the parameter name will show you the format in which the field needs to be added for client data entry in the exchange form on the website.

![](<../../../.gitbook/assets/image (1)_eng.png>)
{% endhint %}

Create and add an [additional field](https://premium.gitbook.io/main/osnovnye-nastroiki/valyuty-i-napravleniya-obmena/dopolnitelnye-polya) for the relevant currencies for **fund payouts** through Quixfer. Be sure to specify a value in the "**Unique ID**" field (use lowercase letters) and make the field mandatory for completion.

<figure><img src="../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1)_eng.png" alt="" width="461"><figcaption></figcaption></figure>

After this, the field will appear in the exchange form and will be mandatory for clients when creating a request.

<figure><img src="../../../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (1) (1)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

Example of filling out for the currency T-Bank RUB (highlighted names from the "Unique ID" fields):

<figure><img src="../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

Example of filling out for the currency Bank transfer GEL (Georgian Lari):

<figure><img src="../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

## Continuing the Setup

Next, proceed to configure the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-merchantov-avtovyplat).