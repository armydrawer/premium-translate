# Ivanpay

{% hint style="danger" %}
<mark style="color:red;">Before setting up auto payouts, please read the</mark> [<mark style="color:blue;">risk warning</mark>](https://premium.gitbook.io/main/en/basic-settings/merchants-and-auto-payments/auto-payments/risk-warning)<mark style="color:blue;">!</mark>
{% endhint %}

{% hint style="info" %}
If you need to update the module on the server, please refer to the [instructions](https://premium.gitbook.io/main/en/en/basic-settings/faq/updating-script-files-on-the-server/how-to-update-files-on-the-server#merchant-and-auto-payout-modules).
{% endhint %}

## Merchant Account Settings <a href="#nastroiki-v-lichnom-kabinete-merchanta" id="nastroiki-v-lichnom-kabinete-merchanta"></a>

{% hint style="warning" %}
To discuss terms and connection, please contact a [service representative](https://t.me/IvanPay_pro).

**Disclaimer**: When connecting your website to any service, please assess the potential risks of collaboration on your own.
{% endhint %}

Register on the [IvanPay](https://ivanpay.com/) service.

In your merchant account, copy the information from the "**Your API Address**" field, as well as the API key provided to you by the service representative.

## Module Settings <a href="#nastroiki-modulya" id="nastroiki-modulya"></a>

In the admin panel, create a new merchant in the "**Auto Payouts**" section by clicking "**Add Auto Payout**."

Select Ivanpay from the dropdown menu in the "**Module**" field, enter a name for the module, and click "**Save**."

<figure><img src="../../../.gitbook/assets/Arc_OcgFEcjunz (1).png" alt="" width="426"><figcaption></figcaption></figure>

Fill in the required authorization fields.

**Domain** — the merchant's domain, previously copied from the merchant account in the "**Your API Address**" field.

**API Key** — the **API Key** provided to you by your Ivanpay manager.

## Special Fields

<figure><img src="../../../.gitbook/assets/выплата1 (1).png" alt="" width="398"><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/выплата2 (1).png" alt="" width="399"><figcaption></figcaption></figure>

**Payment Method** — select the required method for fund payouts.

{% hint style="warning" %}
Please note the unique feature of the Ivanpay service — **whenever possible**, payouts are made from the card of the bank you selected in the module settings. However, if there are no cards from the selected bank, the payout will be made from a card of another bank that is currently available on the service (the method remains unchanged and is either CARD or SBP).
{% endhint %}

When using the **\[SBP] SBP** method (without specifying a bank), you need to provide the merchant with the name of the bank that the client will select in the exchange form.

To do this, create a new additional field in the "**Currencies**" -> "**Additional Currency Fields**" section and configure it according to the screenshot below:

<figure><img src="../../../.gitbook/assets/image (1937)_eng.png" alt="" width="412"><figcaption></figcaption></figure>

The list of banks to be specified in the "**Options**" field for different language versions:

{% tabs %}
{% tab title="For the ru-version" %}
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

{% tab title="For the en-version" %}
Alfa-Bank

SberBank

T-Bank

RNCB Bank

Otkritie

Russian Standard

Bank AVANGARD

Raiffeisenbank

Gazprombank

Pochta Bank

Rosselkhozbank

ROSBANK

Promsvyazbank

MTS Bank

Sovcombank

Bank Uralsib

Bank VTB

Bank AK BARS

Bank OZON

Bank UBRD - Ural

Bank Expobank

Bank ZENIT

Primsotsbank

UniCredit Bank

UNISTREAM COMMERCIAL BANK

Yandex Bank

Bank Levoberezhny
{% endtab %}
{% endtabs %}

After that, add the additional field for the currency selected for payout in this exchange direction in the field settings:

Or in the currency settings under the "**Additional Fields**" tab:

Save the changes.

After this, the field will be displayed in the exchange form, and the client will need to select one of the options when creating a request.

## Continuing the Setup

Next, proceed to configure the merchant by following the [general setup instructions](https://premium.gitbook.io/main/en/basic-settings/merchants-and-auto-payments/auto-payments/obshie-nastroiki-merchantov-avtovyplat).
