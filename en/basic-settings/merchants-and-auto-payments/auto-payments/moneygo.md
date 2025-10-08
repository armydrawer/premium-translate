# MoneyGo

{% hint style="danger" %}
<mark style="color:red;">Before setting up auto payouts, please read the</mark> [<mark style="color:blue;">risk warning</mark>](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/preduprezhdenie-o-riskakh)<mark style="color:blue;">!</mark>
{% endhint %}

{% hint style="info" %}
If you need to update the module on the server, please refer to the [instructions](https://premium.gitbook.io/main/en/basic-settings/faq/updating-script-files-on-the-server/how-to-update-files-on-the-server#merchant-and-auto-payout-modules).
{% endhint %}

## Merchant Account Settings <a href="#nastroiki-v-lichnom-kabinete-merchanta" id="nastroiki-v-lichnom-kabinete-merchanta"></a>

Register for the [MoneyGo](https://money-go.com/ru/register) service. After registration, request API access from your MoneyGo manager or submit a request for API access to work with the module through the [feedback form](https://money-go.com/ru/helpdesk) (under the "**Contacts**" section on the website), selecting the "**Collaboration**" option and filling out the required fields.

<figure><img src="../../../.gitbook/assets/image (2010)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

## Module Settings <a href="#nastroiki-modulya" id="nastroiki-modulya"></a>

In the admin panel, create a new merchant in the "**Auto Payouts**" -> "**Add Auto Payout**" section.

Select MoneyGo from the dropdown list in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/image (216)_eng.png" alt="" width="452"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (217)_eng.png" alt="" width="446"><figcaption></figcaption></figure>

**Client ID** — The ID provided to you by your MoneyGo manager.

**Client Secret** — The client key provided to you by your MoneyGo manager.

**Token** — This field should remain empty.

**U-wallet** — The USD wallet from your MoneyGo account.

<figure><img src="../../../.gitbook/assets/image (218)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

**E-wallet, R-wallet** — These fields should remain empty.

## Special Fields

{% hint style="warning" %}
For the module to function correctly for the currency "**Receiving**" in the exchange direction where MoneyGo is used for payouts, the mandatory field "**To** **Account**" must be active. This field will be filled out by the client in the application creation form (indicating their wallet in the MoneyGo system).

![](<../../../.gitbook/assets/image (219)_eng.png>)
{% endhint %}

## Continuing the Setup

Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-merchantov-avtovyplat).