# Webmoney

{% hint style="danger" %}
<mark style="color:red;">Перед настройкой автовыплат обязательно прочитайте</mark> [<mark style="color:blue;">предупреждение о рисках</mark>](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/preduprezhdenie-o-riskakh)<mark style="color:blue;">!</mark>
{% endhint %}

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-avtovyplat)
{% endhint %}

## Настройки в личном кабинете мерчанта

1. Авторизуйтесь на сайте [Webmoney ](https://merchant.webmoney.ru/conf/default.asp)под своим WMID или зарегистрируйтесь, если ещё не имеет аккаунта.
2. Активируйте [XML-интерфейс Х2](https://wiki.webmoney.ru/projects/webmoney/wiki/interfeys_x2). Рекомендуем [ограничить работу интерфейса X2](https://security.webmoney.ru/) по IP-адресу сервера. Если вы хотите получать резерв на кошельках в режиме реального времени, то вам необходимо также подключить [XML-интерфейс Х9](https://wiki.webmoney.ru/projects/webmoney/wiki/interfeys_x9).
3. В WebMoney Keeper Classic в пункте меню "**Инструменты" → "Параметры программы"** перейдите на вкладку **"Безопасность"** и нажмите кнопку **"Сохранить ключ в файл"**.\
   Пройдите процедуры, которые предлагает выполнить WM Keeper. Укажите путь для сохранения файла ключей, дважды введите пароль от файла ключей.

<figure><img src="../../../.gitbook/assets/Screenshot_36 (2).png" alt=""><figcaption></figcaption></figure>

4. Сохраненный файл ключей .kwm загрузите на сервер из-под пользователя, созданного для сайта (не root) в директорию:\
   `ваш_домен/wp-content/plugins/premiumbox/paymerchants/webmoney/dostup/`

## Настройки модуля

В панели администратора создайте нового мерчанта в разделе "**Мерчанты**" -> "**Добавить автовыплату".**

Выберите Webmoney в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../.gitbook/assets/image (1551).png" alt="" width="438"><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/image (1552).png" alt="" width="447"><figcaption></figcaption></figure>

**WMID** — укажите ваш WMID

**Имя файла ключей .kwm** — название файла ключей

**Пароль от файла ключей .kwm** — пароль от файла ключей

**WM\* кошелек** — номер вашего кошелька из ЛК Webmoney

## Продолжение настройки

Далее произведите настройку мерчанта автовыплаты следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-merchantov-avtovyplat).
