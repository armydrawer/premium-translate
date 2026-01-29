# Finora



{% hint style="danger" %}
Перед настройкой автовыплат обязательно прочитайте [предупреждение о рисках!](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/preduprezhdenie-o-riskakh)
{% endhint %}

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat)
{% endhint %}

{% hint style="warning" %}
Для обсуждения условий и подключения свяжитесь с представителем сервиса.

**Дисклеймер**: при подключении вашего сайта к тому или иному сервису, пожалуйста, самостоятельно оценивайте возможные риски сотрудничества.
{% endhint %}

{% hint style="warning" %}
Обращаем ваше внимание, что при использовании модуля автовыплаты Finora фактическая сумма выплаты всегда округляется до двух знаков после запятой на стороне сервиса.
{% endhint %}

## Настройки модуля

В панели администратора создайте нового мерчанта в разделе "**Мерчанты**" ➔ "**Добавить автовыплату".**

Выберите Finora в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../.gitbook/assets/изображение (2).png" alt="" width="378"><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/изображение (2) (1).png" alt="" width="409"><figcaption></figcaption></figure>

**Логин (ЛК)** — логин от вашего ЛК в Finora

**OTP ключ (ЛК)** — OTP-ключ от вашего ЛК в Finora

**Логин (SSO выплата)** — логин от сервиса в Finora

**OTP ключ (SSO выплата)** — OTP-ключ от сервиса в Finora

**Приватный ключ** — приватный ключ, из вашего ЛК в Finora

{% hint style="warning" %}
Перед началом работы вам нужно сгенерировать публичный ключ (**Public key**), который следует сохранить в ЛК платежной системы (**Security - Your Public Key**), а приватный ключ (**Private key**) в настройках модуля в поле "**Приватный ключ**"

![](<../../../.gitbook/assets/изображение (195).png>)

Для удобства работы пара ключей автоматически генерируется для работы с мерчантом (для корректной работы генератора на сервере должна быть запущена служба/расширение **Sodium**). Скопируйте эти ключи из настроек модуля автовыплаты и вставьте их в соответствующие поля согласно интсрукции выше.

![](<../../../.gitbook/assets/изображение (194).png>)
{% endhint %}

## Особые поля

<figure><img src="../../../.gitbook/assets/изображение (3).png" alt=""><figcaption></figcaption></figure>

**Способ оплаты** — выберите подходящий метод из списка

{% hint style="info" %}
При использовании метода "**Карта**" вам необходимости&#x20;
{% endhint %}

Для работы модуля автовыплаты без использования [задания cron](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-sozdat-zadanie-cron-na-servere), укажите ссылку из настроек модуля

<figure><img src="../../../.gitbook/assets/изображение (197).png" alt=""><figcaption></figcaption></figure>

&#x20;в ЛК Finora в поле **PayOut Webhook**:

<figure><img src="../../../.gitbook/assets/изображение (196).png" alt=""><figcaption></figcaption></figure>

## Продолжение настройки <a href="#prodolzhenie-nastroiki" id="prodolzhenie-nastroiki"></a>

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-merchantov-avtovyplat).
