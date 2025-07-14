# MoneyGo

{% hint style="danger" %}
<mark style="color:red;">Before setting up auto payouts, be sure to read the</mark> [<mark style="color:blue;">risk warning</mark>](https://premiumexchanger.com/wiki/preduprezhdenie-auto/)<mark style="color:blue;">!</mark>
{% endhint %}

{% hint style="info" %}
If you need to update the module on your server, please follow the [instructions here](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-avtovyplat).
{% endhint %}

## Settings in the Merchant Dashboard <a href="#merchant-dashboard-settings" id="merchant-dashboard-settings"></a>

Register for an account at [MoneyGo](https://money-go.com/ru/register). After registering, request API access from your MoneyGo manager or submit a request for API access to work with the module via the [contact form](https://money-go.com/ru/helpdesk) (under the "**Contacts**" section on the website). Select "**Cooperation**" and fill in the required fields.

<figure><img src="../../../.gitbook/assets/image (2010).png" alt=""><figcaption></figcaption></figure>

## Module Settings <a href="#module-settings" id="module-settings"></a>

In the admin panel, create a new merchant by navigating to "**Auto Payouts**" -> "**Add Auto Payout**."

Select MoneyGo from the dropdown menu in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (216).png" alt="" width="452"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (217).png" alt="" width="446"><figcaption></figcaption></figure>

- **Client ID** — the ID provided to you by your MoneyGo manager  
- **Client Secret** — the client key provided to you by your MoneyGo manager  
- **Token** — leave this field empty  
- **U-wallet** — your USD wallet from your MoneyGo account dashboard

<figure><img src="../../../.gitbook/assets/image (218).png" alt="" width="563"><figcaption></figcaption></figure>

- **E-wallet**, **R-wallet** — leave these fields empty

## Special Fields

{% hint style="warning" %}
For the module to work correctly, the "**To Account**" field must be enabled and mandatory for the "**Receiving**" currency in the exchange direction where MoneyGo is used for payouts. This field will be filled in by the client when creating a request (the client must specify their wallet in the MoneyGo system).

![](<../../../.gitbook/assets/image (219).png>)
{% endhint %}

## Continuing Setup

Next, complete the merchant setup by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-merchantov-avtovyplat).