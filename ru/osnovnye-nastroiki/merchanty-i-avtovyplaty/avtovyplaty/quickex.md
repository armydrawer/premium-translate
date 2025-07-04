# Quickex

{% hint style="danger" %}
<mark style="color:red;">Перед настройкой автовыплат обязательно прочитайте</mark> [<mark style="color:blue;">предупреждение о рисках</mark>](https://premiumexchanger.com/wiki/preduprezhdenie-auto/)<mark style="color:blue;">!</mark>
{% endhint %}

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-avtovyplat)
{% endhint %}

## Настройки в личном кабинете мерчанта <a href="#nastroiki-v-lichnom-kabinete-merchanta" id="nastroiki-v-lichnom-kabinete-merchanta"></a>

{% hint style="warning" %}
Обращаем ваше внимание, что модуль автовыплаты технический и **не производит** саму выплату — модуль на приём Quickex производит выплату сразу же после поступления средств от клиента, а модуль автовыплаты подтверждает выплату средств для изменения статуса заявки на "**Выполненная**".&#x20;

Использовать модуль автовыплаты Quickex **всегда необходимо** в паре с [модулем на приём](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/quickex).

Также необходимо учитывать, что выплата средств **всегда** производится по курсу самого сервиса, поэтому крайне желательно использовать [парсер](https://premium.gitbook.io/main/osnovnye-nastroiki/valyuty-i-napravleniya-obmena/kursy-valyut/parser-kursov-valyut-parsery-2.0) Quickex для курса в направлении обмена, где используется Quickex, а также включить [пересчет заявок по курсу обмена](https://premium.gitbook.io/main/osnovnye-nastroiki/valyuty-i-napravleniya-obmena/sozdanie-novogo-napravleniya#pereschet-po-kursu-obmena) для совпадения фактически выплачиваемой суммы с суммой из заявки.
{% endhint %}

## Настройки модуля <a href="#nastroiki-modulya" id="nastroiki-modulya"></a>

В панели администратора создайте нового мерчанта в разделе "**Автовыплаты**" ➔ "**Добавить автовыплату".**

Выберите Quickex в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../.gitbook/assets/image (29).png" alt="" width="389"><figcaption></figcaption></figure>

Авторизационные поля заполнять не требуется.

<figure><img src="https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252Fhcpgo0esYP63gs8hEYlt%252Fimage.png%3Falt%3Dmedia%26token%3D601c0074-951c-408a-b11c-7856129e1e3d&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=1fde9588&#x26;sv=2" alt="" width="563"><figcaption></figcaption></figure>

**Домен —** поле заполняется только в случае, если вам дополнительно написал об этом менеджер Quickex (во всех остальных случаях поле остается пустым)

## Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-merchantov-avtovyplat).
