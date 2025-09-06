# WebMoney

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере - воспользуйтесь [инструкцией](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat)
{% endhint %}

{% hint style="warning" %}
В целях безопасности ваших средств в системе WebMoney настоятельно рекомендуем вам включить следующие настройки в разделе "[Подтверждение операций](https://security.webmoney.ru/asp/transconfirm.asp)": E-NUM-подтверждение, SMS-подтверждение.

![](<../../../../.gitbook/assets/image (1609).png>)

**Примечание:** По умолчанию мерчант оплаты "WebMoney" не производит автоматическую проверку персональных данных клиента через XML-интерфейс X19.

Для подключения автоматической проверки персональных данных через XML-интерфейс X19 вам потребуется дополнительно настроить модуль X19. Подробнее о работе данного модуля читайте в [соответствующем разделе](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/webmoney/x19).

Подробнее об XML-интерфейсе X19 и требованиям к обменным операция WebMoney читайте по [ссылке](https://wiki.webmoney.ru/projects/webmoney/wiki/%D0%98%D0%BD%D1%82%D0%B5%D1%80%D1%84%D0%B5%D0%B9%D1%81_X19).

Для ручной проверки персональных клиента данных используйте [официальный веб-интерфейс X19](https://verification.webmoney.ru/XTest/X19.aspx).

Требования к обменным пунктам, которые работают с WebMoney, читайте по [ссылке](https://www.megastock.ru/exchange_rules.aspx?lang=ru).
{% endhint %}

## Настройки в личном кабинете мерчанта

1. Авторизуйтесь на сайте [Webmoney ](https://merchant.webmoney.ru/conf/default.asp)под своим WMID или зарегистрируйтесь, если ещё не имеете аккаунта.
2. Перейдите в раздел "[**Список кошельков**](https://merchant.webmoney.ru/conf/purses.asp)" и перейдите по ссылке "**Настроить"** напротив каждого используемого кошелька

<figure><img src="../../../../.gitbook/assets/image (1602).png" alt=""><figcaption></figcaption></figure>

3. Настройте и сохраните следующие параметры:

* Выберите рабочий режим
* Укажите произвольное "**Торговое имя**". Например адрес вашего сайта
* Укажите "**Secret Key**", который потребуется для дальнейшей настройки
* Укажите адрес вашего сайта для параметров "**Result/Success/Fail URL**"
* Отметьте галочки для параметров "**Передавать параметры в предварительном запросе**" и "**Позволять использовать URL, передаваемые в форме**", "**Высылать оповещение об ошибке на кипер**"
* Для опции "**Метод формирования контрольной подписи"** выберите: "**SHA256**"

<figure><img src="../../../../.gitbook/assets/image (1606).png" alt=""><figcaption></figcaption></figure>

## Настройки модуля

В панели администратора создайте нового мерчанта в разделе "**Мерчанты**" -> "**Добавить мерчант".**

Выберите Webmoney в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../../.gitbook/assets/image (1608).png" alt="" width="442"><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../../.gitbook/assets/image (1607).png" alt="" width="454"><figcaption></figcaption></figure>

**WM\* кошелек** — номер вашего кошелька из ЛК Webmoney

**Secret Key WM\* кошелька** — секретный ключ, указанный вами в настройках кошелька

## Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).
