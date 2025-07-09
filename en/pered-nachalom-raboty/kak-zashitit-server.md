---
layout:
  width: default
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
---

# How to Secure Your Server

## General Recommendations

Many standard hosting services have limited options for fine-tuning security settings. Therefore, we recommend hosting your exchanger on a virtual private server (VPS/VDS) and configuring it properly to reduce the risk of hacking. Usually, hosting providers offer paid services for setting up virtual servers. You can also hire external specialists for configuration, but only those you trust.

* On your hosting provider’s control panel (billing system), where your site is hosted, enable SMS-based two-factor authentication for your account. Use any other available login restrictions offered by your hosting provider. For example, with Reg.ru, at a minimum, enable SMS authentication and email notifications for account logins;
* Update the **Ioncube Loader** module to the latest version;
* Install and configure the **fail2ban** module on your server;
* Install antivirus software and a port scanner on the server. Set up regular scans of server files and open ports;
* Configure the firewall. Block ports used for FTP, SSH, and various shell clients;
* Block the default URLs for the server’s login page. For example, with ISPmanager, these are: `https://ip_address/manager`, `https://ip_address/manager/ispmngr`, and `https://ip_address/ispmngr`;
* Change the default port for the server login page. ISPmanager typically uses port 1500—choose any other free port number;
* Block access to phpMyAdmin. Setting folder permissions to 444 on the phpMyAdmin directory is usually sufficient;
* Block access to webmail clients, such as `https://ip_address/webmail/`, `https://ip_address/roundcube/`, etc. Setting folder permissions to 444 on the mail client directory is usually enough;
* For all server users, including **root**, set passwords that are at least 15–25 characters long;
* Do not store backup copies of files or databases on the server, especially not in the website’s root directory.

## **Service and Option Configuration**

Here is a natural English translation of the provided text:

---

*   Disable the possibility of running [web shells](https://encyclopedia.kaspersky.ru/glossary/web-shell/) by editing the `php.ini` file (either modify the existing directive or add a new one):

    ```ini
    disable_functions = exec,system,passthru,shell_exec,proc_open,show_source
    ```

<details>

<summary>If you are using ISPmanager, follow these steps:</summary>

1. Log in to ISPmanager as the <mark style="color:red;">**root user**</mark>.

2. Go to the "**Sites**" section, select your website, and click the "**PHP Settings for the Site**" button.

<figure><img src="../../.gitbook/assets/image (2181).png" alt=""><figcaption></figcaption></figure>

3. Use the search to find the `disable_functions` directive, check its box, and click the pencil icon ("**Edit variable**").

<figure><img src="../../.gitbook/assets/image (2182).png" alt=""><figcaption></figcaption></figure>

4. Add the listed functions (do not remove the existing values — append the following functions): **`exec,system,passthru,shell_exec,proc_open,show_source`**, then save the changes.

    <figure><img src="../../.gitbook/assets/image (2183).png" alt="" width="544"><figcaption></figcaption></figure>

</details>

*   Disable file loading via **`allow_url_include` and `allow_url_fopen`** — this reduces the risk of remote code execution:

    ```ini
    allow_url_fopen = Off
    allow_url_include = Off
    ```

<details>

<summary>If you are using ISPmanager, follow these steps:</summary>

1. Log in to ISPmanager as the <mark style="color:red;">**root user**</mark>.

2. Go to the "**Sites**" section, select your website, and click the "**PHP Settings for the Site**" button.

<figure><img src="../../.gitbook/assets/image (2181).png" alt="" width="563"><figcaption></figcaption></figure>

3. Search for directives containing `allow_url`, check their boxes, and click the pencil icon ("**Edit variable**").

<figure><img src="../../.gitbook/assets/image (2185).png" alt="" width="563"><figcaption></figcaption></figure>

4. Set the values to `Off` and save the changes.

<figure><img src="../../.gitbook/assets/image (2184).png" alt="" width="563"><figcaption></figcaption></figure>

</details>

*   Disable certain extensions if they are not needed. For example:

    ```ini
    extension = phar.so ; ; // if phar is not used
    ```

<details>

<summary>If you are using ISPmanager, follow these steps:</summary>

1. Log in to ISPmanager as the <mark style="color:red;">**root user**</mark>.

2. Go to the "**PHP**" section, select the PHP version [used by your website](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-proverit-versiyu-php-ispolzuyushuyusya-dlya-saita), and click the "**Extensions**" button.

<figure><img src="../../.gitbook/assets/image (2186).png" alt="" width="563"><figcaption></figcaption></figure>

</details>

---

If you need the text adapted for a specific audience or style, please let me know!

Here is a natural, fluent English translation of the provided text:

---

3. Use the search function to find extensions containing the text **`phar`** (as an example), check the box next to them, and click the pencil icon ("**Disable Extension**").

<figure><img src="../../.gitbook/assets/image (2187).png" alt="" width="531"><figcaption></figcaption></figure>

4. Click the button and confirm disabling the extension in the pop-up window.

</details>

*   Restrict access to `php.ini` and `wp-config.php` using the `.htaccess` file:

    ```ini
    <FilesMatch "^(php\.ini|wp-config\.php)$">
        Order deny,allow
        Deny from all
    </FilesMatch>
    ```



<details>

<summary>If you are using ISPmanager, follow these steps:</summary>

1. Log in to ISPmanager as <mark style="color:yellow;">**any user**</mark>.

2. Go to the "**Sites**" section, select your site, and click the "**Site Files**" button.

<figure><img src="../../.gitbook/assets/image (2188).png" alt=""><figcaption></figcaption></figure>

3. Find the `.htaccess` file and open it for editing by double-clicking.

<figure><img src="../../.gitbook/assets/image (2190).png" alt="" width="479"><figcaption></figcaption></figure>

4. Paste the text shown above into the file and save your changes.

<figure><img src="../../.gitbook/assets/image (2191).png" alt="" width="543"><figcaption></figcaption></figure>

</details>

## Setting File Permissions

<figure><img src="../../.gitbook/assets/image (1).png" alt="" width="563"><figcaption></figcaption></figure>

If you see a warning about errors in the admin bar indicated by an animated <mark style="color:red;">red circle</mark>, open the errors section.

If the section shows an error about incorrect file permissions, change the permissions of the specified files to more secure settings (~~strikethrough value~~ — <mark style="color:red;">current permissions</mark>, after ➔ <mark style="color:green;">recommended permissions</mark>).

{% hint style="success" %}
[Official WordPress guide](https://developer.wordpress.org/advanced-administration/security/hardening/#file-permissions) on setting file permissions
{% endhint %}

{% hint style="info" %}
Warnings also appear in the "Dashboard" section, under the "Security Check" block.

<img src="../../.gitbook/assets/image (2).png" alt="" data-size="original">
{% endhint %}

\
If you are using ISPmanager, go to the "**Sites**" section, select your site, and click the "**Site Files**" button.

<figure><img src="../../.gitbook/assets/image (2188).png" alt=""><figcaption></figcaption></figure>

Select the file with incorrect permissions and click the "Attributes" button.

<figure><img src="../../.gitbook/assets/image (2193).png" alt=""><figcaption></figcaption></figure>

Enter the recommended permissions in the "Access Rights" field and save your changes.

<figure><img src="../../.gitbook/assets/image (2197).png" alt="" width="248"><figcaption></figcaption></figure>

After updating the permissions, the warning will disappear from the admin panel.

---

If you need the text adapted for a specific audience or style, feel free to ask!