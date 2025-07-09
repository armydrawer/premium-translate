# How to Update WordPress

{% hint style="info" %}
We recommend updating WordPress whenever a new version with the format **x.x.1** is released (for example, **6.4.3**), because versions like **x.x** (for example, **6.4.0**) may contain bugs that are usually fixed in the **x.x.1** update.
{% endhint %}

To update WordPress, follow these steps:

1. Back up your files and database. If you skip this step, it will be difficult to restore your site if something goes wrong during the update.
2. Open the `wp-config.php` file on your server ([root folder location guide](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-naiti-kornevuyu-papku-saita-na-servere)).

<figure><img src="../../.gitbook/assets/image (1572).png" alt="" width="394"><figcaption></figcaption></figure>

3. Find the line below and change the parameter from **true** to **false** temporarily during the update. Save the changes.

<figure><img src="../../.gitbook/assets/изображение (108).png" alt=""><figcaption><p>define('DISALLOW_FILE_MODS', false);</p></figcaption></figure>

4. In your site’s admin panel, go to "**Dashboard → Updates**" and click the "**Update to version x.x.x**" button.

<figure><img src="../../.gitbook/assets/изображение (153).png" alt=""><figcaption></figcaption></figure>

5. After the update is complete, open the `wp-config.php` file again and change the parameter back from **false** to **true**. Save the changes.

<figure><img src="../../.gitbook/assets/изображение (26).png" alt=""><figcaption><p>define('DISALLOW_FILE_MODS', true);</p></figcaption></figure>

After that, your WordPress installation will be up to date.