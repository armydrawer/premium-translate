# Updating from Version 2.3 to 2.4

{% embed url="https://www.youtube.com/watch?v=PpNKzThZsCs" %}
Video guide for updating the script
{% endembed %}

{% hint style="warning" %}
Before starting the script update, ensure that the Ioncube Loader on your server is updated to version 12.0 or higher. If your current version is below 12, follow this [**guide to check the installed version**](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-obnovit-ioncube-loader). Your hosting provider's technical support can assist with the update.
{% endhint %}

{% hint style="warning" %}
If you are using merchant and auto-payout modules developed specifically for you by us, **please request updated versions of these modules in your Telegram group** (**not through the bot-based technical support**).

If you are using merchant, auto-payout, or other types of modules from third-party developers, they will not work with version 2.4 unless updated by their respective developers.
{% endhint %}

{% hint style="danger" %}
<mark style="color:red;">**Make sure to back up your website and database before updating!**</mark>

If something goes wrong during the update, you will be able to restore your website from the backup. Backup methods may vary depending on your hosting provider, so contact their technical support for guidance.

The simplest way to [**create a website backup**](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-sdelat-bekap-saita) is through your server control panel (e.g., ISP Manager or other software) using the built-in file manager or via an FTP client. Download the website files to your computer, and also export the database from the database management section or via PhpMyAdmin.
{% endhint %}

---

### Steps to Update:

1. In the exchange platform's admin panel, go to the "**Console**" section and enable maintenance mode to prevent users from making transactions during the update.

    <figure><img src="../../.gitbook/assets/image (1724).png" alt=""><figcaption></figcaption></figure>

2. In the "**Plugins**" section, deactivate the "**Premium Exchanger**" and "**Premium Exchanger hooks**" plugins.

    <figure><img src="https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FkanwK9s5DFo0cPzJd5Qn%252Fimage.png%3Falt%3Dmedia%26token%3D20ad3b3d-d619-4685-9146-08966a0d94f0&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=3b6bd9f3590a5f0a5aaa0d90711dfee97002c88ddb0f638e89ec840df877542a" alt=""><figcaption></figcaption></figure>

3. Using an FTP client or file manager, delete the contents of the **`/wp-content/plugins/premiumbox/`** folder on your server, **except** for the following files and folders:

   - **`/flags/`**
   - **`/languages/`**
   - **`/merchants/`** (if you haven’t renamed any files or folders inside the **`merchants`** folder, you can delete it as well)
   - **`/moduls/`**

   {% hint style="warning" %}
   If you **use** the Webmoney module, do not delete the **`x19`** folder inside **`moduls`**. If you don’t use it, you can delete the **`moduls`** folder entirely.
   {% endhint %}

   - **`/paymerchants/`** (if you haven’t renamed any files or folders inside the **`paymerchants`** folder, you can delete it as well)
   - **`/sms/`**
   - **`/userdata.php`**

   <figure><img src="https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FZnqfDaglTQ0LigKamF9G%252Fimage.png%3Falt%3Dmedia%26token%3D1bd35a48-772d-4170-a33e-9a3eadb3a014&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=41f54ff04d225224f01677ab6ed6cb37b5453bb1b682544b766d2ce8b248a73f" alt=""><figcaption></figcaption></figure>

4. Go to the "[**Your Licenses**](https://premiumexchanger.com/ulicense/)" section and download the license files archive (`license.zip`) by clicking the "**Download for version 2.4**" link.

   <figure><img src="../../.gitbook/assets/image (1726).png" alt="" width="491"><figcaption></figcaption></figure>

   Upload the downloaded archive to the [root folder of your website](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-naiti-kornevuyu-papku-saita-na-servere) using the <mark style="color:green;">**user created for the website**</mark> (not <mark style="color:red;">**root**</mark>!) and **make sure to extract the archive**.

   {% hint style="warning" %}
   **This step is mandatory, even if the license files were previously uploaded to the server. Otherwise, the website will not function!**
   {% endhint %}

5. Go to the "[**Your Scripts**](https://premiumexchanger.com/uscripts/)" section and download the archive with **update files for version 2.4** corresponding to your PHP version.

   {% hint style="warning" %}
   Make sure you know the exact PHP version installed on your server to select the correct archive.

   [**Guide to checking the PHP version installed on your server**](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-proverit-versiyu-php-ustanovlennuyu-na-servere)
   {% endhint %}

   <figure><img src="../../.gitbook/assets/image (431).png" alt="" width="563"><figcaption></figcaption></figure>

6. Upload the contents of the update archive to your website's root folder using the <mark style="color:green;">**user created for the website**</mark> (not <mark style="color:red;">**root**</mark>!). Use an FTP client or file manager and extract the archive, replacing the existing files.

7. In the "**Plugins**" section, activate the "**Premium Exchanger**" and "**Premium Exchanger hooks**" plugins.

8. Go to **"Exchange Settings" → "Migration"** and, in the "**Migration (if version is below 2.4)**" block, complete each step sequentially.

   <figure><img src="../../.gitbook/assets/image (432).png" alt=""><figcaption></figcaption></figure>

   For each step, the system will calculate the total number of requests to process. You can specify the number of requests to handle per cycle.

   {% hint style="warning" %}
   By default, the number of requests is set to 50. If you are unsure about your server's capacity, we recommend keeping the default value.

   If necessary, you can specify a different value, but if the cycle becomes too resource-intensive for the server, it may result in an error.
   {% endhint %}

   {% hint style="info" %}
   You may see "**Technical Step X**" buttons next to the "**Step X**" buttons. If the number of requests is too large for the server to calculate, use the "**Technical Step X**" button instead. This allows you to manually set the number of requests without the server calculating them.

   When using a **technical step**, we recommend setting a large number, such as 100,000.
   {% endhint %}

9. Go to "**Settings → Permalinks**" and click "**Save Changes**" without making any changes to the page.

10. Go to "**Exchange Settings → General Settings**" and disable maintenance mode.

    <figure><img src="../../.gitbook/assets/image (430).png" alt=""><figcaption></figcaption></figure>

    Alternatively, in the same section, set the "**Update Mode**" parameter to "**No**" and save the changes.

    <figure><img src="https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FD5YdRKPsWXynjlHPwdlM%252Fimage.png%3Falt%3Dmedia%26token%3D4bd5505a-e775-4478-b296-7d2bc5674825&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=18e1d61f8a35ed927e0d7be63e76703a80a07fda96c68b7bfa5405c5caf7da73" alt=""><figcaption></figcaption></figure>

    {% hint style="warning" %}
    Maintenance mode is automatically enabled after deactivating and reactivating the main plugin, so it must always be disabled manually.
    {% endhint %}

11. [Clear your browser cache](https://www.unisender.com/ru/blog/kak-ochistit-kehsh-v-brauzerah/).

12. <mark style="color:red;">**Delete all previously uploaded script zip archives, website backups, and the `damp_db.sql` file from the root folder on the server.**</mark>

13. Disable maintenance mode.