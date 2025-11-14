# How to Transfer a Website

## How to Transfer/Copy a Website to a Subdomain

{% hint style="warning" %}
If you already have a live website on your main domain, you can transfer or copy it to a subdomain. However, if you plan to make changes to the subdomain, you may encounter difficulties transferring the database back to the main domain later.

This is because the main site will continue to operate, accumulating up-to-date data such as new user registrations and requests, while the subdomain may have different settings. In such cases, data synchronization will no longer be possible.
{% endhint %}

The Premium Exchanger script license includes the option to create a test version of your website on a subdomain, which can later be transferred to the main domain.

To do this, specify your subdomain on the [**Your Licenses**](https://premiumexchanger.com/ulicense/) page:

<figure><img src="../../.gitbook/assets/%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5%20(142)_eng.png" alt=""><figcaption></figcaption></figure>

You can create a subdomain using the ISP Manager server control panel by following [this guide](https://www.ihc.ru/articles/sozdanie-poddomenov-v-ispmanager.html).

Install the script on the subdomain by following [this guide](https://premium.gitbook.io/main/en/pered-nachalom-raboty/instrukciya-po-ustanovke).

{% hint style="warning" %}
Please note that license files are updated with the subdomain information after you specify the subdomain on the **Your Licenses** page. Once the subdomain is specified, it is <mark style="color:red;">**mandatory**</mark> to update the license files on the server and upload them to the root folder of the subdomain.
{% endhint %}

After setting up the website on the subdomain and testing its functionality, you will need to transfer it to the main domain. To do this, use ISP Manager to move all files to the main domain folder and update the site name in the copied database (in the `_options` table, specifically the `siteurl` and `home` fields).

<figure><img src="../../../ru/.gitbook/assets/image (706) (1).png" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
If you plan to transfer all requests and settings from the subdomain to the main domain with full replacement, there should be no issues.

However, if you want to transfer only the settings from the subdomain to the main domain (while the main domain already has a live site), synchronization between the two sites will not be possible. This is because two separate databases will be used, which cannot be linked.
{% endhint %}

## How to Transfer a Website to Another Server

### Preparation for Transfer

#### What You’ll Need:

* Access to the old server (hosting)
* Access to the new server (hosting)
* An FTP client or file manager
* A program for working with archives (e.g., WinRAR, 7-Zip)
* Access to the database (phpMyAdmin or equivalent)

### Step 1: Create a Backup of Your Files

#### Using the Hosting File Manager:

1. Log in to the control panel of your old hosting provider.
2. Open the file manager.
3. Navigate to the root folder of your website (usually `public_html` or `www`).
4. Select all WordPress files and folders.
5. Click "Archive" or "Create Archive."
6. Choose the archive format (ZIP is recommended).
7. Wait for the archive to be created.
8. Download the archive to your computer.

#### Using an FTP Client:

1. Connect to the server using an FTP client (e.g., FileZilla, WinSCP).
2. Download all files from the root folder of your website.
3. Create an archive of the files on your computer.

{% hint style="danger" %}
**Important:** Ensure that all files, including hidden ones (e.g., `.htaccess`), are downloaded.
{% endhint %}

### Step 2: Create a Backup of Your Database

1. Log in to your hosting control panel.
2. Find the "Databases" or "phpMyAdmin" section.
3. Open phpMyAdmin.
4. Select your website’s database from the list on the left.
5. Go to the "Export" tab.
6. Choose export options:
   * **Export Method:** Quick (or Custom for large databases)
   * **Format:** SQL
   * **Options:** Include CREATE DATABASE
7. Click "Go" or "Export."
8. Download the resulting SQL file to your computer.

### Step 3: Upload Files to the New Server

#### Preparing the New Hosting:

1. Ensure that the new hosting supports PHP and MySQL.
2. Create a new database (if it wasn’t created automatically).
3. Note down the database connection details:
   * Database name
   * Database user name
   * Database user password
   * Database host (usually `localhost`)

#### Uploading Files:

1. Log in to the file manager of the new hosting provider.
2. Navigate to the root folder of your website (`public_html` or `www`).
3. Remove any default hosting files (if present).
4. Upload the WordPress archive.
5. Extract the archive into the root folder.
6. Verify that all files have been extracted correctly.

### Step 4: Restore the Database

1. Open phpMyAdmin on the new hosting.
2. Select the newly created database.
3. Go to the "Import" tab.
4. Click "Choose File" and select the downloaded SQL file.
5. Ensure the correct format (SQL) is selected.
6. Click "Go" or "Import."
7. Wait for the import process to complete.

### Step 5: Configure Database Connection

1. Locate the `wp-config.php` file in the root folder of your website.
2. Open it for editing using the file manager or download it to your computer.
3. Update the following lines with the new database details:

```php
// Database name
define('DB_NAME', 'new_database_name');

// Database user
define('DB_USER', 'new_database_user');

// Database password
define('DB_PASSWORD', 'new_password');

// Database host
define('DB_HOST', 'localhost'); // or another host provided by your hosting provider
```

4. Save the changes.
5. If edited locally, upload the file back to the server.

### Step 6: Test Your Website

1. Open your website in a browser using the new address.
2. Check the main pages.
3. Log in to the WordPress admin panel (`/wp-admin/`).
4. Test all functionality.

#### Common Issues and Solutions:

**Database Connection Error:**

* Verify the database details in `wp-config.php`.
* Ensure the database was fully imported.

**Incorrect Links:**

* Update the site URL in WordPress settings.

**Image Issues:**

* Check file permissions for the `wp-content/uploads` folder.
* Ensure all files were uploaded.

### Alternative Options

#### Fresh Installation (if data is not critical):

1. Download the latest version of WordPress from the official website.
2. Install WordPress on the new hosting.
3. Reconfigure the site from scratch.
4. Export only the content from the old site if needed.

#### Hosting Provider Services:

Many hosting providers offer free or paid website migration services:

* Contact the support team of your new hosting provider.
* Provide access details for the old hosting.
* Wait for the migration to be completed by their specialists.

### Security Recommendations

* Change all passwords after the migration.
* Update WordPress and all plugins to the latest versions.
* Review security settings.
* Create new backups on the new hosting.

Once the migration is complete and all functionality is verified, you can safely delete files from the old hosting.
