# OnlyPays

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat)
{% endhint %}

## Настройки в личном кабинете мерчанта

{% hint style="warning" %}
Для обсуждения условий и подключения, свяжитесь с [представителем сервиса](https://t.me/only7pay).

**Дисклеймер**: при подключении вашего сайта к тому или иному сервису, пожалуйста, самостоятельно оценивайте возможные риски сотрудничества.
{% endhint %}

После регистрации вашего аккаунта через представителя сервиса OnlyPays, активируйте бота ([LK\_onLy\_Pays\_bot](https://t.me/LK_onLy_Pays_bot)) кнопкой "**Start**". Через бота вы получаете доступ к своему личному кабинету.

<figure><img src="../../../.gitbook/assets/image (2172).png" alt="" width="434"><figcaption></figcaption></figure>

## Настройки модуля

В панели администратора создайте нового мерчанта в разделе "**Мерчанты**" ➔ "**Добавить мерчант".**

Выберите OnlyPays в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../.gitbook/assets/image (2170).png" alt="" width="447"><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/image (2169).png" alt="" width="454"><figcaption></figcaption></figure>

**Домен** — оставьте поле пустым

ID проекта — ID вашего проекта, выданный вам представителем OnlyPays

**Секретный ключ** — API ключ, выданный вам представителем OnlyPays

## Особые поля

<figure><img src="../../../.gitbook/assets/image (2171).png" alt=""><figcaption></figcaption></figure>

**СБП** — выдача реквизитов банковских карт или номера телефона для оплаты через СБП

{% hint style="success" %}
Для автоматического обновления статуса заявок без создания задания cron на сервере передайте мерчанту ссылку для вебхука (поле "**Webhook URL**") и попросите установить его для модуля на приём.

![](<../../../.gitbook/assets/image (2173).png>)
{% endhint %}

## Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).\
