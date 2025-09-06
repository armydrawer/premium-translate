# ArchEx

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat)
{% endhint %}

## Настройки в личном кабинете мерчанта

{% hint style="warning" %}
Для получения h2h-ключа, который необходим для авторизации в модуле, свяжитесь с [представителем сервиса](https://t.me/archex_headsupport) (после регистрации на сервисе напишите ему, что вам нужен h2h ключ для скрипта Premium Exchanger)

**Дисклеймер**: при подключении вашего сайта к тому или иному сервису оценивайте, пожалуйста, самостоятельно возможные риски сотрудничества.
{% endhint %}

[Зарегистрируйтесь на сервисе](https://dash.archex.io/signin/) и авторизуйтесь в личном кабинете. Создайте новый проект.

<figure><img src="../../../.gitbook/assets/image (2095).png" alt=""><figcaption></figcaption></figure>

Заполните указанные данные и выберите пункт "**Merchant**" в выпадающем списке "**Модуль**".

<figure><img src="../../../.gitbook/assets/image (2096).png" alt=""><figcaption></figcaption></figure>

В настройках профиля скопируйте API токен (это **API токен профиля)**.

<figure><img src="../../../.gitbook/assets/image (2100).png" alt=""><figcaption></figcaption></figure>

Перейдите в настройки проекта. Для работы коллбэка для изменения статуса заявки укажите URL из настроек модуля мерчанта в настройках проекта и добавьте в вайтлист вашего файрвола все IP-адреса мерчанта, с которых они отправляют коллбэки (список адресов запрашивайте напрямую у мерчанта).

Скопируйте API токен с этой же страницы (это **API токен проекта**).

<figure><img src="../../../.gitbook/assets/image (2099).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (2097).png" alt=""><figcaption></figcaption></figure>

Отметьте методы, которые планируете использовать.

<figure><img src="../../../.gitbook/assets/image (2098).png" alt=""><figcaption></figcaption></figure>

## Настройки модуля

В панели администратора создайте нового мерчанта в разделе "**Мерчанты**" -> "**Добавить мерчант".**

Выберите ArchEx в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../.gitbook/assets/image (2093).png" alt="" width="464"><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/image (2092).png" alt="" width="458"><figcaption></figcaption></figure>

**API токен профиля** — API токен профиля, скопированный ранее в ЛК мерчанта

**API токен проекта** — API токен проекта, скопированный ранее в ЛК мерчанта

**Host2Host ключ** — ключ, выданный вам [представителем мерчанта](https://t.me/archex_headsupport)

## Особые поля

<figure><img src="../../../.gitbook/assets/image (2094).png" alt="" width="389"><figcaption></figcaption></figure>

**Способ оплаты** — выберите подходящий способ для приема средств от клиента

{% hint style="warning" %}
Для каждого используемого способа оплаты необходимо создать отдельную копию модуля мерчанта, в которой выбрать соответствующий способ, а затем подключить эту копию на вкладке "**Мерчанты и выплаты**" в настройках направления обмена, где в валюте "**Отдаю**" будет подходящая валюта
{% endhint %}

## Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).\
