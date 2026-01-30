# 1Plat

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-merchantov)
{% endhint %}

{% hint style="warning" %}
Для обсуждения условий и подключения свяжитесь с [представителем сервиса](https://t.me/Exe_PMx).

**Дисклеймер**: при подключении вашего сайта к тому или иному сервису, пожалуйста, самостоятельно оценивайте возможные риски сотрудничества.
{% endhint %}

{% hint style="warning" %}
Обращаем ваше внимание, что при использовании модуля на прием средств Finora фактическая сумма выплаты всегда округляется до четырех знаков после запятой на стороне сервиса.
{% endhint %}

## Настройки модуля

В панели администратора создайте нового мерчанта в разделе "**Мерчанты**" ➔ "**Добавить мерчант".**

Выберите 1Plat в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

**Домен** — оставьте поле пустым

**ID магазина** — ID вашего магазина на сервисе 1Plat

**Секретный ключ** — ключ, переданный вам менеджером 1Plat

## Особые поля

<figure><img src="../../../.gitbook/assets/image (9).png" alt=""><figcaption></figcaption></figure>

**Тип мерчанта** (выбранный пункт закрепляется за модулем, изменить его в дальнейшем не получится):

* **Payment Link** — возвращает в заявке ссылку для оплаты, опция работает совместно с выбранным ниже способом оплаты
* **Requisites** — возвращает карту или телефон для перевода средств в самой заявке через шорткод \[to\_account]

<figure><img src="../../../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

**Способ оплаты** — выберите подходящий метод из списка или укажите вручную свой вариант в поле "**Добавить**" (допустимые варианты уточняйте у менеджера 1Plat).

<figure><img src="../../../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
Обращаем ваше внимание, что для каждого метода необходимо создавать отдельную копию модуля мерчанта.
{% endhint %}

Для работы модуля на прием средств без использования [задания cron](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-sozdat-zadanie-cron-na-servere), укажите ссылку из настроек модуля

<figure><img src="../../../.gitbook/assets/image (10).png" alt=""><figcaption></figcaption></figure>

в ЛК 1Plat в разделе "Магазин - Настройки - Коллбек":

<figure><img src="../../../.gitbook/assets/image (12).png" alt="" width="563"><figcaption></figcaption></figure>

## Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).<br>
