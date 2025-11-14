# How to Restore Access to the Exchange Panel?

Use one of the methods below to regain access.

***

## Lost Password for an Existing User

{% hint style="info" %}
If you’ve lost your password, first try resetting it using the dedicated form on the website: **`https://your_domain/lostpass/`**. If you receive an email with instructions to reset your password, follow the steps provided in the email.

If you don’t receive the email, it could mean that either password resets are disabled for this user due to security settings, or the [email template](https://premium.gitbook.io/main/en/basic-settings/uvedomleniya-administratoram-i-klientam/uvedomleniya-po-e-mail#nastroika-shablonov-pisem) for this type of notification hasn’t been configured.
{% endhint %}

In this case, you’ll need to manually reset the password for the existing administrator user.

1. Download the file from the link below:
2. Open the **`setpass.php`** file locally using a text editor (e.g., Notepad++) and edit the following lines: **`user_login`** and **`pass`**.

<figure><img src="../../../ru/.gitbook/assets/Screenshot_33 (4).png" alt=""><figcaption></figcaption></figure>

3. Save the changes. Ensure the file is encoded in UTF-8 without BOM.
4. Upload the **`setpass.php`** file to the [root directory](https://premium.gitbook.io/main/en/basic-settings/faq/kak-naiti-kornevuyu-papku-saita-na-servere) of your website.
5. Access the file in your browser at **`https://your_domain/setpass.php`**. A blank page will appear, indicating the password has been updated to the one specified in the file.
6. Log in to the admin panel as usual (typically at **`https://your_domain/prmmxchngr`**) using the new password.
7. Delete the **`setpass.php`** file from the root directory.

***

## Lost PIN Code for Admin Panel Login

If PIN-based authentication is enabled but you’re not receiving the PIN and can’t access the admin panel, follow these steps:

1. Open the **`/wp-content/plugins/premiumbox/userdata.php`** file.

<figure><img src="../../.gitbook/assets/image (1204)_eng.png" alt=""><figcaption><p>ISP Manager, folder structure</p></figcaption></figure>

2. Locate the line containing **`PN_ADMIN_GOWP`** and change its value from **false** to **true**, then save the file.

{% hint style="warning" %}
The **`PN_ADMIN_GOWP`** directive temporarily resets the admin panel login URL to **`https://your_domain/wp-admin/`**. During this time, email-based authentication will also be disabled.
{% endhint %}

<figure><img src="../../.gitbook/assets/image (1030)_eng.png" alt=""><figcaption><p>File: userdata.php</p></figcaption></figure>

3. Log in to the website at the standard URL **`https://your_domain/wp-admin/`** without entering a PIN code.
4. Adjust the necessary [settings](https://premium.gitbook.io/main/en/navigaciya/nastroiki/dvukhfaktornaya-avtorizaciya-2fa-v-paneli-upravleniya-saitom) to ensure proper notification functionality.
5. Revert the **true** value back to **false** in the **`userdata.php`** file.

***

## Lost URL for Admin Panel Login

If you’ve forgotten the URL for accessing the admin panel, follow these steps:

1. Open the **`/wp-content/plugins/premiumbox/userdata.php`** file.

<figure><img src="../../.gitbook/assets/image (1204)_eng.png" alt=""><figcaption><p>ISP Manager, folder structure</p></figcaption></figure>

2. Locate the line containing **`PN_ADMIN_GOWP`** and change its value from **false** to **true**, then save the file.

<figure><img src="../../.gitbook/assets/image (1030)_eng.png" alt=""><figcaption><p>File: userdata.php</p></figcaption></figure>

3. Log in to the admin panel at **`https://your_domain/wp-admin/`**.
4. Check the URL fields in the "**Settings**" -> "**General**" section. Ensure only the domain is specified, and the protocol **https://** is included before the domain name.

<figure><img src="../../../ru/.gitbook/assets/image (667) (1).png" alt=""><figcaption></figcaption></figure>

5. Verify the login URL in the "**Settings**" -> "**Main Settings**" section and update it if necessary.

<figure><img src="../../../ru/.gitbook/assets/image (630) (1).png" alt="" width="563"><figcaption></figcaption></figure>

6. Revert the **true** value back to **false** in the **`userdata.php`** file. Next time, log in using the URL specified in the settings.

***

## Unable to Access Admin Panel Due to IP Restrictions

If you’re locked out of the admin panel due to IP restrictions, you’ll need to create a temporary administrator account to disable the restrictions for the existing admin.

1. Download the file from the link below:

{% file src="../../../ru/.gitbook/assets/createuser (1).php" %}

2. Open the **`createuser.php`** file using a text editor (e.g., Notepad++) and edit the following lines: **`user_login`**, **`pass`**, and **`email`**.

<figure><img src="../../../ru/.gitbook/assets/Screenshot_34 (4).png" alt=""><figcaption></figcaption></figure>

3. Save the changes. Ensure the file is encoded in UTF-8 without BOM.
4. Upload the **`createuser.php`** file to the [root directory](https://premium.gitbook.io/main/en/basic-settings/faq/kak-naiti-kornevuyu-papku-saita-na-servere) of your website.
5. Access the file in your browser at **`https://your_domain/createuser.php`**. A blank page will appear, indicating the new user has been created.
6. Log in to the admin panel as usual (typically at **`https://your_domain/prmmxchngr`**) using the new credentials.
7. Delete the **`createuser.php`** file from the root directory.

***

## Premium Exchanger Plugin Deactivated

If the Premium Exchanger plugin has been deactivated and you can’t access the admin panel, follow these steps:

1. Temporarily rename the **`/wp-content/themes/exchanger/functions.php`** file on the server. You can use any temporary name.

<figure><img src="../../.gitbook/assets/%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5%20(165)_eng.png" alt=""><figcaption></figcaption></figure>

2. Log in to the admin panel using your credentials at **`https://your_domain/wp-admin/`**.
3. In the admin panel, go to the "**Plugins**" section and activate the "**Premium Exchanger**" plugin.

<figure><img src="../../.gitbook/assets/%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5%20(42)_eng.png" alt=""><figcaption></figcaption></figure>

4. Rename the **`functions.php`** file back to its original name.
