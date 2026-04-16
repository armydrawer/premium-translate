# Loderunner

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-merchantov)
{% endhint %}

{% hint style="warning" %}
Для обсуждения условий и подключения свяжитесь с [представителем сервиса](https://t.me/roinotgoall).

**Дисклеймер**: при подключении вашего сайта к тому или иному сервису, пожалуйста, самостоятельно оценивайте возможные риски сотрудничества.
{% endhint %}

{% hint style="warning" %}
Обращаем ваше внимание, что при использовании модуля на прием средств Loderunner фактическая сумма оплаты всегда округляется до 2 знаков после запятой на стороне сервиса.

Реквизиты могут быть выданы не сразу, поэтому [опция "**Ожидание реквизитов от мерчанта**"](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov#podklyuchenie-neskolkikh-merchantov) рекомендуется к выбору в настройках модуля.

![](<../../../.gitbook/assets/изображение (1).png>)
{% endhint %}

Пройдите регистрацию на сервисе Loderunner с помощью [представителя сервиса](https://t.me/roinotgoall). Получите от представителя API-ключ для работы с Premium Exchanger.

## Настройки модуля

В панели администратора создайте нового мерчанта в разделе "**Мерчанты**" ➔ "**Добавить мерчант".**

Выберите Loderunner в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../.gitbook/assets/изображение (239).png" alt=""><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/изображение (240).png" alt=""><figcaption></figcaption></figure>

**Домен** — оставьте поле пустым

**API ключ** — ключ, выданный вам представителем Loderunner

## Особые поля

{% hint style="warning" %}
При приеме средств с использованием мерчанта Loderunner **необходимо** добавить дополнительные поля в форму обмена для заполнения его клиентом при создании заявки.

Для этого создайте и добавьте [дополнительные поля](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/valyuty-i-napravleniya/dobavlenie-novoi-valyuty#vkladka-dop.-polya) к соответствующим валютам для приёма средств через Loderunner.

Обязательно укажите переменную в поле "**Уникальный ID**" (указывайте название в нижнем регистре) и сделайте поле обязательным к заполнению.

**1. Дополнительное поле для** <mark style="color:$warning;">валюты</mark> **для имени держателя карты (опционально)**

* **Уникальный ID**: `give_cardholder`

<img src="https://premium.gitbook.io/main/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FyBUMmdMiMlEvL4OlAoxr%252Fimage.png%3Falt%3Dmedia%26token%3D9669cfff-79cc-49fb-a222-50ecccb3fa5e&#x26;width=300&#x26;dpr=4&#x26;quality=100&#x26;sign=50a9f19f&#x26;sv=2" alt="" data-size="original">

*   **Приоритет обработки (можно выбрать любой вариант)**:

    1. `give_cardholder` (приоритетное поле)
    2. Автоматическое формирование из ФИО клиента (`last_name + first_name + second_name`) — стандартные поля "**Фамилия**", "**Имя**", "**Отчество**" для направления обмена (не валюты!)
    3. После этого поля будут отображаться в форме обмена, а также будут обязательными к заполнению клиентом при создании заявки.

    ![](https://premium.gitbook.io/main/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FcoBFe70zmN1JtepEFM68%252Fimage.png%3Falt%3Dmedia%26token%3Da5a19b16-bc6f-425d-89ed-bb07c7065e00\&width=300\&dpr=4\&quality=100\&sign=d8ed43c6\&sv=2)

**2. Дополнительное поле для** <mark style="color:$warning;">валюты</mark> **для номера карты (опционально)**

* **Уникальный ID**: `give_account`
* **Приоритет обработки (можно выбрать любой вариант)**:
  1. `give_account` (приоритетное поле)
  2. Поле "**Со счета"** из настроек валюты "**Отдаю**"

![](<../../../.gitbook/assets/изображение (2).png>)

**3. Дополнительное поле для** <mark style="color:$warning;">направления обмена</mark> **для номера телефона (опционально)**

* **Уникальный ID**: `give_phone`
* **Приоритет обработки (можно выбрать любой вариант)**:
  1. `give_phone` (приоритетное поле)
  2. Стандартное поле "**Телефон**" для направления обмена (не валюты!)**.**&#x20;

**4. Дополнительное поле для** <mark style="color:$warning;">направления обмена</mark> **для аккаунта Telegram (опционально)**

* **Уникальный ID**: `give_tg` /`dir_tg`
{% endhint %}

## Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).<br>
