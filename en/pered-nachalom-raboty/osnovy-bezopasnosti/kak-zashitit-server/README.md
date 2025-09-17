# How to Secure a Server

## General Recommendations

Shared hosting often has limited options for fine-tuning security settings. Therefore, we recommend hosting your exchange platform on a Virtual Private Server (VPS/VDS) and configuring it properly to minimize the risk of hacking. Most hosting providers offer paid services for setting up virtual servers. You can also hire external specialists for this task, but only if you trust them.

* Enable SMS authentication for your hosting account (the billing panel used to manage your hosting services). If your hosting provider offers additional login restrictions, enable those as well. For example, if you use Reg.ru, at a minimum, enable SMS authentication and email notifications for account logins.
* Update the **Ioncube Loader** module to the latest version.
* Install and configure the **fail2ban** module on your server.
* Install antivirus software and a port scanner on your server. Set up regular scans of server files and ports.
* Configure a firewall. Block ports used for FTP, SSH, and various shell clients.
* Restrict access to default server login URLs. For example, for ISPmanager, block the following URLs:  
  `https://ip_address/manager`, `https://ip_address/manager/ispmngr`, `https://ip_address/ispmngr`.
* Change the default port for server login. For ISPmanager, the default port is usually 1500. Replace it with any available port number.
* Block access to the phpMyAdmin login page. You can do this by setting the folder permissions for phpMyAdmin to 444.
* Block access to webmail clients, such as `https://ip_address/webmail/` or `https://ip_address/roundcube/`. Similarly, set the folder permissions for the mail client to 444.
* Set passwords of at least 15–25 characters for all server users, including the **root** user.
* Do not store backup files or databases on the server, especially in the root directory of your website.

---

## **Configuring Services and Options**

* Disable the ability to execute [web shells](https://encyclopedia.kaspersky.com/glossary/web-shell/) by editing the `php.ini` file. Add or modify the following directive:

    ```ini
    disable_functions = exec,system,passthru,shell_exec,proc_open,show_source
    ```

<details>
<summary>If you use ISPmanager, follow these steps:</summary>

1. Log in to ISPmanager as the <mark style="color:red;">**root user**</mark>.
2. Navigate to the "**Sites**" section, select your website, and click "**PHP Settings for the Site**."
3. Search for the `disable_functions` directive, check the box next to it, and click the pencil icon ("**Edit Variable**").
4. Add the specified functions (do not remove existing values; simply append the new ones):  
   **`exec,system,passthru,shell_exec,proc_open,show_source`**, and save the changes.

</details>

* Disable file uploads via **`allow_url_include` and `allow_url_fopen`** to reduce the risk of remote code execution:

    ```ini
    allow_url_fopen = Off
    allow_url_include = Off
    ```

<details>
<summary>If you use ISPmanager, follow these steps:</summary>

1. Log in to ISPmanager as the <mark style="color:red;">**root user**</mark>.
2. Navigate to the "**Sites**" section, select your website, and click "**PHP Settings for the Site**."
3. Search for directives containing `allow_url`, check their boxes, and click the pencil icon ("**Edit Variable**").
4. Set the value to `Off` for these variables and save the changes.

</details>

* Disable unnecessary extensions. For example:

    ```ini
    extension = phar.so ; // if phar is not used
    ```

<details>
<summary>If you use ISPmanager, follow these steps:</summary>

1. Log in to ISPmanager as the <mark style="color:red;">**root user**</mark>.
2. Navigate to the "**PHP**" section, select the PHP version [used by your website](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-proverit-versiyu-php-ispolzuyushuyusya-dlya-saita), and click "**Extensions**."
3. Search for the extension (e.g., **`phar`**), check its box, and click the pencil icon ("**Disable Extension**").
4. Confirm the action in the pop-up window.

</details>

* Restrict access to `php.ini` and `wp-config.php` files using `.htaccess`:

    ```ini
    <FilesMatch "^(php\.ini|wp-config\.php)$">
        Order deny,allow
        Deny from all
    </FilesMatch>
    ```

<details>
<summary>If you use ISPmanager, follow these steps:</summary>

1. Log in to ISPmanager as <mark style="color:yellow;">**any user**</mark>.
2. Navigate to the "**Sites**" section, select your website, and click "**Site Files**."
3. Locate the `.htaccess` file and double-click it to edit.
4. Add the above code to the file and save the changes.

</details>

---

## File Permissions Configuration

If you see a warning in the admin panel (e.g., a red animated circle) about incorrect file permissions, navigate to the error section.

If the error indicates incorrect file permissions, update the permissions to more secure values (the ~~strikethrough~~ value represents the **current permissions**, while the ➔ <mark style="color:green;">green value</mark> represents the **recommended permissions**).

{% hint style="success" %}
Refer to the [official WordPress guide](https://developer.wordpress.org/advanced-administration/security/hardening/#file-permissions) for configuring file permissions.
{% endhint %}

{% hint style="info" %}
Warnings can also be found in the "Console" section under the "Security Check" block.
{% endhint %}

If you use ISPmanager, follow these steps:

1. Navigate to the "**Sites**" section, select your website, and click "**Site Files**."
2. Select the file with incorrect permissions and click the "**Attributes**" button.
3. Enter the recommended permissions in the "Access Rights" field and save the changes.

Once the permissions are updated, the warning will disappear from the admin panel.