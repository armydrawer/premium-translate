# OnlyPays

{% hint style="danger" %}
<mark style="color:red;">Перед настройкой автовыплат обязательно прочитайте</mark> [<mark style="color:blue;">предупреждение о рисках</mark>](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/preduprezhdenie-o-riskakh)<mark style="color:blue;">!</mark>
{% endhint %}

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

В панели администратора создайте нового мерчанта в разделе "**Автовыплаты**" ➔ "**Добавить автовыплату".**

Выберите OnlyPays в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../.gitbook/assets/image (2174).png" alt="" width="441"><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/image (2169).png" alt="" width="454"><figcaption></figcaption></figure>

**Домен** — оставьте поле пустым

**ID проекта** — ID вашего проекта, выданный вам представителем Onlypays

**Секретный ключ** — секретный ключ, выданный вам представителем Onlypays

## Особые поля

<figure><img src="../../../.gitbook/assets/image (2171).png" alt=""><figcaption></figcaption></figure>

**СБП** — выплата средств на банковскую карту или по номеру телефона, привязанному к СБП

{% hint style="success" %}
Для автоматического обновления статуса заявок без создания задания cron на сервере передайте мерчанту ссылку для вебхука (поле "**Webhook URL**") и попросите установить его для модуля на приём.

![](<../../../.gitbook/assets/image (2175).png>)
{% endhint %}

## Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-merchantov-avtovyplat).<br>
