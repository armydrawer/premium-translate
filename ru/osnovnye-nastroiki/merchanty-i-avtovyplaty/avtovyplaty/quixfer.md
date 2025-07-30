# Quixfer

{% hint style="danger" %}
<mark style="color:red;">Перед настройкой автовыплат обязательно прочитайте</mark> [<mark style="color:blue;">предупреждение о рисках</mark>](https://premiumexchanger.com/wiki/preduprezhdenie-auto/)<mark style="color:blue;">!</mark>
{% endhint %}

{% hint style="warning" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-merchantov)
{% endhint %}

## Настройки в личном кабинете мерчанта

{% hint style="warning" %}
Для обсуждения условий работы свяжитесь с [представителем сервиса](https://t.me/quixfer).

**Дисклеймер**: при подключении вашего сайта к тому или иному сервису, пожалуйста, самостоятельно оценивайте возможные риски сотрудничества.
{% endhint %}

[Зарегистрируйтесь](https://quixfer.cc/#contacts) на сервисе Quixfer, авторизуйтесь в личном кабинете и перейдите в раздел "**Settings**" ➔ "**Security**".

<figure><img src="../../../.gitbook/assets/image (4) (1).png" alt="" width="563"><figcaption></figcaption></figure>

Сгенерируйте API-ключи и сохраните их в текстовый файл.

<figure><img src="../../../.gitbook/assets/image (5) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## Настройки модуля

В панели администратора создайте нового мерчанта в разделе "**Автовыплаты**" ➔ "**Добавить автовыплату".**

Выберите Quixfer в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../.gitbook/assets/image (2) (1).png" alt="" width="472"><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/image (1) (1) (1) (1) (1).png" alt="" width="460"><figcaption></figcaption></figure>

**Домен** — оставьте поле пустым

**API ключ** — Public Key из личного кабинета Quixfer, скопированный ранее

**Секретный ключ** — Private Key из личного кабинета Quixfer, скопированный ранее

## Особые поля

<figure><img src="../../../.gitbook/assets/image (2) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

**Способ оплаты** — выберите необходимый способ для выплаты средств или пункт "**Автоматически**" — в этом случае выплата будет производиться согласно xml-коду валюты из направления обмена, где подключен модуль (список методов будет отображаться только после указания корректных API-ключей для авторизации в модуле).

## Дополнительные поля <a href="#dopolnitelnye-polya" id="dopolnitelnye-polya"></a>

Для корректного получения реквизитов для валюты на прием, где используется Quixfer, необходимо добавить в форму обмена **обязательные** доп. поля. Под полем "**Способ оплаты**" отображается подсказка по необходимым полям для каждого метода оплаты.

<figure><img src="../../../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

Создайте и добавьте [дополнительное поле](https://premium.gitbook.io/main/osnovnye-nastroiki/valyuty-i-napravleniya-obmena/dopolnitelnye-polya) к соответствующим валютам для **выплаты средств** через Quixfer. Обязательно укажите значение в поле "**Уникальный ID**" (указывайте название в нижнем регистре) и сделайте поле обязательным к заполнению.

<figure><img src="../../../.gitbook/assets/image (2).png" alt="" width="461"><figcaption></figcaption></figure>

После этого поле будет отображаться в форме обмена, а также будет обязательным к заполнению клиентов при создании заявки.

<figure><img src="../../../.gitbook/assets/image (3).png" alt="" width="563"><figcaption></figcaption></figure>

Пример заполнения для валюты T-Банк RUB (выделены названия из полей "Уникальный ID"):

<figure><img src="../../../.gitbook/assets/image (1).png" alt="" width="563"><figcaption></figcaption></figure>

Пример заполнения для валюты Bank transfer GEL (грузинский лари):

<figure><img src="../../../.gitbook/assets/image (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-merchantov-avtovyplat).\
