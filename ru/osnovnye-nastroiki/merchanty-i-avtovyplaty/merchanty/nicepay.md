# Nicepay

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat)
{% endhint %}

## Настройки в личном кабинете мерчанта

{% hint style="warning" %}
Для обсуждения условий и подключения свяжитесь с [представителем сервиса](https://t.me/nice_sup).

**Дисклеймер**: при подключении вашего сайта к тому или иному сервису оценивайте, пожалуйста, самостоятельно возможные риски сотрудничества.
{% endhint %}

{% hint style="success" %}
Вы можете использовать курс для направлений обмена от Nicepay — для этого в разделе "**Парсеры 2.0**" ➔ "**Настройки"** выберите сам источник (отметьте его галочкой),

![](<../../../.gitbook/assets/image (23).png>)

затем создайте необходимые курсы по [инструкции](https://premium.gitbook.io/main/osnovnye-nastroiki/valyuty-i-napravleniya-obmena/kursy-valyut/parser-kursov-valyut-parsery-2.0).

Доступные курсы валют:

* USDT ➔ USD
* USDT ➔ RUB (и обратный)
* USDT ➔ EUR
* USDT ➔ KZT (и обратный)
* USDT ➔ UAH (и обратный)
* USDT ➔ TJS

Выберите нужный курс в направлении обмена на вкладке "**Автокорректировка курса**".

![](<../../../.gitbook/assets/image (26).png>)
{% endhint %}

Пройдите регистрацию на сервисе Nicepay с помощью [представителя сервиса](https://t.me/nice_sup) и авторизуйтесь в [личном кабинете](https://nicepay.io/ru/app).

<figure><img src="../../../.gitbook/assets/image (41).png" alt="" width="506"><figcaption></figcaption></figure>

В личном кабинете мерчанта создайте новый проект в разделе "**Платежные решения**".

<figure><img src="../../../.gitbook/assets/image (36).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (37).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (38).png" alt="" width="563"><figcaption></figcaption></figure>

Перейдите в настройки созданного проекта.

<figure><img src="../../../.gitbook/assets/image (40).png" alt="" width="563"><figcaption></figcaption></figure>

Скопируйте ID мерчанта и Secret Key в буфер обмена или текстовый файл.

<figure><img src="../../../.gitbook/assets/image (39).png" alt="" width="563"><figcaption></figcaption></figure>

## Настройки модуля

В панели администратора создайте нового мерчанта в разделе "**Мерчанты**" -> "**Добавить мерчант".**

Выберите Nicepay в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../.gitbook/assets/image (35).png" alt="" width="379"><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/image (34).png" alt="" width="423"><figcaption></figcaption></figure>

**Домен** — оставьте поле пустым

**ID мерчанта** — ID мерчанта, скопированный ранее в ЛК мерчанта

**Секретный ключ** — Secret Key, скопированный ранее в ЛК мерчанта

## Особые поля

**Merchant type** — выберите формат мерчанта

<figure><img src="../../../.gitbook/assets/image (2131).png" alt=""><figcaption></figcaption></figure>

* **Payment Link** — реквизиты будут отображаться на отдельной платежной странице
* **Requisites** — реквизиты будут отображаться в самой заявке через шорткод \[to\_account]

{% hint style="warning" %}
Обратите внимание, что выбранный метод фиксируется в модуле после создания первой заявки через него — если вам необходимо использовать другой метод, создайте отдельную копию модуля.
{% endhint %}

**Способ оплаты** — выберите необходимый способ для приема средств

<figure><img src="../../../.gitbook/assets/image (30).png" alt="" width="419"><figcaption></figcaption></figure>

## Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).\
