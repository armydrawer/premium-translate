# Payscrow Cascade

{% hint style="danger" %}
<mark style="color:red;">Before setting up automatic payouts, please read the</mark> [<mark style="color:blue;">risk warning</mark>](https://premium.gitbook.io/main/en/basic-settings/merchants-and-auto-payments/auto-payments/risk-warning)<mark style="color:blue;">!</mark>
{% endhint %}

{% hint style="info" %}
If you need to update the module on the server, please refer to the [instructions](https://premium.gitbook.io/main/en/en/basic-settings/faq/updating-script-files-on-the-server/how-to-update-files-on-the-server#merchant-and-auto-payout-modules).
{% endhint %}

## Merchant Account Settings <a href="#nastroiki-v-lichnom-kabinete-merchanta" id="nastroiki-v-lichnom-kabinete-merchanta"></a>

{% hint style="warning" %}
To discuss terms and connection, please contact a [service representative](https://t.me/Payscrow).

**Disclaimer**: When connecting your website to any service, please assess the potential risks of collaboration on your own.
{% endhint %}

Register and log in to your merchant account. In the "Terminals" section ➔ "**API Settings**," copy the API key for authorization in the automatic payout module.

<figure><img src="../../../../.gitbook/assets/image (11) (2).png" alt="" width="563"><figcaption></figcaption></figure>

In the "**Order Status for Sale**" field, enter the URL from the automatic payout module settings (Callback URL).

<figure><img src="../../../../.gitbook/assets/image (12) (2).png" alt=""><figcaption></figcaption></figure>

## Module Settings <a href="#nastroiki-modulya" id="nastroiki-modulya"></a>

In the admin panel, create a new merchant in the "**Automatic Payouts**" ➔ "**Add Automatic Payout**" section.

Select Payscrow Cascade from the dropdown list in the "**Module**" field, provide a name for the module, and click "**Save**."

Fill in the required authorization fields.

**API Key** — The API key copied from the merchant account.

## Special Fields

<figure><img src="../../../../.gitbook/assets/image (10) (2).png" alt="" width="422"><figcaption></figcaption></figure>

**Payment Method** — Choose the appropriate method for disbursing funds.

* **\[BankCard, RUB] Any Bank in Russia** — provides a card number from any bank\
  • **\[BankCard, RUB] {bank\_name}** — provides a card number from the specified bank
* **\[SBP, RUB] SBP {bank\_name}** — provides a phone number for payment linked to the card of the selected bank

{% hint style="warning" %}
Please note that for successful payouts to Russian bank cards, you must select an aggregate method (for example, "Any Bank in Russia"), and for SBP payouts, you should specify the bank.
{% endhint %}

## Continuing the Setup

Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/main/en/basic-settings/merchants-and-auto-payments/auto-payments/obshie-nastroiki-merchantov-avtovyplat).
