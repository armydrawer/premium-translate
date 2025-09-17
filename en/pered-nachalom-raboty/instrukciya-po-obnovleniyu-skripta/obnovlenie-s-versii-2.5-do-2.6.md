# Updating from Version 2.5 to 2.6

{% embed url="https://www.youtube.com/watch?v=XX2Wpv-dAFk" %}
Video Guide for Script Update
{% endembed %}

{% hint style="success" %}
The list of script updates for version 2.6 is available via [**this link**](https://premium.gitbook.io/main/pered-nachalom-raboty/instrukciya-po-obnovleniyu-skripta/spisok-obnovlenii#versiya-2.6).
{% endhint %}

{% hint style="warning" %}
Before starting the script update, make sure to update the Ioncube Loader on your server to version 13.0 or higher. If your current version is below 13, refer to the [**guide for checking the installed version**](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-proverit-versiyu-ioncube-ustanovlennuyu-na-servere) and the [**update guide**](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-obnovit-ioncube-loader). Your hosting provider's technical support can assist with this update.
{% endhint %}

{% hint style="warning" %}
Starting with version 2.6, support for **PHP 7.1, 7.2, 7.3, and 7.4** has been discontinued for security reasons, and support for **PHP 8.2** has been added. If you were using **PHP 7.4 or lower** in version 2.5, you must update your server's PHP version before proceeding with the script update. We recommend contacting your hosting provider's support team for assistance with the PHP update.

[**Guide for checking the PHP version installed on your server**](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-proverit-versiyu-php-ustanovlennuyu-na-servere)
{% endhint %}

{% hint style="warning" %}
If you are using merchant and auto-payout modules developed specifically for you by us, **request updated modules** in your Telegram group (**not through the bot's technical support**).

If you are using merchant and auto-payout modules or other types of modules from third-party developers, they will not work on version 2.6 unless updated by their respective developers.
{% endhint %}

{% hint style="warning" %}
If you were using the Electrum modules and/or "Trading Actions" in version 2.5, **request updated modules for version 2.6** in your Telegram group (**not through the bot's technical support**).
{% endhint %}

{% hint style="danger" %}
<mark style="color:red;">**Before updating, make sure to create a backup of your website and database!**</mark>

If something goes wrong during the update, you can always restore your website from the backup. Backup methods may vary depending on your hosting provider, so contact their technical support for guidance.

The simplest way to [**create a website backup**](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-sdelat-bekap-saita) is through your server's control panel (e.g., ISP Manager or other software) using the built-in file manager or via an FTP client. Download the website files to your computer, and also export the database via the database management section or PhpMyAdmin.
{% endhint %}

{% hint style="warning" %}
**Note: Updating the script from version 2.5 to 2.6 requires a free update of custom website themes!**

If you are using a custom theme, send the theme archive for adaptation to version 2.6.\
To do this, navigate to the folder on your server located at `www/<site_name>/wp-content/themes/`, find the folder with your theme, archive it, download it to your computer, and send the archive to your Telegram group.
{% endhint %}

---

### Update Steps:

1. In the exchanger's admin panel, go to the "**Console**" section and enable the exchanger's maintenance mode to prevent users from making transactions during the update.

    <figure><img src="../../.gitbook/assets/image (879).png" alt=""><figcaption></figcaption></figure>

2. In the "**Plugins**" section, deactivate the "**Premium Exchanger**" and "**Premium Exchanger hooks**" plugins.

    <figure><img src="../../.gitbook/assets/image (1169).png" alt=""><figcaption></figcaption></figure>

3. Using an FTP client or file manager, delete the contents of the **`/wp-content/plugins/premiumbox/`** folder on your server, <mark style="color:green;">**except**</mark> for the following files and folders:

   - **`/flags/`**
   - **`/languages/`**
   - **`/moduls/`** (but first, read the note below)
   - **`/sms/`**
   - **`/userdata.php`**

{% hint style="danger" %}
- If you **use** [**internal accounts**](https://premium.gitbook.io/main/osnovnye-nastroiki/nastroiki/vnutrennie-scheta/obmen-s-uchastiem-vnutrennego-scheta-polzovatelya), do not delete the **domacc** folder inside the **`moduls`** folder.
- If you **do not use** internal accounts, you can delete the **`moduls`** folder entirely.

After updating the script, you will need to migrate internal accounts to the new module — [**migration guide**](https://premium.gitbook.io/main/pered-nachalom-raboty/instrukciya-po-obnovleniyu-skripta/obnovlenie-s-versii-2.5-do-2.6#id-2.-obnovlenie-modulya-vnutrennii-schyot-tolko-esli-vnutrennie-scheta-ispolzovalis-v-versii-2.5-.-esl) **(only relevant if you used internal accounts in version 2.5).**

- If you **use** the Webmoney module, do not delete the **`x19`** folder inside the **`moduls`** folder.
- If you **do not use** the Webmoney module, you can delete the **`moduls`** folder entirely.
{% endhint %}

<figure><img src="../../.gitbook/assets/image (1775).png" alt="" width="563"><figcaption><p><strong>Delete all files and folders marked with a checkmark on your server</strong></p></figcaption></figure>

4. Delete all old license files from the root folder of your website.

    <figure><img src="../../.gitbook/assets/image (1774).png" alt="" width="432"><figcaption></figcaption></figure>

    Go to the "[**Your Licenses**](https://premiumexchanger.com/ulicense/)" section and download the license files archive `license.zip` by clicking the "**Download for version 2.6**" link.

    <figure><img src="../../.gitbook/assets/image (473).png" alt="" width="485"><figcaption></figcaption></figure>

    Upload the downloaded archive to the [root folder of your website](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-naiti-kornevuyu-papku-saita-na-servere) under the <mark style="color:green;">**user created for the website**</mark> (not <mark style="color:red;">**root**</mark>!) and **make sure to extract the archive**.

{% hint style="danger" %}
**Step 4 is mandatory, even if the license files were previously uploaded to the server. Otherwise, the website will not function!**
{% endhint %}

5. Go to the "[**Your Scripts**](https://premiumexchanger.com/uscripts/)" section and download the archive with **update files for version 2.6** corresponding to your PHP version.

{% hint style="danger" %}
You must know the exact PHP version installed on your server to select the correct archive.\
[**Guide for checking the PHP version installed on your server**](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-proverit-versiyu-php-ustanovlennuyu-na-servere)
{% endhint %}

<figure><img src="../../.gitbook/assets/image (472).png" alt="" width="563"><figcaption></figcaption></figure>

6. Upload the contents of the update archive to the root folder of your website under the <mark style="color:green;">**user created for the website**</mark> (not <mark style="color:red;">**root**</mark>!). Use an FTP client or file manager. Extract the archive and replace the files.

7. Go to the "**Plugins**" section and activate the "**Premium Exchanger**" and "**Premium Exchanger hooks**" plugins.

8. Navigate to **"Exchanger Settings" → "Migration"** and, in the "**Migration (if version is below 2.6)**" block, complete each step sequentially.

<figure><img src="../../.gitbook/assets/image (1682).png" alt="" width="390"><figcaption></figcaption></figure>

For each step, the system will calculate the total number of requests to process. You can specify the number of requests to process per cycle.

<figure><img src="../../.gitbook/assets/image (500).png" alt="" width="345"><figcaption></figcaption></figure>

{% hint style="warning" %}
By default, the number of requests is set to 50. If you're unsure about your server's capacity, we recommend keeping the default value.

You can specify a different value if needed, but if the server cannot handle the specified load, it may result in an error.
{% endhint %}

{% hint style="info" %}
You may see "**Technical Step X**" buttons next to the "**Step X**" buttons. In some cases, the number of requests may be too large for the server to calculate. In such cases, use the "**Technical Step X**" button, which allows you to manually specify the number of requests without server-side calculations.

If using a **technical step**, manually set a large number of requests, such as 100,000.
{% endhint %}

9. Go to **"Settings" → "Permalinks"** and click "**Save Changes**" without making any modifications.

10. Navigate to **"Exchanger Settings" → "General Settings"** and disable the update mode.

<figure><img src="../../.gitbook/assets/image (1729).png" alt=""><figcaption></figcaption></figure>

Alternatively, in the same section, set the "**Update Mode**" parameter to "**No**" and save the changes.

<figure><img src="../../.gitbook/assets/image (474).png" alt="" width="255"><figcaption></figcaption></figure>

{% hint style="warning" %}
Update mode is automatically enabled each time the main plugin is deactivated and reactivated, so it must always be manually disabled.
{% endhint %}

### Translation into Naturalistic English:

11. If you are using the "**Parsers 2.0**" or "**BestChange Parser**" modules, after disabling the update mode, you need to manually start the parsers in their respective sections by following the Cron link.

   For Parsers 2.0:

   <figure><img src="../../.gitbook/assets/image (394).png" alt=""><figcaption></figcaption></figure>

   For the BestChange Parser:

   <figure><img src="../../.gitbook/assets/image (392).png" alt="" width="563"><figcaption></figcaption></figure>

12. [Clear your browser cache](https://www.unisender.com/ru/blog/kak-ochistit-kehsh-v-brauzerah/).

   <figure><img src="../../.gitbook/assets/image (395).png" alt="" width="563"><figcaption></figcaption></figure>

13. <mark style="color:red;">**Make sure to delete any uploaded script zip archives and website backups from the root folder on the server.**</mark>

   <figure><img src="../../.gitbook/assets/image (396).png" alt="" width="563"><figcaption></figcaption></figure>

14. Disable maintenance mode in the "**Console**" section.

15. <mark style="color:green;">**The update has been successfully completed!**</mark>

---

### Changes in the Admin Panel

After the update, you need to make some changes in the admin panel to ensure the script functions correctly.

1. To enable email registration confirmation, activate the "**Email Confirmation Before Registration**" (**confirmregmail**) module in the "**Modules**" section. If you don’t use this feature, you can leave the module disabled.

<details>

<summary>2. Updating the "<strong>Internal Account</strong>" module (only if <a href="https://premium.gitbook.io/main/osnovnye-nastroiki/nastroiki/vnutrennie-scheta/obmen-s-uchastiem-vnutrennego-scheta-polzovatelya">internal accounts</a> were used in version 2.5!).<br><br>If you didn’t use internal accounts before and want to start using them in version 2.6, skip this step. Activate the **iac** module in the "**Modules**" section and configure it according to <a href="https://premium.gitbook.io/main/osnovnye-nastroiki/nastroiki/vnutrennie-scheta">this guide</a>.</summary>

If you are using the **"Internal Account" (domacc)** module, as well as merchant modules for receiving payments and auto-payouts **domacc**:

![](<../../.gitbook/assets/image (1644).png>)![](<../../.gitbook/assets/image (1645).png>)

<mark style="color:red;">**you must**</mark> switch to the new **"Internal Account Module" (iac)**.

Steps to migrate to the new module:

- Activate the new **iac** module in the "**Modules**" section (the **domacc** module must also **remain enabled** during the migration process).
- Complete the migration steps sequentially — Step 7 and Step 8 in the "**Exchange Settings**" -> "**Migration**" section.

![](<../../.gitbook/assets/image (1646).png>)

![](<../../.gitbook/assets/image (1647).png>)![](<../../.gitbook/assets/image (1648).png>)

- Disable the old **domacc** module in the "**Modules**" section, then delete the module from the server (path to the module folder: `wp-content/plugins/premiumbox/moduls/domacc)`\
  ![](<../../.gitbook/assets/image (1649).png>)
- Remove the merchant and auto-payout modules **domacc** in the admin panel under **"Merchants" -> "Merchants"** and **"Merchants" -> "Auto-payouts"**, then delete the modules from the server (paths to the module folders: `wp-content/plugins/premiumbox/moduls/merchants/domacc` and `wp-content/plugins/premiumbox/moduls/paymerchants/domacc`).
- Add the new **iac** merchant and auto-payout modules in the **"Merchants" -> "Merchants"** and **"Merchants" -> "Auto-payouts"** sections, and configure them according to [this guide](https://premium.gitbook.io/main/osnovnye-nastroiki/nastroiki/vnutrennie-scheta).
- Assign the newly created merchants to the appropriate exchange directions (found under the "**Merchants and Payouts**" tab in the exchange direction settings).

![](<../../.gitbook/assets/image (463).png>)

<mark style="color:red;">**Important!**</mark> If, when using merchant modules for receiving payments and auto-payouts with internal accounts, the internal account number for debiting and/or crediting funds is not specified in the exchange form, it will default to **`currency code + client ID`** from the client’s profile (found under "**Personal Data**" -> "**Internal Account**").

![](<../../.gitbook/assets/image (1655).png>)![](<../../.gitbook/assets/image (1654).png>)

If an account number is specified in the exchange form, that account will be used for debiting/crediting (note that this allows you to transfer funds to another user’s account if their ID is known).

![](<../../.gitbook/assets/image (1656).png>)

Continue updating the script.

</details>

3. Starting from version 2.6, the **"Captcha for the Website (Image Selection)" (sitecaptcha_img)** module automatically generates options for users to select on the website. In the previous version, you could create custom tasks, but starting from version 2.6, this option is disabled, and any changes to the captcha’s appearance will immediately reflect on the website.

4. After the update, in the "**Exchange Settings**" -> "**General Settings**" section, <mark style="color:red;">**you must**</mark> select the logic for handling requests when using merchants for receiving payments under the "**Action if the merchant fails**" option.  
   For more details on how this option works, refer to the guide "[**General Merchant Settings**](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov#podklyuchenie-neskolkikh-merchantov)".