# Ivanpay

{% hint style="danger" %}
<mark style="color:red;">Before setting up auto payouts, be sure to read</mark> [<mark style="color:blue;">the risk warning</mark>](https://premiumexchanger.com/wiki/preduprezhdenie-auto/)<mark style="color:blue;">!</mark>
{% endhint %}

{% hint style="info" %}
If you need to update the module on your server, please follow this [instruction](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-avtovyplat).
{% endhint %}

## Settings in the Merchant’s Personal Account <a href="#nastroiki-v-lichnom-kabinete-merchanta" id="nastroiki-v-lichnom-kabinete-merchanta"></a>

{% hint style="warning" %}
To discuss terms and connection details, please contact the [service representative](https://t.me/IvanPay_pro).

**Disclaimer:** When connecting your website to any service, please independently assess the potential risks involved in the partnership.
{% endhint %}

Register an account on the [IvanPay service](https://ivanpay.com/).

<figure><img src="../../../.gitbook/assets/image (214).png" alt=""><figcaption></figcaption></figure>

In your merchant personal account, copy the information from the "**Your API Address**" field, as well as the API key provided to you by the service representative.

<figure><img src="../../../.gitbook/assets/image (215).png" alt=""><figcaption></figcaption></figure>

## Module Settings <a href="#nastroiki-modulya" id="nastroiki-modulya"></a>

In the admin panel, create a new merchant under "**Auto Payouts**" -> "**Add Auto Payout**."

Select Ivanpay from the dropdown menu in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/Arc_OcgFEcjunz.png" alt="" width="426"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (293).png" alt="" width="421"><figcaption></figcaption></figure>

**Domain** — the merchant domain you previously copied from the "**Your API Address**" field in your merchant account.

**API Key** — the API key provided to you by your Ivanpay manager.

## Special Fields

<figure><img src="../../../.gitbook/assets/выплата1.png" alt="" width="398"><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/выплата2.png" alt="" width="399"><figcaption></figcaption></figure>

**Payment Method** — select the desired method for making payouts.

{% hint style="warning" %}
Please note a particular feature of the Ivanpay service — **whenever possible**, payouts are made from a bank card of the bank you selected in the module settings. However, if no cards from the selected bank are available, the payout will be made from a card of another bank currently available in the service. The payout method itself does not change and remains the original one — either CARD or SBP.
{% endhint %}

When using the **\[SBP] SBP** method (without specifying a bank), you need to pass the merchant the name of the bank that the client will select in the exchange form.

To do this, create a new custom field in the "**Currencies**" section → "**Additional currency fields**" and configure it as shown in the screenshot below:

<figure><img src="../../../.gitbook/assets/image (1937).png" alt="" width="412"><figcaption></figcaption></figure>

List of banks to include in the "**Options**" field for different language versions:

{% tabs %}
{% tab title="For the Russian version" %}
Альфа-Банк  
СберБанк  
Т-Банк  
РНКБ  
Открытие  
Русский Стандарт  
Авангард  
Райффайзен  
Газпромбанк  
Почта банк  
Россельхозбанк  
РОСБАНК  
Промсвязьбанк  
МТС Банк  
Совкомбанк  
Банк Уралсиб  
ОТП банк  
ВТБ  
Ак Барс Банк  
Ozon Банк  
Банк УБРиР  
Экспобанк  
Банк ЗЕНИТ  
Примсоцбанк  
ЮниКредит Банк  
АО КБ ЮНИСТРИМ  
Яндекс Банк  
Банк Левобережный  
{% endtab %}

{% tab title="For the English version" %}
Alfa-Bank  
SberBank  
T-Bank  
RNCB Bank  
Otkritie  
Russian Standard  
Bank Avangard  
Raiffeisenbank  
Gazprombank  
Pochta Bank  
Rosselkhozbank  
ROSBANK  
Promsvyazbank  
MTS Bank  
Sovcombank  
Bank Uralsib  
OTP Bank  
VTB Bank  
Ak Bars Bank  
Ozon Bank  
UBRiR Bank  
Expobank  
Zenit Bank  
Primsotsbank  
UniCredit Bank  
UNISTREAM Commercial Bank  
Yandex Bank  
Levoberezhny Bank  
{% endtab %}
{% endtabs %}

Next, add the custom field for the currency selected for payout in this exchange direction within the field’s own settings:

<figure><img src="../../../.gitbook/assets/image (289).png" alt="" width="386"><figcaption></figcaption></figure>

Or in the currency settings under the "**Additional fields**" tab:

<figure><img src="../../../.gitbook/assets/image (288).png" alt="" width="366"><figcaption></figcaption></figure>

Save your changes.

After that, the field will appear in the exchange form, and the client will be required to select one of the options when creating a request.

<figure><img src="../../../.gitbook/assets/image (290).png" alt="" width="521"><figcaption></figcaption></figure>

## Continuing the setup

Then proceed with configuring the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-merchantov-avtovyplat).