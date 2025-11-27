# MoneyGo

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat)
{% endhint %}

## Настройки в личном кабинете мерчанта

Пройдите регистрацию на сервисе [MoneyGo](https://money-go.com/ru/register). После регистрации запросите доступ к API у вашего MoneyGo менеджера или оставьте заявку на получения доступа к API для работы с модулем через [форму обратной связи](https://money-go.com/ru/helpdesk) (раздел "**Контакты**" на сайте), выбрав пункт "**Сотрудничество**" и заполнив обязательные поля.

<figure><img src="../../../.gitbook/assets/image (2011).png" alt=""><figcaption></figcaption></figure>

## Настройки модуля

В панели администратора создайте нового мерчанта в разделе "**Мерчанты**" -> "**Добавить мерчант".**

Выберите MoneyGo в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../.gitbook/assets/image (224).png" alt="" width="455"><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/image (2113).png" alt="" width="454"><figcaption></figcaption></figure>

**Client ID** — **Client ID**, переданный вам менеджером MoneyGo

**Client Secret** — ключ клиента (**Secret**), переданный вам менеджером MoneyGo

**Form Secret Key** — ключ мерчанта (**Token for the form**), переданный вам менеджером MoneyGo

**U-кошелек** — кошелек для USD из личного кабинета MoneyGo

<figure><img src="../../../.gitbook/assets/image (226).png" alt="" width="563"><figcaption></figcaption></figure>

**E-, R-кошелек** — поля не заполняются

{% hint style="warning" %}
Для корректной работы модуля для валюты "**Отдаю**" из направления обмена, где используется MoneyGo на прием средств, должно быть активно обязательное к заполнению поле "**Со счета**", которое будет заполнять клиент в форме создания заявки (указывать свой кошелек в системе MoneyGo)

![](<../../../.gitbook/assets/image (231).png>)
{% endhint %}

## Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).<br>
