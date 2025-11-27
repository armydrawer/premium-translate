# Diffpay

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat)
{% endhint %}

## Настройки в личном кабинете мерчанта

{% hint style="warning" %}
Для обсуждения условий и подключения, свяжитесь с [представителем сервиса](https://t.me/diffpay).

**Дисклеймер**: при подключении вашего сайта к тому или иному сервису, самостоятельно пожалуйста оценивайте возможные риски сотрудничества.
{% endhint %}

Зарегистрируйтесь и авторизуйтесь в сервисе [Diffpay](https://diffpay.pro/login).&#x20;

Перейдите в раздел "**Профиль**" и скопируйте выпущенный ключ API в буфер обмена или текстовый файл.

<figure><img src="../../../.gitbook/assets/image (1857).png" alt="" width="563"><figcaption></figcaption></figure>

## Настройки модуля

В панели администратора создайте нового мерчанта в разделе "**Мерчанты**" -> "**Добавить мерчант".**

Выберите Diffpay в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../.gitbook/assets/image (1856).png" alt="" width="374"><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/image (1897).png" alt="" width="455"><figcaption></figcaption></figure>

**Домен** — домен мерчанта (укажите в этом поле [https://diffpay.pro](https://diffpay.pro))

**API ключ** — **Ключ API** из ЛК Diffpay

## Особые поля

<figure><img src="../../../.gitbook/assets/image (1854).png" alt="" width="353"><figcaption></figcaption></figure>

**Способ оплаты** — выберите необходимый способ для приема средств (список методов будет отображаться только после указания корректного API-ключа для авторизации в модуле)

{% hint style="warning" %}
Для каждого используемого способа оплаты необходимо создать отдельную копию модуля мерчанта, в которой выбрать соответствующий способ, а затем подключить эту копию на вкладке "**Мерчанты и выплаты**" в настройках направления обмена, где в валюте "**Отдаю**" будет подходящая валюта
{% endhint %}

## Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).<br>
