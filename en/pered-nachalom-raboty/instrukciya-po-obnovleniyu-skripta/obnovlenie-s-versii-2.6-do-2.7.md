# Updating from Version 2.6 to 2.7

{% hint style="success" %}
The list of script updates for version 2.7 is available via [**this link**](https://premium.gitbook.io/main/pered-nachalom-raboty/instrukciya-po-obnovleniyu-skripta/spisok-obnovlenii#versiya-2.7).
{% endhint %}

---

{% hint style="warning" %}
Before starting the script update, ensure that **Ioncube Loader** on your server is updated to version 14.0 or higher. If your current version is below 14, refer to the [**guide on checking your installed version**](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-proverit-versiyu-ioncube-ustanovlennuyu-na-servere) and the [**update instructions**](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-obnovit-ioncube-loader). Your hosting provider's technical support team can assist with this process.
{% endhint %}

---

{% hint style="warning" %}
If you are using merchant and auto-payout modules developed specifically for you by us, **please request updated versions of these modules** in your Telegram group (**do not contact technical support via the bot**).

If you are using merchant and auto-payout modules or other types of modules from third-party developers, they will not work with version 2.7 unless updated by their respective developers.
{% endhint %}

---

{% hint style="warning" %}
If you were using the **Electrum** modules and/or the **"Trading Actions"** feature in version 2.6, **please request updated modules for version 2.7** in your Telegram group (**do not contact technical support via the bot**).
{% endhint %}

---

{% hint style="warning" %}
**Important:** If you are updating the script from version 2.6 to 2.7, you will need to update (free of charge) any custom-designed themes developed by us for your website.

If you are using such a theme, please send us the theme archive for adaptation to version 2.7. To do this:
1. Navigate to the folder on your server located at `www/<site_name>/wp-content/themes/`.
2. Find the folder containing your theme, compress it into an archive, and download it to your computer.
3. Send the archive to your Telegram group.
{% endhint %}

---

{% hint style="danger" %}
<mark style="color:red;">**Before updating, make sure to create a backup of your website and database!**</mark>

If something goes wrong during the update, you will be able to restore your website from the backup. Backup methods may vary depending on your hosting provider, so contact your hosting provider's technical support team for assistance.

The simplest way to [**create a website backup**](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-sdelat-bekap-saita) is through your server's control panel (e.g., ISP Manager or other software) using the built-in file manager or an FTP client. Download the website files to your computer, and also export the database via the database management section or PhpMyAdmin.
{% endhint %}

---

## Update Process

1. In the exchanger's admin panel, go to the "**Console**" section and enable **technical mode** to prevent users from making transactions on the website during the update.

    <figure><img src="../../.gitbook/assets/image (879).png" alt=""><figcaption></figcaption></figure>

2. In the "**Plugins**" section, deactivate the "**Premium Exchanger**" and "**Premium Exchanger hooks**" plugins.

    <figure><img src="../../.gitbook/assets/image (254).png" alt=""><figcaption></figcaption></figure>

3. Using an FTP client or file manager, delete the contents of the **`/wp-content/plugins/premiumbox/`** folder on your server, <mark style="color:green;">**except**</mark> for the following files and folders:

   - **`/flags/`**
   - **`/languages/`**
   - **`/moduls/`** (but first, read the note below)
   - **`/sms/`**
   - **`/userdata.php`**

   {% hint style="info" %}
   - If you **use** the Webmoney module, do not delete the **`x19`** folder inside the **`moduls`** folder.
   - If you **do not use** the Webmoney module, you can delete the **`moduls`** folder entirely.
   {% endhint %}

    <figure><img src="../../.gitbook/assets/image (1775).png" alt="" width="563"><figcaption><p><strong>Delete all files and folders marked with checkmarks on your server.</strong></p></figcaption></figure>

4. Delete all files related to the previous license from the root folder of your website.

    <figure><img src="../../.gitbook/assets/image (1774).png" alt="" width="432"><figcaption></figcaption></figure>

    Then, go to the "[**Your Licenses**](https://premiumexchanger.com/ulicense/)" section and download the `license.zip` archive for version 2.7 by clicking the "**Download for version 2.7**" link.

    <figure><img src="../../.gitbook/assets/image (255).png" alt="" width="430"><figcaption></figcaption></figure>

    Upload the downloaded archive to the [root folder of your website](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-naiti-kornevuyu-papku-saita-na-servere) using the <mark style="color:green;">**user created for the website**</mark> (not <mark style="color:red;">**root**</mark>!), and **make sure to extract the archive**.

    {% hint style="danger" %}
    **Step 4 is mandatory, even if the license files were previously uploaded to the server. Otherwise, the website will not function!**
    {% endhint %}

5. Go to the "[**Your Scripts**](https://premiumexchanger.com/uscripts/)" section and download the archive with **update files for version 2.7** corresponding to your PHP version.

    {% hint style="danger" %}
    Make sure you know the exact PHP version installed on your server to select the correct archive.\
    [**Guide to checking your server's PHP version**](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-proverit-versiyu-php-ustanovlennuyu-na-servere)
    {% endhint %}

    <figure><img src="../../.gitbook/assets/image (257).png" alt="" width="563"><figcaption></figcaption></figure>

6. Upload the contents of the update archive to the root folder of your website using the <mark style="color:green;">**user created for the website**</mark> (not <mark style="color:red;">**root**</mark>!), and extract the archive, replacing the existing files.

7. In the "**Plugins**" section, activate the "**Premium Exchanger**" and "**Premium Exchanger hooks**" plugins.

8. Go to **"Exchanger Settings" → "Migration"** and, in the "**Migration (if version is below 2.7)**" block, complete each step sequentially.

    {% hint style="danger" %}
    If you used the AML module in version 2.6, enable the AML module in the "**Modules**" section <mark style="color:red;">**after**</mark> updating the script and <mark style="color:red;">**before**</mark> performing the migration to ensure proper settings transfer.

    Similarly, if you used coefficients (in the "**Parsers 2.0**" → "**Custom Coefficients**" section), enable the corresponding module in the "**Modules**" section <mark style="color:red;">**after**</mark> updating the script and <mark style="color:red;">**before**</mark> performing the migration to ensure proper transfer of coefficients from version 2.6.
    {% endhint %}

    <figure><img src="../../.gitbook/assets/image (2214).png" alt="" width="362"><figcaption></figcaption></figure>

    When running each step, the system will calculate the total number of requests to be processed. You can specify the number of requests to be processed per cycle.

    {% hint style="warning" %}
    By default, the number of requests is set to 50. If you're unsure about your server's capacity, we recommend leaving the default value.

    If necessary, you can specify a different value, but if the cycle with the chosen value is too resource-intensive for the server, it may result in an error.
    {% endhint %}

    {% hint style="info" %}
    You may see "**Technical Step X**" buttons next to the "**Step X**" buttons. In some cases, the number of requests may be too large for the server to calculate. In such cases, use the "**Technical Step X**" button, which allows you to manually specify the number of requests without server-side calculations.

    If using a **technical step**, set a large number, such as 100,000.
    {% endhint %}

9. Go to the "**Settings → Permalinks**" section and click "**Save Changes**" without making any modifications to the page.

    <figure><img src="../../.gitbook/assets/image (259).png" alt="" width="563"><figcaption></figcaption></figure>

10. Go to the "**Requests**" section and disable the update mode.

    <figure><img src="../../.gitbook/assets/image (260).png" alt=""><figcaption></figcaption></figure>

    {% hint style="warning" %}
    Update mode is automatically enabled every time the main plugin is deactivated and reactivated, so it must always be disabled manually.
    {% endhint %}

11. If you use the "**Parsers 2.0**" or "**BestChange Parser**" modules, restart the parsers manually by following the Cron link in the respective sections.

    For Parsers 2.0:

    <figure><img src="../../.gitbook/assets/image (394).png" alt=""><figcaption></figcaption></figure>

    For the BestChange Parser:

    <figure><img src="../../.gitbook/assets/image (392).png" alt="" width="563"><figcaption></figcaption></figure>

12. [Clear your browser cache](https://www.unisender.com/ru/blog/kak-ochistit-kehsh-v-brauzerah/).

    <figure><img src="../../.gitbook/assets/image (395).png" alt="" width="563"><figcaption></figcaption></figure>

13. <mark style="color:red;">**Be sure to delete all uploaded script zip archives and website backups from the root folder on your server.**</mark>

14. Turn off the maintenance mode in the "**Console**" section.  
15. <mark style="color:green;">**The update was successfully completed!**</mark>