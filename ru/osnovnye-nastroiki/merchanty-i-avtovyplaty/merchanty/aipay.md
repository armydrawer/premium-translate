# AI-pay

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat)
{% endhint %}

## Настройки в личном кабинете мерчанта

{% hint style="warning" %}
Для обсуждения условий работы свяжитесь с [представителем сервиса](https://t.me/AI_pay_kirill).

**Дисклеймер**: при подключении вашего сайта к тому или иному сервису, пожалуйста, самостоятельно оценивайте возможные риски сотрудничества.
{% endhint %}

Зарегистрируйтесь на сервисе AI-pay с помощью [представителя сервиса](https://t.me/AI_pay_kirill) и запросите API-ключи для подключения к Premium Exchanger.

## Настройки модуля

В панели администратора создайте нового мерчанта в разделе "**Мерчанты**" ➔ "**Добавить мерчант".**

Выберите AI-pay в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../.gitbook/assets/image (7) (1).png" alt="" width="329"><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="338"><figcaption></figcaption></figure>

**Домен** — оставьте поле пустым

**API UID** — идентификатор, переданный вам ранее представителем AI-pay

**API ключ** — API ключ, переданный вам ранее представителем AI-pay

## Особые поля

<figure><img src="../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

**Способ оплаты** — выберите необходимый способ для приема средств от клиента:

**Карта** — выдача реквизитов банковской карты

**Счет** — выдача номера банковского счета

**Телефон** — выдача номера телефона для приема средств по СБП

{% hint style="warning" %}
При приеме средств с использованием мерчанта AI-pay **необходимо** добавить дополнительные поля в форму обмена для заполнения его клиентом при создании заявки.

Для этого создайте и добавьте [дополнительные поля](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/valyuty-i-napravleniya/dobavlenie-novoi-valyuty#vkladka-dop.-polya) к соответствующим валютам для приёма средств через AI-pay.

Обязательно укажите переменную в поле "**Уникальный ID**" (указывайте название в нижнем регистре) и сделайте поле обязательным к заполнению.

**1. Дополнительное поле для&#x20;**<mark style="background-color:blue;">**валюты**</mark>**&#x20;для имени держателя карты (при использовании метода "Карта" или "Счет")**

* **Уникальный ID**: `give_cardholder`/`cardholder`

<img src="https://premium.gitbook.io/main/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FyBUMmdMiMlEvL4OlAoxr%252Fimage.png%3Falt%3Dmedia%26token%3D9669cfff-79cc-49fb-a222-50ecccb3fa5e&#x26;width=300&#x26;dpr=4&#x26;quality=100&#x26;sign=50a9f19f&#x26;sv=2" alt="" data-size="original">

* **Назначение**: Полное имя держателя карты/счета
*   **Приоритет обработки (можно выбрать любой вариант)**:

    1. `give_cardholder` или `cardholder` (приоритетное поле)
    2. Автоматическое формирование из ФИО клиента (`last_name + first_name + second_name`) — стандартные поля "**Фамилия**", "**Имя**", "**Отчество**" для направления обмена (не валюты!)
    3. После этого поля будут отображаться в форме обмена, а также будут обязательными к заполнению клиентом при создании заявки.

    ![](https://premium.gitbook.io/main/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FcoBFe70zmN1JtepEFM68%252Fimage.png%3Falt%3Dmedia%26token%3Da5a19b16-bc6f-425d-89ed-bb07c7065e00\&width=300\&dpr=4\&quality=100\&sign=d8ed43c6\&sv=2)

**2. Дополнительное поле для&#x20;**<mark style="background-color:blue;">**направления обмена**</mark>**&#x20;для номера телефона (при использовании метода "Телефон")**

* **Уникальный ID**: `give_phone`/`phone` /`give_account`/`account`
* **Назначение**: номер телефона клиента
* **Приоритет обработки (можно выбрать любой вариант)**:
  1. `give_phone`/`phone` /`give_account`/`account` (приоритетное поле)
  2. Поле "**Со счета**" из настроек валюты "**Отдаю**"

<img src="../../../.gitbook/assets/image (2254).png" alt="" data-size="original">
{% endhint %}

## Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).<br>
