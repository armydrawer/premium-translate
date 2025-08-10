# Volet (ex-Advcash)

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat)
{% endhint %}

{% hint style="danger" %}
<mark style="color:red;">Перед настройкой автовыплат обязательно прочитайте</mark> [<mark style="color:blue;">предупреждение о рисках</mark>](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/preduprezhdenie-o-riskakh)<mark style="color:blue;">!</mark>
{% endhint %}

### Настройки в личном кабинете мерчанта <a href="#nastroiki-v-lichnom-kabinete-merchanta" id="nastroiki-v-lichnom-kabinete-merchanta"></a>

Пройдите регистрацию в системе [Volet](https://account.volet.com/register) и верифицируйте ваш аккаунт для работы с API.

{% hint style="warning" %}
Для приема средств на счета мерчанта достаточно создать **SCI (shopping cart interface)** по инструкции, указанной ниже. Если вы также хотите выплачивать средства со счетов мерчанта, то дополнительно создайте новый **API (application programming interface).**
{% endhint %}

Создайте новое API для работы с мерчантом.

Перейдите в раздел "**Для разработчиков**" и нажмите кнопку "**Создать новый API**".

<figure><img src="https://2722984412-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fm9kqZXsNykrN6VyxxXBO%2Fuploads%2F8psSPCSWSTp1eiIzISZY%2Fimage.png?alt=media&#x26;token=7fcdd5aa-7089-4f80-9182-1d30016517ca" alt="" width="188"><figcaption></figcaption></figure>

<figure><img src="https://2722984412-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fm9kqZXsNykrN6VyxxXBO%2Fuploads%2FBcpqskUKVk3ULEZiLhi7%2Fimage.png?alt=media&#x26;token=fcf15fff-1f8a-4914-9cbc-9edb4d625a09" alt=""><figcaption></figcaption></figure>

Заполните открывшуюся форму и нажмите "**Сохранить**".

<figure><img src="https://2722984412-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fm9kqZXsNykrN6VyxxXBO%2Fuploads%2FWmhrfWDVi8w3DV4id8XE%2Fimage.png?alt=media&#x26;token=c03423b1-5978-40bc-90bb-6432e2cbb3a3" alt="" width="375"><figcaption></figcaption></figure>

### Настройки модуля <a href="#nastroiki-modulya" id="nastroiki-modulya"></a>

В панели администратора создайте нового мерчанта в разделе "**Мерчанты**" -> "**Добавить автовыплату".**

Выберите AdvCash в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../.gitbook/assets/image (674).png" alt=""><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/image (675).png" alt=""><figcaption></figcaption></figure>

**Имя API** — **название API**, указанное в личном кабинете AdvCash&#x20;

**Email аккаунта** — **электронная почта**, указанная в личном кабинете AdvCash

**Пароль API** — **пароль для API**, указанный в личном кабинете AdvCash

**Номера кошельков** — укажите желаемые номера кошельков для выплаты фиатных валют из личного кабинета AdvCash

<figure><img src="../../../.gitbook/assets/image (676).png" alt=""><figcaption></figcaption></figure>

### Продолжение настройки <a href="#prodolzhenie-nastroiki" id="prodolzhenie-nastroiki"></a>

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-avtovyplat).
