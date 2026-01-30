# Quixfer

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat)
{% endhint %}

## Настройки в личном кабинете мерчанта

{% hint style="warning" %}
Для обсуждения условий работы свяжитесь с [представителем сервиса](https://t.me/quixfer).

**Дисклеймер**: при подключении вашего сайта к тому или иному сервису, пожалуйста, самостоятельно оценивайте возможные риски сотрудничества.
{% endhint %}

[Зарегистрируйтесь](https://quixfer.cc/#contacts) на сервисе Quixfer, авторизуйтесь в личном кабинете и перейдите в раздел "**Settings**" ➔ "**Security**".

<figure><img src="../../../.gitbook/assets/image (4) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="375"><figcaption></figcaption></figure>

Сгенерируйте API-ключи и сохраните их в текстовый файл.

<figure><img src="../../../.gitbook/assets/image (5) (1) (1) (1) (1) (1).png" alt="" width="375"><figcaption></figcaption></figure>

## Настройки модуля

В панели администратора создайте нового мерчанта в разделе "**Мерчанты**" ➔ "**Добавить мерчант".**

Выберите Quixfer в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="486"><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="460"><figcaption></figcaption></figure>

**Домен** — оставьте поле пустым

**API ключ** — Public Key из личного кабинета Quixfer, скопированный ранее

**Секретный ключ** — Private Key из личного кабинета Quixfer, скопированный ранее

## Особые поля

<figure><img src="../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

**Способ оплаты** — выберите необходимый способ оплаты для приема средств или пункт "**Автоматически**" — в этом случае реквизиты будут запрашиваться согласно xml-коду валюты из направления обмена, где подключен модуль (список методов будет отображаться только после указания корректных API-ключей для авторизации в модуле).

### Дополнительные поля

Для корректного получения реквизитов для валюты на прием, где используется Quixfer, необходимо добавить в форму обмена <mark style="color:red;">**обязательные**</mark> доп. поля. Под полем "**Способ оплаты**" отображается подсказка по необходимым полям для каждого метода оплаты.

<figure><img src="../../../.gitbook/assets/image (5) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

Создайте и добавьте [дополнительное поле](https://premium.gitbook.io/main/osnovnye-nastroiki/valyuty-i-napravleniya-obmena/dopolnitelnye-polya) к соответствующим валютам для приёма средств через Quixfer. Обязательно укажите значение в поле "**Уникальный ID**" согласно таблице выше (указывайте название в нижнем регистре) и сделайте поле обязательным к заполнению.

<figure><img src="https://premium.gitbook.io/main/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FyBUMmdMiMlEvL4OlAoxr%252Fimage.png%3Falt%3Dmedia%26token%3D9669cfff-79cc-49fb-a222-50ecccb3fa5e&#x26;width=300&#x26;dpr=4&#x26;quality=100&#x26;sign=50a9f19f&#x26;sv=2" alt="" width="375"><figcaption></figcaption></figure>

После этого поле будет отображаться в форме обмена, а также будет обязательным к заполнению клиентов при создании заявки.

<figure><img src="https://premium.gitbook.io/main/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FcoBFe70zmN1JtepEFM68%252Fimage.png%3Falt%3Dmedia%26token%3Da5a19b16-bc6f-425d-89ed-bb07c7065e00&#x26;width=300&#x26;dpr=4&#x26;quality=100&#x26;sign=d8ed43c6&#x26;sv=2" alt="" width="375"><figcaption></figcaption></figure>

Пример заполнения для валюты T-Банк RUB (выделены названия из полей "Уникальный ID"):

<figure><img src="../../../.gitbook/assets/image (2205).png" alt="" width="375"><figcaption></figcaption></figure>

Пример заполнения для валюты Bank transfer GEL (грузинский лари):

<figure><img src="../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="375"><figcaption></figcaption></figure>

## Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).<br>
