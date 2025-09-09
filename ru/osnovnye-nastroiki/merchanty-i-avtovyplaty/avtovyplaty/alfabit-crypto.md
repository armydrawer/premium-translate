# Alfabit Crypto

{% hint style="danger" %}
<mark style="color:red;">Перед настройкой автовыплат обязательно прочитайте</mark> [<mark style="color:blue;">предупреждение о рисках!</mark>](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/preduprezhdenie-o-riskakh)
{% endhint %}

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat)
{% endhint %}

## Настройки в личном кабинете мерчанта <a href="#nastroiki-v-lichnom-kabinete-merchanta" id="nastroiki-v-lichnom-kabinete-merchanta"></a>

{% hint style="warning" %}
Для обсуждения условий и подключения, свяжитесь с [представителем сервиса](https://t.me/AlfaBitSupportVIP)

**Дисклеймер**: при подключении вашего сайта к тому или иному сервису, пожалуйста, самостоятельно оценивайте возможные риски сотрудничества.
{% endhint %}

Пройдите регистрацию и верификацию в сервисе [Alfabit](https://pay.alfabit.org/). Перейдите в раздел "**Мерчанты**" и нажмите кнопку "**Создать мерчант**".

<figure><img src="../../../.gitbook/assets/image (358).png" alt=""><figcaption></figcaption></figure>

Заполните указанные поля и нажмите кнопку "**Создать проект**".

<div><figure><img src="../../../.gitbook/assets/image (359).png" alt="" width="375"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/image (1795).png" alt="" width="357"><figcaption></figcaption></figure> <figure><img src="../../../.gitbook/assets/image (1796).png" alt="" width="356"><figcaption></figcaption></figure></div>

Перейдите в настройки мерчанта, выберите вкладку "**API ключи**" и нажмите кнопку "**Добавить**".

<figure><img src="../../../.gitbook/assets/image (360).png" alt=""><figcaption></figcaption></figure>

Заполните указанные поля и нажмите кнопку "**Сохранить**".

<figure><img src="../../../.gitbook/assets/image (361).png" alt="" width="363"><figcaption></figcaption></figure>

{% hint style="info" %}
Выберите один или оба пункта "**Прием средств/Вывод средств**" в зависимости от цели использования мерчанта.

Добавьте IP-адрес вашего сервера для пункта "**Доверенные IP**" (желательно).
{% endhint %}

<figure><img src="../../../.gitbook/assets/image (362).png" alt="" width="352"><figcaption></figcaption></figure>

Сохраните сгенерированный ключ в текстовый файл и нажмите кнопку "**Готово**".

## Настройки модуля <a href="#nastroiki-modulya" id="nastroiki-modulya"></a>

В панели администратора создайте нового мерчанта в разделе "**Автовыплаты**" -> "**Добавить автовыплату".**

Выберите Alfabit Crypto в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../.gitbook/assets/image (1791).png" alt="" width="467"><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/image (1792).png" alt="" width="455"><figcaption></figcaption></figure>

**API ключ** — **публичный ключ**, сгенерированный в ЛК Alfabit

## Особые поля

**Конвертация из другой валюты (укажите код)** — выберите "**Нет**" (если не планируете использовать опцию) или валюту, из которой будет производиться конвертация (по курсу мерчанта) в валюту для выплаты непосредственно перед самой выплатой по заявке

**Валюта** — выберите необходимую валюту для выплаты или пункт "**Автоматически**" (в этом случае выплата будет производиться согласно коду валюты "**Получаю**" из направления обмена, где подключен модуль автовыплаты) (список методов будет отображаться только после указания корректного API-ключа для авторизации в модуле).

<figure><img src="../../../.gitbook/assets/image (1895).png" alt="" width="476"><figcaption></figcaption></figure>

{% hint style="warning" %}
Для каждого используемого способа оплаты необходимо создать отдельную копию модуля автовыплаты, в которой выбрать соответствующий способ, а затем подключить эту копию на вкладке "**Мерчанты и выплаты**" в настройках направления обмена, где в валюте "**Получаю**" будет подходящая валюта
{% endhint %}

{% hint style="warning" %}
Обратите внимание на минимальные суммы для выплаты для валют, используемых вами (раздел "**Мерчанты**", вкладка "**Тарифы**" в ЛК Alfabit) — суммы для выплаты по заявкам должны превышать минимальные суммы, в противном случае мерчант не сможет произвести выплату:\
![](<../../../.gitbook/assets/image (1797).png>)
{% endhint %}

## Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-merchantov-avtovyplat).
