# Paylonium

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat)
{% endhint %}

## Настройки в личном кабинете мерчанта

{% hint style="warning" %}
Для обсуждения условий работы свяжитесь с представителем сервиса.

**Дисклеймер**: при подключении вашего сайта к тому или иному сервису, пожалуйста, самостоятельно оценивайте возможные риски сотрудничества.
{% endhint %}

Зарегистрируйтесь на сервисе Paylonium и авторизуйтесь в личном кабинете мерчанта. Создайте новый проект в разделе "**Проекты**". Заполните в открывшемся окне требуемые поля, отправьте заявку на рассмотрение и ожидайте смены статуса с "**На модерации**" на "**Активен**".

После активации проекта перейдите в его настройки и скопируйте выделенные ключи.

## Настройки модуля

В панели администратора создайте нового мерчанта в разделе "**Мерчанты**" ➔ "**Добавить мерчант".**

Выберите Paylonium в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../.gitbook/assets/image (343).png" alt=""><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/image (364).png" alt=""><figcaption></figcaption></figure>

**Домен** — оставьте поле пустым

**Key ID** — ID, скопированный ранее в ЛК Paylonium

**Приватный ключ** — ключ, скопированный ранее в ЛК Paylonium

## Особые поля

**Тип мерчанта:**

<figure><img src="../../../.gitbook/assets/image (365).png" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
Тип мерчанта закрепляется за настраиваемым модулем без возможности его изменения после первой созданной заявки с использованием этого модуля.

&#x20;Для того, чтобы использовать другой тип мерчанта, необходимо создать отдельную копию, выбрав другой тип и подключить её в нужном направлении обмена.
{% endhint %}

* **Requisites** — реквизиты от мерчанта будут отображаться в заявке

<figure><img src="../../../.gitbook/assets/image (382).png" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
При выборе этого типа выдачи реквизитов время создания заявок может увеличиться до 20 секунд из-за подбора реквизитов на стороне мерчанта
{% endhint %}

* **Payment link** — в заявке будет отображаться кнопка "**Перейти к оплате**", при нажатии на которую клиент попадет на платежную страницу мерчанта, где будут отображаться реквизиты или выполняться подбор реквизитов:

<div><figure><img src="../../../.gitbook/assets/image.png" alt="" width="467"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/image (428).png" alt="" width="562"><figcaption></figcaption></figure></div>

**При оплате этим методом клиенту будет необходимо прикрепить чек после оплаты заявки:**

<figure><img src="../../../.gitbook/assets/image (1).png" alt="" width="436"><figcaption></figcaption></figure>

**После загрузки чека клиент должен дождаться его обработки:**

<figure><img src="../../../.gitbook/assets/image (418).png" alt="" width="531"><figcaption></figcaption></figure>

**Способ оплаты:**

<figure><img src="../../../.gitbook/assets/image (371).png" alt=""><figcaption><p>При выборе пункта "Requisites"</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (370).png" alt=""><figcaption><p>При выборе пункта "Payment link"</p></figcaption></figure>

* **Any** — будут выдаваться реквизиты любого типа
* **Card** — номер банковской карты
* **SBP** — номер номера телефона, привязанного к СБП
* **TPay** — реквизиты для оплаты через T-Pay ([https://www.tbank.ru/t-pay/online/](https://www.tbank.ru/t-pay/online/))

## Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).
