# Script Installation Instructions

{% hint style="info" %}
The images provided in the instructions may differ from those used in your personal system.

Here and throughout the text, replace "**your_domain**" with the direct address of your website (for example, if your website address is **premiumexchanger.com**, then you should replace "**your_domain**" with **premiumexchanger.com**).
{% endhint %}

{% hint style="danger" %}
Please note that **all** files must be uploaded under a <mark style="color:green;">user created for the site</mark> (not <mark style="color:red;">root</mark>). Uploading files under the <mark style="color:red;">root user</mark> will lead to unstable site operation.

If you have already uploaded files under the root user, you need to take the following actions:

1. Backup all files on the server
2. [Download from our website](https://premiumexchanger.com/uscripts/) the distribution for UPDATE for your script version (usually version 2.5) and your PHP version

<img src="../.gitbook/assets/image (1509).png" alt="" data-size="original">

3. Upload it to the root folder of the site and unpack the archive, replacing the files
{% endhint %}

## Recommended Security Settings and Server System Requirements <a href="#chapter1" id="chapter1"></a>

We recommend implementing the following server settings to reduce the risks of server hacking where your site is located:

* Update the [Ioncube Loader](https://www.ioncube.com/loaders.php) module to the latest version;
* Install the [fail2ban](https://github.com/fail2ban/fail2ban) module on the server;
* Install an antivirus on the server;
* Block ports for FTP, SSH, and various Shell clients;
* Block standard addresses to the server authorization form. For example, for ISP Manager it is:\
  • `https://ip_address/manager/`\
  • `https://ip_address/manager/ispmngr/`\
  • `https://ip_address/ispmngr/`
* Change the default port for the server authorization form. For ISP Manager, port 1500 is usually used. Set any available port value;
* Block access to phpmyadmin address and port;
* Block access to mail clients. For example,\
  • `https://ip_address/webmail/`\
  • `https://ip_address/roundcube/`\
  • and similar
* Set a password of at least 15-25 characters for all server users, including root.

System requirements for the server:

* PHP 8.1/8.2/8.3;
* MySQL 5.0 and above;
* IonCube Loader 13.0 and above;
* Task scheduler (cron);
* Required additional PHP functions, extensions, and libraries: iconv, mb, curl, gd, openssl, soap, gmpobject, ziparchive.

## Installing the main product on the server <a href="#chapter2" id="chapter2"></a>

**1. Uploading files**

{% hint style="danger" %}
We would like to remind you again that site files should **always** be uploaded under the <mark style="color:green;">user created for the site</mark>, not under the <mark style="color:red;">root user</mark>.
{% endhint %}

In your account in the "[**Your scripts**](https://premiumexchanger.com/uscripts/)" section, download the corresponding script build depending on the PHP version installed on your server. If you do not know which version is installed on your server, please contact your hosting technical support.

<figure><img src="../.gitbook/assets/image (763).png" alt="" width="335"><figcaption><p>The script distribution already contains all available merchants and modules.<br>Separate installation of merchants and modules is not required.</p></figcaption></figure>

The downloaded archive or its contents should be uploaded to the server. The upload should be done to the root folder of the site (usually the folders `public_html, www`, or `docs`). Use the built-in file manager in the control panel or use an FTP client for file upload: Total Commander, CuteFTP, and others. The FTP client should have binary file transfer mode enabled (usually this mode is set by default).

**2. Generating a license**

In the "[**Your licenses**](https://premiumexchanger.com/ulicense/)" section, download the archive with the license files `license.zip`. To do this, specify the name of your domain (also specify the subdomain name if necessary) where the script will be installed and click the "**Save**" button. Then click on the "**Download for version X.X**" button. Upload the downloaded `license.zip` archive to the root folder of your site (usually the folders `public_html, www`, or `docs`) and extract the archive.

{% hint style="warning" %}
<mark style="color:red;">If the domain name for the license is not specified and saved, you cannot download the archive with the license files.</mark> <mark style="color:red;"></mark><mark style="color:red;">**Be careful**</mark> <mark style="color:red;"></mark><mark style="color:red;">when specifying the domain name to avoid errors. It is impossible to change, redo, or replace the license for another domain. You will need an additional license for a second domain.</mark>
{% endhint %}

License files are responsible for the script's functionality, so you need to follow these rules:

* License files cannot be renamed. Use them with the names you downloaded them with.
* License files should be located in the root folder of the site (usually the folders `public_html`, `www`, or `docs`).
* The permissions for the license files should be set to 644.
* The content of the license files should remain unchanged.

**3. Creating a Database**

In the server control panel (for example, ISP Manager), find the "**Databases**" section and create a new database. Enter the database name, database user name, and generate a complex password:

<figure><img src="../.gitbook/assets/image (1080).png" alt=""><figcaption></figcaption></figure>

Remember or write down this information, as you will need it later.

**4. Installation**

Paste the following link into your browser's address bar:

`https://your_domain/installer/`, go to it, and follow the instructions:

4.1. Select the installation language.

<figure><img src="../.gitbook/assets/image (586).png" alt="" width="563"><figcaption></figcaption></figure>

4.2. Check the basic system requirements of your server. If any of the parameters do not meet the requirements, you will see a warning about it. Click "**Skip**" if the check did not reveal any errors. If errors were found, correct them and restart the installation process.

<figure><img src="../.gitbook/assets/image (587).png" alt="" width="563"><figcaption></figcaption></figure>

4.3. Check the functions and PHP libraries of your server. If any of the parameters do not meet the requirements, you will see a warning about it. Click "**Skip**" if no errors are found. If errors are detected, correct them and restart the installation process.

4.4. Check the write permission of certain files and folders. If any of the parameters do not meet the requirements, you will see a warning about it. Click "**Skip**" if no errors are found. If errors are detected, correct them and restart the installation process.

4.5. Fill in the database name, database username, and password that you specified in step 3. Click the "**Update Config**" button.

4.6. Click the "**Choose File**" button and select the file `damp_db.sql`. The files are located in the root of the downloaded archive on your computer. Specify the [full address of the site](#user-content-fn-1)[^1]. Click the "**Import**" button.

If the system cannot import the database file and displays an error, manually import the database file through phpmyadmin, which is available on your server. Then in the database, in the `pr_options` table, specify the full name of your site for the `home` and `siteurl` values.

4.7. Enter the personal email of the site administrator, the site email (create a corresponding mailbox on the server), the sender's name (usually the site name), and set the login and password for the administrator to access the control panel. Click the "**Install**" button.

4.8. Choose the language of the site and the control panel.

4.9. **Be sure to delete the installer files!** On the final step of the installation, click on the link: "**Attention! Click here to delete the installer files**".

**Script installation completed.**

5. Site Control Panel

**Default control panel address:** `https://your_domain/prmmxchngr/`

Use the login and password provided during installation.

## Installing additional modules <a href="#chapter3" id="chapter3"></a>

{% hint style="info" %}
The script distribution already includes all available merchants and modules. Separate installation of merchants and modules is not required.
{% endhint %}

**1. Merchant modules for receiving payments**

1.1. In your personal account in the section "[**Your scripts**](https://premiumexchanger.com/uscripts/)" in the "**Additional modules**" block, download the merchant module for receiving payments for the required payment system.

1.2. Upload the contents of the downloaded archive to the server in the directory `your_domain/wp-content/plugins/premiumbox/merchants.`

Then configure the module according to the instructions described in the [user manual](https://premium.gitbook.io/rukovodstvo-polzovatelya/navigaciya/merchanty-i-vyplaty).

**2. Auto payment modules**

2.1. In your personal account in the section "[**Your scripts**](https://premiumexchanger.com/uscripts/)" in the "**Additional modules**" block, download the auto payment module for the required payment system.

2.2. Upload the contents of the downloaded archive to the server in the directory `your_domain/wp-content/plugins/premiumbox/paymerchants`.

Then configure the module according to the instructions described in the [user manual](https://premium.gitbook.io/rukovodstvo-polzovatelya/navigaciya/merchanty-i-vyplaty/vyplaty).

[^1]: Cyrillic domain should be specified in the format `xn--90aiufb.xn--p1ai`