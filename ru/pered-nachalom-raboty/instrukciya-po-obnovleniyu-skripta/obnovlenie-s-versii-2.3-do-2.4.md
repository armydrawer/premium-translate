# Обновление с версии 2.3 до 2.4

{% embed url="https://www.youtube.com/watch?v=PpNKzThZsCs" %}
Видеоинструкция по обновлению скрипта
{% endembed %}

{% hint style="warning" %}
Перед началом обновление скрипта, выполните обновление на сервере Ioncube Loader до версии 12.0 и выше (если установленная версия ниже 12 — [**инструкция по проверке установленной версии**](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-obnovit-ioncube-loader)). В обновлении поможет техническая поддержка вашего хостинга.
{% endhint %}

{% hint style="warning" %}
Если вы используете модули мерчантов и автовыплат, разработанными нами персонально для вас **—** запросите обновленные модули в вашей группе в Телеграм (**не в технической поддержке через бота**).

Если вы используете модули мерчантов и автовыплат, а также другие типы модулей от сторонних разработчиков, то они не будут работать на версии 2.4 без их обновления со стороны разработчиков.
{% endhint %}

{% hint style="danger" %}
<mark style="color:red;">**Перед обновлением обязательно сделайте резервную копию сайта и базы данных!**</mark>

В случае, если во время обновления что-то пойдет не так, вы всегда сможете восстановить сайт из резервной копии. Способы резервного копирования могут отличаться в зависимости от хостинга, поэтому вам стоит обратиться в техническую поддержку вашего хостинга с данным вопросом.

Самый простой способ [**сделать резервную копию сайта**](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-sdelat-bekap-saita) — через панель управления сервером (ISP Manager или другое ПО) с помощью встроенного в панель файлового менеджера или через FTP-клиент (скачайте на компьютер файлы сайта, а также в разделе управления базами данных или через PhpMyAdmin скачайте БД сайта).
{% endhint %}

1.  В панели управления обменником в разделе "**Консоль**" включите технический режим работы обменника, чтобы пользователи обменника не совершали заявки на сайте во время обновления скрипта.

    <figure><img src="../../.gitbook/assets/image (1724).png" alt=""><figcaption></figcaption></figure>
2.  В разделе "**Плагины**" деактивируйте плагины "**Premium Exchanger**" и "**Premium Exchanger hooks**".

    <figure><img src="https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FkanwK9s5DFo0cPzJd5Qn%252Fimage.png%3Falt%3Dmedia%26token%3D20ad3b3d-d619-4685-9146-08966a0d94f0&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=3b6bd9f3590a5f0a5aaa0d90711dfee97002c88ddb0f638e89ec840df877542a" alt=""><figcaption></figcaption></figure>
3. С помощью FTP-клиента или файлового менеджера удалите на сервере содержимое папки **`/wp-content/plugins/premiumbox/`**, **кроме** следующих файлов и папок внутри неё:

* **`/flags/`**
* **`/languages/`**
* **`/merchants/`** (если вы не меняли названия файлов и папок внутри папки **`merchants`** — можете её также удалить)
* **`/moduls/`**

{% hint style="warning" %}
Если вы **используете** модуль Webmoney, не удаляйте папку **`x19`** внутри папки **`moduls`**, если не используете — можете удалить папку **`moduls`** целиком)
{% endhint %}

* **`/paymerchants/`** (если вы **не меняли** названия файлов и папок внутри папки **`paymerchants`** — можете её также удалить)
* **`/sms/`**
* **`/userdata.php`**

<figure><img src="https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FZnqfDaglTQ0LigKamF9G%252Fimage.png%3Falt%3Dmedia%26token%3D1bd35a48-772d-4170-a33e-9a3eadb3a014&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=41f54ff04d225224f01677ab6ed6cb37b5453bb1b682544b766d2ce8b248a73f" alt=""><figcaption></figcaption></figure>

4. Перейдите в раздел "[**Ваши лицензии**](https://premiumexchanger.com/ulicense/)" и скачайте архив с файлами лицензии `license.zip`. Для этого нажмите на ссылку "**Скачать для версии 2.4**".

<figure><img src="../../.gitbook/assets/image (1726).png" alt="" width="491"><figcaption></figcaption></figure>

Скачанный архив загрузите в [корневую папку вашего сайта](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-naiti-kornevuyu-papku-saita-na-servere) под <mark style="color:green;">**пользователем, созданным для сайта**</mark> (не <mark style="color:red;">**root**</mark>!) и **обязательно** распакуйте архив.

