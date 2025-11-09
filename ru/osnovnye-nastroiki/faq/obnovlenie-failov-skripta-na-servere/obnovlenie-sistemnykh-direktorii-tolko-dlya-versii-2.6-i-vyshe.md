# Обновление системных директорий (только для версии 2.6 и выше)

Данное обновление **требуется** произвести в целях повышения безопасности работы скрипта.

Файлы скрипта всегда должны загружаться и быть распакованы на сервере из-под <mark style="color:green;">**пользователя, созданного для сайта**</mark> **(**&#x43D;е <mark style="color:red;">**root**</mark>**)**!

{% hint style="info" %}
Ниже дана инструкци по обновления файлов всего скрипта, но вы можете обновить только следующие папки:\
`\wp-content\plugins\premiumbox\default\admin`\
&#x20;`\wp-content\plugins\premiumbox\default\users`\
&#x20;`\wp-content\plugins\premiumbox\premium\includes`

Учитывайте, что если у вас есть собственные доработки в коде модуля, они будут затерты файлами из официального дистрибутива при обновлении файлов (в этом случае замените  их модифицированными файлами файлы после обновления скрипта из сделанного бэкапа)&#x20;
{% endhint %}

Вам необходимо:

* Сделать [бэкап всех файлов сайта на сервере](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-sdelat-bekap-saita)
* Скачать [дистрибутив **для обновления**](https://premiumexchanger.com/uscripts/) **под вашу версию скрипта** (версия PHP не имеет значения — выберите любой из дистрибутивов)

<figure><img src="../../../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="523"><figcaption></figcaption></figure>

<figure><img src="https://premium.gitbook.io/main/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252F1ANz8GezorAjnZIR1Gyf%252Fimage.png%3Falt%3Dmedia%26token%3D243ee6d1-6049-4fdc-98ee-a27b20c1578e&#x26;width=300&#x26;dpr=4&#x26;quality=100&#x26;sign=5ad34fa2&#x26;sv=2" alt="" width="563"><figcaption></figcaption></figure>

*   Загрузить архив в [корневую папку сайта](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-naiti-kornevuyu-papku-saita-na-servere)&#x20;

    <figure><img src="../../../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

и распаковать его с заменой существующих файлов

<figure><img src="../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (4) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="531"><figcaption></figcaption></figure>

Обновление файлов завершено!
