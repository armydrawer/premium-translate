# Heleket

{% hint style="danger" %}
<mark style="color:red;">Перед настройкой автовыплат обязательно прочитайте</mark> [<mark style="color:blue;">предупреждение о рисках</mark>](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/preduprezhdenie-o-riskakh)<mark style="color:blue;">!</mark>
{% endhint %}

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat)
{% endhint %}

## Настройки в личном кабинете мерчанта

Пройдите регистрацию/авторизацию в системе [Heleket](https://dash.heleket.com/signup).

{% hint style="warning" %}
Для подключения к сервису и получения специального тарифа для обменника, свяжитесь с [представителем сервиса Heleket](https://t.me/business_Heleket) в Телеграм и сообщите, что вы пришли по рекомендации от Premium Exchanger.

**Дисклеймер**: при подключении вашего сайта к тому или иному сервису, самостоятельно пожалуйста оценивайте возможные риски сотрудничества.
{% endhint %}

Перейдите в раздел "**Merchants**"

<figure><img src="../../../.gitbook/assets/image (2082).png" alt="" width="563"><figcaption></figcaption></figure>

Нажмите на кнопку "**Create merchant**".

<figure><img src="../../../.gitbook/assets/image (2075).png" alt=""><figcaption></figcaption></figure>

В открывшемся окне укажите имя вашего проекта и нажмите "**Create merchant**".

<figure><img src="../../../.gitbook/assets/image (2074).png" alt="" width="563"><figcaption></figcaption></figure>

После успешного добавления продавца перейдите к его настройке.

<figure><img src="../../../.gitbook/assets/image (2076).png" alt="" width="375"><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (2077).png" alt=""><figcaption></figcaption></figure>

Отправьте запрос на получения доступа к API для вашего сайта.

<figure><img src="../../../.gitbook/assets/image (2078).png" alt=""><figcaption></figcaption></figure>

В поле "**Merchant ID**" будет указан ID вашего мерчанта, сохраните его в текстовый файл.

<figure><img src="../../../.gitbook/assets/image (2081).png" alt="" width="414"><figcaption></figcaption></figure>

Укажите домен и название вашего сайта.

<figure><img src="../../../.gitbook/assets/image (2079).png" alt="" width="563"><figcaption></figcaption></figure>

Подтвердите владение доменом с помощью любого из трех пунктов (самый быстрый вариант — HTML-файл в корневой папке сайта).

<figure><img src="../../../.gitbook/assets/image (2080).png" alt="" width="563"><figcaption></figcaption></figure>

Ожидайте завершения модерации вашего проекта.

Перейдите в раздел "**Settings**" ➔ "**API**" и выпустите новый ключ для автовыплаты по кнопке "**Generate**".

<figure><img src="../../../.gitbook/assets/image (2073).png" alt=""><figcaption></figcaption></figure>

Сохраните сгенерированный ключ в текстовый файл.

<figure><img src="../../../.gitbook/assets/image (2072).png" alt="" width="375"><figcaption></figcaption></figure>

На вкладке "**API Integration**" в настройках мерчанта будут отображаться ID мерчанта, а также ключи для приема и выплаты средств.

<figure><img src="../../../.gitbook/assets/image (2083).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (2084).png" alt="" width="563"><figcaption></figcaption></figure>

При необходимости перегенерируйте ключи и сохраните все данные в текстовый файл.

{% hint style="info" %}
Если вы используете мерчанта только на выплату средств — ключ для приема средств не требуется.
{% endhint %}

{% hint style="danger" %}
Обратите внимание, что вывод средств будет временно заблокирован (на 24 часа) после создания или перегенерации API ключа для выплаты (Payout API key).
{% endhint %}

## Настройки модуля

В панели администратора в разделе "**Мерчанты**" ➔ "**Автовыплаты"** нажмите кнопку "**Добавить**" и выберите Heleket.

<figure><img src="../../../.gitbook/assets/image (2070).png" alt="" width="440"><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/image (685).png" alt="" width="463"><figcaption></figcaption></figure>

**Merchant id** — **Merchant ID** из личного кабинета Heleket

**Api key** — **Payment API key**, сгенерированный в личном кабинете Heleket

**Payment api key** — **Payout API key**, сгенерированный в личном кабинете Heleket

## Особые поля

<figure><img src="../../../.gitbook/assets/image (511).png" alt=""><figcaption></figcaption></figure>

**Приоритет** — выберите размер комиссии, которая будет взиматься мерчантом (влияет на скорость обработки транзакций):\
• **recommended** — сбалансированная скорость и размер комиссии (рекомендуемый выбор)\
• **economy** — низкая скорость и низкая комиссия\
• **high** — высокая скорость и высокая комиссия\
• **highest** — максимальная скорость и очень высокая комиссия

**Комиссия** — выберите из выпадающего тип комиссии:\
• **По сумме** — комиссия будет взиматься из выплаты по заявке\
• **По балансу** — комиссия будет взиматься с вашего баланса у мерчанта при выплате

**Код валюты** — укажите код выплачиваемой валюты согласно требованиям мерчанта

**Сеть** — укажите сеть выплачиваемой валюты согласно требованиям мерчанта

**Код валюты (автоконвертация)** — активация выплаты из валюты с указанным кодом (обычно это USDT), без необходимости хранения **выплачиваемой валюты** на счетах Heleket (обмен из **валюты для покупки** в **валюту для выплаты** будет осуществляться по биржевому курсу при запросе выплаты)

{% hint style="info" %}
**Полезные ссылки:**

Комиссии мерчанта (информация доступна только авторизованным пользователям) —[dash.heleket.com/ru/business/merchant/{id\_вашего\_мерчанта}/commissions](https://dash.heleket.com/ru/business/merchant/ccc8c2c5-0966-40ed-b35d-40554d0d0791/commissions)\
![](<../../../.gitbook/assets/image (15).png>)

Перечень доступных валют и сетей — [doc.heleket.com/ru/other/reference](https://doc.heleket.com/ru/other/reference)
{% endhint %}

## Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-merchantov-avtovyplat).
