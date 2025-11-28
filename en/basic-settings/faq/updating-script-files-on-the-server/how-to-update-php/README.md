# How to Update PHP

Updating PHP from version 8.1 to 8.2 on Ubuntu (example)

By following these steps, you can upgrade to the latest PHP version.

***

### Step 1: [First, check your current PHP version](https://premium.gitbook.io/main/en/basic-settings/faq/kak-proverit-versiyu-php-ustanovlennuyu-na-servere)

***

### Step 2: Add the PHP Repository

To upgrade to PHP 8.2, you need to add the PHP repository to your system. Use the following commands in the terminal to add the repository:

```bash
sudo apt install software-properties-common
sudo add-apt-repository ppa:ondrej/php
sudo apt update
```

***

### Step 3: Upgrade PHP

Once the repository is added and the system is updated, you can install PHP 8.2 using the following command:

```bash
sudo apt install php8.2
```

During the installation, you may be prompted to confirm the update and enter your password. Follow the on-screen instructions to proceed.

***

### Step 4: Verify the PHP Update

After the installation is complete, run the following command to ensure PHP 8.2 is installed:

```bash
php -v
```

***

### Step 5: Install PHP 8.2 Extensions

If your projects require specific PHP extensions, you can install them using the `apt` package manager. For example:

```bash
sudo apt install php8.2
```

***

### Step 6: Restart the Web Server

If you’re using PHP with a web server like Apache or Nginx, you’ll need to restart the server for the changes to take effect:

```bash
sudo service apache2 restart # For Apache
sudo service nginx restart   # For Nginx
```

***

**Note:** If your system still shows an older PHP version, you can use the following command to select the new version from the available options:

```bash
sudo update-alternatives --config php
```

Afterward, recheck the PHP version your web server is using.

***

### Switching PHP Versions for the Premium Exchanger Script

Download and upload the appropriate distribution files for **the installed script version and the new PHP version.**

* **Installation files** — Use these if you’re installing the script from scratch.
* **Update files** — Use these if you’re updating an existing script.

1. Upload the archive to the root folder of your server and extract it, replacing the existing files.
2. In ISP Manager, change the PHP version for your website to the new version and save the changes.
