# MoneyGo



{% hint style="danger" %}
<mark style="color:red;">Перед настройкой автовыплат обязательно прочитайте</mark> [<mark style="color:blue;">предупреждение о рисках</mark>](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/preduprezhdenie-o-riskakh)<mark style="color:blue;">!</mark>
{% endhint %}

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat)
{% endhint %}

## Настройки в личном кабинете мерчанта <a href="#nastroiki-v-lichnom-kabinete-merchanta" id="nastroiki-v-lichnom-kabinete-merchanta"></a>

Пройдите регистрацию на сервисе [MoneyGo](https://money-go.com/ru/register). После регистрации запросите доступ к API у вашего MoneyGo менеджера или оставьте заявку на получения доступа к API для работы с модулем через [форму обратной связи](https://money-go.com/ru/helpdesk) (раздел "**Контакты**" на сайте), выбрав пункт "**Сотрудничество**" и заполнив обязательные поля.

<figure><img src="../../../.gitbook/assets/image (2010).png" alt="" width="563"><figcaption></figcaption></figure>

## Настройки модуля <a href="#nastroiki-modulya" id="nastroiki-modulya"></a>

В панели администратора создайте нового мерчанта в разделе "**Автовыплаты**" -> "**Добавить автовыплату".**

Выберите MoneyGo в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../.gitbook/assets/image (216).png" alt="" width="452"><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/image (217).png" alt="" width="446"><figcaption></figcaption></figure>

**Client ID** — ID, переданный вам менеджером MoneyGo

**Client Secret** — ключ клиента, переданный вам менеджером MoneyGo

**Token** — поле не заполняется

**U-кошелек** — кошелек для USD из личного кабинета MoneyGo

<figure><img src="../../../.gitbook/assets/image (218).png" alt="" width="563"><figcaption></figcaption></figure>

**E-, R-кошелек** — поля не заполняются

## Особые поля

{% hint style="warning" %}
Для корректной работы модуля для валюты "**Получаю**" из направления обмена, где используется MoneyGo на выплату средств, должно быть активно обязательное к заполнению поле "**На** **счет**", которое будет заполнять клиент в форме создания заявки (указывать свой кошелек в системе MoneyGo)

![](<../../../.gitbook/assets/image (219).png>)
{% endhint %}

## Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-merchantov-avtovyplat).
