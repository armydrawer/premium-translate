# OTC

{% hint style="danger" %}
<mark style="color:red;">Перед настройкой автовыплат обязательно прочитайте</mark> [<mark style="color:blue;">предупреждение о рисках</mark>](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/preduprezhdenie-o-riskakh)<mark style="color:blue;">!</mark>
{% endhint %}

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat)
{% endhint %}

## Настройки в личном кабинете мерчанта

Пройдите регистрацию в системе [OTC](https://globalotc.ru/auth).

Зайдите в личный кабинет, затем в раздел "**API**" и выпустите API-ключи.

<figure><img src="../../../.gitbook/assets/image (722).png" alt="" width="563"><figcaption></figcaption></figure>

Нажмите на кнопку "**Создать API ключи**" и в всплывающем окне укажите произвольное название для ключей.

<figure><img src="../../../.gitbook/assets/image (723).png" alt=""><figcaption></figcaption></figure>

После заполнения названия нажмите "**Создать**" — в форме отобразится пара ключей.

<figure><img src="../../../.gitbook/assets/image (724).png" alt="" width="563"><figcaption></figcaption></figure>

Скопируйте их по нажатию на кнопки копирования и сохраните в текстовый файл.

<figure><img src="../../../.gitbook/assets/image (725).png" alt="" width="194"><figcaption></figcaption></figure>

## **Настройки модуля**

В панели администратора создайте нового мерчанта в разделе "**Автовыплаты**" -> "**Добавить автовыплату".**

Выберите OTC в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../.gitbook/assets/image (726).png" alt="" width="563"><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/image (727).png" alt=""><figcaption></figcaption></figure>

**API ключ** - API-ключ, сгенерированный в ЛК OTC при создании API-ключа

**Секретный ключ** - секретный ключ, сгенерированный в ЛК OTC при создании API-ключа

## Особые поля

<figure><img src="../../../.gitbook/assets/image (688).png" alt=""><figcaption></figcaption></figure>

**Способ оплаты** — выберите из выпадающего списка валюту/банк, с использованием которого будет производиться выплата

<figure><img src="../../../.gitbook/assets/image (506).png" alt=""><figcaption></figcaption></figure>

**Конвертация из USDT** — активация выплаты из USDT, без необходимости хранения **рублей** на счетах OTC (обмен из USDT в RUB для выплаты будет осуществляться по биржевому курсу при запросе выплаты) — <mark style="color:red;">**опция работает только для выплат в RUB**</mark>

{% hint style="warning" %}
При выплате по валютам AZN, EUR, USD с использованием мерчанта **необходимо** добавить дополнительные поля в форму обмена для заполнения их клиентом при создании заявки.

Для этого добавьте [дополнительные поля](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/valyuty-i-napravleniya/dobavlenie-novoi-valyuty#vkladka-dop.-polya) к соответствующим валютам:\
![](<../../../.gitbook/assets/image (730).png>)![](<../../../.gitbook/assets/image (731).png>)

Обязательно укажите в поле "**Уникальный ID**" (указывайте названия в нижнем регистре):\
• `get_cardholder`(поле "[**Фамилия и имя**](#user-content-fn-1)[^1]")

• `get_cardexpire`(поле "[**Срок действия карты**](#user-content-fn-1)[^1]")

Пример заполнения дополнительного поля "**Срок действия карты**"\
![](<../../../.gitbook/assets/image (732).png>)
{% endhint %}

{% hint style="warning" %}
При выплате по СБП в настройках валюты на вкладке "**Настройки полей**" переименуйте поле "**На счет**" на "**Ваш номер телефона**" и оставьте только цифры доступными к заполнению поля в форме обмена.\
**Минимальный** лимит по выплате через СБП — **10000 RUB**.

![](<../../../.gitbook/assets/image (1406).png>)
{% endhint %}

{% hint style="warning" %}
Также при выплате через СБП вы можете предложить клиенту выбор банка на странице обмена (при этом выбор **способа оплаты** в настройках модуля не будет играть роли — выберите любой пункт из списка).

Для этого добавьте [дополнительное поле для **валюты выплаты**](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/valyuty-i-napravleniya/dobavlenie-novoi-valyuty#vkladka-dop.-polya) с типом доп. поля "**Выбор**", указав следующие настройки (названия банков и их коды указаны на скриншоте ниже, вы можете указать только используемые банки в списке в настройках доп. поля):\
![](<../../../.gitbook/assets/image (507).png>)

• Корректно заполненное доп. поле с уникальным ID — **bankname:**

![](<../../../.gitbook/assets/image (509).png>)\
&#xNAN;**`Сбербанк / Сбер`**\
**`Тинькофф / Тинькофф Банк`**\
**`Банк ВТБ`**\
**`АЛЬФА-БАНК`**\
**`Райффайзенбанк`**\
**`Банк ОТКРЫТИЕ`** \
**`Газпромбанк`**\
**`Промсвязьбанк`**\
**`Хоум кредит`**

После добавления поля, оно будет отображаться в форме обмена, где клиент сможет выбрать банк из списка, от которого ему поступят средства от обменника, самостоятельно.

![](<../../../.gitbook/assets/image (510).png>)
{% endhint %}

## Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-merchantov-avtovyplat).

[^1]: поле может иметь любое название
