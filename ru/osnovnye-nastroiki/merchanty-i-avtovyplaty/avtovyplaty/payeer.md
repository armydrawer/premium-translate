# Payeer

{% hint style="danger" %}
<mark style="color:red;">Перед настройкой автовыплат обязательно прочитайте</mark> [<mark style="color:blue;">предупреждение о рисках</mark>](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/preduprezhdenie-o-riskakh)<mark style="color:blue;">!</mark>
{% endhint %}

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-avtovyplat)
{% endhint %}

{% hint style="danger" %}
В связи с тем, что Payeer всегда округляет комиссию за транзакцию в большую сторону, ваши клиенты могут получать сумму либо больше заявленной, либо меньше заявленной. Погрешность возможна до десятых долей.
{% endhint %}

## Настройки в личном кабинете мерчанта

1. Пройдите регистрацию/авторизацию в системе [Payeer](https://payeer.com/).
2. Пройдите верификацию аккаунта в разделе "**Профиль и верификация**" для использования API.
3. Пройдите процедуру подтверждения вашего домена.

<figure><img src="../../../.gitbook/assets/image (954).png" alt="" width="524"><figcaption></figcaption></figure>

4. Перейдите в раздел "**API" -> "Массовые выплаты**" и нажмите кнопку "**Добавить**". Заполните указанные поля и нажмите "**Добавить АПИ**".

* **Название** — название сервиса в ЛК мерчанта, произвольное название&#x20;
* **Секретный ключ** — ключ, который будет использоваться для авторизации в API
* **IP-адрес** — IP-адрес вашего сервера

<figure><img src="../../../.gitbook/assets/image (1542).png" alt="" width="563"><figcaption></figcaption></figure>

## Настройки модуля

В панели администратора в разделе "**Мерчанты**" -> "**Автовыплаты"** нажмите кнопку "**Добавить**" и выберите Payeer.

<figure><img src="../../../.gitbook/assets/image (1539).png" alt="" width="490"><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/image (1540).png" alt="" width="446"><figcaption></figcaption></figure>

**Номер кошелька** — кошелек, указанный в личном кабинете Payeer

**API ID**  — ID из личного кабинета Payeer

**API ключ** — секретный ключ из личного кабинета Payeer

## Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).
