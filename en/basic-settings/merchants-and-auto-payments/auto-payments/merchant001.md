# Merchant001

{% hint style="danger" %}
<mark style="color:red;">Before setting up auto payouts, please read the</mark> [<mark style="color:blue;">risk warning</mark>](https://premium.gitbook.io/main/en/basic-settings/merchants-and-auto-payments/auto-payments/risk-warning)<mark style="color:blue;">!</mark>
{% endhint %}

{% hint style="info" %}
If you need to update the module on the server, please refer to the [instructions](https://premium.gitbook.io/main/en/en/basic-settings/faq/updating-script-files-on-the-server/how-to-update-files-on-the-server#merchant-and-auto-payout-modules).
{% endhint %}

## Merchant Account Settings

{% hint style="warning" %}
To discuss terms and connection, please contact a [service representative](https://t.me/merch001online).

**Disclaimer**: When connecting your website to any service, please assess the potential risks of collaboration on your own.
{% endhint %}

In your [merchant account](https://app.merchant001.io/merchant/api), generate a token for API authorization and copy it to your clipboard or save it in a text file.

<figure><img src="../../../.gitbook/assets/image (1717)_eng.png" alt=""><figcaption></figcaption></figure>

## **Module Settings**

In the admin panel, create a new merchant in the "**Auto Payouts**" -> "**Add Auto Payout**" section.

Select Merchant001 from the dropdown list in the "**Module**" field, provide a name for the module, and click "**Save**".

<figure><img src="../../../.gitbook/assets/image (1628)_eng.png" alt="" width="449"><figcaption></figcaption></figure>

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/image (1629)_eng.png" alt="" width="491"><figcaption></figcaption></figure>

**Token** — the domain generated in the Merchant001 account after creating API access.

## Special Fields

<figure><img src="../../../.gitbook/assets/image (1630)_eng.png" alt="" width="430"><figcaption></figcaption></figure>

**Payment Method** — available payout options (when making a payout, your merchant account will convert from USDT to RUB at the market rate).

When using the "**Transfer via SBP**" method, you must provide the merchant with the bank name that the client will select in the exchange form.

{% hint style="success" %}
If you are using a currency that already includes the bank name in its title (for example, **SBP T-Bank** or **SBP Sber**) — creating an additional field is <mark style="color:green;">**not required**</mark> (the currency name will be passed automatically). In all other cases, creating an additional field is necessary.
{% endhint %}

To do this, create a new additional field in the "**Currencies**" -> "**Additional Currency Fields**" section and configure it according to the screenshot below:

<figure><img src="https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FEbpC5wuOdzNjbcWl6uMw%252Fimage_eng.png%3Falt%3Dmedia%26token%3Df492a8b8-4299-4c37-8fb4-281b702e4a07&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=cc43be2f&#x26;sv=1" alt="" width="563"><figcaption></figcaption></figure>

Here is a list of banks to include in the "**Options**" field for different language versions:

{% tabs %}
{% tab title="For ru-version" %}
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

{% tab title="For en-version" %}
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

After that, add the additional field for the currency selected for payout in this exchange direction in the settings of the field itself:

<figure><img src="https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FdpeqgjfYafIq473jYRtm%252Fimage_eng.png%3Falt%3Dmedia%26token%3D8a4d7e3a-43ad-41ad-ab33-85685cc48b56&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=6b7a4abe&#x26;sv=1" alt="" width="375"><figcaption></figcaption></figure>

Or in the currency settings under the "**Additional Fields**" tab:

<figure><img src="https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252F95K4xQBIe6IxZomKPUAn%252Fimage_eng.png%3Falt%3Dmedia%26token%3D33e8957f-3ee1-4075-8d13-12897756eacb&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=788cd580&#x26;sv=1" alt="" width="375"><figcaption></figcaption></figure>

Save the changes.

After this, the field will appear in the exchange form, and the client will need to select one of the options when creating a request.

<figure><img src="https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252F7UGhEmtrSnAHov7P8Z89%252Fimage_eng.png%3Falt%3Dmedia%26token%3D6fcc59ea-b292-4803-8b6f-c547a73b4fe5&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=5f0e9aa&#x26;sv=1" alt="" width="375"><figcaption></figcaption></figure>

## Continuing the Setup

Next, proceed to configure the merchant by following the [general setup instructions](https://premium.gitbook.io/main/en/basic-settings/merchants-and-auto-payments/auto-payments/obshie-nastroiki-merchantov-avtovyplat).