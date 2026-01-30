# Payscrow Cascade

{% hint style="danger" %}
<mark style="color:red;">Перед настройкой автовыплат обязательно прочитайте</mark> [<mark style="color:blue;">предупреждение о рисках</mark>](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/preduprezhdenie-o-riskakh)<mark style="color:blue;">!</mark>
{% endhint %}

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat)
{% endhint %}

## Настройки в личном кабинете мерчанта <a href="#nastroiki-v-lichnom-kabinete-merchanta" id="nastroiki-v-lichnom-kabinete-merchanta"></a>

{% hint style="warning" %}
Для обсуждения условий и подключения, свяжитесь с [представителем сервиса](https://t.me/Payscrow).

**Дисклеймер**: при подключении вашего сайта к тому или иному сервису, пожалуйста, самостоятельно оценивайте возможные риски сотрудничества.
{% endhint %}

Зарегистрируйтесь и авторизуйтесь в ЛК мерчанта. В разделе "Терминалы" ➔ "**Настройки API**" скопируйте API-ключ для авторизации в модуле автовыплаты.

<figure><img src="../../../../.gitbook/assets/image (11) (1).png" alt="" width="563"><figcaption></figcaption></figure>

В поле "**Статус заказа продать**" укажите URL из настроек модуля автовыплаты (Callback URL)

<figure><img src="../../../../.gitbook/assets/image (12) (1).png" alt=""><figcaption></figcaption></figure>

## Настройки модуля <a href="#nastroiki-modulya" id="nastroiki-modulya"></a>

В панели администратора создайте нового мерчанта в разделе "**Автовыплаты**" ➔ "**Добавить автовыплату".**

Выберите Payscrow Cascade в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../../.gitbook/assets/image (8) (1).png" alt="" width="492"><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../../.gitbook/assets/image (9) (1).png" alt="" width="464"><figcaption></figcaption></figure>

**API ключ** — API ключ, скопированный в ЛК мерчанта

## Особые поля

<figure><img src="../../../../.gitbook/assets/image (10) (1).png" alt="" width="422"><figcaption></figcaption></figure>

**Способ оплаты** — выберите необходимый способ для выплаты средств

* **\[BankCard, RUB] Любой банк РФ** — выдача номера карты любого банка\
  • **\[BankCard, RUB] {название\_банка}** — выдача номера карты указанного банка
* **\[SBP, RUB] СБП {название\_банка}** — выдача номера телефона для оплаты по нему, к которому привязана карта выбранного банка

{% hint style="warning" %}
Обратите внимание, что для корректной работы выплаты на банковские карты РФ необходимо выбирать агрегатный метод (к примеру, "Любой банк РФ"), а для выплаты по СБП — метод с указанием банка
{% endhint %}

## Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-merchantov-avtovyplat).
