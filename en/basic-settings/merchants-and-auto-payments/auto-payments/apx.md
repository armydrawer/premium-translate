# APX

{% hint style="danger" %}
Before setting up automatic payouts, please read the [risk warning!](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/preduprezhdenie-o-riskakh)
{% endhint %}

{% hint style="info" %}
If you need to update the module on the server, please refer to the [instructions](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat).
{% endhint %}

{% hint style="warning" %}
For discussions regarding terms and connection, please contact a [service representative](https://t.me/apxarchi).

**Disclaimer**: When connecting your website to any service, please assess the potential risks of collaboration on your own.
{% endhint %}

Register on the [APX service](https://www.apx.archi/auth/signup) and log in to your personal account. Create a new API key.

<figure><img src="../../../.gitbook/assets/изображение.png" alt=""><figcaption></figcaption></figure>

Copy the generated key to your clipboard or text file.

<figure><img src="../../../.gitbook/assets/изображение (242).png" alt=""><figcaption></figcaption></figure>

## Module Settings

In the admin panel, create a new merchant in the "**Merchants**" ➔ "**Add Automatic Payout**" section.

<figure><img src="../../../.gitbook/assets/изображение (3).png" alt=""><figcaption></figcaption></figure>

Select APX from the dropdown menu in the "**Module**" field, enter a name for the module, and click "**Save**."

Fill in the required authorization fields.

<figure><img src="../../../.gitbook/assets/изображение (2).png" alt=""><figcaption></figcaption></figure>

**Domain** — leave this field empty.

**API key** — a key copied in the APX personal account

## Special fields

{% hint style="info" %}
### Дополнительные поля для заявки <a href="#dopolnitelnye-polya-dlya-zayavki" id="dopolnitelnye-polya-dlya-zayavki"></a>

When paying out funds using APX autopayout, you **need** to add additional fields to the exchange form for the client to fill it out when creating an application.

To do this, create and add additional fields **to the corresponding currencies** on the '**Receiving**' side for payouts via APX.

Be sure to specify the variable in the '**Unique ID**' field (specify the name in lowercase) and make the field mandatory.

1. **Bank name field&#x20;**<mark style="color:red;">**(required)**</mark>

* **Unique ID:** `get_bankname`

<p align="center"><img src="../../../.gitbook/assets/изображение (243).png" alt="" data-size="original"></p>

* **Processing priority (you can choose any option):**

1. Add. Currency field with ID `get_bankname`
2. Auto value: currency code '**Receiving**' (must contain '**RUB**' in the name)

<img src="../../../.gitbook/assets/изображение (244).png" alt="" data-size="original">

2. **Card number field&#x20;**<mark style="color:red;">**(required)**</mark>

* Unique ID: `get_account`
* Processing priority (you can choose any option):

1. Add. Currency field with ID `get_account`
2. Automatic value: standard '**To account**' field of the currency '**Receiving**'

<img src="../../../.gitbook/assets/изображение (245).png" alt="" data-size="original">

3. **Поле для имени держателя карты&#x20;**<mark style="color:yellow;">**(опционально)**</mark>

* **Уникальный ID**: `get_cardholder`/`cardholder`
* **Приоритет обработки (можно выбрать любой вариант)**:
  1. Доп. поле валюты с ID `get_cardholder`&#x20;
  2. Автоматическое формирование из ФИО клиента (`last_name + first_name + second_name`) — стандартные поля "**Фамилия**", "**Имя**", "**Отчество**" для **направления обмена (не валюты!)**

4. **Поле для номера телефона&#x20;**<mark style="color:yellow;">**(опционально)**</mark>

* **Уникальный ID**: `get_phone`
* **Приоритет обработки (можно выбрать любой вариант)**:
  1. Доп. поле валюты с ID `get_phone`&#x20;
  2.  Стандартное доп. поле "**Телефон**" **для направления обмена (не валюты!)** с + как первым символом в форме для заполнения<br>

      <figure><img src="../../../.gitbook/assets/изображение (246).png" alt=""><figcaption></figcaption></figure>

После этого поля будут отображаться в форме обмена, а также будет обязательным к заполнению клиентом при создании заявки.
{% endhint %}

## Continue Configuration <a href="#prodolzhenie-nastroiki" id="prodolzhenie-nastroiki"></a>

Next, configure the merchant by following the [general setup instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-merchantov-avtovyplat).
