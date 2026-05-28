# Unite

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat)
{% endhint %}

## Настройки в личном кабинете мерчанта

{% hint style="warning" %}
Для обсуждения условий работы свяжитесь с [представителем сервиса](https://t.me/Paylonium_TeamLead).

**Дисклеймер**: при подключении вашего сайта к тому или иному сервису, пожалуйста, самостоятельно оценивайте возможные риски сотрудничества.
{% endhint %}

Зарегистрируйтесь на [сервисе Unite](https://unitekass.org/#contacts) и авторизуйтесь в личном кабинете мерчанта. Создайте новый проект в разделе "**Проекты**". Заполните в открывшемся окне требуемые поля, отправьте заявку на рассмотрение и ожидайте смены статуса с "**На модерации**" на "**Активен**".

После активации проекта перейдите в его настройки и скопируйте выделенные ключи.

## Настройки модуля

В панели администратора создайте нового мерчанта в разделе "**Мерчанты**" ➔ "**Добавить мерчант".**

Выберите Unite в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../.gitbook/assets/image (736).png" alt=""><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/image (364).png" alt=""><figcaption></figcaption></figure>

**Домен** — оставьте поле пустым

**Key ID** — ID, переданный вам ранее представителем Unite

**Приватный ключ** — ключ, переданный вам ранее представителем Unite

## Особые поля

**Тип мерчанта:**

<figure><img src="../../../.gitbook/assets/image (365).png" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
Тип мерчанта закрепляется за настраиваемым модулем без возможности его изменения после первой созданной заявки с использованием этого модуля.

Для того, чтобы использовать другой тип мерчанта, необходимо создать отдельную копию, выбрав другой тип и подключить её в нужном направлении обмена.
{% endhint %}

* **Requisites** — реквизиты от мерчанта будут отображаться в самой заявке

<figure><img src="../../../.gitbook/assets/image (382).png" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
При выборе этого типа выдачи реквизитов время создания заявок может увеличиться до 20 секунд из-за подбора реквизитов на стороне мерчанта
{% endhint %}

* **Payment link** — в заявке будет отображаться кнопка "**Перейти к оплате**", при нажатии на которую клиент попадет на платежную страницу мерчанта, где будут отображаться реквизиты или выполняться подбор реквизитов с последующим их отображением:

<div><figure><img src="../../../.gitbook/assets/image (864).png" alt=""><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/image (811).png" alt=""><figcaption></figcaption></figure></div>

При оплате методом **Payment link** клиенту будет необходимо прикрепить чек после оплаты заявки:

<figure><img src="../../../.gitbook/assets/image (740).png" alt=""><figcaption></figcaption></figure>

После загрузки чека клиент должен дождаться его обработки:

<figure><img src="../../../.gitbook/assets/image (769).png" alt=""><figcaption></figcaption></figure>

**Способ оплаты:**

{% tabs %}
{% tab title="При выборе пункта "Requisites"" %}
<figure><img src="../../../.gitbook/assets/image (371).png" alt=""><figcaption><p>При выборе пункта "Requisites"</p></figcaption></figure>

* **Card** — номер банковской карты
* **SBP** — номер номера телефона, привязанного к СБП
{% endtab %}

{% tab title="При выборе пункта "Payment link"" %}
<figure><img src="../../../.gitbook/assets/image (370).png" alt=""><figcaption></figcaption></figure>



* **Any** — будут выдаваться реквизиты любого формата, указанного ниже
* **Card** — номер банковской карты
* **SBP** — номер номера телефона, привязанного к СБП
* **TPay** — реквизиты для оплаты через [сервис T-Pay](https://www.tbank.ru/t-pay/online/)
{% endtab %}
{% endtabs %}

## Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).
