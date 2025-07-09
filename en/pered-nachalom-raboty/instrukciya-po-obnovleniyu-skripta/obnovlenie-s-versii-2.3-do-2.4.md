# Updating from Version 2.3 to 2.4

{% embed url="https://www.youtube.com/watch?v=PpNKzThZsCs" %}
Video tutorial for updating the script
{% endembed %}

{% hint style="warning" %}
Before starting the script update, make sure to upgrade the Ioncube Loader on your server to version 12.0 or higher (if your current version is below 12 — see the [**instructions on how to check your installed version**](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-obnovit-ioncube-loader)). Your hosting provider’s technical support can assist you with this update.
{% endhint %}

{% hint style="warning" %}
If you are using merchant and auto-payout modules that we have custom-developed specifically for you, **please request the updated modules in your Telegram group** (**do not request them via the support bot**).

If you are using merchant and auto-payout modules, or any other modules from third-party developers, they will not work on version 2.4 without updates from their respective developers.
{% endhint %}

{% hint style="danger" %}
<mark style="color:red;">**Make sure to back up your website and database before starting the update!**</mark>

If anything goes wrong during the update, you will be able to restore your site from the backup. Backup procedures may vary depending on your hosting provider, so please contact your hosting support for guidance.

The easiest way to [**back up your website**](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-sdelat-bekap-saita) is through your server control panel (ISP Manager or other software) using the built-in file manager, or via an FTP client (download your site files to your computer). Also, download your site database through the database management section or PhpMyAdmin.
{% endhint %}

1.  In the exchanger control panel, go to the "**Console**" section and enable technical mode to prevent users from submitting exchange requests during the script update.

    <figure><img src="../../.gitbook/assets/image (1724).png" alt=""><figcaption></figcaption></figure>
2.  In the "**Plugins**" section, deactivate the "**Premium Exchanger**" and "**Premium Exchanger hooks**" plugins.

3. Using an FTP client or file manager, delete the contents of the **`/wp-content/plugins/premiumbox/`** folder on your server, **except** for the following files and folders inside it:

* **`/flags/`**
* **`/languages/`**
* **`/merchants/`** (if you haven’t renamed any files or folders inside the **`merchants`** folder, you can delete this folder as well)
* **`/moduls/`**

{% hint style="warning" %}
If you **use** the Webmoney module, do **not** delete the **`x19`** folder inside the **`moduls`** folder. If you don’t use it, you can delete the entire **`moduls`** folder.
{% endhint %}

* **`/paymerchants/`** (if you **haven’t renamed** any files or folders inside the **`paymerchants`** folder, you can delete this folder as well)
* **`/sms/`**
* **`/userdata.php`**

4. Go to the "[**Your Licenses**](https://premiumexchanger.com/ulicense/)" section and download the license files archive named `license.zip`. To do this, click the link "**Download for version 2.4**".

Download the archive and upload it to the [root folder of your website](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-naiti-kornevuyu-papku-saita-na-servere) using the <mark style="color:green;">**user account created specifically for your website**</mark> (do **not** use the <mark style="color:red;">**root**</mark> user!). Then, **make sure to extract the archive**.

{% hint style="warning" %}
**Step 4 is mandatory, even if the license files were previously uploaded to the server — otherwise, the site will not work!**
{% endhint %}

5. Go to the "[**Your Scripts**](https://premiumexchanger.com/uscripts/)" section and download the archive with the **update files for version 2.4** that matches your PHP version.

{% hint style="warning" %}
You must know the exact PHP version installed on your server to select the correct archive.
{% endhint %}

Here is a natural, fluent English translation of the provided text:

---

[**Instructions for Checking the PHP Version Installed on Your Server**](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-proverit-versiyu-php-ustanovlennuyu-na-servere)

<figure><img src="../../.gitbook/assets/image (431).png" alt=""><figcaption></figcaption></figure>

6. Upload the contents of the update archive to the root folder of your website using the **user account created specifically for the site** (not the **root** user!). Use an FTP client or a file manager. Extract the archive, overwriting existing files.

7. Go to the "**Plugins**" section and activate the "**Premium Exchanger**" and "**Premium Exchanger hooks**" plugins.

8. Navigate to **Exchanger Settings → Migration**, and in the "**Migration (if version is below 2.4)**" block, perform each step in sequence.

<figure><img src="../../.gitbook/assets/image (432).png" alt=""><figcaption></figcaption></figure>

When you start each step, the system will determine the total number of queries that need to be executed. You can specify how many queries will be processed in one cycle.

<figure src="https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FFWLOCy5yHQlES4XZhyNP%252Fimage.png%3Falt%3Dmedia%26token%3D816f2042-40ad-417d-a819-dbab4d1cdaed&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=4f8942c4fdec930998beb26d9d6e249c4bda071b60c73d1199f594510b85daed" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
By default, the number of queries is set to 50. If you are unsure about your server’s capacity, we recommend leaving this value unchanged.

You can specify a different number if needed, but if processing that many queries in one cycle is too demanding for your server, it may cause an error.
{% endhint %}

{% hint style="info" %}
You may notice buttons labeled "**Technical Step X**" next to the "**Step X**" buttons. Before executing each step, the system calculates the number of queries required. Sometimes this number can be very large, and the server may struggle to calculate it.

In such cases, instead of using the "**Step X**" button, use the "**Technical Step X**" button. This allows you to manually specify the number of queries to process without the server calculating the total number.
{% endhint %}

---

Let me know if you need any adjustments or further help!

If you are using the **technical step**, you need to manually specify the number of requests. We recommend setting this to a deliberately large number, for example, 100,000.

9. Go to "**Settings → Permalinks**" and click the "**Save Changes**" button without making any changes on the page.  
10. Go to "**Exchange Settings → General Settings**" and disable the update mode.

<figure><img src="../../.gitbook/assets/image (430).png" alt=""><figcaption></figcaption></figure>

Alternatively, in the same section, set the "**Update Mode**" parameter to "**No**" and save the changes.

<figure><img src="https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FD5YdRKPsWXynjlHPwdlM%252Fimage.png%3Falt%3Dmedia%26token%3D4bd5505a-e775-4478-b296-7d2bc5674825&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=18e1d61f8a35ed927e0d7be63e76703a80a07fda96c68b7bfa5405c5caf7da73" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
Update mode is reactivated every time the main plugin is deactivated and then reactivated, so you must always disable it manually.
{% endhint %}

11. [Clear your browser cache](https://www.unisender.com/ru/blog/kak-ochistit-kehsh-v-brauzerah/).  
12. <mark style="color:red;">**Be sure to delete all previously uploaded script zip archives, site backups, and the file damp_db.sql from the root folder on your server.**</mark>  
13. Disable maintenance mode.