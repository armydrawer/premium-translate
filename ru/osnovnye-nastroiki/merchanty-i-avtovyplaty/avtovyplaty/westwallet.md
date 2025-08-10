# WestWallet

{% hint style="danger" %}
<mark style="color:red;">Перед настройкой автовыплат обязательно прочитайте</mark> [<mark style="color:blue;">предупреждение о рисках</mark>](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/preduprezhdenie-o-riskakh)<mark style="color:blue;">!</mark>
{% endhint %}

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-avtovyplat)
{% endhint %}

{% hint style="danger" %}
Обратите внимание, что при обновлении файлов модуля автовыплаты WestWallet на сервере сбрасывается настройка размера комиссии за транзакцию на пункт **medium.**

Если до обновления  у вас было выбрано значение, отличное от **medium** — выберите его повторно в настройках модуля!

![](<../../../.gitbook/assets/image (1742).png>)
{% endhint %}

## Настройки в личном кабинете мерчанта

Пройдите регистрацию на сайте [WestWallet](https://westwallet.io/). После подтверждения регистрации сервисом, авторизуйтесь в личном кабинете и перейдите в раздел "**Настройки**".

<figure><img src="../../../.gitbook/assets/image (1412).png" alt=""><figcaption></figcaption></figure>

В разделе "**API ключи**" нажмите на кнопку "**Добавить API ключ**".

<figure><img src="../../../.gitbook/assets/image (1414).png" alt="" width="563"><figcaption></figcaption></figure>

В открывшемся окне отметьте необходимые права в зависимости от способа работы с мерчантом (для выплаты средств нужно отметить все пункты, кроме "**Генерировать адреса**").

Также желательно указать IP-адрес вашего сервера для большей безопасности работы с мерчантом.

Сохраните данные публичного и приватного ключа в текстовый файл. Нажмите кнопку "**Сохранить**".

<figure><img src="../../../.gitbook/assets/image (1413).png" alt="" width="438"><figcaption></figcaption></figure>

## Настройки модуля

В панели администратора создайте нового мерчанта в разделе "**Автовыплаты**" -> "**Добавить автовыплату".**

Выберите WestWallet в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../.gitbook/assets/image (689).png" alt="" width="505"><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/image (690).png" alt="" width="453"><figcaption></figcaption></figure>

**Публичный ключ** — публичный ключ, сгенерированный в ЛК WestWallet

**Приватный ключ** — приватный ключ, сгенерированный в ЛК WestWallet

### Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-avtovyplat).

## **Особые поля**

<figure><img src="../../../.gitbook/assets/image (691).png" alt=""><figcaption></figcaption></figure>

**Комиссия за транзакцию** — выберите размер комиссии, которая будет взиматься сервисом за предоставление услуг. Чем выше комиссия, тем быстрее будет совершена выплата.

{% hint style="danger" %}
Обратите внимание, что при выборе пункта "**low**" выплата будет производиться через 36-48 часов

![](<../../../.gitbook/assets/image (1632).png>)
{% endhint %}
