# Utopia

{% hint style="danger" %}
<mark style="color:red;">Перед настройкой автовыплат обязательно прочитайте</mark> [<mark style="color:blue;">предупреждение о рисках</mark>](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/preduprezhdenie-o-riskakh)<mark style="color:blue;">!</mark>
{% endhint %}

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-avtovyplat)
{% endhint %}

## Настройки на стороне мерчанта

{% hint style="info" %}
Первоначальную настройку сервиса на вашем сервере вам поможет произвести техподдержка мерчанта:

* Utopia Messenger: UNKNOWN1\
  ![](<../../../.gitbook/assets/image (248).png>)
* Telegram: [@utp1984](https://t.me/utp1984)
* Email: [1984@u.is](mailto:1984@u.is)
{% endhint %}

Скачайте [приложение Utopia](https://u.is/en/download.html) под вашу операционную систему и установите его. Пройдите процесс регистрации и создайте новый кошелек.

<figure><img src="../../../.gitbook/assets/image (1995).png" alt="" width="375"><figcaption><p>Создание аккаунта</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (1996).png" alt=""><figcaption><p>Заполните указанные поля</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (1998).png" alt=""><figcaption><p>Укажите путь до папки, где будет храниться приватный ключ и придумайте пароль для кошелька</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (1999).png" alt=""><figcaption><p>Генерация приватного ключа</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (2000).png" alt=""><figcaption><p>Публичный ключ — это адрес вашего кошелька</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (2003).png" alt=""><figcaption><p>Главная страница приложения</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (2001).png" alt="" width="326"><figcaption><p>Доступные валюты</p></figcaption></figure>

## Настройки модуля <a href="#nastroiki-modulya" id="nastroiki-modulya"></a>

В панели администратора создайте нового мерчанта в разделе "**Автовыплаты**" -> "**Добавить автовыплату".**

Выберите Utopia в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../.gitbook/assets/image (1992).png" alt="" width="390"><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/image (1993).png" alt="" width="428"><figcaption></figcaption></figure>

**API ключ** — ключ, скопированный в ЛК мерчанта

**Домен** — URL для подключения (IP-адрес вашего сервера + порт, присвоенный приложению при первоначальной настройке)

**Токен** — публичный ключ (адрес вашего кошелька, полученный при регистрации в сервисе)

{% hint style="info" %}
Для корректной выдачи реквизитов код валюты из "**Получаю**" должен быть выбран как USD, UUSD или CRP (токен Crypton)

![](<../../../.gitbook/assets/image (2002).png>)
{% endhint %}

## Модуль Utopia Voucher

В качестве выплаты ваучеров Utopia настройте отдельный модуль.

### Настройки модуля <a href="#nastroiki-modulya-1" id="nastroiki-modulya-1"></a>

В панели администратора создайте нового мерчанта в разделе "**Автовыплаты**" -> "**Добавить автовыплату".**

Выберите Utopia Voucher в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../.gitbook/assets/image (193).png" alt="" width="453"><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/image (1993).png" alt="" width="428"><figcaption></figcaption></figure>

**Домен** — URL для подключения (IP-адрес вашего сервера + порт, присвоенный приложению при первоначальной настройке)

**Токен** — публичный ключ (адрес вашего кошелька, полученный при регистрации в сервисе)

<figure><img src="../../../.gitbook/assets/image (193).png" alt="" width="453"><figcaption></figcaption></figure>

### Особые поля

<figure><img src="../../../.gitbook/assets/image (194).png" alt="" width="362"><figcaption></figcaption></figure>

**E-mail пользователя** — выберите тип поля, которое будет заполнять клиент в форме обмена — на указанный e-mail будет отправляться ваучер при автовыплате по заявке

{% hint style="info" %}
По умолчанию выбран пункт "**E-mail пользователя"** — обязательное поле, которое заполняет клиент при создании заявки.

![](<../../../.gitbook/assets/image (196).png>)

Если же вы хотите, чтобы клиент указывал отдельный e-mail, на который будет отправляться купон, переименуйте поле "**На счет**" в настройках валюты на "**E-mail, на который будет отправлен ваучер**" или "**E-mail для ваучера**"

![](<../../../.gitbook/assets/image (197).png>)
{% endhint %}

## Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-merchantov-avtovyplat).
