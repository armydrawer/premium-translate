# GoldEx



{% hint style="danger" %}
<mark style="color:red;">Перед настройкой автовыплат обязательно прочитайте</mark> [<mark style="color:blue;">предупреждение о рисках!</mark>](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/preduprezhdenie-o-riskakh)
{% endhint %}

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat)
{% endhint %}

## Настройки в личном кабинете мерчанта <a href="#nastroiki-v-lichnom-kabinete-merchanta" id="nastroiki-v-lichnom-kabinete-merchanta"></a>

После получения доступ к личному кабинету авторизуйтесь в нём и перейдите в раздел "**Preferences**".

<figure><img src="../../../.gitbook/assets/image (301).png" alt="" width="411"><figcaption></figcaption></figure>

Скопируйте указанный на странице токен в буфер обмена.

<figure><img src="../../../.gitbook/assets/image (300).png" alt=""><figcaption></figcaption></figure>

## Настройки модуля

В панели администратора создайте нового мерчанта в разделе "**Автовыплаты**" -> "**Добавить автовыплату".**

Выберите GoldEx в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../.gitbook/assets/image (294).png" alt="" width="433"><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/image (295).png" alt="" width="466"><figcaption></figcaption></figure>

**Токен** — токен, ранее скопированный в ЛК мерчанта (раздел "**Preferences**")

## Особые поля

<figure><img src="../../../.gitbook/assets/image (2198).png" alt="" width="483"><figcaption></figcaption></figure>

**Способ оплаты** — выберите подходящий способ оплаты

{% hint style="warning" %}
Для каждого используемого способа оплаты необходимо создать отдельную копию модуля автовыплаты, в которой выбрать соответствующий способ, а затем подключить эту копию на вкладке "**Мерчанты и выплаты**" в настройках направления обмена.

Также обратите внимание, что **обязательно** нужно создавать отдельную копию модуля GoldEx на каждый используемый диапазон сумм из вышеуказнного выпадающего списка и устанавливать соответствующий диапазон сумм в каждой версии модуля,\
![](<../../../.gitbook/assets/image (2197).png>)\
чтобы из несколько подключенных в одном направлении копий модуля с разными диапазонами сумм автоматически подбиралась нужная копия в зависимости от суммы в заявке.
{% endhint %}

Вы можете передавать мерчанту данные от клиента через дополнительные поля, созданные для валюты "**Получаю**". Для этого создайте доп. поля и отметьте их галочкой в настройках валюты. Когда клиент будет заполнять эти поля в форме обмена при создании заявки, данные из них будут передаваться мерчанту.

{% hint style="info" %}
Названия полей:

* `get_cardholder` или `cardholder` — ФИО держателя карты
* `get_bankname` или `bankname` — название банка
* `get_iban` или `iban` — IBAN банка
* `get_phone` или `phone` — номер телефона
* `get_inn` или `inn` — ИНН
* `get_revTagWiseTag` или `revTagWiseTag` — идентификаторы [Revolut](https://help.revolut.com/ru-EE/help/transfers/internal-transfers/username-payments/revtags/)/[Wise](https://wise.com/ru/help/articles/6DtiR7Ugdp7hfoKJHfRfvJ/%D1%87%D1%82%D0%BE-%D1%82%D0%B0%D0%BA%D0%BE%D0%B5-wisetag-%D0%B8-%D0%BA%D0%B0%D0%BA-%D0%B5%D0%B3%D0%BE-%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D1%8C)

Указывайте название из списка выше в поле "**Уникальный ID**" (остальные поля заполняются по вашему усмотрению)

![](<../../../.gitbook/assets/image (2063).png>)
{% endhint %}

<figure><img src="../../../.gitbook/assets/image (303).png" alt="" width="563"><figcaption><p>Настройки доп. полей (в скобках указан уникальный ID из одноименного поля из настроек каждого доп. поля)</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (305).png" alt="" width="533"><figcaption><p>Форма обмена</p></figcaption></figure>

## Продолжение настройки

Далее произведите настройку модуля следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-merchantov-avtovyplat).
