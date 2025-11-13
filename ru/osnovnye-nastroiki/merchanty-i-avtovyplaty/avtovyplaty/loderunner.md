# Loderunner

{% hint style="danger" %}
<mark style="color:red;">Перед настройкой автовыплат обязательно прочитайте</mark> [<mark style="color:blue;">предупреждение о рисках!</mark>](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/preduprezhdenie-o-riskakh)
{% endhint %}

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat)
{% endhint %}

## Настройки в личном кабинете мерчанта

{% hint style="warning" %}
Для обсуждения условий работы свяжитесь с [представителем сервиса](https://t.me/oleg6781).

**Дисклеймер**: при подключении вашего сайта к тому или иному сервису, пожалуйста, самостоятельно оценивайте возможные риски сотрудничества.
{% endhint %}

Зарегистрируйтесь на сервисе Loderunner с помощью [представителю сервиса](https://t.me/oleg6781) и запросите API-ключ для подключения к Premium Exchanger.

## Настройки модуля

В панели администратора создайте нового мерчанта в разделе "**Мерчанты**" ➔ "**Добавить автовыплату".**

Выберите Loderunner в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../.gitbook/assets/image (2218).png" alt="" width="395"><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/image (2219).png" alt="" width="432"><figcaption></figcaption></figure>

**Домен** — оставьте поле пустым

**API ключ** — API ключ, переданный вам ранее представителем Loderunner

## Особые поля

<figure><img src="../../../.gitbook/assets/image (2220).png" alt="" width="278"><figcaption></figcaption></figure>

**Статистика** — включение или отключение передачи дополнительных данных о заявке для расчетов в личном кабинете

### [Дополнительные поля](https://premium.gitbook.io/main/osnovnye-nastroiki/valyuty-i-napravleniya-obmena/dopolnitelnye-polya)

<mark style="color:red;">**Необходимо**</mark> также передавать мерчанту данные от клиента через дополнительные поля, созданные для валюты "**Получаю**". Для этого создайте доп. поля и отметьте их галочкой в настройках валюты. Когда клиент будет заполнять эти поля в форме обмена при создании заявки, данные из них будут передаваться мерчанту.

Указывайте название из списка ниже в поле "**Уникальный ID**" (остальные поля заполняются по вашему усмотрению) для каждого дополнительного поля.

<figure><img src="https://premium.gitbook.io/main/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FAUKYMBIlttlhEVWigqYZ%252Fimage.png%3Falt%3Dmedia%26token%3D164622ad-c56b-4d07-ad97-9a918effd5eb&#x26;width=300&#x26;dpr=4&#x26;quality=100&#x26;sign=bd108799&#x26;sv=2" alt="" width="375"><figcaption></figcaption></figure>

ID для доп. полей (через `/` указаны подходящие значения для поля "**Уникальный ID**"):

* **Название банка:** `get_bankname`/`bankname`
* **Номер карты:** активация поля "**Выводить поле "На  счет"**"

<figure><img src="../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

* **ФИО держателя карты:** `get_cardholder`/`cardholder`
* **Телефон для СБП:** `get_phone`/`phone`/активация поля "**Выводить поле "На  счет"**"
* Телеграм для связи (<mark style="color:orange;">**дополнительное поле в направлении обмена, а не в валюте!**</mark>): `dir_tg`/`get_tg`/`tg`

Активация созданных доп. полей валюты "Получаю" (в скобках указан уникальный ID из одноименного поля из настроек каждого доп. поля)

<figure><img src="https://premium.gitbook.io/main/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FM842FBd18fqWCI8EaduC%252Fimage.png%3Falt%3Dmedia%26token%3D6aeff3a7-4ae6-47eb-9b88-25d17c9e146b&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=9c12e4cd&#x26;sv=2" alt="" width="563"><figcaption></figcaption></figure>

Форма обмена

<figure><img src="https://premium.gitbook.io/main/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252F3U0WTMvGp9dlw5dzwyqJ%252Fimage.png%3Falt%3Dmedia%26token%3Dee980067-efa0-407c-ad97-c1d6406cb4e4&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=26bdeb64&#x26;sv=2" alt="" width="375"><figcaption><p>Отображение доп. полей в форме обмена на сайте</p></figcaption></figure>

## Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).\
