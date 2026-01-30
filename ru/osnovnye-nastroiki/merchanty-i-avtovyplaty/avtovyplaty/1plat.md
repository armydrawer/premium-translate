# 1Plat



{% hint style="danger" %}
Перед настройкой автовыплат обязательно прочитайте [предупреждение о рисках!](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/preduprezhdenie-o-riskakh)
{% endhint %}

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat)
{% endhint %}

{% hint style="warning" %}
Для обсуждения условий и подключения свяжитесь с представителем сервиса.

**Дисклеймер**: при подключении вашего сайта к тому или иному сервису, пожалуйста, самостоятельно оценивайте возможные риски сотрудничества.
{% endhint %}

{% hint style="warning" %}
Обращаем ваше внимание, что при использовании модуля автовыплаты Finora фактическая сумма выплаты всегда округляется до двух знаков после запятой на стороне сервиса.
{% endhint %}

Пройдите регистрацию на сервисе [1Plat](https://1plat.money/user/reg) и авторизуйтесь в личном кабинете. Создайте новый магазин

<figure><img src="https://premium.gitbook.io/main/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FDcA3ojce9SPst39S6liy%252Fimage.png%3Falt%3Dmedia%26token%3D87c1b7d6-0980-4944-b0ff-bf2f840fbea6&#x26;width=768&#x26;dpr=3&#x26;quality=100&#x26;sign=12a57ed4&#x26;sv=2" alt="" width="563"><figcaption></figcaption></figure>

Заполните данные в новом окне и сохраните их.

<figure><img src="https://premium.gitbook.io/main/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FEG8wFY7cWtrWH0caX989%252Fimage.png%3Falt%3Dmedia%26token%3D8f60df99-964e-4da2-9a7b-154381ad686b&#x26;width=768&#x26;dpr=3&#x26;quality=100&#x26;sign=32ccf277&#x26;sv=2" alt="" width="375"><figcaption></figcaption></figure>

## Настройки модуля

В панели администратора создайте нового мерчанта в разделе "**Мерчанты**" ➔ "**Добавить автовыплату".**

Выберите 1Plat в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../.gitbook/assets/изображение (2) (1).png" alt="" width="378"><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/изображение (2) (1) (1).png" alt="" width="409"><figcaption></figcaption></figure>

**Логин (ЛК)** — логин от вашего ЛК в Finora

**OTP ключ (ЛК)** — OTP-ключ, выданный вам менеджером Finora

**Логин (SSO выплата)** — логин, выданный вам менеджером Finora

**OTP ключ (SSO выплата)** — OTP-ключ, выданный вам менеджером Finora

**Приватный ключ** — приватный ключ, из вашего ЛК в Finora (выпускается по инструкции ниже)

{% hint style="warning" %}
Перед началом работы вам нужно сгенерировать публичный ключ (**Public key**), который следует сохранить в ЛК платежной системы (**Security - Your Public Key**), а приватный ключ (**Private key**) в настройках модуля в поле "**Приватный ключ**"

![](<../../../.gitbook/assets/изображение (198).png>)

Для удобства работы пара ключей автоматически генерируется для работы с мерчантом (для корректной работы генератора ключей на сервере должна быть запущена служба/расширение **Sodium**). Скопируйте эти ключи из настроек модуля автовыплаты и вставьте их в соответствующие поля согласно инструкции выше.

![](<../../../.gitbook/assets/изображение (194).png>)
{% endhint %}

## Особые поля

<figure><img src="../../../.gitbook/assets/изображение (3).png" alt=""><figcaption></figcaption></figure>

**Способ оплаты** — выберите подходящий метод из списка

{% hint style="info" %}
## Дополнительные поля для заявки

При выплате средств с использованием автовыплаты 1Plat **необходимо** добавить дополнительные поля в форму обмена для заполнения его клиентом при создании заявки.

Для этого создайте и добавьте [дополнительные поля](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/valyuty-i-napravleniya/dobavlenie-novoi-valyuty#vkladka-dop.-polya) к соответствующим валютам для выплаты средств через 1Plat.

Обязательно укажите переменную в поле "**Уникальный ID**" (указывайте название в нижнем регистре) и сделайте поле обязательным к заполнению.

**1. Поле для имени держателя карты (при использовании метода "Card")**

* **Уникальный ID**: `get_cardholder`/`cardholder`

<img src="../../../.gitbook/assets/image (2235).png" alt="" data-size="original">

* **Назначение**: Полное имя держателя карты/счета
*   **Приоритет обработки (можно выбрать любой вариант)**:

    1. `get_cardholder` или `cardholder` (приоритетное поле)
    2. Автоматическое формирование из ФИО клиента (`last_name + first_name + second_name`) — стандартные поля "**Фамилия**", "**Имя**", "**Отчество**" для направления обмена (не валюты!)
    3. После этого поле будет отображаться в форме обмена, а также будет обязательным к заполнению клиентом при создании заявки.

    <figure><img src="../../../.gitbook/assets/image (2236).png" alt="" width="434"><figcaption></figcaption></figure>

**2. Поле для номера телефона (при использовании метода "Телефон")**

* **Уникальный ID**: `get_phone`/`phone`
* **Назначение**: номер телефона клиента
* **Приоритет обработки (можно выбрать любой вариант)**:
  1. `get_phone` или `phone` (приоритетное поле)
  2. `user_phone` из основных данных заявки — стандартное поле "**Телефон**" для направления обмена (не валюты!)

**3. Поле для названия банка (при использовании метода "Карта" или "Счет") — опционально**

* **Уникальный ID**: `get_bankname`/`bankname`
* **Назначение**: номер телефона клиента
* **Приоритет обработки (можно выбрать любой вариант)**:
  1. `get_bankname`или `bankname` (приоритетное поле)
  2. **Автоматическое значение:** Телефон пользователя из заявки (`user_phone`), либо из поля `account_get` (если указан телефон как реквизит)
{% endhint %}

Для работы модуля автовыплаты без использования [задания cron](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-sozdat-zadanie-cron-na-servere), укажите ссылку из настроек модуля

<figure><img src="../../../.gitbook/assets/изображение (197).png" alt=""><figcaption></figcaption></figure>

&#x20;в ЛК Finora в поле **PayOut Webhook**:

<figure><img src="../../../.gitbook/assets/изображение (196).png" alt=""><figcaption></figcaption></figure>

## Продолжение настройки <a href="#prodolzhenie-nastroiki" id="prodolzhenie-nastroiki"></a>

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-merchantov-avtovyplat).
