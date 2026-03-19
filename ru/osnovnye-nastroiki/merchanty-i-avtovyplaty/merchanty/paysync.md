# PaySync

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat)
{% endhint %}

## Настройки в личном кабинете мерчанта

{% hint style="warning" %}
Для обсуждения условий работы свяжитесь с [представителем сервиса](https://t.me/psync).

**Дисклеймер**: при подключении вашего сайта к тому или иному сервису, пожалуйста, самостоятельно оценивайте возможные риски сотрудничества.
{% endhint %}

{% hint style="info" %}
Обращаем ваше внимание, что при использовании модуля на прием средств PaySync cумма из заявки округляется до 0 знаков после запятой (в "Инструкция по оплате для пользователя" сумма форматируется под необходимую для мерчанта).
{% endhint %}

Зарегистрируйтесь на сервисе PaySync с помощью представителя сервиса и авторизуйтесь в личном кабинете мерчанта.

## Настройки модуля

В панели администратора создайте нового мерчанта в разделе "**Мерчанты**" ➔ "**Добавить мерчант".**

Выберите PaySync в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../.gitbook/assets/изображение (2) (1) (1) (1) (1).png" alt="" width="367"><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/изображение (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="420"><figcaption></figcaption></figure>

**Домен** — оставьте поле пустым

**API ключ** — API ключ, скопированный из ЛК PaySync

<figure><img src="../../../.gitbook/assets/изображение (206).png" alt=""><figcaption></figcaption></figure>

**ID клиента** — ID, скопированный из ЛК PaySync

<figure><img src="../../../.gitbook/assets/изображение (207).png" alt="" width="217"><figcaption></figcaption></figure>

## Особые поля

<figure><img src="../../../.gitbook/assets/изображение (3) (1) (1).png" alt=""><figcaption></figcaption></figure>

**Тип мерчанта** (выбранный пункт закрепляется за копией модуля, изменить его в дальнейшем для этой копии не получится):

* **Payment Link** — возвращает в заявке ссылку для оплаты по QR-коду, опция работает совместно с выбранным способом оплаты
* **Requisites** — возвращает карту или телефон для перевода средств в самой заявке через шорткод \[to\_account]

<figure><img src="../../../.gitbook/assets/изображение (5).png" alt="" width="563"><figcaption></figcaption></figure>

**Способ оплаты** — выберите необходимый способ для приема средств от клиента:

{% hint style="info" %}
Все способы можно использовать и для получения реквизитов, и для ссылки, кроме SBPQR - только для получения ссылки.
{% endhint %}

**Заявка** — использование кода валюты из направления обмена для подбора реквизитов (выберите **\[Отдаете] Код валюты**)

**Доп. поля** — использование [доп.поля валюты](https://premium.gitbook.io/main/osnovnye-nastroiki/valyuty-i-napravleniya-obmena/dopolnitelnye-polya#dopolnitelnye-polya-dlya-valyuty) "**Отдаю**" для подбора реквизитов

**Способ оплаты** — ручной выбор валюты для подбора реквизитов по ней

Для обновления статусов заявок на основании платежей, совершенных через мерчанта, укажите в ЛК PaySync ссылку на вебхук, взятую из настроек модуля мерчанта.

<figure><img src="../../../.gitbook/assets/изображение (204).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/изображение (205).png" alt=""><figcaption></figcaption></figure>

## Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).