{% hint style="warning" %}
**Выполните шаг 4 в обязательном порядке, даже если файлы лицензии были ранее загружены на сервер — в противном случае сайт не будет работать!**
{% endhint %}

5. Перейдите в раздел "[**Ваши скрипты**](https://premiumexchanger.com/uscripts/)" и на странице скачайте архив с **файлами для обновления версии 2.4** под вашу версию PHP.

{% hint style="warning" %}
Необходимо точно знать версию PHP, установленную на вашем сервере, для выбора подходящего архива.

\
[**Инструкция по проверке версии PHP, установленной на сервере**](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-proverit-versiyu-php-ustanovlennuyu-na-servere)
{% endhint %}

<figure><img src="../../.gitbook/assets/image (431).png" alt="" width="563"><figcaption></figcaption></figure>

6. Загрузите содержимое архива с обновлением в корневую папку вашего сайта под <mark style="color:green;">**пользователем, созданным для сайта**</mark> (не <mark style="color:red;">**root**</mark>!). Используйте FTP-клиент, либо файловый менеджер. Распакуйте архив с заменой файлов.
7. Перейдите в раздел "**Плагины**" и активируйте плагины "**Premium Exchanger"** и "**Premium Exchanger hooks**".
8. Перейдите в раздел **Настройки обменника" → "Миграция"** и в блоке "**Миграция (если версия меньше 2.4)**" поочередно выполните каждый шаг.

<figure><img src="../../.gitbook/assets/image (432).png" alt=""><figcaption></figcaption></figure>

При запуске каждого шага система определит общее количество запросов, которые нужно выполнить. У вас есть возможность задать количество запросов, которое будет обработано за один цикл.

<figure><img src="https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FFWLOCy5yHQlES4XZhyNP%252Fimage.png%3Falt%3Dmedia%26token%3D816f2042-40ad-417d-a819-dbab4d1cdaed&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=4f8942c4fdec930998beb26d9d6e249c4bda071b60c73d1199f594510b85daed" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
По умолчанию количество запросов = 50. Если вы не уверены в мощности вашего сервера, то рекомендуем не менять значение по умолчанию.

При необходимости вы можете указать любое другое значение, но если выполнение цикла с указанным значением окажется слишком ресурсоемким для сервера — это вызовет ошибку.
{% endhint %}

{% hint style="info" %}
Вы можете увидеть кнопки "**Технический шаг X**" рядом с кнопками "**Шаг X**". Перед выполнением каждого шага, система определяется количество запросов, которые необходимо выполнить. В некоторых случаях количество запросов может быть слишком велико и сервер может не справиться с их подсчетом. В этом случае вместо кнопки "**Шаг X**" стоит использовать кнопку "**Технический шаг X**", которая позволяет задавать произвольное количество запросов вручную без подсчета количества запросов сервером.

Если вы используете **технический шаг**, то вам необходимо задать вручную количество запросов. Рекомендуем установить заведомо большое число, например, 100000.
{% endhint %}

9. Перейдите в раздел "**Настройки" → "Постоянные ссылки"** и нажмите на кнопку "**Сохранить изменения**", не внося никаких изменений на странице.
10. Перейдите в раздел "**Настройки обменника" → "Основные настройки"** и отключите режим обновления.

<figure><img src="../../.gitbook/assets/image (430).png" alt=""><figcaption></figcaption></figure>

Альтернативный вариант — в этом же разделе для параметра "**Режим обновления**" выберите "**Нет**" и сохраните изменения.

<figure><img src="https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FD5YdRKPsWXynjlHPwdlM%252Fimage.png%3Falt%3Dmedia%26token%3D4bd5505a-e775-4478-b296-7d2bc5674825&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=18e1d61f8a35ed927e0d7be63e76703a80a07fda96c68b7bfa5405c5caf7da73" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
Режим обновления активируется каждый раз после деактивации и повторной активации основного плагина, поэтому режим всегда необходимо отключать вручную.
{% endhint %}

11. [Очистите кэш в браузере](https://www.unisender.com/ru/blog/kak-ochistit-kehsh-v-brauzerah/).
12. <mark style="color:red;">**Обязательно удалите из корневой папки на сервере все ранее загруженные zip-архивы скрипта и бэкапы сайта, а также файл damp\_db.sql.**</mark>
13. Отключите режим технического обслуживания.
