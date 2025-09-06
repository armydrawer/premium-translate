# Payscrow Cascade

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat)
{% endhint %}

{% hint style="info" %}
Для отображения в заявке для клиента ФИО владельца карты, выданной мерчантом, добавьте шорткод \[dest\_tag] в инструкции в настройках мерчанта

![](<../../../../.gitbook/assets/image (1686).png>)
{% endhint %}

## Настройки в личном кабинете мерчанта

{% hint style="warning" %}
Для обсуждения условий и подключения, свяжитесь с [представителем сервиса](https://t.me/Payscrow).

**Дисклеймер**: при подключении вашего сайта к тому или иному сервису, пожалуйста, самостоятельно оценивайте возможные риски сотрудничества.
{% endhint %}

Зарегистрируйтесь и авторизуйтесь в ЛК мерчанта. В разделе "**Терминалы**" ➔ "**Настройки API**" скопируйте API-ключ для авторизации в модуле мерчанта.

<figure><img src="../../../../.gitbook/assets/image (2222).png" alt=""><figcaption></figcaption></figure>

В поле "**Статус заказа купить**" укажите URL из настроек модуля автовыплаты (Webhook URL).

<figure><img src="../../../../.gitbook/assets/image (2224).png" alt=""><figcaption></figcaption></figure>

## Настройки модуля

В панели администратора создайте нового мерчанта в разделе "**Мерчанты**" ➔ "**Добавить мерчант".**

Выберите Payscrow Cascade в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../../.gitbook/assets/image (2225).png" alt="" width="499"><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../../.gitbook/assets/image (2226).png" alt="" width="442"><figcaption></figcaption></figure>

**Домен** — оставьте поле пустым

**API ключ** — API ключ, скопированный ранее в ЛК Payscrow

## Особые поля

<figure><img src="../../../../.gitbook/assets/image (2227).png" alt="" width="416"><figcaption></figcaption></figure>

Тип мерчанта:

* **Payment link** — в заявке будет отображаться кнопка "**Перейти к оплате**", при нажатии на которую клиент попадет на платежную страницу мерчанта, где будут отображаться реквизиты или выполняться подбор реквизитов
* **Requisites** — реквизиты от мерчанта будут отображаться в заявке

{% hint style="warning" %}
Тип мерчанта закрепляется за настраиваемым модулем без возможности его изменения после первой созданной заявки с использованием этого модуля.

![](https://premium.gitbook.io/main/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FzcRcd0cY32xbgh1lhGx6%252Fimage.png%3Falt%3Dmedia%26token%3Df1f65b44-fd81-4597-98d5-b705a410977f\&width=300\&dpr=4\&quality=100\&sign=57a702c3\&sv=2)![](https://premium.gitbook.io/main/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FVQqDVFVlJ7dwBTiSb2Rf%252Fimage.png%3Falt%3Dmedia%26token%3D16a4d0bc-48dc-4280-8e0a-8733cdb18f94\&width=300\&dpr=4\&quality=100\&sign=7c7aa62c\&sv=2)&#x20;

Для того, чтобы использовать другой тип мерчанта, необходимо создать отдельную копию, выбрав другой тип и подключить её в нужном направлении обмена.
{% endhint %}

**Способ оплаты** — доступные форматы выдачи реквизитов для клиентов

* **\[BankAccount, RUB] Счёт Сбербанк** — выдача номера счёта Сбербанк
* **\[BankCard, RUB] Любой банк РФ** — выдача номера карты любого банка\
  • **\[BankCard, RUB] {название\_банка}** — выдача номера карты указанного банка
* **\[SBP, RUB] СБП** — выдача номера телефона для оплаты по нему\
  • **\[SBP, RUB] СБП {название\_банка}** — выдача номера телефона для оплаты по нему, к которому привязана карта выбранного банка
* **\[TransBankCard, RUB]** — выдача номера карты любого трансграничного банка\
  • **\[TransBankCard, RUB] {название\_банка}** — выдача номера карты указанного трансграничного банка
* **\[TransSBP, RUB] СБП** — выдача номера телефона для оплаты по нему\
  • **\[TransSBP, RUB] СБП {название\_банка}** — выдача номера телефона для оплаты по нему, к которому привязана карта выбранного трансграничного банка

## Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).\
