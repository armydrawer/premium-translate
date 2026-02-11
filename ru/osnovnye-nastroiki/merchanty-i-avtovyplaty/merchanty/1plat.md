# 1Plat

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-merchantov)
{% endhint %}

{% hint style="warning" %}
Для обсуждения условий и подключения свяжитесь с представителем сервиса.

**Дисклеймер**: при подключении вашего сайта к тому или иному сервису, пожалуйста, самостоятельно оценивайте возможные риски сотрудничества.
{% endhint %}

{% hint style="warning" %}
Обращаем ваше внимание, что при использовании модуля на прием средств 1Plat фактическая сумма оплаты всегда округляется до 0 знаков после запятой на стороне сервиса.
{% endhint %}

Пройдите регистрацию на сервисе [1Plat](https://1plat.money/user/reg) и авторизуйтесь в личном кабинете. Создайте новый магазин

<figure><img src="../../../.gitbook/assets/image (118).png" alt="" width="563"><figcaption></figcaption></figure>

Заполните данные в новом окне и сохраните их.

<figure><img src="../../../.gitbook/assets/image (209).png" alt="" width="424"><figcaption></figcaption></figure>

## Настройки модуля

В панели администратора создайте нового мерчанта в разделе "**Мерчанты**" ➔ "**Добавить мерчант".**

Выберите 1Plat в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

**Домен** — оставьте поле пустым

**ID магазина** — ID вашего магазина на сервисе 1Plat

<figure><img src="../../../.gitbook/assets/image (50).png" alt=""><figcaption></figcaption></figure>

**Секретный ключ** — ключ, скопированный в разделе "Магазин - Настройки" в ЛК 1Plat

<figure><img src="../../../.gitbook/assets/image (22).png" alt=""><figcaption></figcaption></figure>

## Особые поля

<figure><img src="../../../.gitbook/assets/image (9).png" alt=""><figcaption></figcaption></figure>

**Тип мерчанта** (выбранный пункт закрепляется за модулем, изменить его в дальнейшем не получится):

* **Payment Link** — возвращает в заявке ссылку для оплаты, опция работает совместно с выбранным способом оплаты
* **Requisites** — возвращает реквизиты для перевода средств в самой заявке через шорткод \[to\_account]

<figure><img src="../../../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

**Способ оплаты** — выберите подходящий метод из списка или укажите вручную свой вариант в поле "**Добавить**" (допустимые варианты уточняйте у менеджера 1Plat).

Способ работает только при выбранном типе мерчанта "**Payment Link**":

**qr** — выдача QR-кода

Способ работает только при выбранном типе мерчанта "**Requisites**":&#x20;

**alfa** — выдача реквизитов Альфа-Банка

**card** — выдача номер карты любого банка

**mobile** — выдача номера телефона для оплаты

**sbp** — выдача номер телефона для оплаты по СБП

{% hint style="info" %}
![](https://premium.gitbook.io/main/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252Fgit-blob-9c7c3991793897a1f0aa1328c54be13c30991283%252Fimage.png%3Falt%3Dmedia\&width=300\&dpr=3\&quality=100\&sign=5caf9bc3\&sv=2)
{% endhint %}

{% hint style="danger" %}
Обращаем ваше внимание, что для каждого метода необходимо создавать отдельную копию модуля мерчанта.
{% endhint %}

Для работы модуля на прием средств без использования [задания cron](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-sozdat-zadanie-cron-na-servere), укажите ссылку из настроек модуля

<figure><img src="../../../.gitbook/assets/image (10).png" alt=""><figcaption></figcaption></figure>

в ЛК 1Plat в разделе "Магазин - Настройки - Коллбек":

<figure><img src="../../../.gitbook/assets/image (12).png" alt="" width="563"><figcaption></figcaption></figure>

## Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).<br>
