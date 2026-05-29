# Unite

{% hint style="danger" %}
Before setting up automatic payouts, please read the [risk warning!](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/preduprezhdenie-o-riskakh)
{% endhint %}

{% hint style="info" %}
If you need to update the module on the server, please refer to the [instructions](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat)
{% endhint %}

## Merchant Account Settings

{% hint style="warning" %}
To discuss terms and connection, please contact a [service representative](https://t.me/Paylonium_TeamLead).

**Disclaimer**: When connecting your website to any service, please assess the potential risks of collaboration on your own.
{% endhint %}

Register on the [Unite service](https://unitekass.org/#contacts) and log in to your merchant account.

Create a new project in the "**Projects**" section. Fill in the required fields in the pop-up window, submit your application for review, and wait for the status to change from "**Under Moderation**" to "**Active**."

Once your project is activated, go to its settings and copy the highlighted keys.

## Module Settings

In the admin panel, create a new merchant in the "**Merchants**" ➔ "**Add Automatic Payout**" section.

Select Unite from the drop-down list in the "**Module**" field, provide a name for the module, and click "**Save**."

Fill in the specified authorization fields.

<figure><img src="../../../.gitbook/assets/image (384).png" alt=""><figcaption></figcaption></figure>

**Domain** — leave this field empty.

**Username** — the username in Latin characters that you created and provided to the Unite representative for your account.

**Private Key PEM** — the private key previously provided to you by the Unite representative.

**Private Key Password** — the password for the private key, also provided to you by the Unite representative.

## Special Fields

<figure><img src="../../../.gitbook/assets/image (385).png" alt=""><figcaption></figcaption></figure>

**Payment Method:**

* **Card** — payout to a bank card
* **Qiwi** — payout to a Qiwi wallet
* **SBP** — payout to the phone number linked to SBP
* **Mobile top-up** — top-up for a mobile phone number

**Bank Code (SBP only):**

* **Additional Fields (Currencies)** — use the [additional currency field](https://premium.gitbook.io/main/osnovnye-nastroiki/valyuty-i-napravleniya-obmena/dopolnitelnye-polya#dopolnitelnye-polya-dlya-valyuty) "**Receiving**"
* **Additional Fields (Direction)** — use the [additional exchange direction field](https://premium.gitbook.io/main/osnovnye-nastroiki/valyuty-i-napravleniya-obmena/dopolnitelnye-polya#dopolnitelnye-polya-dlya-napravleniya-obmena)
* **Bank Code (SBP only)** — manually select the bank for SBP payouts

<div><figure><img src="../../../.gitbook/assets/image (403).png" alt=""><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/image (410).png" alt=""><figcaption></figcaption></figure></div>

## Continuing the Setup

Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).<br>
