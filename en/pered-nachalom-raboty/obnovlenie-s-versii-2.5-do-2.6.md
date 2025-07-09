# Updating from Version 2.5 to 2.6

{% embed url="https://www.youtube.com/watch?v=XX2Wpv-dAFk" %}
Video tutorial on how to update the script
{% endembed %}

{% hint style="success" %}
The list of script updates for version 2.6 is available [**here**](https://premium.gitbook.io/main/pered-nachalom-raboty/instrukciya-po-obnovleniyu-skripta/spisok-obnovlenii#versiya-2.6)
{% endhint %}

{% hint style="warning" %}
Before updating the script, please update the Ioncube Loader on your server to version 13.0 or higher. If your installed version is below 13, see the [**instructions for checking your installed version**](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-proverit-versiyu-ioncube-ustanovlennuyu-na-servere) and the [**instructions for updating**](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-obnovit-ioncube-loader). Your hosting provider’s technical support can assist you with this update.
{% endhint %}

{% hint style="warning" %}
Starting with version 2.6, support for **PHP 7.1, 7.2, 7.3, and 7.4** has been removed for security reasons, and support for **PHP 8.2** has been added. If you were using **PHP 7.4** or lower with version 2.5, you must update your server’s PHP version before updating the script. We recommend contacting your hosting provider’s support team to perform the PHP upgrade.

[**Instructions for checking the PHP version installed on your server**](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-proverit-versiyu-php-ustanovlennuyu-na-servere)
{% endhint %}

{% hint style="warning" %}
If you are using merchant and auto-payout modules developed personally for you by us, please request the updated modules in your Telegram group (**do not request them through the support bot**).

If you are using merchant and auto-payout modules or other types of modules from third-party developers, please note that they will not work with version 2.6 unless updated by their developers.
{% endhint %}

{% hint style="warning" %}
If you used the Electrum modules and/or "Trading Actions" in version 2.5, please request the updated modules for version 2.6 in your Telegram group (**do not request them through the support bot**).
{% endhint %}

{% hint style="danger" %}
<mark style="color:red;">**Be sure to back up your website and database before updating!**</mark>
{% endhint %}

If something goes wrong during the update, you can always restore your website from a backup. Backup methods may vary depending on your hosting provider, so it’s best to contact your hosting support team for guidance.

The easiest way to [**create a website backup**](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-sdelat-bekap-saita) is through your server control panel (ISP Manager or other software) using the built-in file manager, or via an FTP client. Download your website files to your computer, and also export the website database through the database management section or PhpMyAdmin.

{% hint style="warning" %}
**Please note — when updating the script from version 2.5 to 2.6, a free update of custom site themes is required!**

If you are using a custom theme, please send an archive of it for adaptation to version 2.6.\
To do this, navigate on your server to the folder `www/<your_site_name>/wp-content/themes/`, find your theme’s folder, archive it, download it to your computer, and then send the archive to your Telegram group.  
{% endhint %}

1. In the exchanger control panel, go to the "**Console**" section and enable technical mode to prevent users from submitting exchange requests during the script update.

    <figure><img src="../../.gitbook/assets/image (879).png" alt=""><figcaption></figcaption></figure>

2. In the "**Plugins**" section, deactivate the "**Premium Exchanger**" and "**Premium Exchanger hooks**" plugins.

    <figure><img src="../../.gitbook/assets/image (1169).png" alt=""><figcaption></figcaption></figure>

3. Using an FTP client or file manager, delete the contents of the **`/wp-content/plugins/premiumbox/`** folder on the server, **except** for the following files and folders inside it:

* **`/flags/`**
* **`/languages/`**
* **`/moduls/`** (please read the note below first)

{% hint style="danger" %}
- If you **use** [**internal accounts**](https://premium.gitbook.io/main/osnovnye-nastroiki/nastroiki/vnutrennie-scheta/obmen-s-uchastiem-vnutrennego-scheta-polzovatelya), do **not** delete the **domacc** folder inside the **`moduls`** directory.
- If you **do not use** internal accounts, you can delete the entire **`moduls`** folder.
{% endhint %}

After updating the script, you need to transfer the internal accounts to the new module — [**transfer instructions**](https://premium.gitbook.io/main/pered-nachalom-raboty/instrukciya-po-obnovleniyu-skripta/obnovlenie-s-versii-2.5-do-2.6#id-2.-obnovlenie-modulya-vnutrennii-schyot-tolko-esli-vnutrennie-scheta-ispolzovalis-v-versii-2.5-.-esl) **(this step is only necessary if you used internal accounts in version 2.5)**

* If you **use** the Webmoney module, do **not** delete the **`x19`** folder inside the **`moduls`** directory.
* If you **do not use** the Webmoney module, you can delete the entire **`moduls`** folder.

---

* **`/sms/`**
* **`/userdata.php`**

<figure><img src="../../.gitbook/assets/image (1775).png" alt="" width="563"><figcaption><p><strong>Delete all files and folders marked with a checkmark on your server</strong></p></figcaption></figure>

4. Delete all files from the previous license in your website’s root folder.

<figure><img src="../../.gitbook/assets/image (1774).png" alt="" width="432"><figcaption></figcaption></figure>

Go to the "[**Your Licenses**](https://premiumexchanger.com/ulicense/)" section and download the license files archive named `license.zip`. To do this, click the "**Download for version 2.6**" link.

<figure><img src="../../.gitbook/assets/image (473).png" alt="" width="485"><figcaption></figcaption></figure>

Upload the downloaded archive to the [root folder of your website](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-naiti-kornevuyu-papku-saita-na-servere) using the **user account created specifically for the website** (do **not** use the **root** user!) and **make sure to extract the archive**.

{% hint style="danger" %}
**Step 4 is mandatory, even if the license files were previously uploaded to the server — otherwise, the site will not work!**
{% endhint %}

5. Go to the "[**Your Scripts**](https://premiumexchanger.com/uscripts/)" section and download the archive with the **update files for version 2.6** that matches your PHP version.

{% hint style="danger" %}
You must know the exact PHP version installed on your server to select the correct archive.\
[**Instructions on how to check the PHP version installed on your server**](https://premiumgitbook.io/main/osnovnye-nastroiki/faq/kak-proverit-versiyu-php-ustanovlennuyu-na-servere)
{% endhint %}

<figure><img src="../../.gitbook/assets/image (472).png" alt="" width="563"><figcaption></figcaption></figure>

6. Upload the contents of the update archive to the root folder of your website using the **user account created specifically for the site** (not the **root** user!). Use an FTP client or a file manager. Extract the archive, overwriting existing files.

7. Go to the "**Plugins**" section and activate the "**Premium Exchanger**" and "**Premium Exchanger hooks**" plugins.

8. Navigate to **Exchanger Settings → Migration**, and in the "**Migration (if your version is below 2.6)**" block, perform each step in order.

<figure><img src="../../.gitbook/assets/image (1682).png" alt="" width="390"><figcaption></figcaption></figure>

When you start each step, the system will determine the total number of requests that need to be processed. You can specify how many requests will be handled in each cycle.

<figure><img src="../../.gitbook/assets/image (500).png" alt="" width="345"><figcaption></figcaption></figure>

{% hint style="warning" %}
By default, the number of requests per cycle is set to 50. If you’re unsure about your server’s capacity, we recommend leaving this value unchanged.

You can change this number if needed, but if the server struggles to handle the specified amount of requests in one cycle, it may cause errors.
{% endhint %}

{% hint style="info" %}
You may notice buttons labeled "**Technical Step X**" next to the regular "**Step X**" buttons. Before executing each step, the system calculates the number of requests required. Sometimes this number can be too large for the server to handle.

In such cases, instead of using the "**Step X**" button, use the "**Technical Step X**" button. This option lets you manually specify the number of requests without the server calculating them.

If you use a **technical step**, you must manually enter the number of requests. We recommend setting this to a large number, such as 100,000.
{% endhint %}

9. Go to **Settings → Permalinks** and click the **Save Changes** button without making any changes on the page.  
10. Navigate to **Exchange Settings → General Settings** and disable the update mode.

<figure><img src="../../.gitbook/assets/image (1729).png" alt=""><figcaption></figcaption></figure>

Alternatively, in the same section, set the **Update Mode** option to **No** and save the changes.

<figure><img src="../../.gitbook/assets/image (474).png" alt="" width="255"><figcaption></figcaption></figure>

{% hint style="warning" %}
Update mode is automatically enabled every time the main plugin is deactivated and reactivated, so you must always disable it manually.
{% endhint %}

11. If you are using the **Parsers 2.0** or **BestChange parser** modules, after disabling update mode, you need to manually start the parsers by clicking the Cron link in their respective sections.  
    To run Parsers 2.0:

    <figure><img src="../../.gitbook/assets/image (394).png" alt=""><figcaption></figcaption></figure>

    To run the BestChange parser:

    <figure><img src="../../.gitbook/assets/image (392).png" alt="" width="563"><figcaption></figcaption></figure>
12. [Clear your browser cache](https://www.unisender.com/ru/blog/kak-ochistit-kehsh-v-brauzerah/).

    <figure><img src="../../.gitbook/assets/image (395).png" alt="" width="563"><figcaption></figcaption></figure>
13. <mark style="color:red;">**Be sure to delete any uploaded script zip archives and site backups from the root folder on your server.**</mark>

    <figure><img src="../../.gitbook/assets/image (396).png" alt="" width="563"><figcaption></figcaption></figure>
14. Disable maintenance mode in the **Console** section.  
15. <mark style="color:green;">**The update has been completed successfully!**</mark>

### Changes in the Admin Panel

After the update, you need to make some changes in the admin panel to ensure the script works correctly.

1. To enable email confirmation during registration, activate the **Email Confirmation Before Registration** module (**confirmregmail**) in the **Modules** section. If you do not use this feature, you can leave the module disabled.

<details>

Here is a natural, fluent English translation of the provided text:

---

### 2. Updating the "<strong>Internal Account</strong>" Module (only if <a href="https://premium.gitbook.io/main/osnovnye-nastroiki/nastroiki/vnutrennie-scheta/obmen-s-uchastiem-vnutrennego-scheta-polzovatelya">internal accounts</a> were used in version 2.5!)

If you have **not** used internal accounts before and want to start using them in version 2.6, you can skip this step. Simply activate the **iac** module in the "**Modules**" section and configure it following the <a href="https://premium.gitbook.io/main/osnovnye-nastroiki/nastroiki/vnutrennie-scheta">instructions</a>.

---

If you are currently using the **"Internal Account" (domacc)** module, as well as the merchant modules for receiving payments and auto payouts **domacc**:

![](<../../.gitbook/assets/image (1644).png>) ![](<../../.gitbook/assets/image (1645).png>)

It is <mark style="color:red;">**necessary**</mark> to switch to the new **"Internal Account Module" (iac)**.

### Migration Instructions for the New Module:

* Activate the new **iac** module in the "**Modules**" section (the **domacc** module must also be enabled during the migration process).
* Perform the migration steps sequentially — complete Step 7 and Step 8 in "**Exchange Settings**" -> "**Migration**".

![](<../../.gitbook/assets/image (1646).png>)

![](<../../.gitbook/assets/image (1647).png>) ![](<../../.gitbook/assets/image (1648).png>)

* After migration, disable the old **domacc** module in the "**Modules**" section, then delete the module from the server (module folder path: `wp-content/plugins/premiumbox/moduls/domacc`).

  ![](<../../.gitbook/assets/image (1649).png>)

* Remove the **domacc** merchant and auto payout modules via the admin panel under "**Merchants** -> Merchants" and "**Merchants** -> Auto Payouts**, then delete their folders from the server (paths: `wp-content/plugins/premiumbox/moduls/merchants/domacc` and `wp-content/plugins/premiumbox/moduls/paymerchants/domacc`).
* Add the new **iac** merchant and auto payout modules in "**Merchants** -> Merchants" and "**Merchants** -> Auto Payouts**" and configure them according to the [instructions](https://premium.gitbook.io/main/osnovnye-nastroiki/nastroiki/vnutrennie-scheta).
* Assign the newly created merchants to the appropriate exchange directions (in the "**Merchants and Payouts**" tab within the exchange direction settings).

![](<../../.gitbook/assets/image (463).png>)

---

If you need any further help with the migration or configuration, please refer to the linked documentation or contact support.

**Important!**  
If, when using merchant modules for deposits and automatic payouts with internal accounts, the internal account number for debiting and/or crediting funds is not specified in the exchange form, it will default to **`currency code + client ID`** from the client’s profile (under "**Personal Data**" -> "**Internal Account**").

![](<../../.gitbook/assets/image (1655).png>)![](<../../.gitbook/assets/image (1654).png>)

If an account is specified in the exchange form, that account will be used for debiting/crediting (note that this allows transferring currency to another exchanger user’s account if their ID is known).

![](<../../.gitbook/assets/image (1656).png>)

Please continue updating the script.

---

3. Starting from version 2.6, the **"Captcha for Website (Image Selection)" (sitecaptcha_img)** module automatically generates options for users to choose from on the site. In the previous version, you could create custom tasks, but from version 2.6 onward, this option is disabled, so any changes to the captcha’s appearance will be immediately reflected on the site.  
4. After updating, in the "**Exchanger Settings**" -> "**General Settings**" section, it is **mandatory** to select the logic for handling requests when using merchant modules for deposits under the option "**Action if merchant fails**".  
   For more details on how this option works, please refer to the instructions in "[**General Merchant Settings**](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov#podklyuchenie-neskolkikh-merchantov)".