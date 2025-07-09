# How to Upgrade PHP

Upgrading PHP from version 8.1 to 8.2 on Ubuntu (example)

By following these steps, you can upgrade to the latest PHP version.

### Step 1: [Check your current PHP version](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-proverit-versiyu-php-ustanovlennuyu-na-servere)

### Step 2: Add the PHP repository

To upgrade to PHP 8.2, you need to add the PHP repository to your system. Run the following commands in the terminal:

```bash
sudo apt install software-properties-common
sudo add-apt-repository ppa:ondrej/php
sudo apt update
```

### Step 3: Upgrade PHP

After adding the repository and updating your package list, install PHP 8.2 with:

```bash
sudo apt install php8.2
```

During installation, you may be prompted to confirm the upgrade and enter your password. Follow the on-screen instructions to proceed.

### Step 4: Verify the PHP upgrade

Run the following command to confirm that PHP 8.2 is installed:

```bash
php -v
```

### Step 5: Install PHP 8.2 extensions

If your projects require specific PHP extensions, you can install them using apt. For example:

```bash
sudo apt install php8.2-[extension_name]
```

Replace `[extension_name]` with the name of the extension you need.

### Step 6: Restart your web server

To apply the changes, restart your web server if you’re using PHP with Apache or Nginx:

```bash
sudo service apache2 restart   # For Apache
sudo service nginx restart     # For Nginx
```

**Note:** If your system still shows the old PHP version, you can select the active PHP version manually by running:

```bash
sudo update-alternatives --config php
```

Then verify again which PHP version your web server is using.

---

### Switching PHP version for the Premium Exchanger script

Download and upload the distribution files compatible with your installed script version and the new PHP version.

- **Installation files** — for fresh installations of the script  
- **Update files** — for upgrading an existing installation

![Screenshot](../../../.gitbook/assets/image%20(74).png)

Upload the archive to the server’s root directory and extract it, overwriting any existing files.

<figure><img src="../../../.gitbook/assets/image (75).png" alt="" width="491"><figcaption></figcaption></figure>

In ISP Manager, change the PHP version for your website to the new one and save the changes.

<figure><img src="../../../.gitbook/assets/image (76).png" alt="" width="467"><figcaption></figcaption></figure>