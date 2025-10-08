# Update from Version 2.3 to 2.4

{% embed url="https://www.youtube.com/watch?v=PpNKzThZsCs" %}
Video tutorial for updating the script
{% endembed %}

{% hint style="warning" %}
Before starting the script update, please update the Ioncube Loader on your server to version 12.0 or higher (if the installed version is below 12 — [**instructions for checking the installed version**](https://premium.gitbook.io/main/en/basic-settings/faq/kak-obnovit-ioncube-loader)). Your hosting provider's technical support can assist you with the update.
{% endhint %}

{% hint style="warning" %}
If you are using merchant and auto-payment modules developed specifically for you, please request the updated modules in your Telegram group (**not through technical support via the bot**).

If you are using merchant and auto-payment modules, as well as other types of modules from third-party developers, they will not work on version 2.4 without updates from the developers.
{% endhint %}

{% hint style="danger" %}
<mark style="color:red;">**Before updating, make sure to back up your website and database!**</mark>

If something goes wrong during the update, you can always restore your site from the backup. Backup methods may vary depending on your hosting provider, so it's advisable to contact their technical support for assistance.

The easiest way to [**back up your website**](https://premium.gitbook.io/main/en/basic-settings/faq/kak-sdelat-bekap-saita) is through your server's control panel (ISP Manager or other software) using the built-in file manager or via an FTP client (download the website files to your computer, and also download the database from the database management section or through PhpMyAdmin).
{% endhint %}

1. In the exchange panel, go to the "**Console**" section and enable technical mode to prevent users from making requests on the site during the script update.

    <figure><img src="../../.gitbook/assets/image (1724)_eng.png" alt=""><figcaption></figcaption></figure>
2. In the "**Plugins**" section, deactivate the "**Premium Exchanger**" and "**Premium Exchanger hooks**" plugins.

    <figure><img src="https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FkanwK9s5DFo0cPzJd5Qn%252Fimage_eng.png%3Falt%3Dmedia%26token%3D20ad3b3d-d619-4685-9146-08966a0d94f0&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=3b6bd9f3590a5f0a5aaa0d90711dfee97002c88ddb0f638e89ec840df877542a" alt=""><figcaption></figcaption></figure>
3. Using an FTP client or file manager, delete the contents of the **`/wp-content/plugins/premiumbox/`** folder on the server, **except** for the following files and folders inside it:

* **`/flags/`**
* **`/languages/`**
* **`/merchants/`** (if you haven't changed the names of the files and folders inside the **`merchants`** folder, you can delete it as well)
* **`/moduls/`**

{% hint style="warning" %}
If you **are using** the Webmoney module, do not delete the **`x19`** folder inside the **`moduls`** folder; if you are not using it, you can delete the **`moduls`** folder entirely.
{% endhint %}

* **`/paymerchants/`** (if you **haven't changed** the names of the files and folders inside the **`paymerchants`** folder, you can delete it as well)
* **`/sms/`**
* **`/userdata.php`**

<figure><img src="https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FZnqfDaglTQ0LigKamF9G%252Fimage_eng.png%3Falt%3Dmedia%26token%3D1bd35a48-772d-4170-a33e-9a3eadb3a014&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=41f54ff04d225224f01677ab6ed6cb37b5453bb1b682544b766d2ce8b248a73f" alt=""><figcaption></figcaption></figure>

4. Go to the "[**Your Licenses**](https://premiumexchanger.com/ulicense/)" section and download the archive with the license files `license.zip`. Click on the link "**Download for version 2.4**".

<figure><img src="../../.gitbook/assets/image (1726)_eng.png" alt="" width="491"><figcaption></figcaption></figure>

Upload the downloaded archive to the [root folder of your website](https://premium.gitbook.io/main/en/basic-settings/faq/kak-naiti-kornevuyu-papku-saita-na-servere) using the <mark style="color:green;">**user created for the site**</mark> (not <mark style="color:red;">**root**</mark>!) and **make sure to extract the archive**.

{% hint style="warning" %}
**Make sure to complete step 4, even if the license files were previously uploaded to the server — otherwise, the site will not function!**
{% endhint %}

5. Go to the "[**Your Scripts**](https://premiumexchanger.com/uscripts/)" section and download the archive with the **files for updating to version 2.4** for your PHP version.

{% hint style="warning" %}
You need to know the exact PHP version installed on your server to select the appropriate archive.

\
[**Instructions for checking the PHP version installed on the server**](https://premium.gitbook.io/main/en/basic-settings/faq/kak-proverit-versiyu-php-ustanovlennuyu-na-servere)
{% endhint %}

<figure><img src="../../.gitbook/assets/image (431)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

6. Upload the contents of the update archive to the root folder of your website using the <mark style="color:green;">**user created for the site**</mark> (not <mark style="color:red;">**root**</mark>!). Use an FTP client or file manager. Extract the archive, replacing the existing files.
7. Go to the "**Plugins**" section and activate the "**Premium Exchanger**" and "**Premium Exchanger hooks**" plugins.
8. Navigate to the "**Exchange Settings** → "Migration"** section and sequentially complete each step in the "**Migration (if version is less than 2.4)**" block.

<figure><img src="../../.gitbook/assets/image (432)_eng.png" alt=""><figcaption></figcaption></figure>

When you start each step, the system will determine the total number of requests that need to be processed. You can specify the number of requests to be handled in one cycle.

<figure><img src="https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FFWLOCy5yHQlES4XZhyNP%252Fimage_eng.png%3Falt%3Dmedia%26token%3D816f2042-40ad-417d-a819-dbab4d1cdaed&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=4f8942c4fdec930998beb26d9d6e249c4bda071b60c73d1199f594510b85daed" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
By default, the number of requests = 50. If you are unsure about your server's capacity, we recommend not changing the default value.

You can specify any other value if necessary, but if the cycle execution with the specified value proves too resource-intensive for the server, it will result in an error.
{% endhint %}

{% hint style="info" %}
You will see "**Technical Step X**" buttons next to the "**Step X**" buttons. Before executing each step, the system determines the number of requests that need to be processed. In some cases, the number of requests may be too high, and the server may struggle to handle the count. In this case, instead of the "**Step X**" button, you should use the "**Technical Step X**" button, which allows you to manually specify an arbitrary number of requests without the server counting them.

If you use the **technical step**, you will need to manually specify the number of requests. We recommend setting a large number, such as 100,000.
{% endhint %}

9. Go to the "**Settings** → "Permalinks"** section and click the "**Save Changes**" button without making any changes on the page.
10. Navigate to the "**Exchange Settings** → "General Settings"** section and disable the update mode.

<figure><img src="../../.gitbook/assets/image (430)_eng.png" alt=""><figcaption></figcaption></figure>

An alternative option is to select "**No**" for the "**Update Mode**" parameter in the same section and save the changes.

<figure><img src="https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FD5YdRKPsWXynjlHPwdlM%252Fimage_eng.png%3Falt%3Dmedia%26token%3D4bd5505a-e775-4478-b296-7d2bc5674825&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=18e1d61f8a35ed927e0d7be63e76703a80a07fda96c68b7bfa5405c5caf7da73" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
The update mode is activated each time the main plugin is deactivated and reactivated, so it must always be manually disabled.
{% endhint %}

11. [Clear your browser cache](https://www.unisender.com/ru/blog/kak-ochistit-kehsh-v-brauzerah/).
12. <mark style="color:red;">**Make sure to delete all previously uploaded zip archives of the script and website backups from the root folder on the server, as well as the file damp_db.sql.**</mark>
13. Disable maintenance mode.