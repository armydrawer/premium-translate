# APX



{% hint style="danger" %}
Перед настройкой автовыплат обязательно прочитайте [предупреждение о рисках!](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/preduprezhdenie-o-riskakh)
{% endhint %}

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat)
{% endhint %}

{% hint style="warning" %}
Для обсуждения условий и подключения свяжитесь с [представителем сервиса](https://t.me/apxarchi).

**Дисклеймер**: при подключении вашего сайта к тому или иному сервису, пожалуйста, самостоятельно оценивайте возможные риски сотрудничества.
{% endhint %}

Пройдите регистрацию на [сервисе APX](https://www.apx.archi/auth/signup) и авторизуйтесь в личном кабинете. Создайте новый API-ключ.

<figure><img src="../../../.gitbook/assets/изображение (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

Скопируйте сгенерированный ключ в буфер обмена или текстовый файл.

<figure><img src="../../../.gitbook/assets/изображение (5).png" alt=""><figcaption></figcaption></figure>

## Настройки модуля

В панели администратора создайте нового мерчанта в разделе "**Мерчанты**" ➔ "**Добавить автовыплату".**

<figure><img src="../../../.gitbook/assets/изображение (3) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

Выберите APX в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить".**

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/изображение (2) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

**Домен** — оставьте поле пустым

**API ключ** — ключ, скопированный в ЛК APX

## Особые поля

{% hint style="info" %}
### Дополнительные поля для заявки <a href="#dopolnitelnye-polya-dlya-zayavki" id="dopolnitelnye-polya-dlya-zayavki"></a>

При выплате средств с использованием автовыплаты APX **необходимо** добавить дополнительные поля в форму обмена для заполнения его клиентом при создании заявки.

Для этого создайте и добавьте [дополнительные поля](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/valyuty-i-napravleniya/dobavlenie-novoi-valyuty#vkladka-dop.-polya) **к соответствующим валютам** на стороне "**Получаю**" для выплаты средств через APX.

Обязательно укажите переменную в поле "**Уникальный ID**" (указывайте название в нижнем регистре) и сделайте поле обязательным к заполнению.

1. **Поле для названия банка&#x20;**<mark style="color:red;">**(обязательно)**</mark>

* **Уникальный ID**: `get_bankname`

<p align="center"><img src="../../../.gitbook/assets/изображение (235).png" alt="" data-size="original"></p>

*   **Приоритет обработки (можно выбрать любой вариант)**:

    1. Доп. поле валюты с ID `get_bankname`&#x20;
    2. Автоматическое значени&#x435;**:** код валюты "**Получаю**" (должен содержать "**RUB**" в названии)

    &#x20;

    <figure><img src="../../../.gitbook/assets/изображение (236).png" alt="" width="561"><figcaption></figcaption></figure>

2. **Поле для номера карты&#x20;**<mark style="color:red;">**(обязательно)**</mark>

* **Уникальный ID**: `get_account`
*   **Приоритет обработки (можно выбрать любой вариант)**:

    1. Доп. поле валюты с ID `get_account`&#x20;
    2. Автоматическое значение: стандартное поле "**На счет**" валюты "**Получаю**"

    <figure><img src="../../../.gitbook/assets/изображение (237).png" alt=""><figcaption></figcaption></figure>

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

      <figure><img src="../../../.gitbook/assets/изображение (238).png" alt=""><figcaption></figcaption></figure>

После этого поля будут отображаться в форме обмена, а также будет обязательным к заполнению клиентом при создании заявки.
{% endhint %}

## Продолжение настройки <a href="#prodolzhenie-nastroiki" id="prodolzhenie-nastroiki"></a>

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-merchantov-avtovyplat).
