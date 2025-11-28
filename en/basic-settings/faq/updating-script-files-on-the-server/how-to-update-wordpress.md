# How to Update WordPress?

{% hint style="info" %}
We recommend updating WordPress whenever a new version with the format **x.x.1-9** (e.g., **6.4.3**) is released. Versions with the format **x.x.0** (e.g., **6.4.0**) may contain bugs that are typically fixed in subsequent **x.x.1** releases.
{% endhint %}

To update WordPress, follow these steps:

1. **Back up your files and database.**\
   This is crucial because if any issues arise during the update, it will be difficult to restore your site without a backup.
2. **Open the `wp-config.php` file on your server.**\
   This file is located in the [root directory](https://premium.gitbook.io/main/en/basic-settings/faq/kak-naiti-kornevuyu-papku-saita-na-servere) of your site.

<figure><img src="../../../.gitbook/assets/image (629) (1).png" alt="" width="394"><figcaption></figcaption></figure>

3. **Temporarily disable file modification restrictions.**\
   Locate the following line in the `wp-config.php` file and change the parameter from **true** to **false**. Save the changes.

<figure><img src="../../../.gitbook/assets/%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5%20(108)_eng.png" alt=""><figcaption><p>define('DISALLOW_FILE_MODS', false);</p></figcaption></figure>

4. **Update WordPress via the admin dashboard.**\
   Go to the "**Dashboard → Updates**" section in your site’s admin panel and click the "**Update to version x.x.x**" button.

<figure><img src="../../../.gitbook/assets/%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5%20(153)_eng.png" alt=""><figcaption></figcaption></figure>

5. **Re-enable file modification restrictions.**\
   After the update is complete, go back to the `wp-config.php` file and change the parameter from **false** back to **true**. Save the changes.

<figure><img src="../../../.gitbook/assets/%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5%20(26)_eng.png" alt=""><figcaption><p>define('DISALLOW_FILE_MODS', true);</p></figcaption></figure>

Once you’ve completed these steps, your WordPress installation will be updated to the latest version.
