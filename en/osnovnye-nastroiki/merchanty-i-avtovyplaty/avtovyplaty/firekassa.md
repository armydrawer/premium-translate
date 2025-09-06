# Firekassa

{% hint style="danger" %}
<mark style="color:red;">Перед настройкой автовыплат обязательно прочитайте</mark> [<mark style="color:blue;">предупреждение о рисках</mark>](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/preduprezhdenie-o-riskakh)<mark style="color:blue;">!</mark>
{% endhint %}

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat)
{% endhint %}

{% hint style="danger" %}
Модуль работает только с банками (выплаты на карты) - поддержки выплат на Qiwi, Юmoney или по номеру телефона на данный момент нет
{% endhint %}

## Настройки в личном кабинете мерчанта

Пройдите регистрацию на сайте [Vanilapay](https://web.vanilapay.com/) (при работе с RUB) или на сайте [Gamepay](https://web.gampay.cc/) (при работе с UAH).

Зайдите в личный кабинет, раздел "**Сайты**" -> "**Список сайтов**" и добавьте новый сайт.

<figure><img src="../../../.gitbook/assets/image (808).png" alt=""><figcaption></figcaption></figure>

Заполните указанные поля, кроме "**URL уведомлений**" и "**URL уведомлений для выплат**" и нажмите "**Добавить**".

<figure><img src="../../../.gitbook/assets/image (809).png" alt="" width="563"><figcaption></figcaption></figure>

В открывшемся окне перейдите на вкладку "**API**".

<figure><img src="../../../.gitbook/assets/image (810).png" alt=""><figcaption></figcaption></figure>

Обновите **API Bearer Token** и **API Sign Token**, нажав **"Изменить"** на каждой строке поочередно.

<figure><img src="../../../.gitbook/assets/image (811).png" alt=""><figcaption></figcaption></figure>

Скопируйте ключи и сохраните их в текстовый файл.

## **Настройки модуля**

В панели администратора создайте нового мерчанта в разделе "**Автовыплаты**" -> "**Добавить автовыплату".**

Выберите Firekassa в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../.gitbook/assets/image (805).png" alt=""><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/image (1488).png" alt=""><figcaption></figcaption></figure>

**API url** — укажите URL сервиса, с которым будете работать:\
• **https://admin.gampay.cc** — при работе с UAH (альтернативный URL - **https://web.gampay.cc)**\
• **https://admin.vanilapay.com** — при работе с RUB (альтернативный URL - **https://web.vanilapay.com)**

**API ключ** — **API Bearer Token** из личного кабинета Firekassa

**Секретный ключ** — **API Sign Token** из личного кабинета Firekassa

## Особые поля

**Тип**:

<figure><img src="../../../.gitbook/assets/image (707).png" alt=""><figcaption></figcaption></figure>

* **Тип** — выбор банка для выплаты средств (RUB, UAH)

{% hint style="warning" %}
Список банков и платежных систем для этой опции подгружается по API от мерчанта — если какого-то типа не хватает, обратитесь к мерчанту за его включением
{% endhint %}

## Продолжение настройки

Далее произведите настройку автовыплаты следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-merchantov-avtovyplat).
