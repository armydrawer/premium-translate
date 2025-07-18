# Как обновить WordPress?

{% hint style="info" %}
Мы рекомендуем обновлять WordPress при выходе каждой свежей версии с индексом **x.x.1-9** (к примеру **6.4.3**), так как в версии **x.x.0** (к примеру, **6.4.0**) могут содержаться ошибки, которые обычно бывают исправлены в **x.x.1**.
{% endhint %}

Чтобы обновить WordPress, необходимо:

1. Выполнить резервное копирование файлов и базы данных. Если этого не сделать, то в случае возникновения проблем при обновлении будет сложно восстановить работу сайта.
2. Открыть файл `wp-config.php` на сервере ([корневая папка](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-naiti-kornevuyu-papku-saita-na-servere)).

<figure><img src="../../../.gitbook/assets/image (1572).png" alt="" width="394"><figcaption></figcaption></figure>

3. Для указанной ниже строки параметр **true** на период обновления WP заменить на **false**. Сохранить изменения.

<figure><img src="../../../.gitbook/assets/изображение (108).png" alt=""><figcaption><p>define('DISALLOW_FILE_MODS', false);</p></figcaption></figure>

4. В панели управления сайтом перейти в раздел "**Консоль" → "Обновления"** и нажать кнопку "**Обновить до версии х.х.х**".

<figure><img src="../../../.gitbook/assets/изображение (153).png" alt=""><figcaption></figcaption></figure>

5. В файле `wp-config.php` для указанной ниже строки параметр **false** заменить обратно на **true**. Сохранить изменения.

<figure><img src="../../../.gitbook/assets/изображение (26).png" alt=""><figcaption><p>define('DISALLOW_FILE_MODS', true);</p></figcaption></figure>

После этого у вас будет установлена актуальная версия WordPress.
