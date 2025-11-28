# Exnode

{% hint style="danger" %}
<mark style="color:red;">Перед настройкой автовыплат обязательно прочитайте</mark> [<mark style="color:blue;">предупреждение о рисках</mark>](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/preduprezhdenie-o-riskakh)<mark style="color:blue;">!</mark>
{% endhint %}

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat)
{% endhint %}

{% hint style="warning" %}
Так как коллбэки от Exnode могут фильтроваться Cloudflare (если он используется вами), необходимо запросить актуальные IP-адреса у Exnode и добавить их в белый список по [инструкции](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/dobavlenie-ip-adresov-v-whitelist-v-cloudflare)
{% endhint %}

## Настройки в личном кабинете мерчанта

{% hint style="warning" %}
Для обсуждения условий и подключения, свяжитесь с [представитлем сервиса](https://t.me/exnode_crypto).

**Дисклеймер**: при подключении вашего сайта к тому или иному сервису, самостоятельно пожалуйста оценивайте возможные риски сотрудничества.
{% endhint %}

Пройдите регистрацию в системе [Exnode](https://pay.exnode.ru/).

Зайдите в личный кабинет, раздел "**Настройки**" и выпустите API-ключи.

<figure><img src="../../../.gitbook/assets/image (1373).png" alt="" width="563"><figcaption></figcaption></figure>

После нажатия на кнопку "**Поменять**" обновите страницу — в разделе "**API - ключи**" будет отображаться ваша [пара ключей](#user-content-fn-1)[^1], скопируйте их по соответствующей кнопке и сохраните в текстовом файле.

<figure><img src="../../../.gitbook/assets/image (1374).png" alt="" width="319"><figcaption></figcaption></figure>

## **Настройки модуля**

В панели администратора создайте нового мерчанта в разделе "**Автовыплаты**" -> "**Добавить автовыплату".**

Выберите Exnode в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../.gitbook/assets/image (1375).png" alt=""><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/image (1376).png" alt=""><figcaption></figcaption></figure>

**Privatу Key** - приватный ключ, сгенерированный в ЛК Exnode при создании API-ключа

**Public key** - публичный ключ, сгенерированный в ЛК Exnode при создании API-ключа

### Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-merchantov-avtovyplat).

## Особые поля

<figure><img src="../../../.gitbook/assets/image (1378) (1).png" alt=""><figcaption></figcaption></figure>

**Код валюты** — выберите из выпадающего списка валюту, которую будете выплачивать

{% hint style="warning" %}
Для каждой валюты необходимо создать [отдельную копию модуля автовыплаты](#user-content-fn-2)[^2], в которой выбрать соответствующую валюту, а затем подключить эту копию на вкладке "**Мерчанты и выплаты**" в настройках направления обмена, где в валюте "**Получаю**" будет выбранная валюта

<img src="../../../.gitbook/assets/image (1380).png" alt="" data-size="original">
{% endhint %}

[^1]: публичный и приватный

[^2]: укажите индивидуальное название для каждой копии в поле "Заголовок" для удобства последующей настройки
