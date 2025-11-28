# How to Secure Your Server

## General Recommendations

Often, standard hosting services have limited options for fine-tuning security, so we recommend hosting your exchange service on a Virtual Private Server (VPS/VDS) and configuring it to reduce the risk of hacking. Typically, hosting providers offer paid services for setting up virtual servers. You can hire external specialists for configuration, but only those you trust.

* On the hosting service (billing for managing the service) where your site is hosted, enable SMS authorization for your account. Set up other access restrictions if your hosting provider offers them. For Reg.ru hosting, at a minimum, enable SMS authorization and email notifications for account logins.
* Update the **Ioncube Loader** module to the latest version.
* Install and configure the **fail2ban** module on the server.
* Install antivirus software and a port scanner on the server. Set up regular scans of server files and ports.
* Configure the firewall. Block ports for FTP, SSH, and various shell clients.
* Block standard URLs for server login forms. For example, for Ispmanager, these are: `https://ip_address/manager`, `https://ip_address/manager/ispmngr`, `https://ip_address/ispmngr`.
* Change the default port for the server login form. For Ispmanager, the default port is usually 1500. Set it to any available port number.
* Block access to phpMyAdmin. You can do this by setting the permissions of the phpMyAdmin folder to 444 on the server.
* Block access to webmail clients. For example, `https://ip_address/webmail/`, `https://ip_address/roundcube/`, etc. Again, set the permissions of the mail client folder to 444 on the server.
* For all server users, including **root**, set a password that is at least 15-25 characters long.
* Do not store backups of files and databases on the server, especially in the root directory of the site.

## **Configuring Services and Options**

*   Disable the use of [web shells](https://encyclopedia.kaspersky.ru/glossary/web-shell/) through the php.ini file (edit the existing directive or add a new one):

    ```ini
    disable_functions = exec,system,passthru,shell_exec,proc_open,show_source
    ```

<details>

<summary>If you are using Ispmanager, follow these steps:</summary>

1. Log in to Ispmanager as a <mark style="color:red;">**root user**</mark>.
2. Go to the "**Websites**" section, select your website, and click the "PHP Settings for the Site" button.

<figure><img src="../../../.gitbook/assets/image (2181) (1).png" alt=""><figcaption></figcaption></figure>

3. Search for the `disable_functions` directive, check it, and click the pencil button ("**Edit Variable**").

<figure><img src="../../../.gitbook/assets/image (2182) (1).png" alt=""><figcaption></figcaption></figure>

4.  Add the specified functions (do not remove the previous values — just append the specified functions): **`exec,system,passthru,shell_exec,proc_open,show_source`** and save the changes.

    <figure><img src="../../../.gitbook/assets/image (2183) (1).png" alt="" width="544"><figcaption></figcaption></figure>

</details>

*   Disable file uploads through **`allow_url_include` and `allow_url_fopen`** — this will reduce the risk of remote code execution:

    ```ini
    allow_url_fopen = Off
    allow_url_include = Off
    ```

<details>

<summary>If you are using Ispmanager, follow these steps:</summary>

1. Log in to Ispmanager as a <mark style="color:red;">**root user**</mark>.
2. Go to the "**Websites**" section, select your website, and click the "**PHP Settings for the Site**" button.

<figure><img src="../../../.gitbook/assets/image (2181) (1).png" alt="" width="563"><figcaption></figcaption></figure>

3. Search for the directives containing `allow_url`, check them, and click the pencil button ("**Edit Variable**").

<figure><img src="../../../.gitbook/assets/image (2185) (1).png" alt="" width="563"><figcaption></figcaption></figure>

4. Set `Off` for the variables and save the changes.

<figure><img src="../../../.gitbook/assets/image (2184) (1).png" alt="" width="563"><figcaption></figcaption></figure>

</details>

*   Disable certain extensions (if they are not needed). For example:

    ```ini
    extension = phar.so ; // if phar is not used
    ```

<details>

<summary>If you are using Ispmanager, follow these steps:</summary>

1. Log in to Ispmanager as a <mark style="color:red;">**root user**</mark>.
2. Go to the "**PHP**" section, select the PHP version [that your website is using](https://premium.gitbook.io/main/en/basic-settings/faq/kak-proverit-versiyu-php-ispolzuyushuyusya-dlya-saita) and click the "Extensions" button.

<figure><img src="../../../.gitbook/assets/image (2186) (1).png" alt="" width="563"><figcaption></figcaption></figure>

3. Search for the extension **`phar`** (for example), check it, and click the pencil button ("**Disable Extension**").

<figure><img src="../../../.gitbook/assets/image (2187) (1).png" alt="" width="531"><figcaption></figcaption></figure>

4. Click the button and confirm the disabling of the extension in the pop-up window.

</details>

*   Restrict access to `php.ini` and `wp-config.php` through the `.htaccess` file:

    ```ini
    <FilesMatch "^(php\.ini|wp-config\.php)$">
        Order deny,allow
        Deny from all
    </FilesMatch>
    ```

<details>

<summary>If you are using Ispmanager, follow these steps:</summary>

1. Log in to Ispmanager as <mark style="color:yellow;">**any user**</mark>.
2. Go to the "**Websites**" section, select your website, and click the "**Website Files**" button.

<figure><img src="../../../.gitbook/assets/image (2188) (1).png" alt=""><figcaption></figcaption></figure>

3. Find the `.htaccess` file and enter edit mode by double-clicking it.

<figure><img src="../../../.gitbook/assets/image (2189) (1).png" alt="" width="479"><figcaption></figcaption></figure>

4. Add the text specified above to the file and save the changes.

<figure><img src="../../../.gitbook/assets/image (2191) (1).png" alt="" width="543"><figcaption></figcaption></figure>

</details>

## File Permissions Configuration

<figure><img src="../../../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

If a warning about file permission errors appears in the admin panel as an animated <mark style="color:red;">red circle</mark>, open the section with errors.

If the section displays an error about incorrect file permissions, change the permissions of the specified files to more secure settings (~~struck-through value~~ — <mark style="color:red;">current permissions</mark>, after ➔ <mark style="color:green;">recommended permissions</mark>).

{% hint style="success" %}
[Official instructions](https://developer.wordpress.org/advanced-administration/security/hardening/#file-permissions) from WordPress on configuring file permissions.
{% endhint %}

{% hint style="info" %}
Warnings are also displayed in the "Console" section, under the "Security Check" block.

<img src="../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1)_eng.png" alt="" data-size="original">
{% endhint %}

\
When using Ispmanager, go to the "**Websites**" section, select your website, and click the "**Website Files**" button.

<figure><img src="../../../.gitbook/assets/image (2188) (1).png" alt=""><figcaption></figcaption></figure>

Select the file with incorrect permissions and click the "Attributes" button.

<figure><img src="../../../.gitbook/assets/image (2193) (1).png" alt=""><figcaption></figcaption></figure>

Set the recommended permissions in the "Access Rights" field and save the changes.

<figure><img src="../../../.gitbook/assets/image (2197) (1).png" alt="" width="248"><figcaption></figcaption></figure>

After changing the permissions, the warning will disappear from the admin panel.
