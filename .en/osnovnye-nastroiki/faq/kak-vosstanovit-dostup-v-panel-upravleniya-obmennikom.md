# How to Restore Access to the Exchange Control Panel

Use one of the methods below to regain access.

## Lost Password for an Existing User

{% hint style="info" %}
If you’ve lost your password, first try to reset it using the password recovery form on the website at **`https://your_domain/lostpass/`**. If you receive a password reset email, follow the instructions provided.

If you don’t receive the email, it may be because password resets are disabled for this user in the security settings, or the [email template](https://premium.gitbook.io/main/osnovnye-nastroiki/uvedomleniya-administratoram-i-klientam/uvedomleniya-po-e-mail#nastroika-shablonov-pisem) for this type of notification is not configured.
{% endhint %}

In this case, you will need to manually reset the password for the existing administrator user.

1. Download the file from the link below:

{% file src="../../.gitbook/assets/setpass.php" %}

2. Open the **`setpass.php`** file locally in a text editor (for example, Notepad++) and edit the following lines: **`user_login`** and **`pass`**.

<figure><img src="../../.gitbook/assets/Screenshot_33.png" alt=""><figcaption></figcaption></figure>

3. Save the changes. Make sure the file encoding is UTF-8 without BOM.
4. Upload the **`setpass.php`** file to the [root folder](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-naiti-kornevuyu-papku-saita-na-servere) of your website.
5. Open your browser and navigate to **`https://your_domain/setpass.php`** — the page will appear blank, indicating the password has been changed to the one specified in the file.
6. Log in to the control panel as usual (typically at **`https://your_domain/prmmxchngr`**) using the new password.
7. Delete the **`setpass.php`** file from the root folder immediately after.

## Lost PIN Code for Admin Panel Access

If PIN code authentication is enabled but you’re not receiving the PIN and cannot access the control panel, do the following:

* Open the file **`/wp-content/plugins/premiumbox/userdata.php`**.

<figure><img src="../../.gitbook/assets/image (1204).png" alt=""><figcaption><p>ISP Manager folder structure</p></figcaption></figure>

* Find the line containing **`PN_ADMIN_GOWP`** and change its value from **false** to **true**, then save the file.

This will disable PIN code authentication and allow you to log in normally.

Here is a natural, fluent English translation of the provided text:

---

{% hint style="warning" %}
The **`PN_ADMIN_GOWP`** directive allows you to temporarily reset the login URL for the admin panel to **`your_domain/wp-admin/`**. During this period, the option to log in via email authorization will also be disabled.
{% endhint %}

<figure><img src="../../.gitbook/assets/image (1030).png" alt=""><figcaption><p>File: userdata.php</p></figcaption></figure>

* Log in to the site using the standard address **`https://your_domain/wp-admin/`** without entering a PIN code.
* Make the necessary [settings](https://premium.gitbook.io/rukovodstvo-polzovatelya/navigaciya/nastroiki/dvukhfaktornaya-avtorizaciya-2fa-v-paneli-upravleniya-saitom) to ensure notifications work correctly.
* Change the value back from **true** to **false** in the **`userdata.php`** file.

## Lost the URL to access the admin panel?

If you have forgotten the URL to access the admin panel, you need to:

* Open the file **`/wp-content/plugins/premiumbox/userdata.php`**.

<figure><img src="../../.gitbook/assets/image (1204).png" alt=""><figcaption><p>ISP Manager folder structure</p></figcaption></figure>

* In the specified line (**`PN_ADMIN_GOWP`**), change **false** to **true** and save the changes.

<figure><img src="../../.gitbook/assets/image (1030).png" alt=""><figcaption><p>File: userdata.php</p></figcaption></figure>

* Log in to the admin panel at **`https://your_domain/wp-admin/`**.
* Check the URLs in both fields under "**Settings**" -> "**General**" (only the domain name should be specified, and the protocol **https://** must be included before the domain name).

<figure><img src="../../.gitbook/assets/image (667).png" alt=""><figcaption></figcaption></figure>

* Verify the login URL under "**Settings**" -> "**Main Settings**" and update it if necessary.

<figure><img src="../../.gitbook/assets/image (1573).png" alt="" width="563"><figcaption></figcaption></figure>

* Change the value back from **true** to **false** in the **`userdata.php`** file, and next time you log in, use the URL specified in the settings.

## Unable to access the admin panel due to IP address restrictions?

In this case, you need to create a new temporary administrator user to disable IP restrictions for the existing administrator.

1. Download the file from the link below:

{% file src="../../.gitbook/assets/createuser.php" %}

2. Open the `createuser.php` file with a text editor (for example, Notepad++) and edit the following lines: **`user_login`**, **`pass`**, and **`email`**.

<figure><img src="../../.gitbook/assets/Screenshot_34.png" alt=""><figcaption></figcaption></figure>

---

If you need any further help or adjustments, just let me know!

3. Save the changes. The file encoding must be UTF-8 without BOM.  
4. Upload the **`createuser.php`** file to the [root folder](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-naiti-kornevuyu-papku-saita-na-servere) of your website.  
5. Using your browser, go to **`https://your_domain/createuser.php`** — after opening this link, a blank page will appear, indicating that the new user has been created.  
6. Log in to the control panel as usual (typically at **`https://your_domain/prmmxchngr`**) using the new username and password.  
7. Delete the **`createuser.php`** file from the root folder.  

## Premium Exchanger Plugin Deactivated

If the Premium Exchanger plugin has been deactivated and you cannot access the control panel, follow these steps:

1. Temporarily rename the file **`/wp-content/themes/exchanger/functions.php`** on your server. The temporary filename can be anything you choose.  

    <figure><img src="../../.gitbook/assets/изображение (165).png" alt=""><figcaption></figcaption></figure>  
2. Log in to the control panel at **`https://your_domain/wp-admin/`** using your username and password.  
3. In the control panel, go to the "**Plugins**" section and activate the "**Premium Exchanger**" plugin.  

    <figure><img src="../../.gitbook/assets/изображение (42).png" alt=""><figcaption></figcaption></figure>  
4. Rename the **`functions.php`** file back to its original name.