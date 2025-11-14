# Update from Version 2.6 to 2.7

{% hint style="success" %}
A list of updates for the script version 2.7 is available at [**this link**](https://premium.gitbook.io/main/en/pered-nachalom-raboty/instrukciya-po-obnovleniyu-skripta/spisok-obnovlenii#versiya-2.7).
{% endhint %}

{% hint style="warning" %}
Before starting the script update, please update the Ioncube Loader on your server to version 14.0 or higher (if your current version is below 14 — refer to the [**instructions for checking the installed version**](https://premium.gitbook.io/main/en/basic-settings/faq/kak-proverit-versiyu-ioncube-ustanovlennuyu-na-servere)\*\* and the [**update instructions**](https://premium.gitbook.io/main/en/basic-settings/faq/kak-obnovit-ioncube-loader)). Your hosting provider's technical support can assist you with the update.
{% endhint %}

{% hint style="warning" %}
If you are using merchant and auto-payment modules developed specifically for you, please request updated modules in your Telegram group (**not through technical support via the bot**).

If you are using merchant and auto-payment modules, as well as other types of modules from third-party developers, they will not work on version 2.7 without updates from the developers.
{% endhint %}

{% hint style="warning" %}
If you used the Electrum modules and/or "Trading Actions" in version 2.6, please request the modules for version 2.7 in your Telegram group (**not through technical support via the bot**).
{% endhint %}

{% hint style="warning" %}
**Please note — when updating the script from version 2.6 to 2.7, a free update is required for those with a custom design developed by us for the site!**

If you are using such a design, please send an archive of the theme for adaptation to version 2.7.\
To do this, navigate to the folder on your server at `www/<site_name>/wp-content/themes/`, find the folder with your theme, compress it into an archive, download it to your computer, and then send the archive to your Telegram group.
{% endhint %}

{% hint style="danger" %}
<mark style="color:red;">**Before updating, make sure to back up your website and database!**</mark>

If something goes wrong during the update, you can always restore your site from the backup. Backup methods may vary depending on your hosting, so it's advisable to contact your hosting provider's technical support for assistance.

The simplest way to [**back up your site**](https://premium.gitbook.io/main/en/basic-settings/faq/kak-sdelat-bekap-saita) is through the server control panel (ISP Manager or other software) using the built-in file manager or via an FTP client (download the site files to your computer, and also download the site's database from the database management section or through PhpMyAdmin).
{% endhint %}

## Update Process

1.  In the exchange panel, go to the "**Console**" section and enable technical mode to prevent users from making requests on the site during the script update.

    <figure><img src="../../../ru/.gitbook/assets/image (879) (1).png" alt=""><figcaption></figcaption></figure>
2.  In the "**Plugins**" section, deactivate the "**Premium Exchanger**" and "**Premium Exchanger hooks**" plugins.\\

    <figure><img src="../../.gitbook/assets/image%20(254)_eng.png" alt=""><figcaption></figcaption></figure>
3. Using an FTP client or file manager, delete the contents of the **`/wp-content/plugins/premiumbox/`** folder on the server, <mark style="color:green;">**except for**</mark> the following files and folders inside it:

* **`/flags/`**
* **`/languages/`**
* **`/moduls/`** (but first, read the text in the block below)

{% hint style="info" %}
- If you **are using** the Webmoney module — do not delete the **`x19`** folder inside the **`moduls`** folder.
- If you **are not using** the Webmoney module — you can delete the **`moduls`** folder entirely.
{% endhint %}

* **`/sms/`**
* **`/userdata.php`**

<figure><img src="../../.gitbook/assets/image (1775)_eng.png" alt="" width="563"><figcaption><p><strong>Delete all checked files and folders on your server</strong></p></figcaption></figure>

4.  Delete all files from the previous license in the root folder of your site.\\

    <figure><img src="../../.gitbook/assets/image (1774)_eng.png" alt="" width="432"><figcaption></figcaption></figure>

Go to the "[**Your Licenses**](https://premiumexchanger.com/ulicense/)" section and download the archive with the license files `license.zip`. To do this, click on the "**Download for version 2.7**" link.\\

<figure><img src="../../.gitbook/assets/image%20(255)_eng.png" alt="" width="430"><figcaption></figcaption></figure>

Upload the downloaded archive to the [root folder of your site](https://premium.gitbook.io/main/en/basic-settings/faq/kak-naiti-kornevuyu-papku-saita-na-servere) using the <mark style="color:green;">**user created for the site**</mark> (not <mark style="color:red;">**root**</mark>!) and **make sure to extract the archive**.

{% hint style="danger" %}
**Make sure to complete step 4, even if the license files were previously uploaded to the server — otherwise, the site will not function!**
{% endhint %}

5. Go to the "[**Your Scripts**](https://premiumexchanger.com/uscripts/)" section and download the archive with **update files for version 2.7** that matches your PHP version.

{% hint style="danger" %}
You need to know the exact PHP version installed on your server to select the appropriate archive.\
[**Instructions for checking the PHP version installed on the server**](https://premium.gitbook.io/main/en/basic-settings/faq/kak-proverit-versiyu-php-ustanovlennuyu-na-servere).
{% endhint %}

<figure><img src="../../.gitbook/assets/image%20(257)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

6. Upload the contents of the update archive to the root folder of your site using the <mark style="color:green;">**user created for the site**</mark> (not <mark style="color:red;">**root**</mark>!). Use an FTP client or file manager. Extract the archive, replacing the files.
7. Go to the "**Plugins**" section and activate the "**Premium Exchanger**" and "**Premium Exchanger hooks**" plugins.
8. Go to the "**Exchange Settings** → "Migration"\*\* section and sequentially complete each step in the "**Migration (if version is less than 2.7)**" block.

{% hint style="danger" %}
If you used AML modules in version 2.6 — you need to enable the AML module in the "**Modules**" section <mark style="color:red;">**after**</mark> updating the script and <mark style="color:red;">**before**</mark> performing the migration for the correct transfer of settings from version 2.6.

<img src="../../.gitbook/assets/image (2009)_eng.png" alt="" data-size="original">

The same applies if you used coefficients (in the "**Parsers 2.0**" section ➔ "**Custom Coefficients**") — if you used coefficients in version 2.6, you need to enable the module of the same name in the "**Modules**" section <mark style="color:red;">**after**</mark> updating the script and <mark style="color:red;">**before**</mark> performing the migration for the correct transfer of coefficients from version 2.6.

<img src="../../.gitbook/assets/image (2015)_eng.png" alt="" data-size="original">
{% endhint %}

<figure><img src="../../../ru/.gitbook/assets/image (258).png" alt="" width="362"><figcaption></figcaption></figure>

When you start each step, the system will determine the total number of requests that need to be executed. You can specify the number of requests to be processed in one cycle.

<figure><img src="../../.gitbook/assets/image%20(500)_eng.png" alt="" width="345"><figcaption></figcaption></figure>

{% hint style="warning" %}
By default, the number of requests = 50. If you are unsure about your server's capacity, we recommend not changing the default value.

If necessary, you can specify any other value, but if the execution cycle with the specified value is too resource-intensive for the server, it will cause an error.
{% endhint %}

{% hint style="info" %}
You will see "**Technical Step X**" buttons next to the "**Step X**" buttons. Before executing each step, the system determines the number of requests that need to be executed. In some cases, the number of requests may be too large, and the server may struggle to count them. In this case, instead of the "**Step X**" button, you should use the "**Technical Step X**" button, which allows you to manually specify an arbitrary number of requests without the server counting them.

If you use the **technical step**, you need to manually specify the number of requests. We recommend setting a deliberately large number, such as 100,000.
{% endhint %}

9.  Go to the "**Settings** → "Permalinks"\*\* section and click the "**Save Changes**" button without making any changes on the page.\\

    <figure><img src="../../.gitbook/assets/image%20(259)_eng.png" alt="" width="563"><figcaption></figcaption></figure>
10. Go to the "**Requests**" section and disable the update mode.\\

    <figure><img src="../../.gitbook/assets/image%20(260)_eng.png" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
The update mode is activated each time the main plugin is deactivated and reactivated, so it must always be manually disabled.
{% endhint %}

11. If you are using the "**Parsers 2.0**" or "**Bestchange Parser**" modules — after disabling the update mode, you need to start the parsers in the corresponding sections by manually following the Cron link.\
    For the operation of Parsers 2.0:

    <figure><img src="../../.gitbook/assets/image%20(394)_eng.png" alt=""><figcaption></figcaption></figure>

    For the operation of the BestChange parser:

    <figure><img src="../../.gitbook/assets/image%20(392)_eng.png" alt="" width="563"><figcaption></figcaption></figure>
12. [Clear your browser cache](https://www.unisender.com/ru/blog/kak-ochistit-kehsh-v-brauzerah/).\\

    <figure><img src="../../.gitbook/assets/image%20(395)_eng.png" alt="" width="563"><figcaption></figcaption></figure>
13. <mark style="color:red;">**Make sure to delete all uploaded zip archives of the script and site backups from the root folder on the server.**</mark>\\
14. Disable maintenance mode in the "**Console**" section.
15. <mark style="color:green;">**Update completed successfully!**</mark>
