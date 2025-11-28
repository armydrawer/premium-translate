# Update from Version 2.5 to 2.6

{% embed url="https://www.youtube.com/watch?v=XX2Wpv-dAFk" %}
Video tutorial for updating the script
{% endembed %}

{% hint style="success" %}
A list of updates for version 2.6 is available at [**this link**](https://premium.gitbook.io/main/en/pered-nachalom-raboty/instrukciya-po-obnovleniyu-skripta/spisok-obnovlenii#versiya-2.6).
{% endhint %}

{% hint style="warning" %}
Before starting the script update, please ensure that the Ioncube Loader on your server is updated to version 13.0 or higher (if your current version is below 13, refer to the [**instructions for checking the installed version**](https://premium.gitbook.io/main/en/basic-settings/faq/kak-proverit-versiyu-ioncube-ustanovlennuyu-na-servere)\*\* and [**instructions for updating**](https://premium.gitbook.io/main/en/basic-settings/faq/kak-obnovit-ioncube-loader)). Your hosting provider's technical support can assist you with the update.
{% endhint %}

{% hint style="warning" %}
Starting from version 2.6, support for **PHP 7.1, 7.2, 7.3**, and **7.4** has been removed for security reasons, and support for **PHP 8.2** has been added. If you were using **PHP 7.4** or lower in version 2.5, you need to update the PHP version on your server before updating the script. We recommend updating PHP through your hosting provider's technical support.

[**Instructions for checking the PHP version installed on the server**](https://premium.gitbook.io/main/en/basic-settings/faq/kak-proverit-versiyu-php-ustanovlennuyu-na-servere).
{% endhint %}

{% hint style="warning" %}
If you are using merchant and auto-payment modules that were specifically developed for you, please request updated modules in your Telegram group (**not through technical support via the bot**).

If you are using merchant and auto-payment modules, as well as other types of modules from third-party developers, they will not work on version 2.6 without updates from the developers.
{% endhint %}

{% hint style="warning" %}
If you used the Electrum modules and/or "Trading Actions" in version 2.5, please request the modules for version 2.6 in your Telegram group (**not through technical support via the bot**).
{% endhint %}

{% hint style="danger" %}
<mark style="color:red;">**Before updating, make sure to back up your website and database!**</mark>

If something goes wrong during the update, you can always restore your site from the backup. Backup methods may vary depending on your hosting provider, so you should contact their technical support for assistance.

The easiest way to [**back up your website**](https://premium.gitbook.io/main/en/basic-settings/faq/kak-sdelat-bekap-saita) is through your server's control panel (ISP Manager or other software) using the built-in file manager or via an FTP client (download the website files to your computer, and also download the database from the database management section or through PhpMyAdmin).
{% endhint %}

{% hint style="warning" %}
**Please note — when updating the script from version 2.5 to 2.6, you need to update (for free) any custom themes for your website!**

If you are using such a theme, please send the archive for adaptation to version 2.6.\
To do this, navigate to the folder on your server at `www/<your_site_name>/wp-content/themes/`, find the folder with your theme, zip it, download it to your computer, and then send the archive in your Telegram group.
{% endhint %}

1.  In the exchange panel, go to the "**Console**" section and enable technical mode for the exchanger so that users cannot make requests on the site during the script update.

    <figure><img src="../../.gitbook/assets/image (879) (1).png" alt=""><figcaption></figcaption></figure>
2.  In the "**Plugins**" section, deactivate the "**Premium Exchanger**" and "**Premium Exchanger hooks**" plugins.

    <figure><img src="../../.gitbook/assets/image (1169)_eng.png" alt=""><figcaption></figcaption></figure>
3. Using an FTP client or file manager, delete the contents of the **`/wp-content/plugins/premiumbox/`** folder on the server, <mark style="color:green;">**except for**</mark> the following files and folders inside it:

* **`/flags/`**
* **`/languages/`**
* **`/moduls/`** (but first, read the text in the block below)

{% hint style="danger" %}
- If you **are using** [**internal accounts**](https://premium.gitbook.io/main/en/basic-settings/nastroiki/vnutrennie-scheta/obmen-s-uchastiem-vnutrennego-scheta-polzovatelya) — do not delete the **domacc** folder inside the **`moduls`** folder.
- If you **are not using** internal accounts — you can delete the **`moduls`** folder entirely.

\
After updating the script, you need to transfer internal accounts to the new module — [**instructions for transferring**](https://premium.gitbook.io/main/en/pered-nachalom-raboty/instrukciya-po-obnovleniyu-skripta/obnovlenie-s-versii-2.5-do-2.6#id-2.-obnovlenie-modulya-vnutrennii-schyot-tolko-esli-vnutrennie-scheta-ispolzovalis-v-versii-2.5-.-esl) **(relevant only if you used internal accounts in 2.5)**

* If you **are using** the Webmoney module, do not delete the **`x19`** folder inside the **`moduls`** folder.
* If you **are not using** the Webmoney module — you can delete the **`moduls`** folder entirely.
{% endhint %}

* **`/sms/`**
* **`/userdata.php`**

<figure><img src="../../.gitbook/assets/image (1775)_eng.png" alt="" width="563"><figcaption><p><strong>Delete all checked files and folders from your server</strong></p></figcaption></figure>

4.  Delete all files from the previous license in the root folder of your website.\\

    <figure><img src="../../.gitbook/assets/image (1774)_eng.png" alt="" width="432"><figcaption></figcaption></figure>

Go to the "[**Your Licenses**](https://premiumexchanger.com/ulicense/)" section and download the archive with the license files `license.zip`. To do this, click on the link "**Download for version 2.6**".

Upload the downloaded archive to the [root folder of your website](https://premium.gitbook.io/main/en/basic-settings/faq/kak-naiti-kornevuyu-papku-saita-na-servere) under <mark style="color:green;">**the user created for the site**</mark> (not <mark style="color:red;">**root**</mark>!) and **be sure to extract the archive**.

{% hint style="danger" %}
**Make sure to complete step 4, even if the license files were previously uploaded to the server — otherwise, the site will not function!**
{% endhint %}

5. Go to the "[**Your Scripts**](https://premiumexchanger.com/uscripts/)" section and download the archive with **files for updating to version 2.6** for your PHP version.

{% hint style="danger" %}
You need to know the exact PHP version installed on your server to select the appropriate archive.\
[**Instructions for checking the PHP version installed on the server**](https://premium.gitbook.io/main/en/basic-settings/faq/kak-proverit-versiyu-php-ustanovlennuyu-na-servere).
{% endhint %}

6. Upload the contents of the update archive to the root folder of your website under <mark style="color:green;">**the user created for the site**</mark> (not <mark style="color:red;">**root**</mark>!). Use an FTP client or file manager. Extract the archive, replacing the files.
7. Go to the "**Plugins**" section and activate the "**Premium Exchanger**" and "**Premium Exchanger hooks**" plugins.
8. Navigate to the "**Exchange Settings** → "Migration"\*\* section and sequentially complete each step in the "**Migration (if version is less than 2.6)**" block.

<figure><img src="../../.gitbook/assets/image (1682)_eng.png" alt="" width="390"><figcaption></figcaption></figure>

When starting each step, the system will determine the total number of requests that need to be processed. You can specify the number of requests to be processed in one cycle.

{% hint style="warning" %}
By default, the number of requests = 50. If you are unsure about your server's capacity, we recommend not changing the default value.

If necessary, you can specify any other value, but if the execution cycle with the specified value is too resource-intensive for the server, it will result in an error.
{% endhint %}

{% hint style="info" %}
You will see "**Technical Step X**" buttons next to the "**Step X**" buttons. Before executing each step, the system determines the number of requests that need to be processed. In some cases, the number of requests may be too large, and the server may struggle to handle the count. In this case, instead of the "**Step X**" button, you should use the "**Technical Step X**" button, which allows you to manually specify an arbitrary number of requests without the server counting them.

If you use the **technical step**, you will need to manually set the number of requests. We recommend setting a large number, such as 100,000.
{% endhint %}

9. Go to the "**Settings" → "Permalinks"** section and click the "**Save Changes**" button without making any changes on the page.
10. Navigate to the "**Exchange Settings" → "General Settings"** section and disable the update mode.

<figure><img src="../../.gitbook/assets/image (1729)_eng.png" alt=""><figcaption></figcaption></figure>

An alternative option is to select "**No**" for the "**Update Mode**" parameter in this section and save the changes.

{% hint style="warning" %}
The update mode is activated each time the main plugin is deactivated and reactivated, so it must always be manually disabled.
{% endhint %}

11. If you are using the "**Parsers 2.0**" or "**Bestchange parser**" modules, after disabling the update mode, you need to manually start the parsers in the corresponding sections by following the Cron link.

For the operation of Parsers 2.0:

For the operation of the BestChange parser:

12. [Clear your browser cache](https://www.unisender.com/ru/blog/kak-ochistit-kehsh-v-brauzerah/).
13. <mark style="color:red;">**Make sure to delete any uploaded zip archives of the script and website backups from the root folder on the server.**</mark>
14. Disable maintenance mode in the "**Console**" section.
15. <mark style="color:green;">**The update was successful!**</mark>

### Changes in the Admin Panel

After the update, you need to make changes in the admin panel for the script to function correctly.

1. To enable email registration confirmation, you need to activate the "**Email Confirmation Before Registration**" (**confirmregmail**) module in the "**Modules**" section. If you are not using this option, you can leave the module turned off.

<details>

<summary>2. Update the "<strong>Internal Account</strong>" module (only if <a href="https://premium.gitbook.io/main/en/basic-settings/nastroiki/vnutrennie-scheta/obmen-s-uchastiem-vnutrennego-scheta-polzovatelya">internal accounts</a> were used in version 2.5!).<br><br>If you have not used internal accounts before and want to use them in version 2.6, skip this step. Activate the iac module in the "<strong>Modules</strong>" section and configure it according to the <a href="https://premium.gitbook.io/main/en/basic-settings/nastroiki/vnutrennie-scheta">instructions</a>.</summary>

If you are using the **"Internal Account" (domacc)** module, as well as merchant modules for receiving and auto payouts **domacc**:

![](<../../.gitbook/assets/image (1644)_eng.png>) ![](<../../.gitbook/assets/image (1645)_eng.png>)

<mark style="color:red;">**It is necessary**</mark> to switch to the new **"Internal Account Module" (iac)**.

Instructions for transitioning to the new module:

* Activate the new **iac** module in the "**Modules**" section (the **domacc** module must also **be enabled** for successful migration).
* Sequentially perform the migration — steps 7 and 8 in the "**Exchange Settings**" -> "**Migration**" section.

![](<../../.gitbook/assets/image (1646)_eng.png>)

![](<../../.gitbook/assets/image (1647)_eng.png>) ![](<../../.gitbook/assets/image (1648)_eng.png>)

* Disable the old **domacc** module in the "**Modules**" section, and then delete the module from the server (the path to the module folder is `wp-content/plugins/premiumbox/moduls/domacc)`\
  ![](<../../.gitbook/assets/image (1649)_eng.png>)
* Remove the merchant and auto payout **domacc** modules in the admin panel from the **"Merchants" -> "Merchants"** and **"Merchants" -> "Auto Payouts"** sections, then delete the modules from the server (the paths to the module folders are `wp-content/plugins/premiumbox/moduls/merchants/domacc` and `wp-content/plugins/premiumbox/moduls/paymerchants/domacc`).
* Add the new merchant and auto payout **iac** in the **"Merchants" -> "Merchants"** and **"Merchants" -> "Auto Payouts"** sections and configure them according to the [instructions](https://premium.gitbook.io/main/en/basic-settings/nastroiki/vnutrennie-scheta).
* Add the created merchants to the appropriate exchange directions (the "**Merchants and Payouts**" tab in the exchange direction settings).

<mark style="color:red;">**Important!**</mark> If the internal account number for debiting and/or crediting funds is not specified in the exchange form when using merchant modules for receiving and auto payouts, it will default to **`currency code + client id`** from the client's profile (section "**Personal Data**" -> "**Internal Account**").

![](<../../.gitbook/assets/image (1655)_eng.png>) ![](<../../.gitbook/assets/image (1654)_eng.png>)

If the account is specified in the exchange form, that account will be used for debiting/crediting (note that this way you can transfer currency to another user's account if their ID is known).

![](<../../.gitbook/assets/image (1656)_eng.png>)

Continue with the script update.

</details>

3. Starting from version 2.6, the **"Captcha for the Site (Image Selection)" (sitecaptcha\_img)** module automatically generates options for users to choose from on the site. In the previous version of the module, you could create your own tasks; starting from version 2.6, this option has been disabled, so changes to the captcha's appearance will be reflected on the site immediately.
4. After the update, in the "**Exchange Settings**" -> "**General Settings**" section, <mark style="color:red;">**make sure to**</mark> select the logic for handling requests when using receiving merchants for the option "**Action if the merchant fails**."\
   For more details on how this option works, refer to the "[**General Merchant Settings**](https://premium.gitbook.io/main/en/en/basic-settings/merchants-and-auto-payments/merchants/general-merchant-settings#podklyuchenie-neskolkikh-merchantov)" guide.
