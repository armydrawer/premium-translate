# Unite

{% hint style="danger" %}
Перед настройкой автовыплат обязательно прочитайте [предупреждение о рисках!](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/preduprezhdenie-o-riskakh)
{% endhint %}

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat)
{% endhint %}

## Настройки в личном кабинете мерчанта

{% hint style="warning" %}
Для обсуждения условий и подключения, свяжитесь с [представителем сервиса](https://t.me/Paylonium_TeamLead).

**Дисклеймер**: при подключении вашего сайта к тому или иному сервису, пожалуйста, самостоятельно оценивайте возможные риски сотрудничества.
{% endhint %}

Зарегистрируйтесь на [сервисе Unite](https://unitekass.org/#contacts) и авторизуйтесь в личном кабинете мерчанта.

Создайте новый проект в разделе "**Проекты**". Заполните в открывшемся окне требуемые поля, отправьте заявку на рассмотрение и ожидайте смены статуса с "**На модерации**" на "**Активен**".

После активации проекта перейдите в его настройки и скопируйте выделенные ключи.

## Настройки модуля

В панели администратора создайте нового мерчанта в разделе "**Мерчанты**" ➔ "**Добавить автовыплату".**

Выберите Unite в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../.gitbook/assets/image (735).png" alt=""><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/image (384).png" alt=""><figcaption></figcaption></figure>

**Домен** — оставьте поле пустым

**Username** — юзернейм на латинцие, придуманный вами и переданный представителя Unite для указания его в ЛК

**Приватный ключ PEM** — приватный ключ, переданный вам ранее представителем Unite

**Пароль приватного ключа** — пароль для приватного ключа, переданный вам ранее представителем Unite

## Особые поля

<figure><img src="../../../.gitbook/assets/image (385).png" alt=""><figcaption></figcaption></figure>

**Способ оплаты:**

* **Card** — выплата на банковскую карту
* **Qiwi** — выплата на Qiwi-кошелек
* **SBP** — выплата по номеру телефона, привязанному к СБП
* **Mobile top-up** — пополнение номера мобильного телефона

**Bank code (SBP only):**

* **Доп. поля (Валюты)** — использование [доп.поля валюты](https://premium.gitbook.io/main/osnovnye-nastroiki/valyuty-i-napravleniya-obmena/dopolnitelnye-polya#dopolnitelnye-polya-dlya-valyuty) "**Получаю**"
* **Доп. поля (Направление)** — использование [доп.поля направления обмена](https://premium.gitbook.io/main/osnovnye-nastroiki/valyuty-i-napravleniya-obmena/dopolnitelnye-polya#dopolnitelnye-polya-dlya-napravleniya-obmena)
* **Bank code (SBP only)** — ручной выбор банка для выплаты по СБП

<div><figure><img src="../../../.gitbook/assets/image (403).png" alt=""><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/image (410).png" alt=""><figcaption></figcaption></figure></div>

## Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).<br>
