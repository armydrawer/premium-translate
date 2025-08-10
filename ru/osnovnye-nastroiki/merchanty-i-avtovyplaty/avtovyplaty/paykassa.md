# PayKassa

{% hint style="danger" %}
<mark style="color:red;">Перед настройкой автовыплат обязательно прочитайте</mark> [предупреждение о рисках](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/preduprezhdenie-o-riskakh)!
{% endhint %}

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере - воспользуйтесь [инструкцией](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-avtovyplat)
{% endhint %}

## Настройки в личном кабинете мерчанта

Пройдите регистрацию/авторизацию в системе [PayKassa](https://paykassa.pro/).

Перейдите в раздел "**API**" и нажмите кнопку "**Добавить API**"

<figure><img src="../../../.gitbook/assets/image (1255).png" alt=""><figcaption></figcaption></figure>

Заполните открывшуюся форму:

<figure><img src="../../../.gitbook/assets/image (1256).png" alt="" width="330"><figcaption></figcaption></figure>

**Название API** - любое подходящее название

**API Password** - пароль для авторизации в модуле мерчанта

**Описание API** - комментарий для созданного API

**Укажите список разрешенных IP-адресов, с указанием или без указания сетевой маски** - IP-адрес вашего сервера

В настройках созданного API вы найдете его ID.

<figure><img src="../../../.gitbook/assets/image (1257).png" alt=""><figcaption></figcaption></figure>

## **Настройки модуля**

В панели администратора в разделе "**Автовыплаты**" -> "**Автовыплаты"** нажмите кнопку "**Добавить**" и выберите PayKassa.

<figure><img src="../../../.gitbook/assets/image (1254).png" alt="" width="512"><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/image (1258).png" alt="" width="447"><figcaption></figcaption></figure>

**ID магазина для выплат** - необходимо создать мерчанта по [инструкции](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/paykassa#nastroiki-v-lichnom-kabinete-merchanta) и указать его ID

**API ID** - ID API из личного кабинета Paykassa

**API пароль** - пароль, сгенерированный Paykassa при создании мерчанта (API Password)

## Особые поля

<figure><img src="../../../.gitbook/assets/image (808).png" alt=""><figcaption></figcaption></figure>

**Тип транзакции** - выбор валюты/сети для автовыплаты

<figure><img src="../../../.gitbook/assets/image (814).png" alt=""><figcaption></figcaption></figure>

**Приоритет (только для сети Bitcoin)** - выбор количества [времени для проведения (валидации) транзакции](#user-content-fn-1)[^1], размер комиссии зависит от выбранного параметра (low - комиссия ниже, скорость валидации транзакции ниже, high - комиссия выше, скорость валидации транзакции выше)\
![](<../../../.gitbook/assets/image (813).png>)

## Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-merchantov-avtovyplat).

[^1]: Среднее время на транзакцию составляет от двадцати минут до часа, но когда сеть перегружена, то время транзакции многократно увеличивается
