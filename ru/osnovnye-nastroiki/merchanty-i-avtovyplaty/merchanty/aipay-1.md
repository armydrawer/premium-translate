# Optimoney

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat)
{% endhint %}

## Настройки в личном кабинете мерчанта

{% hint style="warning" %}
Для обсуждения условий работы свяжитесь с представителем сервиса.

**Дисклеймер**: при подключении вашего сайта к тому или иному сервису, пожалуйста, самостоятельно оценивайте возможные риски сотрудничества.
{% endhint %}

Зарегистрируйтесь на сервисе [Optimoney](https://client.optimoney.com/register). Авторизуйтесь в личном кабинете

<figure><img src="../../../.gitbook/assets/image (2242).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (2241).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (2240).png" alt=""><figcaption></figcaption></figure>

## Настройки модуля

В панели администратора создайте нового мерчанта в разделе "**Мерчанты**" ➔ "**Добавить мерчант".**

Выберите Optimoney в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../.gitbook/assets/image (2238).png" alt=""><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/image (2239).png" alt=""><figcaption></figcaption></figure>

**Домен** — оставьте поле пустым

**API ключ** — API ключ, переданный вам ранее представителем Optimoney

**Секретный ключ** — API ключ, переданный вам ранее представителем Optimoney

**ID мерчанта** — API ключ, переданный вам ранее представителем Optimoney

**API ключ мерчанта** — API ключ, переданный вам ранее представителем Optimoney

## Особые поля

{% hint style="warning" %}
При приеме средств с использованием мерчанта Optimoney **необходимо** добавить дополнительные поля в форму обмена для заполнения его клиентом при создании заявки.

Для этого создайте и добавьте [дополнительные поля](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/valyuty-i-napravleniya/dobavlenie-novoi-valyuty#vkladka-dop.-polya) к соответствующим валютам для приёма средств через AI-pay.

Обязательно укажите переменную в поле "**Уникальный ID**" (указывайте название в нижнем регистре) и сделайте поле обязательным к заполнению.

#### 1. Поле для имени держателя карты (при использовании метода "**Карта**" или "**Счет**")

* **Уникальный ID**: `give_cardholder`/`cardholder` &#x20;

![](https://premium.gitbook.io/main/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FyBUMmdMiMlEvL4OlAoxr%252Fimage.png%3Falt%3Dmedia%26token%3D9669cfff-79cc-49fb-a222-50ecccb3fa5e\&width=300\&dpr=4\&quality=100\&sign=50a9f19f\&sv=2)

* **Назначение**: Полное имя держателя карты/счета
*   **Приоритет обработки (можно выбрать любой вариант)**:

    1. `give_cardholder`  или `cardholder`  (приоритетное поле)
    2. Автоматическое формирование из ФИО клиента (`last_name + first_name + second_name`) — стандартные поля "**Фамилия**", "**Имя**", "**Отчество**" для направления обмена (не валюты!)
    3. После этого поле будет отображаться в форме обмена, а также будет обязательным к заполнению клиентом при создании заявки.

    ![](https://premium.gitbook.io/main/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FcoBFe70zmN1JtepEFM68%252Fimage.png%3Falt%3Dmedia%26token%3Da5a19b16-bc6f-425d-89ed-bb07c7065e00\&width=300\&dpr=4\&quality=100\&sign=d8ed43c6\&sv=2)

#### 2. Поле для номера телефона (при использовании метода "**Телефон**")

* **Уникальный ID**: `give_phone`/`phone`&#x20;
* **Назначение**: номер телефона клиента
* **Приоритет обработки (можно выбрать любой вариант)**:
  1. `give_phone` или `phone` (приоритетное поле)
  2. `user_phone` из основных данных заявки — стандартное поле "**Телефон**" для направления обмена (не валюты!)
{% endhint %}

## Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).\
