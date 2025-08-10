# Utopia

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat)
{% endhint %}

## Настройки на стороне мерчанта

{% hint style="warning" %}
Первоначальную настройку сервиса на вашем сервере вам поможет произвести техподдержка мерчанта:

* Utopia Messenger: UNKNOWN1\
  ![](<../../../.gitbook/assets/image (248).png>)
* Telegram: [@utp1984](https://t.me/utp1984)
* Email: [1984@u.is](mailto:1984@u.is)
{% endhint %}

Скачайте [приложение Utopia](https://u.is/en/download.html) под вашу операционную систему и установите его. Пройдите процесс регистрации и создайте новый кошелек.

<figure><img src="../../../.gitbook/assets/utopia_GuMWxeYqQj.png" alt="" width="375"><figcaption><p>Создание аккаунта</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/utopia_6KVpKP7MqV.png" alt="" width="563"><figcaption><p>Заполните указанные поля</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/utopia_1dTGinQV89.png" alt="" width="563"><figcaption><p>Укажите путь до папки, где будет храниться приватный ключ и придумайте пароль для кошелька </p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/utopia_HDeIfnYgkC.png" alt="" width="563"><figcaption><p>Генерация приватного ключа</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/utopia_G9GdSU4r7V.png" alt="" width="563"><figcaption><p>Публичный ключ — это адрес вашего кошелька</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/utopia_mRDQ9jaNO5.png" alt="" width="563"><figcaption><p>Главная страница приложения</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/utopia_N9Et2UDpXJ.png" alt="" width="326"><figcaption><p>Доступные валюты</p></figcaption></figure>

## Настройки модуля

В панели администратора создайте нового мерчанта в разделе "**Мерчанты**" -> "**Добавить мерчант".**

Выберите Utopia в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../.gitbook/assets/image (1989).png" alt="" width="418"><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/image (1990).png" alt="" width="452"><figcaption></figcaption></figure>

**Домен** — URL для подключения (IP-адрес вашего сервера + порт, присвоенный приложению при первоначальной настройке)

**Токен** — публичный ключ (адрес вашего кошелька, полученный при регистрации в сервисе)

{% hint style="info" %}
Для корректной выдачи реквизитов код валюты из "Отдаю" должен быть выбран как USD, UUSD или CRP (токен Crypton)

![](<../../../.gitbook/assets/image (199).png>)
{% endhint %}

## Модуль Utopia Voucher

Для приема в качестве платежа ваучеров Utopia настройте отдельный модуль.

### Настройки модуля

В панели администратора создайте нового мерчанта в разделе "**Мерчанты**" -> "**Добавить мерчант".**

Выберите Utopia Voucher в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../.gitbook/assets/image (200).png" alt="" width="471"><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/image (1990).png" alt="" width="452"><figcaption></figcaption></figure>

**Домен** — URL для подключения (IP-адрес вашего сервера + порт, присвоенный приложению при первоначальной настройке)

**Токен** — публичный ключ (адрес вашего кошелька, полученный при регистрации в сервисе)

{% hint style="warning" %}
Для корректного приема ваучеров код валюты из "**Отдаю**" должен быть равен UUSD (американский доллар) или CRP (нативный токен Utopia)

<img src="../../../.gitbook/assets/image (201).png" alt="" data-size="original">

В форме обмена не требуется добавлять поле "**Со счета**" для валюты "**Отдаю**" — в созданной заявке клиенту будет отображаться кнопка "**Перейти к оплате**", по нажатию которой откроется страница с полем для ввода кода ваучера. После воода корректного кода клиент будет перенаправлен обратно на страницу заявки.
{% endhint %}

## Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).\
