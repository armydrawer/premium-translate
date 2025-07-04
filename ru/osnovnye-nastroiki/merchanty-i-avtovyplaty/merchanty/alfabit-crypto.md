# Alfabit Crypto

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-merchantov)
{% endhint %}

{% hint style="warning" %}
Для обсуждения условий и подключения свяжитесь с [представителем сервиса](https://t.me/AlfaBitSupportVIP)

**Дисклеймер**: при подключении вашего сайта к тому или иному сервису, самостоятельно пожалуйста оценивайте возможные риски сотрудничества.
{% endhint %}

## Настройки в личном кабинете мерчанта

Пройдите регистрацию и верификацию в сервисе [Alfabit](https://pay.alfabit.org/). Перейдите в раздел "**Мерчанты**" и нажмите кнопку "**Создать мерчант**".

<figure><img src="../../../.gitbook/assets/image (364).png" alt=""><figcaption></figcaption></figure>

Заполните указанные поля и нажмите кнопку "**Создать проект**".

<div><figure><img src="../../../.gitbook/assets/image (365).png" alt="" width="375"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/image (368).png" alt="" width="357"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/image (367).png" alt="" width="356"><figcaption></figcaption></figure></div>

Перейдите в настройки мерчанта, выберите вкладку "**API ключи**" и нажмите кнопку "**Добавить**".

<figure><img src="../../../.gitbook/assets/image (371).png" alt=""><figcaption></figcaption></figure>

Заполните указанные поля и нажмите кнопку "**Сохранить**".

<figure><img src="../../../.gitbook/assets/image (370).png" alt="" width="363"><figcaption></figcaption></figure>

{% hint style="info" %}
Выберите один или оба пункта "**Прием средств/Вывод средств**" в зависимости от цели использования мерчанта.

Добавьте IP-адрес вашего сервера для пункта "**Доверенные IP**" (желательно).
{% endhint %}

<figure><img src="../../../.gitbook/assets/Arc_qmcPit3Hgb.png" alt="" width="352"><figcaption></figcaption></figure>

&#x20;Сохраните сгенерированный ключ в текстовый файл и нажмите кнопку "**Готово**".

## Настройки модуля

В панели администратора создайте нового мерчанта в разделе "**Мерчанты**" -> "**Добавить мерчант".**

Выберите Alfabit Crypto в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../.gitbook/assets/Arc_NAxwA0DrS1.png" alt="" width="473"><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/image (372).png" alt="" width="458"><figcaption></figcaption></figure>

**API ключ** — **публичный ключ**, сгенерированный в ЛК Alfabit

## Особые поля

<figure><img src="../../../.gitbook/assets/Arc_wNtMcO8Eyp.png" alt="" width="455"><figcaption></figcaption></figure>

**Валюта** — выберите необходимую валюту для приема средств или пункт "**Автоматически**" (в этом случае адрес кошелька будет запрашиваться согласно коду валюты из направления обмена, где подключен мерчант (список методов будет отображаться только после указания корректного API-ключа для авторизации в модуле).

<figure><img src="../../../.gitbook/assets/image (1790).png" alt="" width="435"><figcaption></figcaption></figure>

{% hint style="warning" %}
Обратите внимание на минимальные суммы на приём для валют, используемых вами (раздел "**Мерчанты**", вкладка "**Тарифы**" в ЛК Alfabit) — суммы по заявкам должны превышать минимальные суммы, в противном случае мерчант не обработает платеж:\
![](<../../../.gitbook/assets/image (1797).png>)
{% endhint %}

**Преобразовать к** — выберите валюту, в которую будет конвертироваться платеж (по курсу мерчанта на момент конвертации), принятый от клиента или выберите пункт "**Нет**", чтобы отключить конвертацию. В подсказке под полем указаны возможные пары для конвертации средств (список методов будет отображаться только после указания корректного API-ключа для авторизации в модуле).

<figure><img src="../../../.gitbook/assets/image (1894).png" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
Обратите внимание, что заявки с суммой эквивалентом <12 USDT не будут конвертироваться (ограничения на стороне мерчанта) при включенной опции — средства по таким заявкам будут приходить на счёт в изначальной валюте

![](<../../../.gitbook/assets/image (1788).png>)
{% endhint %}

## Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).\
