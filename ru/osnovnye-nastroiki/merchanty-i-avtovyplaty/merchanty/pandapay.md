# PandaPay



{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat)
{% endhint %}

## Настройки в личном кабинете мерчанта

{% hint style="warning" %}
Для обсуждения условий и подключения свяжитесь с [представителем сервиса](https://t.me/PandaPaySup)

**Дисклеймер**: при подключении вашего сайта к тому или иному сервису, самостоятельно пожалуйста оценивайте возможные риски сотрудничества.
{% endhint %}

После получения реквизитов для входа от представителя сервиса, авторизуйтесь в ЛК [PandaPay](https://pandapay24.com/). Перейдите в раздел "**Настройки**".

<figure><img src="../../../.gitbook/assets/image (122).png" alt="" width="563"><figcaption></figcaption></figure>

Добавьте URL Calback в соответствующем поле.

<figure><img src="../../../.gitbook/assets/image (120).png" alt="" width="563"><figcaption></figcaption></figure>

{% hint style="success" %}
Для обновления статусов заявок укажите актуальный URL Callback в ЛК мерчанта — URL вы найдете в настройках модуля (строка "**Webhook**")

![](<../../../.gitbook/assets/image (121).png>)
{% endhint %}

Создайте новые ключи доступа и скопируйте их в буфер обмена или текстовый файл.

<figure><img src="../../../.gitbook/assets/image (119).png" alt="" width="563"><figcaption></figcaption></figure>

## Настройки модуля

В панели администратора создайте нового мерчанта в разделе "**Мерчанты**" ➔ "**Добавить мерчант".**

Выберите PandaPay в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../.gitbook/assets/image (2092).png" alt="" width="445"><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/image (2093).png" alt="" width="458"><figcaption></figcaption></figure>

**API ключ** — скопированный API ключ из ЛК мерчанта

**Секретный ключ** — скопированный секретный ключ из ЛК мерчанта

## Особые поля

<figure><img src="../../../.gitbook/assets/image (2094).png" alt="" width="456"><figcaption></figcaption></figure>

**Разрешенные страны** — список стран, для которых будет производиться поиск реквизитов.

**Если выбран пункт "ANY"**, то поиск будет производиться по всем странам.\
**Если выбран один или несколько пунктов с конкретными странами**, то поиск будет производиться только по этим странам.\
**Если не отмечен ни один пункт**, то поиск будет производиться по коду валюты "**Отдаю**" из направления обмена

**Способ оплаты** — метод поиска реквизитов:

<figure><img src="../../../.gitbook/assets/image (2097).png" alt="" width="354"><figcaption></figcaption></figure>

* **accountNumber** — номер банковского счета
* **card** — номер банковской карты
* **crossBorderTransfer** — перевод средств между странами
* **SBP** — номер телефона для перевода средств по СБП

{% hint style="info" %}
Кнопки "**Добавить**" позволяют добавлять новые методы без обновления самого модуля на сервере (используйте опции **только** если представитель мерчанта сообщил вам, что это необходимо)
{% endhint %}

## Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).<br>
