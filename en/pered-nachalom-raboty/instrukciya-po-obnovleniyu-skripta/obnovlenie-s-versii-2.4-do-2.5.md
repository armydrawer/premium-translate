# Updating from Version 2.4 to 2.5

{% embed url="https://www.youtube.com/watch?v=PpNKzThZsCs" %}
Video tutorial on how to update the script
{% endembed %}

{% hint style="success" %}
The list of script updates for version 2.5 is available [**here**](https://premium.gitbook.io/main/pered-nachalom-raboty/instrukciya-po-obnovleniyu-skripta/spisok-obnovlenii#versiya-2.5)
{% endhint %}

{% hint style="warning" %}
Before updating the script, please update the Ioncube Loader on your server to version 12.0 or higher (if your current version is below 12 — see the [**instructions to check your installed version**](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-obnovit-ioncube-loader)). Your hosting provider’s technical support can assist you with this update.
{% endhint %}

{% hint style="warning" %}
If you are using merchant and auto-payout modules that we have custom-developed specifically for you, **please request the updated modules in your Telegram group (not through the support bot).**

If you are using merchant and auto-payout modules, or any other modules from third-party developers, they will not work with version 2.5 unless updated by their respective developers.
{% endhint %}

{% hint style="danger" %}
<mark style="color:red;">**Make sure to back up your website and database before updating!**</mark>

If anything goes wrong during the update, you will be able to restore your site from the backup. Backup procedures may vary depending on your hosting provider, so please contact your hosting support for guidance.

The easiest way to [**back up your website**](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-sdelat-bekap-saita) is through your server control panel (ISP Manager or other software) using the built-in file manager, or via an FTP client (download your site files to your computer, and export your database through the database management section or PhpMyAdmin).
{% endhint %}

1. In the exchanger control panel, go to the "**Console**" section and enable technical mode to prevent users from submitting requests on the site during the script update.

2. In the "**Plugins**" section, deactivate the "**Premium Exchanger**" and "**Premium Exchanger hooks**" plugins.

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

4. Go to the "[**Your Licenses**](https://premiumexchanger.com/ulicense/)" section and download the license files archive `license.zip` by clicking the "**Download for version 2.5**" link.

Upload the downloaded archive to the [root folder of your website](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-naiti-kornevuyu-papku-saita-na-servere) using the <mark style="color:green;">**user account created specifically for the website**</mark> (not the <mark style="color:red;">**root**</mark> user!) and **make sure to extract the archive**.

{% hint style="warning" %}
**Step 4 is mandatory, even if the license files were previously uploaded to the server — otherwise, the site will not work!**
{% endhint %}

5. Go to the "[**Your Scripts**](https://premiumexchanger.com/uscripts/)" section and download the archive with the **update files for version 2.5** that correspond to your PHP version.

{% hint style="warning" %}
It is essential to know the exact PHP version installed on your server to select the appropriate archive.

\
[**Instructions for checking the PHP version installed on your server**](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-proverit-versiyu-php-ustanovlennuyu-na-servere)
{% endhint %}

<figure><img src="../../.gitbook/assets/image (1727).png" alt="" width="563"><figcaption></figcaption></figure>

6. Upload the contents of the update archive to the root folder of your website using the <mark style="color:green;">**user account created specifically for the site**</mark> (do **not** use the <mark style="color:red;">**root**</mark> user!). Use an FTP client or a file manager. Extract the archive, overwriting existing files.
7. Go to the "**Plugins**" section and activate the "**Premium Exchanger**" and "**Premium Exchanger hooks**" plugins.
8. Navigate to **Exchange Settings → Migration** and in the "**Migration (if version is below 2.5)**" block, perform each step in order.

<figure><img src="../../.gitbook/assets/image (1728).png" alt=""><figcaption></figcaption></figure>

When you start each step, the system will determine the total number of requests that need to be processed. You can specify how many requests will be handled in one cycle.

<figure><img src="https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FFWLOCy5yHQlES4XZhyNP%252Fimage.png%3Falt%3Dmedia%26token%3D816f2042-40ad-417d-a819-dbab4d1cdaed&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=4f8942c4fdec930998beb26d9d6e249c4bda071b60c73d1199f594510b85daed" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
The default number of requests is 50. If you are unsure about your server’s capacity, we recommend leaving this value unchanged.

You can specify a different number if needed, but if processing a cycle with that number of requests is too demanding for your server, it may cause an error.
{% endhint %}

{% hint style="info" %}
You may notice buttons labeled "**Technical Step X**" next to the "**Step X**" buttons. Before executing each step, the system determines how many requests need to be made. In some cases, the number of requests can be very large, and the server may not be able to handle counting them. In such cases, instead of using the "**Step X**" button, use the "**Technical Step X**" button. This allows you to manually specify the number of requests without the server counting them automatically.

If you use a **technical step**, you need to manually enter the number of requests. We recommend setting this to a deliberately large number, for example, 100,000.
{% endhint %}

9. Go to "**Settings → Permalinks**" and click the "**Save Changes**" button without making any changes on the page.  
10. Go to "**Exchange Settings → General Settings**" and disable the update mode.

<figure><img src="https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FqD6Colq0xrmFjalnTI1c%252Fimage.png%3Falt%3Dmedia%26token%3D5e3e18f3-4570-4531-9ede-3e2f5a3348b9&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=377a9d72ec32e510daea3924a85e30a80b644de9ef0d6ba9cae571a68720010a" alt=""><figcaption></figcaption></figure>

Alternatively, in the same section, set the "**Update Mode**" parameter to "**No**" and save the changes.

<figure><img src="https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FD5YdRKPsWXynjlHPwdlM%252Fimage.png%3Falt%3Dmedia%26token%3D4bd5505a-e775-4478-b296-7d2bc5674825&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=18e1d61f8a35ed927e0d7be63e76703a80a07fda96c68b7bfa5405c5caf7da73" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
The update mode is activated every time the main plugin is deactivated and then reactivated, so you always need to disable this mode manually.
{% endhint %}

11. If you are using the "**Parsers 2.0**" or "**Bestchange parser**" modules, after disabling the update mode, you need to manually start the parsers in their respective sections by clicking the Cron link.  
12. [Clear your browser cache](https://www.unisender.com/ru/blog/kak-ochistit-kehsh-v-brauzerah/).  
13. <mark style="color:red;">**Be sure to delete any uploaded script zip archives and website backups from the server’s root folder.**</mark>  
14. Disable maintenance mode.