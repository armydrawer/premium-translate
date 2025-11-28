# DashPay

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat)
{% endhint %}

{% hint style="warning" %}
Для обсуждения условий и подключения свяжитесь с [представителем сервиса](https://t.me/adamdashpay).

**Дисклеймер**: при подключении вашего сайта к тому или иному сервису оценивайте, пожалуйста, самостоятельно возможные риски сотрудничества.
{% endhint %}

## Настройки в личном кабинете мерчанта

Пройдите регистрацию на сервисе [DashPay](https://dashpayment.pro/). Авторизуйтесь в личном кабинете, перейдите в раздел "**Профиль**" ➔ "**Мерчанты**" и создайте нового мерчанта.

<figure><img src="../../../.gitbook/assets/image (131).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Ссылки для всех полей "**URL для переадресации**" скопируйте позже в настройках созданного модуля мерчанта и укажите их в соответствующих полях (обращайте внимание на конец ссылки!). Сохраните данные настройки.

<img src="../../../.gitbook/assets/image (140).png" alt="" data-size="original">

<img src="../../../.gitbook/assets/image (141).png" alt="" data-size="original">
{% endhint %}

Скопируйте "**Basic токен**" для созданного мерчанта в буфер обмена или текстовый файл.

<figure><img src="../../../.gitbook/assets/image (138).png" alt=""><figcaption></figcaption></figure>

Перейдите на вкладку "**Основные настройки**", нажмите кнопку "Обновить" и скопируйте полученный токен API.

<figure><img src="../../../.gitbook/assets/image (136).png" alt="" width="563"><figcaption></figcaption></figure>

## Настройки модуля

В панели администратора создайте нового мерчанта в разделе "**Мерчанты**" ➔ "**Добавить мерчант".**

Выберите DashPay в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../.gitbook/assets/image (142).png" alt="" width="416"><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/image (133).png" alt="" width="422"><figcaption></figcaption></figure>

**Токен API** — токен API, скопированный ранее в ЛК мерчанта

**Basic токен** — Basic токен, скопированный ранее в ЛК мерчанта

## Особые поля

**Тип мерчанта:**

<figure><img src="../../../.gitbook/assets/image (144).png" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
Тип мерчанта закрепляется за настраиваемым модулем без возможности его изменения после первой созданной заявки с использованием этого модуля.

![](<../../../.gitbook/assets/image (129).png>)![](<../../../.gitbook/assets/image (130).png>)\
Для того, чтобы использовать другой тип мерчанта, необходимо создать отдельную копию, выбрав другой тип и подключить её в нужном направлении обмена.
{% endhint %}

* **Requisites** — реквизиты от мерчанта будут отображаться в заявке

<figure><img src="../../../.gitbook/assets/image (147).png" alt="" width="563"><figcaption></figcaption></figure>

{% hint style="warning" %}
При выборе этого типа выдачи реквизитов время создания заявок может увеличиться до 20 секунд из-за подбора реквизитов на стороне мерчанта
{% endhint %}

* **Payment link** — в заявке будет отображаться кнопка "**Перейти к оплате**", при нажатии на которую клиент попадет на платежную страницу мерчанта, где будут отображаться реквизиты или выполняться подбор реквизитов

<figure><img src="../../../.gitbook/assets/image (148).png" alt="" width="563"><figcaption></figcaption></figure>

**Способ оплаты:**

<figure><img src="../../../.gitbook/assets/image (145).png" alt="" width="360"><figcaption></figcaption></figure>

* **card\_number** — номер банковской карты для приема рублей
* **payment\_account\_number** — номер банковского счета для приема рублей
* **phone\_number** — номер телефона для приема рублей по СБП

## Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).<br>
