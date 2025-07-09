# Updating from Version 2.6 to 2.7

{% hint style="success" %}
The list of script updates for version 2.7 is available [**here**](https://premium.gitbook.io/main/pered-nachalom-raboty/instrukciya-po-obnovleniyu-skripta/spisok-obnovlenii#versiya-2.7)
{% endhint %}

{% hint style="warning" %}
Before starting the script update, please update the Ioncube Loader on your server to version 14.0 or higher.  
If your installed version is below 14, see the [**instructions to check your current version**](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-proverit-versiyu-ioncube-ustanovlennuyu-na-servere) and the [**update guide**](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-obnovit-ioncube-loader).  
Your hosting provider’s technical support can assist you with this update.
{% endhint %}

{% hint style="warning" %}
If you are using merchant and auto-payout modules that we have custom-developed specifically for you, please request the updated modules in your Telegram group (**do not request them via the support bot**).

If you are using merchant, auto-payout, or any other modules from third-party developers, please note that these will not work on version 2.7 unless updated by their developers.
{% endhint %}

{% hint style="warning" %}
If you used Electrum modules and/or the "Trading Actions" module in version 2.6, please request the updated modules for version 2.7 in your Telegram group (**do not request them via the support bot**).
{% endhint %}

{% hint style="warning" %}
**Please note — when updating the script from version 2.6 to 2.7, a free update of any custom-designed themes created by us for your site is required!**

If you are using such a design, please send us an archive of your theme for adaptation to version 2.7.  
To do this, go to the folder `www/<your_site_name>/wp-content/themes/` on your server, find the folder with your theme, archive it, download it to your computer, and then send the archive to your Telegram group.
{% endhint %}

{% hint style="danger" %}
<mark style="color:red;">**Before updating, be sure to make a full backup of your website and database!**</mark>
{% endhint %}

If something goes wrong during the update, you can always restore your website from a backup. Backup methods may vary depending on your hosting provider, so it’s best to contact your hosting support team for guidance on this.

The easiest way to [**create a backup of your site**](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-sdelat-bekap-saita) is through your server control panel (such as ISP Manager or other software) using the built-in file manager, or via an FTP client (download your site files to your computer, and also export your site’s database through the database management section or PhpMyAdmin).

---

## Update Process

1. In the exchanger control panel, go to the "**Console**" section and enable the exchanger’s maintenance mode. This will prevent users from submitting requests on the site while the script is being updated.

    <figure><img src="../../.gitbook/assets/image (879).png" alt=""><figcaption></figcaption></figure>

2. In the "**Plugins**" section, deactivate the "**Premium Exchanger**" and "**Premium Exchanger hooks**" plugins.

    <figure><img src="../../.gitbook/assets/image (254).png" alt=""><figcaption></figcaption></figure>

3. Using an FTP client or file manager, delete the contents of the **`/wp-content/plugins/premiumbox/`** folder on your server, **except** for the following files and folders inside it:

* **`/flags/`**
* **`/languages/`**
* **`/moduls/`** (please read the note below first)

{% hint style="info" %}
- If you **use** the Webmoney module — do **not** delete the **`x19`** folder inside the **`moduls`** directory.
- If you **do not use** the Webmoney module — you can delete the entire **`moduls`** folder.
{% endhint %}

* **`/sms/`**
* **`/userdata.php`**

<figure><img src="../../.gitbook/assets/image (1775).png" alt="" width="563"><figcaption><p><strong>Delete all files and folders marked with a checkmark on your server</strong></p></figcaption></figure>

4. Delete all files related to the previous license from your site’s root folder.

    <figure><img src="../../.gitbook/assets/image (1774).png" alt="" width="432"><figcaption></figcaption></figure>

Go to the "[**Your Licenses**](https://premiumexchanger.com/ulicense/)" section and download the license files archive `license.zip` by clicking the "**Download for version 2.7**" link.

<figure><img src="../../.gitbook/assets/image (255).png" alt="" width="430"><figcaption></figcaption></figure>

Please upload the downloaded archive to the [root folder of your website](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-naiti-kornevuyu-papku-saita-na-servere) using the **user account created specifically for the site** (not the **root** user!) and **make sure to extract the archive**.

{% hint style="danger" %}
**Step 4 is mandatory, even if the license files were previously uploaded to the server — otherwise, the site will not work!**
{% endhint %}

5. Go to the "[**Your Scripts**](https://premiumexchanger.com/uscripts/)" section and download the archive with the **update files for version 2.7** that matches your PHP version.

{% hint style="danger" %}
You must know the exact PHP version installed on your server to select the correct archive.\
[**Instructions on how to check the PHP version installed on your server**](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-proverit-versiyu-php-ustanovlennuyu-na-servere)
{% endhint %}

<figure><img src="../../.gitbook/assets/image (257).png" alt="" width="563"><figcaption></figcaption></figure>

6. Upload the contents of the update archive to the root folder of your website using the **user account created specifically for the site** (not the **root** user!). Use an FTP client or a file manager. Extract the archive and overwrite the existing files.
7. Go to the "**Plugins**" section and activate the "**Premium Exchanger**" and "**Premium Exchanger hooks**" plugins.
8. Navigate to **Exchanger Settings → Migration** and in the "**Migration (if your version is below 2.7)**" block, complete each step in order.

{% hint style="danger" %}
If you used AML modules in version 2.6, you must enable the AML module in the "**Modules**" section **after** updating the script and **before** running the migration to ensure the settings transfer correctly from version 2.6.

![](<../../.gitbook/assets/image (2009).png>)

The same applies if you used coefficients (under "**Parsers 2.0**" → "**Custom Coefficients**") — if you used coefficients in version 2.6, enable the corresponding module in the "**Modules**" section **after** updating the script and **before** running the migration to properly transfer the coefficients from version 2.6.

![](<../../.gitbook/assets/image (2015).png>)
{% endhint %}

<figure><img src="../../.gitbook/assets/image (258).png" alt="" width="362"><figcaption></figcaption></figure>

When starting each step, the system will determine the total number of requests that need to be executed. You have the option to specify how many requests will be processed in a single cycle.

<figure><img src="../../.gitbook/assets/image (500).png" alt="" width="345"><figcaption></figcaption></figure>

{% hint style="warning" %}
By default, the number of requests is set to 50. If you are unsure about your server’s capacity, we recommend leaving this default value unchanged.

If necessary, you can specify a different number, but if processing a cycle with that number proves too resource-intensive for your server, it will cause an error.
{% endhint %}

{% hint style="info" %}
You may notice buttons labeled "**Technical Step X**" next to the "**Step X**" buttons. Before executing each step, the system calculates the number of requests that need to be made. In some cases, this number may be too large for the server to handle. In such cases, instead of using the "**Step X**" button, use the "**Technical Step X**" button, which allows you to manually set any number of requests without the server calculating the total.

If you use a **technical step**, you must manually specify the number of requests. We recommend setting a deliberately high number, such as 100,000.
{% endhint %}

9. Go to "**Settings → Permalinks**" and click the "**Save Changes**" button without making any changes on the page.

<figure><img src="../../.gitbook/assets/image (259).png" alt="" width="563"><figcaption></figcaption></figure>

10. Go to the "**Requests**" section and disable update mode.

<figure><img src="../../.gitbook/assets/image (260).png" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
Update mode is activated every time the main plugin is deactivated and then reactivated, so you always need to disable it manually.
{% endhint %}

11. If you are using the "**Parsers 2.0**" or "**Bestchange Parser**" modules, after disabling update mode, you need to manually start the parsers in their respective sections by following the Cron link.

For Parsers 2.0 operation:

Here is the natural English translation of the provided text:

---

For the BestChange parser to work:

12. [Clear your browser cache](https://www.unisender.com/ru/blog/kak-ochistit-kehsh-v-brauzerah/).

13. **Be sure to delete all uploaded script zip archives and website backups from the server’s root folder.**

14. Disable maintenance mode in the "**Console**" section.

15. **The update was completed successfully!**