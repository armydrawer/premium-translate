# Script Installation Guide

{% hint style="info" %}
The images shown in this guide may differ from those in your personal system.

Throughout this guide, replace "**your_domain**" with the direct address of your website (for example, if your website address is **premiumexchanger.com**, replace "**your_domain**" with **premiumexchanger.com**).
{% endhint %}

{% hint style="danger" %}
Please note that **all** files must be uploaded by the <mark style="color:green;">user account created specifically for the website</mark> (not the <mark style="color:red;">root</mark> user). Uploading files as the <mark style="color:red;">root user</mark> will cause your website to function unstably.

If you have already uploaded files as the root user, please follow these steps:

1. Back up all files on your server.
2. [Download the update package](https://premiumexchanger.com/uscripts/) from our website that matches your script version (usually version 2.5) and your PHP version.

<img src="../.gitbook/assets/image (1509).png" alt="" data-size="original">

3. Upload the package to your website’s root directory and extract the archive, overwriting existing files.
{% endhint %}

## Recommended Security Settings and Server Requirements <a href="#chapter1" id="chapter1"></a>

We recommend applying the following server settings to reduce the risk of your website being compromised:

* Update the [Ioncube Loader](https://www.ioncube.com/loaders.php) module to the latest version.
* Install the [fail2ban](https://github.com/fail2ban/fail2ban) module on your server.
* Install antivirus software on your server.
* Block ports used for FTP, SSH, and various shell clients.
* Block default URLs for server login pages. For example, in ISP Manager, block:\
  • `https://ip_address/manager/`\
  • `https://ip_address/manager/ispmngr/`\
  • `https://ip_address/ispmngr/`
* Change the default port for the server login page. ISP Manager typically uses port 1500; set it to any available port.
* Block access to phpMyAdmin URLs and ports.
* Block access to webmail clients, such as:\
  • `https://ip_address/webmail/`\
  • `https://ip_address/roundcube/`\
  • and similar addresses.
* Set strong passwords of at least 15–25 characters for all server users, including root.


#### Server System Requirements:

* PHP 8.1 / 8.2 / 8.3;
* MySQL 5.0 or higher;
* IonCube Loader 13.0 or higher;
* Task scheduler (cron);
* Required additional PHP functions, extensions, and libraries: iconv, mbstring, curl, gd, openssl, soap, gmp, ziparchive.

## Installing the Main Product on the Server <a href="#chapter2" id="chapter2"></a>

**1. Uploading Files**

{% hint style="danger" %}
Please note again that website files **must always** be uploaded under the <mark style="color:green;">user account created specifically for the website</mark>, and **not** under the <mark style="color:red;">root user</mark>.
{% endhint %}

In your personal account, go to the "[**Your Scripts**](https://premiumexchanger.com/uscripts/)" section and download the appropriate script package according to the PHP version installed on your server. If you are unsure which PHP version is installed, please contact your hosting provider’s technical support for assistance.

<figure><img src="../.gitbook/assets/image (763).png" alt="" width="335"><figcaption><p>The script distribution already includes all available merchants and modules.<br>Separate installation of merchants and modules is not required.</p></figcaption></figure>

Upload the downloaded archive or its contents to your server. The upload should be done to the website’s root directory (usually `public_html`, `www`, or `docs`). Use the file manager built into your control panel, or an FTP client such as Total Commander, CuteFTP, or others. Make sure your FTP client is set to binary transfer mode (this is usually the default setting).

**2. Generating the License**

In the "[**Your Licenses**](https://premiumexchanger.com/ulicense/)" section, download the license files archive `license.zip`. To do this, enter your domain name (and subdomain name if applicable) where the script will be installed, then click the "**Save**" button. After that, click "**Download for version X.X**". Upload the downloaded `license.zip` archive to your website’s root directory (usually `public_html`, `www`, or `docs`) and extract its contents.

<figure><img src="../.gitbook/assets/image (764).png" alt="" width="563"><figcaption></figcaption></figure>

{% hint style="warning" %}
<mark style="color:red;">If the domain name for the license is not specified and saved, you will not be able to download the license files archive.</mark> <mark style="color:red;"></mark><mark style="color:red;">**Please be careful**</mark> <mark style="color:red;"></mark><mark style="color:red;">when entering the domain name to avoid mistakes. It is impossible to change, redo, or transfer the license to another domain. You will need to purchase an additional license for a second domain.</mark>
{% endhint %}

License files are essential for the script to function properly, so please follow these rules carefully:

* Do not rename the license files. Use them exactly as you downloaded them.
* License files must be placed in the website’s root directory (usually `public_html`, `www`, or `docs`).
* The file permissions for the license files should be set to 644.
* The contents of the license files must remain unchanged.

**3. Creating the Database**

In your server’s web control panel (for example, ISP Manager), locate the "**Databases**" section and create a new database. Enter the database name, database username, and generate a strong password:

<figure><img src="../.gitbook/assets/image (1080).png" alt=""><figcaption></figcaption></figure>

Make sure to remember or write down these details, as you will need them later.

**4. Installation**

In your browser’s address bar, enter the following URL:

`https://your_domain/installer/`, then go to this link and follow the instructions:

4.1. Select the installation language.

<figure><img src="../.gitbook/assets/image (586).png" alt="" width="563"><figcaption></figcaption></figure>

4.2. Check your server’s basic system requirements. If any parameter does not meet the requirements, you will see a warning. Click "**Skip**" if no errors are found. If errors are detected, fix them and restart the installation process.

<figure><img src="../.gitbook/assets/image (587).png" alt="" width="563"><figcaption></figcaption></figure>

4.3. Check your server’s PHP functions and libraries. If any of the settings don’t meet the requirements, you will see a warning. Click "**Skip**" if no errors are found. If errors are detected, fix them and restart the installation process.

<figure><img src="../.gitbook/assets/image (588).png" alt="" width="563"><figcaption></figcaption></figure>

4.4. Verify the write permissions for certain files and folders. If any of the settings don’t meet the requirements, you will see a warning. Click "**Skip**" if no errors are found. If errors are detected, fix them and restart the installation process.

<figure><img src="../.gitbook/assets/image (589).png" alt=""><figcaption></figcaption></figure>

4.5. Enter the database name, database username, and password that you specified in step 3. Then click the "**Update Config**" button.

<figure><img src="../.gitbook/assets/Screenshot_8 (2).png" alt="" width="563"><figcaption></figcaption></figure>

4.6. Click the "**Choose File**" button and select the `damp_db.sql` file. These files are located in the root folder of the archive you downloaded to your computer. Enter the [full website URL](#user-content-fn-1)[^1]. Then click "**Import**".

<figure><img src="../.gitbook/assets/image (590).png" alt="" width="563"><figcaption></figcaption></figure>

If the system cannot import the database file and shows an error, import the database manually using phpMyAdmin on your server. Then, in the database table `pr_options`, update the values for `home` and `siteurl` to your site’s full URL.

4.7. Enter the site administrator’s personal email, the site’s email address (make sure to create the corresponding mailbox on your server), the sender name (usually the site name), and set the administrator login and password for accessing the control panel. Click the "**Install**" button.

<figure><img src="../.gitbook/assets/Screenshot_10.png" alt="" width="563"><figcaption></figcaption></figure>

4.8. Select the language for the website and the control panel.

<figure><img src="../.gitbook/assets/image (591).png" alt="" width="563"><figcaption></figcaption></figure>

4.9. **Be sure to delete the installer files!** On the final step of the installation, click the link: "**Attention! Click here to delete the installer files**".\
\
**Script installation is complete.**

5. Website Control Panel\


<figure><img src="../.gitbook/assets/image (1883).png" alt="" width="350"><figcaption></figcaption></figure>

**Default control panel URL:** `https://your_domain/prmmxchngr/`

Use the username and password you specified during installation.

## Installing Additional Modules <a href="#chapter3" id="chapter3"></a>

{% hint style="info" %}
The script distribution package includes all available merchants and modules out of the box. Separate installation of merchants and modules is not required.
{% endhint %}

**1. Merchant Modules for Receiving Payments**

1.1. In your personal account, go to the "[**Your Scripts**](https://premiumexchanger.com/uscripts/)" section and download the merchant module for the required payment system from the "**Additional Modules**" block.

1.2. Upload the contents of the downloaded archive to the server directory `your_domain/wp-content/plugins/premiumbox/merchants`.

Then configure the module according to the instructions provided in the [User Guide](https://premium.gitbook.io/rukovodstvo-polzovatelya/navigaciya/merchanty-i-vyplaty).

**2. Auto-Payout Modules**

2.1. In your personal account, go to the "[**Your Scripts**](https://premiumexchanger.com/uscripts/)" section and download the auto-payout module for the required payment system from the "**Additional Modules**" block.

2.2. Upload the contents of the downloaded archive to the server directory `your_domain/wp-content/plugins/premiumbox/paymerchants`.

Then configure the module according to the instructions provided in the [User Guide](https://premium.gitbook.io/rukovodstvo-polzovatelya/navigaciya/merchanty-i-vyplaty/vyplaty).

[^1]: Cyrillic domains must be entered in the format `xn--90aiufb.xn--p1ai`.