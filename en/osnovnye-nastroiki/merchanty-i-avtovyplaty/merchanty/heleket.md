# Heleket

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере - воспользуйтесь [инструкцией](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat)
{% endhint %}

{% hint style="danger" %}
С 23 июня 2025 года при первом платеже на каждый новый статический адрес (пункт "**Address**" в настройках модуля мерчанта) в сети USDT TRC20 будет взиматься дополнительная комиссия в размере 1 TRX.

Это изменение не затрагивает статические адреса в других валютах и сетях (например, USDT BEP20 и другие) и временные адреса (пункт "**Invoice**").

![](<../../../.gitbook/assets/image (73).png>)
{% endhint %}

## Настройки в личном кабинете мерчанта

Пройдите регистрацию/авторизацию в системе [Heleket](https://dash.heleket.com/signup).

{% hint style="warning" %}
Для подключения к сервису и получения специального тарифа для обменника, свяжитесь с [представителем сервиса Heleket](https://t.me/business_Heleket) в Телеграм и сообщите, что вы пришли по рекомендации от Premium Exchanger.&#x20;

**Дисклеймер**: при подключении вашего сайта к тому или иному сервису, самостоятельно пожалуйста оценивайте возможные риски сотрудничества.
{% endhint %}

Перейдите в раздел "**Merchants**"

<figure><img src="../../../.gitbook/assets/image (2141).png" alt="" width="563"><figcaption></figcaption></figure>

Нажмите на кнопку "**Create merchant**".

<figure><img src="../../../.gitbook/assets/image (2134).png" alt=""><figcaption></figcaption></figure>

В открывшемся окне укажите имя вашего проекта и нажмите "**Create merchant**".

<figure><img src="../../../.gitbook/assets/image (2133).png" alt="" width="563"><figcaption></figcaption></figure>

После успешного добавления продавца перейдите к его настройке.

<figure><img src="../../../.gitbook/assets/image (2135).png" alt="" width="375"><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (2136).png" alt=""><figcaption></figcaption></figure>

Отправьте запрос на получения доступа к API для вашего сайта.

<figure><img src="../../../.gitbook/assets/image (2137).png" alt=""><figcaption></figcaption></figure>

В поле "**Merchant ID**" будет указан ID вашего мерчанта, сохраните его в текстовый файл.

<figure><img src="../../../.gitbook/assets/image (2140).png" alt="" width="414"><figcaption></figcaption></figure>

Укажите домен и название вашего сайта.

<figure><img src="../../../.gitbook/assets/image (2138).png" alt="" width="563"><figcaption></figcaption></figure>

Подтвердите владение доменом с помощью любого из трех пунктов (самый быстрый вариант — HTML-файл в корневой папке сайта).

<figure><img src="../../../.gitbook/assets/image (2139).png" alt="" width="563"><figcaption></figcaption></figure>

Ожидайте завершения модерации вашего проекта.

На вкладке "**API Integration**" в настройках мерчанта будут отображаться ID мерчанта, а также ключи для приема и выплаты средств.

<figure><img src="../../../.gitbook/assets/image (2142).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (2146).png" alt="" width="563"><figcaption></figcaption></figure>

При необходимости перегенерируйте ключ и сохраните все данные в текстовый файл.

## Настройки модуля

В панели администратора в разделе "**Мерчанты**" -> "**Мерчанты"** нажмите кнопку "**Добавить**" и выберите Heleket.

<figure><img src="../../../.gitbook/assets/image (2130).png" alt="" width="443"><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/image (1199).png" alt="" width="460"><figcaption></figcaption></figure>

**Merchant ID** — **Merchant ID** из личного кабинета Heleket

**Api key** — **Payment API key**, сгенерированный в личном кабинете Heleket

## Особые поля

<figure><img src="../../../.gitbook/assets/image (1500).png" alt="" width="329"><figcaption></figcaption></figure>

**Тип** — тип кошелька, который будет выдаваться в заявке (новый кошелек для каждой заявки)\
• **Invoice** — временный адрес кошелька, создаваемый для конкретной сделки, имеет ограничение по времени жизни после выдачи в заявке (прием средств на этот кошелек **ограничен по времени** — 12 часов, начиная с момента выдачи в заявке)\
&#xNAN;_&#x414;ля этого типа кошелька требуется создать задание cron на сервере._\
• **Address** — постоянный адрес кошелька, который привязывается к вашему ЛК у мерчанта, без ограничения по времени жизни (прием средств на этот кошелек **не ограничен по времени**)\
&#xNAN;_&#x421;татус оплаты проверяется по коллбэку, задание Cron для этого типа кошелька не требуется._

{% hint style="warning" %}
При использовании инвойсов рекомендуем указывать это в тексте заявки, чтобы клиент не отправлял средства на кошелек после того, как срок жизни инвойса истёк
{% endhint %}

**Код валюты** — укажите код принимаемой валюты согласно требованиям мерчанта

**Сеть** — укажите сеть принимаемой валюты согласно требованиям мерчанта

{% hint style="info" %}
**Полезные ссылки:**

Комиссии мерчанта (информация доступна только авторизованным пользователям) —[dash.heleket.com/ru/business/merchant/{id\_вашего\_мерчанта}/commissions](https://dash.heleket.com/ru/business/merchant/ccc8c2c5-0966-40ed-b35d-40554d0d0791/commissions)\
![](<../../../.gitbook/assets/image (74).png>)

Перечень доступных валют и сетей — [doc.heleket.com/ru/other/reference](https://doc.heleket.com/ru/other/reference)
{% endhint %}

{% hint style="warning" %}
Вы можете конвертировать принимаемую от клиента валюту в USDT по рыночному курсу — для этого включите опцию для подходящих валют в настройках мерчанта:

![](<../../../.gitbook/assets/image (2144).png>)\


Список валют, для которых можно подключить автоконвертацию:

![](<../../../.gitbook/assets/image (2145).png>)
{% endhint %}

## Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).
