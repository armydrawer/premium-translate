# Script Installation Guide

{% hint style="info" %}
The images provided in this guide may differ from those displayed on your specific system.

Throughout this guide, replace "**your\_domain**" with the direct address of your website. For example, if your website address is **premiumexchanger.com**, you should replace "**your\_domain**" with **premiumexchanger.com**.
{% endhint %}

{% hint style="danger" %}
Please note that **all** files must be uploaded under the <mark style="color:green;">user account created specifically for the website</mark> (not the <mark style="color:red;">root</mark> user). Uploading files as the <mark style="color:red;">root user</mark> may cause the website to function improperly.

If you have already uploaded files as the root user, you need to take the following steps:

1. Back up all files on the server.
2. [Download the update distribution](https://premiumexchanger.com/uscripts/) from our website that matches your script version (most commonly version 2.5) and your PHP version.

<img src="../.gitbook/assets/image (1509).png" alt="" data-size="original">

3. Upload the distribution to the root folder of your website and extract the archive, replacing the existing files.
{% endhint %}

## Recommended Security Settings and Server Requirements <a href="#chapter1" id="chapter1"></a>

We recommend applying the following server settings to reduce the risk of your server being compromised:

* Update the [Ioncube Loader](https://www.ioncube.com/loaders.php) module to the latest version.
* Install the [fail2ban](https://github.com/fail2ban/fail2ban) module on your server.
* Install antivirus software on your server.
* Block ports for FTP, SSH, and various shell clients.
* Restrict access to default server login URLs. For example, for ISP Manager:
  • `https://ip_address/manager/`  
  • `https://ip_address/manager/ispmngr/`  
  • `https://ip_address/ispmngr/`
* Change the default server login port. For ISP Manager, the default port is usually 1500. Set it to any available port.
* Block access to phpMyAdmin and its port.
* Block access to webmail clients. For example:  
  • `https://ip_address/webmail/`  
  • `https://ip_address/roundcube/`  
  • and similar URLs.
* Set a password of at least 15–25 characters for all server users, including the root user.

#### Server Requirements:

* PHP 8.1/8.2/8.3  
* MySQL 5.0 or higher  
* IonCube Loader 13.0 or higher  
* Task scheduler (cron)  
* Required additional PHP functions, extensions, and libraries: iconv, mb, curl, gd, openssl, soap, gmpobject, ziparchive.

## Installing the Main Product on the Server <a href="#chapter2" id="chapter2"></a>

### **1. Uploading Files**

{% hint style="danger" %}
Once again, please note that website files **must always** be uploaded under the <mark style="color:green;">user account created for the website</mark>, not the <mark style="color:red;">root user</mark>.
{% endhint %}

In your personal account, under the "[**Your Scripts**](https://premiumexchanger.com/uscripts/)" section, download the appropriate script build for the PHP version installed on your server. If you are unsure of your server's PHP version, contact your hosting provider's technical support for assistance.

<figure><img src="../.gitbook/assets/image (763).png" alt="" width="335"><figcaption><p>The script distribution already includes all available merchants and modules.<br>No separate installation of merchants or modules is required.</p></figcaption></figure>

Upload the downloaded archive or its contents to your server. Files should be uploaded to the root folder of your website (usually `public_html`, `www`, or `docs`). Use the file manager built into your control panel or an FTP client like Total Commander, CuteFTP, etc. Ensure the FTP client is set to binary file transfer mode (this is typically the default setting).

### **2. Generating a License**

In the "[**Your Licenses**](https://premiumexchanger.com/ulicense/)" section, download the `license.zip` archive. To do this, specify your domain name (and subdomain name, if applicable) where the script will be installed, then click "**Save**." Afterward, click "**Download for version X.X**." Upload the downloaded `license.zip` archive to the root folder of your website (usually `public_html`, `www`, or `docs`) and extract the archive.

<figure><img src="../.gitbook/assets/image (764).png" alt="" width="563"><figcaption></figcaption></figure>

{% hint style="warning" %}
<mark style="color:red;">If the domain name for the license is not specified and saved, you will not be able to download the license files.</mark> <mark style="color:red;">**Be careful**</mark> <mark style="color:red;">when entering the domain name to avoid errors. Licenses cannot be edited, replaced, or transferred to another domain. A new license will be required for a second domain.</mark>
{% endhint %}

License files are critical for the script to function properly, so please follow these rules:

* Do not rename the license files. Use them with the names they were downloaded with.
* License files must be located in the root folder of your website (usually `public_html`, `www`, or `docs`).
* File permissions for the license files should be set to 644.
* The contents of the license files must remain unchanged.

### **3. Creating a Database**

In your server's web control panel (e.g., ISP Manager), locate the "**Databases**" section and create a new database. Enter the database name, database user name, and generate a strong password:

<figure><img src="../.gitbook/assets/image (1080).png" alt=""><figcaption></figcaption></figure>

Save or write down these details, as you will need them later.

### **4. Installation**

In your browser's address bar, enter the following URL:

`https://your_domain/installer/`  

Follow the on-screen instructions:

#### 4.1. Select the installation language.

<figure><img src="../.gitbook/assets/image (586).png" alt="" width="563"><figcaption></figcaption></figure>

#### 4.2. Check your server's main system requirements.  
If any requirements are not met, you will see a warning. Click "**Skip**" if no errors are detected. If errors are found, resolve them and restart the installation process.

<figure><img src="../.gitbook/assets/image (587).png" alt="" width="563"><figcaption></figcaption></figure>

#### 4.3. Verify your server's PHP functions and libraries.  
If any requirements are not met, you will see a warning. Click "**Skip**" if no errors are detected. If errors are found, resolve them and restart the installation process.

<figure><img src="../.gitbook/assets/image (588).png" alt="" width="563"><figcaption></figcaption></figure>

#### 4.4. Check file and folder write permissions.  
If any permissions are incorrect, you will see a warning. Click "**Skip**" if no errors are detected. If errors are found, resolve them and restart the installation process.

<figure><img src="../.gitbook/assets/image (589).png" alt=""><figcaption></figcaption></figure>

#### 4.5. Enter the database name, database user name, and password you created in step 3. Click "**Update Config**."

<figure><img src="../.gitbook/assets/Screenshot_8 (2).png" alt="" width="563"><figcaption></figcaption></figure>

#### 4.6. Click "**Choose File**" and select the `damp_db.sql` file. This file is located in the root of the downloaded archive on your computer. Enter the [full website address](#user-content-fn-1)[^1] and click "**Import**."

<figure><img src="../.gitbook/assets/image (590).png" alt="" width="563"><figcaption></figcaption></figure>

If the system cannot import the database file and displays an error, manually import the database file using phpMyAdmin on your server. Then, in the database, update the `home` and `siteurl` values in the `pr_options` table with your website's full name.

#### 4.7. Enter the admin email, website email (create a corresponding email account on the server), sender name (usually the website name), and set the admin login and password for the control panel. Click "**Install**."

<figure><img src="../.gitbook/assets/Screenshot_10.png" alt="" width="563"><figcaption></figcaption></figure>

#### 4.8. Select the language for the website and control panel.

<figure><img src="../.gitbook/assets/image (591).png" alt="" width="563"><figcaption></figcaption></figure>

#### 4.9. **Delete the installer files!**  
At the final step of the installation, click the link: "**Attention! Click here to delete the installer files**."

**The script installation is complete.**

### **5. Website Control Panel**

<figure><img src="../.gitbook/assets/image (1883).png" alt="" width="350"><figcaption></figcaption></figure>

**Default control panel URL:** `https://your_domain/prmmxchngr/`

Log in using the credentials you set during installation.

### Setting Up Two-Factor Authentication (2FA)

{% hint style="success" %}
To enable two-factor authentication (2FA) for logging into the admin panel, [configure the delivery of authentication codes through your preferred communication channel](https://premium.gitbook.io/main/osnovnye-nastroiki/nastroiki/administratory-i-polzovateli/dvukhfaktornaya-avtorizaciya-2fa-v-paneli-upravleniya-saitom) (via email, Telegram, SMS, or [a 2FA app](https://premium.gitbook.io/main/osnovnye-nastroiki/nastroiki/administratory-i-polzovateli/dvukhfaktornaya-avtorizaciya-2fa-v-paneli-upravleniya-saitom#id-2fa-s-ispolzovaniem-prilozheniya)).
{% endhint %}

---

## Installing Additional Modules <a href="#chapter3" id="chapter3"></a>

{% hint style="info" %}
The script distribution comes "out of the box" with all available merchants and modules pre-installed. There is no need to install merchants or modules separately.
{% endhint %}

### 1. Merchant Modules for Receiving Payments

1.1. In your account, navigate to the "[**Your Scripts**](https://premiumexchanger.com/uscripts/)" section. Under the "**Additional Modules**" block, download the merchant module for receiving payments for the required payment system.

1.2. Upload the contents of the downloaded archive to your server in the directory:  
`your_domain/wp-content/plugins/premiumbox/merchants`.

Next, configure the module according to the instructions provided in the [User Guide](https://premium.gitbook.io/rukovodstvo-polzovatelya/navigaciya/merchanty-i-vyplaty).

---

### 2. Auto-Payout Modules

2.1. In your account, navigate to the "[**Your Scripts**](https://premiumexchanger.com/uscripts/)" section. Under the "**Additional Modules**" block, download the auto-payout module for the required payment system.

2.2. Upload the contents of the downloaded archive to your server in the directory:  
`your_domain/wp-content/plugins/premiumbox/paymerchants`.

Next, configure the module according to the instructions provided in the [User Guide](https://premium.gitbook.io/rukovodstvo-polzovatelya/navigaciya/merchanty-i-vyplaty/vyplaty).

---

[^1]: Cyrillic domain names should be specified in the format `xn--90aiufb.xn--p1ai`.