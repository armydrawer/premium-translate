# Payscrow

{% hint style="danger" %}
<mark style="color:red;">Before setting up automatic payouts, please read the</mark> [<mark style="color:blue;">risk warning</mark>](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/preduprezhdenie-o-riskakh)<mark style="color:blue;">!</mark>
{% endhint %}

{% hint style="info" %}
If you need to update the module on the server, please refer to the [instructions](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat).
{% endhint %}

## Merchant Account Settings <a href="#nastroiki-v-lichnom-kabinete-merchanta" id="nastroiki-v-lichnom-kabinete-merchanta"></a>

{% hint style="warning" %}
To discuss terms and setup, please contact a [service representative](https://t.me/Payscrow).

**Disclaimer**: When connecting your website to any service, please assess the potential risks of collaboration on your own.
{% endhint %}

Register and log in to your merchant account. In the "**Profile**" ➔ "**API Settings**" section, copy the API key and signature key for authorization in the automatic payout module.

<figure><img src="../../../../.gitbook/assets/image (126).png" alt=""><figcaption></figcaption></figure>

In the "**Sale Status**" field, later specify the URL from the automatic payout module settings (Webhook).

<figure><img src="../../../../.gitbook/assets/image (127).png" alt=""><figcaption></figcaption></figure>

## Module Settings <a href="#nastroiki-modulya" id="nastroiki-modulya"></a>

In the admin panel, create a new merchant in the "**Automatic Payouts**" ➔ "**Add Automatic Payout**" section.

Select Payscrow from the dropdown list in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../../.gitbook/assets/image (124).png" alt="" width="444"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../../.gitbook/assets/image (125).png" alt="" width="451"><figcaption></figcaption></figure>

**Domain** — The URL provided to you by the merchant representative.

**API Key** — The API key copied from the merchant account.

**Signature Key** — The signature key copied from the merchant account.

## Special Fields

<figure><img src="../../../../.gitbook/assets/image (128).png" alt="" width="516"><figcaption></figcaption></figure>

**Payment Method** — Choose the necessary method for disbursing funds.

**Who pays the fee:**

* Merchant — The exchange pays the service fee (the fee amount will be deducted from your balance).
* User — The client pays the service fee (in this case, the client will receive 5% less than the original amount requested).

## Continuing the Setup

Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-merchantov-avtovyplat).