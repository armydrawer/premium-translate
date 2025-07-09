# Diagnosing and Resolving Errors When Working with Scripts

General Recommendations

To optimize the performance of your server and database, it’s important to consider several key factors that can affect request processing speed and overall site efficiency. Here are some steps you can take:

**1. Increase Server Capacity:**

* **Add more RAM:** Increasing the server’s RAM is recommended to speed up data processing.
* **Add more CPU cores:** Additional processor cores can accelerate computations and database operations.

**2. Check Server Settings:**

* **Eliminate unnecessary tasks:** Make sure there are no redundant tasks or processes running on the server that could slow it down.
* **Optimize configuration:** Review your server and database settings to ensure they are optimized for efficient performance.

**3. Monitor Performance:**

* **Use monitoring tools:** Employ specialized monitoring tools to track system performance and identify bottlenecks or issues.

**4. Experiment with Configuration:**

* **Run test changes:** Try adjusting resources like memory and CPU cores to see how these changes impact processing speed and overall performance.

**5. Backup Data:**

* **Create regular backups:** Regularly backing up your data helps protect important information and prevents data loss.

Following these steps can help optimize your server and database performance, improve system responsiveness, and reduce request processing times. If needed, consult with experienced system administrators for more precise tuning.

## Known Issues and How to Fix Them

Below are some common errors you might encounter when working with the script, along with solutions to fix them.

<details>

<summary>Infinite redirect / redirect error</summary>

If you experience an infinite redirect loop, go to your server control panel settings (ISP Manager or another panel) and check the box for "**Redirect HTTP requests to HTTPS**" (example shown for ISP Manager).

![](<../../.gitbook/assets/image (313).png>)

</details>

<details>

<summary>Request takes too long to create or doesn’t create at all</summary>

Disable the SMTP server in the "**Messages -> E-mail templates**" section if you are using outgoing mail, then test how quickly the request is created.

If the request is created faster after disabling SMTP, you should switch to one of the [SMTP servers we recommend](https://premium.gitbook.io/main/osnovnye-nastroiki/uvedomleniya-administratoram-i-polzovatelyam/uvedomleniya-po-e-mail#nastroika-smtp).

![](<../../.gitbook/assets/image (1515).png>)

</details>

<details>

<summary>The exchange directions table freezes when selecting currencies</summary>

Adjust the caching settings in your Cloudflare dashboard — select the "**No query string**" option under "**Caching**" -> "**Configuration**".

<img src="../../.gitbook/assets/image (767).png" alt="" data-size="original">

</details>

<details>

<summary>Exported XML file is generated incorrectly</summary>

If you see a file validation error instead of the exported XML file, this usually means that one or more script files contain empty lines at the very beginning.

![](<../../.gitbook/assets/image (1565).png>)

Here’s how the XML file will look when opened locally after downloading it from the browser (right-click -> "Save as" -> XML file):

![](<../../.gitbook/assets/image (1564).png>)

To fix this error, you need to find files with empty first lines. To do this:

1. Locate the website’s root folder (often under root it’s `var/www/www-root/data/www/domain_name`), then navigate there:

```
cd var/www/www-root/data/www/domain_name
```

2. If you’re logged in as the site user, the path is usually shorter:

```
cd www/domain_name
```

3. Run the following command to search for files with empty first lines across all PHP files:

```
find . -name "*.php" -type f -exec sh -c 'if [ "$(head -n 1 "$1" | tr -d "\n")" = "" ]; then echo "$1: empty first line"; fi' _ {} \;
```

The output will list all files whose first line is empty.

![](<../../.gitbook/assets/image (1567).png>)

4. Manually locate each listed file on the server, open it, and remove the empty lines at the beginning.

</details>

Here is a natural, fluent English translation of the provided text:

---

Also, the issue when generating the file may be due to the fact that the first line of the file is missing the XML encoding and version information (the prolog). In this case, you should re-upload the [update script files](https://premiumexchanger.com/uscripts/) over the existing files on the server — make sure to do this as the <mark style="color:green;">user created specifically for the website</mark>, not as <mark style="color:red;">root</mark>!

![](<../../.gitbook/assets/image (1622).png>)

</details>

<details>

<summary>Unstable Website Operation over HTTPS</summary>

Check how the domain is specified under "**Settings**" -> "**General**" in the admin panel. It should be set as **https://your_domain**

![](<../../.gitbook/assets/image (1367).png>)

Also, verify how the domain is set in the database (table `xxxx_options`); it should also be **https://your_domain**

![](<../../.gitbook/assets/image (1369).png>)

You can open the database via the ISP Manager control panel, under the "Databases" section.

![](<../../.gitbook/assets/image (1523).png>)

![](<../../.gitbook/assets/image (1525).png>)

If the "**Web Interface**" button is missing, install phpMyAdmin.

To install phpMyAdmin for database management in ISP Manager, go to "**Settings**" -> "**Software Configuration**", check the box for "**MySQL Administration Web Interface**", then click the "**Install**" button above the list (perform these actions as <mark style="color:red;">root</mark>).

In your Cloudflare dashboard, set the encryption mode to **Flexible** under "**SSL/TLS**" -> "**Overview**".

![](<../../.gitbook/assets/image (1370).png>)

<mark style="background-color:red;">If you are using a self-signed certificate issued outside of Cloudflare, select the option "</mark><mark style="background-color:red;">**Full (Encrypts end-to-end, using a self signed certificate on the server)**</mark><mark style="background-color:red;">"</mark>

Disable the permanent HTTPS redirect in the site settings within ISP Manager.

![](<../../.gitbook/assets/image (1524).png>)

![](<../../.gitbook/assets/image (1368).png>)

</details>

<details>

<summary>Theme Fails to Activate on the Website</summary>

If you see the following error when activating the theme:

![](<../../.gitbook/assets/image (1827).png>)

Enable the `short_open_tag` option in the PHP configuration file (`php.ini`).

To do this, log into ISP Manager as <mark style="color:red;">**root**</mark> and go to the PHP settings (or open the `php.ini` file directly on the server if you’re not using ISP Manager):

![](<../../.gitbook/assets/image (1829).png>)

In the search box at the top right, type `short` and enable the displayed option.

![](<../../.gitbook/assets/image (1828).png>)

---

If you need any further assistance or clarification, feel free to ask!

Here is a natural English translation of the provided text:

---

After that, activate the theme that was showing the error.

</details>

<details>

<summary>Website doesn’t load on some devices/providers</summary>

Disable proxying in your Cloudflare dashboard. Go to the "**DNS**" ➔ "**Records**" section and start editing the A record.

<mark style="color:red;">**Please note that disabling proxying will expose your server’s real IP address to attackers and will disable DDoS protection. Only disable proxying as a last resort.**</mark>

<figure><img src="../../.gitbook/assets/image (42).png" alt=""><figcaption></figcaption></figure>

Turn off proxying in the "**Proxy status**" column.

<figure><img src="../../.gitbook/assets/image (43).png" alt=""><figcaption></figcaption></figure>

Save your changes.

<figure><img src="../../.gitbook/assets/image (44).png" alt=""><figcaption></figcaption></figure>

After these steps, your website should load on all devices and providers.

</details>

<details>

<summary>Website doesn’t load from Russia (disabling ECH)</summary>

Roskomnadzor has started blocking Cloudflare.

Cloudflare has forced all its users to enable Server Name Indication (SNI) encryption. This means that when this option is enabled, it’s impossible to see which website is being accessed over HTTPS. Roskomnadzor responded by blocking sites that use this technology.

As a result, many websites using Cloudflare have become inaccessible to many users in Russia.

If you need to disable Encrypted Client Hello (ECH) for your domain on Cloudflare, follow these steps. This process involves checking the current ECH status and then disabling it via Cloudflare.

<mark style="color:red;">**Please note that disabling ECH does not guarantee access to your site, but it helps in most cases.**</mark>

**Checking if ECH is enabled**

First, check whether ECH is enabled for your domain. To do this, visit the following link, replacing **example.com** with your domain:

[https://dns.google.com/query?name=**example.com**\&type=HTTPS](https://dns.google.com/query?name=example.com\&type=HTTPS)

![](<../../.gitbook/assets/image (2107).png>)

If the response contains the parameter **`ech=`**, this confirms that ECH is supported. If ECH is enabled, proceed to the next step.

\---------------------------------------------------------------------------------------------------------

---

Let me know if you need the rest translated or any adjustments!

## If you have a **free Cloudflare plan**:

**ECH can only be disabled on the free plan via the Cloudflare API.**

You will need:

* Your Cloudflare account **email address**
* Your **Global API Key** — used to authenticate API requests
* Your **Zone ID** — the unique identifier for your domain (zone) in Cloudflare

---

### 1. Get your Global API Key

Go to your Cloudflare profile page here and copy your Global API Key:  
[https://dash.cloudflare.com/profile/api-tokens](https://dash.cloudflare.com/profile/api-tokens)

---

### 2. Find your Zone ID

Go to your domain’s management page in Cloudflare, scroll down, and locate the **Zone ID**. Copy it.

---

### Disabling ECH using curl (Method 1):

Once you have your Global API Key and Zone ID, you can disable ECH using `curl`.

#### Install curl

Curl is a command-line tool for sending HTTP requests, which you’ll need to interact with the Cloudflare API.

- **On Windows:**

  Download and install curl from the [official website](https://curl.se/).

  *To check if curl is installed:*

  - For CMD:
    1. Press Win + R.
    2. Type `cmd` and press Enter.
    3. Run:

       ```bash
       curl --version
       ```

  - For PowerShell:
    1. Press Win + R.
    2. Type `powershell` and press Enter.
    3. Run:

       ```bash
       curl.exe --version
       ```

- **On Linux/macOS:**

  Curl is usually pre-installed. Verify by running:

  ```bash
  curl --version
  ```

---

### Run the following command to disable ECH:

Replace the placeholders with your actual values:

- `{ZONE_ID}` — your Zone ID from the Cloudflare dashboard
- `{ACCOUNT_EMAIL}` — your Cloudflare account email
- `{GLOBAL_API_KEY}` — your Global API Key

**Windows CMD:**

```bash
curl -X PATCH "https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/settings/ech" ^
     -H "X-Auth-Email: {ACCOUNT_EMAIL}" ^
     -H "X-Auth-Key: {GLOBAL_API_KEY}" ^
     -H "Content-Type: application/json" ^
     --data "{\"id\":\"ech\",\"value\":\"off\"}"
```

**Windows PowerShell:**

```powershell
curl -Method PATCH "https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/settings/ech" `
    -Headers @{
        "X-Auth-Email" = "{ACCOUNT_EMAIL}";
        "X-Auth-Key" = "{GLOBAL_API_KEY}";
        "Content-Type" = "application/json"
    } `
    -Body '{"id":"ech","value":"off"}'
```

**Linux/macOS:**

```bash
curl -X PATCH "https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/settings/ech" \
     -H "X-Auth-Email: {ACCOUNT_EMAIL}" \
     -H "X-Auth-Key: {GLOBAL_API_KEY}" \
     -H "Content-Type: application/json" \
     --data '{"id":"ech","value":"off"}'
```

---

This will disable ECH for your domain on Cloudflare’s free plan.

Here is a natural English translation of the provided text:

---

```bash
curl -X PATCH "https://api.cloudflare.com/client/v4/zones/{ZONE_ID}/settings/ech" \
     -H "X-Auth-Email: {ACCOUNT_EMAIL}" \
     -H "X-Auth-Key: {GLOBAL_API_KEY}" \
     -H "Content-Type: application/json" \
     --data '{"id":"ech","value":"off"}'
```

If the request is successful, Cloudflare will return a response confirming that ECH has been disabled:

```bash
{"result":{"id":"ech","value":"off","modified_on":null,"editable":true},"success":true,"errors":[],"messages":[]}
```

### **Disabling ECH Using Postman (Option 2):**

You can perform the same procedure using Postman. Postman is an API testing tool that allows you to send requests to a server, receive responses, and analyze them. It supports HTTPS and lets you create requests with headers, parameters, and body content. This makes it ideal for testing APIs that use encrypted connections to ensure secure data transmission.

To disable ECH in Postman, create a new request and select the PATCH method. Replace `zone_id` with your actual Zone ID in the URL:

```
https://api.cloudflare.com/client/v4/zones/zone_id/settings/ech
```

In the **Headers** tab, add the following keys:

* `X-Auth-Email` — the email address associated with your Cloudflare account;
* `X-Auth-Key` — your Global API Key;
* `Content-Type` — set the value to `application/json`.

![Headers example](<../../.gitbook/assets/image (112).png>)

In the **Body** tab, select **raw** and enter the following JSON:

![Body example](<../../.gitbook/assets/image (113).png>)

```json
{"id": "ech", "value": "off"}
```

Then click the **Send** button.

![Send button](<../../.gitbook/assets/image (114).png>)

## If you have a <mark style="color:green;">paid Cloudflare plan</mark>:

1. Log in to your Cloudflare account.
2. Select your website.
3. Go to the **SSL/TLS** section.
4. Open the **Edge Certificates** tab.
5. Find the **Encrypted Client Hello (ECH)** setting.
6. Simply toggle this option to **Off**.

![ECH toggle](<../../.gitbook/assets/image (111).png>)

---

<details>

<summary>CAPTCHA image is not displaying on website pages</summary>

Set write permissions (for example, 777) on the folder `/wp-content/pn_uploads/captcha/` or `/wp-content/uploads/captcha/`.

![Folder permissions example](https://2722984412-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fm9kqZXsNykrN6VyxxXBO%2Fuploads%2FyUtYC77gja8gTCQ5Qa1y%2Fimage.png?alt=media&token=e0f8b816-5622-42f8-ac21-ebf06d9654ee)

If you don’t know how to do this, please contact your hosting provider’s support team for assistance.

</details>

---

If you need any further help, feel free to ask!

<summary>The right column with currencies ("Receiving") does not appear on the exchanger’s main page after enabling the "Direction Sorting" module</summary>

Perform "**Step 3**" in the "**Exchanger Settings**" -> "**Migration**" section under the "**Special Migration Steps**" block — the currencies in the main table should then display correctly.

![](<../../.gitbook/assets/image (1888).png>)

![](<../../.gitbook/assets/image (1889).png>)

</details>

<details>

<summary>Images do not display in Firefox browser (Partners section)</summary>

![](<../../.gitbook/assets/image (382).png>)![](<../../.gitbook/assets/image (384).png>)

Cause: incorrect export of the original SVG images.

Solution:

1. Upload and extract the archive with images into the `/wp-content/uploads/partners/` folder on the server.
2. In the site admin panel, under the "**Partners**" section, update the image paths accordingly (example: `/wp-content/uploads/partners/bestchange.svg`).\
   ![](<../../.gitbook/assets/image (387).png>)
3. Uploading files to a separate folder instead of overwriting existing ones resolves caching issues with Cloudflare and browsers.

</details>

<details>

<summary>Emails for application status updates and confirmation codes are not being sent</summary>

It’s possible that your domain has been flagged as a spam sender, causing emails to be filtered — please check with your hosting provider’s support team.

Contact your hosting provider to confirm whether they are blocking outgoing emails. There may be server restrictions (for example, [smart relay](https://korporativnaya-pochta.com/articles/smart-relay-zaschita-ot-spama-dlya-korporativnoy-pochty)) that interfere with email delivery.

If the email content appears suspicious to mail services, try modifying or supplementing it to improve deliverability.

Change the subject line of the email sent for the "**New Application**" status to something less formal. Sometimes SMTP server filters block delivery based on the subject.

If emails are only received by some users or end up in the spam folder, check whether your domain has properly configured [SPF and/or DKIM records](https://neuropassenger.ru/dostavlyaemost-pisem/) and set them up if needed.

</details>

Here is a natural English translation of the provided text:

---

* [Check SPF record](https://mxtoolbox.com/spf.aspx)  
* [Check DKIM record](https://mxtoolbox.com/dkim.aspx)

</details>

<details>

<summary>QR code generation in requests is not working</summary>

In version 2.5.2 of the "**QR Code Generator**" module, the service used to generate codes was replaced for improved stability — please update the module to the latest version by following the [instructions](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-skripta).

[Direct download link for the module](https://2574066779-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fm9kqZXsNykrN6VyxxXBO%2Fuploads%2FfYDoTZNwTpp1UzsalKcy%2Fqr_adress.zip?alt=media\&token=f0d2c22e-8619-45d3-9bb4-e141746ec080).

No changes to the shortcode in request status templates are required.

</details>

<details>

<summary>BestChange parser or Parsers 2.0 not working (currency rates not updating)</summary>

<img src="../../.gitbook/assets/image (1260).png" alt="" data-size="original">

Most likely, the files on the server were uploaded as root, but they should be uploaded under the site’s user account — you need to change the ownership of the files and directories. Steps to follow:

* Download the root folder with all files as an archive to your PC  
* Delete these files on the server while logged in as root  
* Log in to ISP Manager as the user created for the site  
* Upload the archive to the server and unpack it to the same path

</details>

<details>

<summary>Data parsing from BestChange export XML file not working</summary>

In the CloudFlare control panel, enable [Bot Fight Mode](https://developers.cloudflare.com/bots/get-started/free/).  
![](<../../.gitbook/assets/image (2090).png>)

Fight Mode has a separate exceptions list — be sure to add the IP address **`162.19.29.225`** to it, regardless of how your other rules are configured.

![](<../../.gitbook/assets/image (2091).png>)

</details>

<details>

<summary>Editing exchange directions is not working</summary>

![](<../../.gitbook/assets/image (1983).png>)

Replace the file on your server at `wp-content/plugins/premiumbox/premium/includes/class-form.php` (the file can be found [at the bottom of this page](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/diagnostika-i-reshenie-oshibok-pri-rabote-so-skriptom#fail-class-form.php-dlya-raznykh-versii-skripta)).

Please note that the file **must always** be uploaded only for the corresponding script version and only under the user account created for the site (<mark style="color:red;">**not root!**</mark>).

<img src="../../.gitbook/assets/image (1982).png" alt="" data-size="original">

</details>

<details>

<summary>Countdown timer on the website is not working</summary>

---

If you need the last section translated as well, please provide the content inside it.

If instead of the timer (the `[js_timer][bid_delete_time][/js_timer]` construct) you see "---" displayed:  
![](<../../.gitbook/assets/image (1891).png>)  
go to "**Settings**" -> "**General Settings**" and set the date format to any option <mark style="color:red;">**except**</mark> d/m/Y:  

![](<../../.gitbook/assets/image (1893).png>)

</details>

<details>

<summary>An error appears: "<strong>No columns in the DB table {table name}</strong>"</summary>

Reactivate the main plugin (Premium Exchanger) in the "**Plugins**" section.  

![](<../../.gitbook/assets/image (513).png>) ![](<../../.gitbook/assets/image (514).png>)  

Then disable the update mode in "**Exchanger Settings**" → "**General Settings**".  

![](<../../.gitbook/assets/image (515).png>)  

After that, the missing columns will be created in the table.

</details>

<details>

<summary>No access to the website</summary>

![](<../../.gitbook/assets/image (1261).png>)  

You need to locate the XXXX_options table in your database using PhpMyAdmin or Adminer and check the **home** and **siteurl** fields (they should contain your current domain).  

<mark style="color:blue;">In ISP Manager, phpMyAdmin can be installed via "Settings — Software Configuration" by checking the box for "MySQL administration web interface" and clicking the "Install" button above the table.</mark>

</details>

<details>

<summary>Clearing merchant logs and enabling auto-cleanup</summary>

When the "Merchant Logs" and "Auto Payout Logs" modules run for a long time, the accumulated logs can quickly fill up the database, which may cause errors on the site if auto-cleanup is not enabled.  

<mark style="color:red;">We recommend enabling logging only while configuring the merchant modules. Once payment acceptance and auto payouts are stable, you can disable logging.</mark>  

You can set up automatic log cleanup in "**Settings**" -> "**Logging Settings**":  
![](<../../.gitbook/assets/image (1371).png>)  

In the "**Settings**" -> "**Cron**" section, copy the cron job URL and create a cron task on your server following [this guide](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-sozdat-zadanie-cron-na-servere) (run frequency: once every 24 hours or less often).  

![](<../../.gitbook/assets/image (672).png>) ![](<../../.gitbook/assets/image (673).png>)  

If logs are not cleared when clicking the "Delete Logs" button in the corresponding section, you will need to clear the logs directly via the database.  
![](<../../.gitbook/assets/image (1372).png>)



Here is a natural, fluent English translation of the provided text:

---

You need to access the database via PhpMyAdmin[^1] or Adminer and open the table [`xxxx_merch_logs`](#user-content-fn-2)[^2] (just in case, make a backup of the database before clearing the table).

Go to the database web interface.

<img src="../../.gitbook/assets/image (775).png" alt="" data-size="original">

_If the web interface is unavailable_ — _follow the instructions below to enable access:_

_How to check which firewall is installed on the server: log in as the <mark style="color:red;">root user</mark> to the ISPmanager panel, then run the command **`ufw status numbered`** in the Shell console._  
_If rules are listed, disable them with **`ufw disable`**. After working with the database, be sure to re-enable the rules using **`ufw enable`**._

_If you see the message **`Command 'ufw' not found`**, it means the firewall rules are managed by **iptables**._  
_To disable the rules, run **`iptables -P INPUT ACCEPT && iptables -P FORWARD ACCEPT`**, and after finishing your database work, reboot the server — the rules will be automatically re-enabled._

Find the table `xxxx_merch_logs` (where xxxx is your table prefix).

![](<../../.gitbook/assets/image (776).png>)

Go to the "Operations" tab.

![](<../../.gitbook/assets/image (774).png>)

Clear the table by clicking "TRUNCATE".

![](<../../.gitbook/assets/image (773).png>)

Confirm the data deletion.

![](<../../.gitbook/assets/image (777).png>)

Repeat these steps for the table [`xxxx_ap_logs`](#user-content-fn-3)[^3].

---

<details>

<summary>404 Error when accessing the exchange direction page</summary>

Most likely, the "**Dash in exchange direction**" module is enabled in the "**Modules**" section, but the settings have not been saved to apply the changes — you can either disable it or leave it enabled (your choice).

![](<../../.gitbook/assets/image (605).png>)

Go to "**Settings -> Permalinks**" and click the "**Save Changes**" button without making any changes on the page.

![](<../../.gitbook/assets/image (606).png>)

After that, check the exchange directions page. If the changes don’t appear immediately, [clear the cache in Cloudflare](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-sbrosit-kesh-v-cloudflare) (if you are using it).

</details>

<details>

<summary>525 Error "SSL handshake failed" when accessing the site</summary>

---

If you need the continuation or further translation, just let me know!

The error "SSL handshake failed" indicates that there was a problem establishing a secure connection between the client (usually a browser) and the server.

In your Cloudflare dashboard, go to the "SSL/TLS" section and set the "Your SSL/TLS encryption mode" option to "Flexible."

<img src="../../.gitbook/assets/image (779).png" alt="" data-size="original">

</details>

<details>

<summary>Admin Panel Errors After Script Update</summary>

Check the contents of the `userdata.php` file following the [instructions here](https://premium.gitbook.io/rukovodstvo-polzovatelya/pered-nachalom-raboty/instrukciya-po-obnovleniyu#ustranenie-nepoladok-posle-obnovleniya).

</details>

<details>

<summary>Error in <code>script.js</code> File</summary>

If you encounter this error, disable caching of `js` files in your site settings within ISP Manager.

![](<../../.gitbook/assets/image (101).png>)

In the "File Extensions for Caching" list, there **must NOT** be a `js` entry. If it’s present, remove it and save the settings.

![](<../../.gitbook/assets/image (102).png>)

</details>

<details>

<summary>Checking Table Sizes in the Database</summary>

If your website or admin panel starts to slow down, the issue might be caused by some database tables growing too large—most often, these are log tables.

To identify the largest tables for cleanup, follow these steps:

1. In ISP Manager, go to the "**Databases**" section, select your database (copy its name to a text file), then go to the "**Users**" section:

<img src="../../.gitbook/assets/image (1530).png" alt="" data-size="original">

2. On the page, select the database owner and click "**Edit**":

![](<../../.gitbook/assets/image (1531).png>)

3. Click the eye icon to view the user’s password. Save the username and password to a text file.

![](<../../.gitbook/assets/image (1532).png>)

4. Go to the "**Shell Client**" section and enter the command:

```
mysql -u username -p
```

Replace **username** with the database username you saved earlier. Run the command, then enter the password when prompted (note: the characters won’t be displayed as you type). Press Enter. If successful, you will see the message "**Welcome to the MySQL monitor.**"

![](<../../.gitbook/assets/image (1533).png>)

5. Next, enter the following command to list the largest tables by size:

```sql
SELECT table_name AS "Table", 
       ROUND(((data_length + index_length) / 1024 / 1024), 2) AS "Size in MB" 
FROM information_schema.TABLES 
WHERE table_schema = "database_name" 
ORDER BY (data_length + index_length) DESC;
```

Replace **database_name** with the name of your database. Press Enter.

This will display the tables sorted by their size in megabytes.

Here is a natural English translation of the provided text:

---

After completing these steps, a list of all tables will be displayed, sorted by size (with the largest tables at the top).

</details>

<details>

<summary>Redirect to a Subdomain When the Main Domain Is Blocked</summary>

First, you need to add the subdomain to your license in the [personal account](https://premiumexchanger.com/ulicense/). After that, add the following code block to your nginx configuration file (replace 123.ru and test.123.ru with your own domain and subdomain):

```nginx
server {
  server_name 123.ru;
  
  listen 80;
  
  location / {
    if ($argument_uri) {
      return 301 https://test.123.ru$request_uri;
    }
    
    ## remaining config here
  }
}
```

Here’s how it works: when a user visits the site, the specified condition is checked. If it’s met, a 301 redirect is issued, passing along all request parameters (including the “tail” of any partner links).

The example above is for nginx; this configuration will not work with Apache.

</details>

<details>

<summary>System Error (Code: anticsfr)</summary>

![](<../../.gitbook/assets/image (1259).png>)![](<../../.gitbook/assets/image (1304).png>)

<img src="../../.gitbook/assets/image (1307).png" alt="" data-size="original">

As a quick temporary fix, simply reload the page in your browser.

This error indicates a problem with session storage on the server or a change in the user’s IP address. Most likely, the user session storage is not configured correctly.

If the session keeps resetting, you will need to adjust your PHP settings.\
![](<../../.gitbook/assets/image (1336).png>)

To fix the issue, configure the session settings as shown in the screenshot below.

![](<../../.gitbook/assets/image (721).png>)

**`session.gc_probability`** and **`session.gc_divisor`**: These two settings together determine the probability that the garbage collection process will run on each request. The probability is calculated as **`gc_probability/gc_divisor`**. For example, if **`gc_probability`** is 1 and **`gc_divisor`** is 1000, garbage collection will run on approximately 0.1% of requests.

**`session.gc_maxlifetime`**: This setting defines the maximum lifetime of a session in seconds. If a session is older than this value, it will be considered “garbage” and deleted during the next garbage collection run.

---

If you need any further help or adjustments, feel free to ask!

**After changing the PHP configuration, you need to restart the web server for the changes to take effect.**

To automatically clear sessions, you can add two daily CRON jobs:

---

**Job 1:**
```bash
find /var/www/*/data/mod-tmp/ -name "sess_*" -exec rm {} \;
```

**Job 2:**
```bash
find /var/www/*/data/bin-tmp/ -name "sess_*" -exec rm {} \;
```

---

<details>
<summary>Control panel or site is slow/unresponsive, errors appear when creating a request</summary>

## Deleting Sessions

Run the following commands via SSH:

Navigate to the site’s data directory (replace **site_username** with the actual username):
```bash
cd /var/www/site_username/data
```

Then execute:
```bash
find mod-tmp -name "sess_*" -mtime +2 -type f -print0 | xargs -0rn 20 rm -f
```
This will delete all session files older than 2 days.

You can also open another SSH session and run:
```bash
df -i
```
This command shows inode usage (the number of files your disk can hold).

---

![Disk inode usage example](../../.gitbook/assets/image (714).png)

The number of inodes varies significantly between servers, so cleaning may take anywhere from 10 minutes to 5 hours.

## Server Access Settings

Please check the [“Settings” → “Cron” section](https://premium.gitbook.io/main/osnovnye-nastroiki/nastroiki/obshie-nastroiki#cron) — the settings there must match the instructions.

If you have modified these settings before, please revert them to their original state.

## PHP Settings

Log into ISP Manager as the **root user** and verify the PHP version used by your site.

![PHP version check](../../.gitbook/assets/image (715).png)

![PHP version selection](../../.gitbook/assets/image (716).png)

Next, open the settings for the selected PHP version:

![PHP version settings](../../.gitbook/assets/image (718).png)

Make sure the following parameters on your server match the values shown in the screenshot below. If they differ, please update them accordingly:

![PHP parameters](../../.gitbook/assets/image (719).png)

To fully clear session files, run:
```bash
find mod-tmp -name "sess_*" -type f -print0 | xargs -0rn 20 rm -f
```

After completing these steps, temporary files will be removed from the server, and PHP’s automatic file cleanup will function properly.

## Increasing Memory Limit

[Section continues...]  
</details>

If you are processing a large amount of data, the script may not have enough allocated RAM on the server to function properly. To increase the memory limit that WordPress can use, follow these steps:

1. On your server, open the file `your_domain/wp-config.php` and add the following lines right after the line `define('WP_DEBUG', false);`, then save the changes:

```php
define('WP_MEMORY_LIMIT', '512M');
define('WP_MAX_MEMORY_LIMIT', '1024M');
```

2. In your server configuration, set the value `MEMORY_LIMIT = 512M`.

---

## Change the IP-based Country Detection Service

In the "**GEO IP**" section under "**IP Detection Settings**," switch the source to **sypexgeo.net**, set the timeout to 7 seconds, and save the changes.

---

## Additional Actions in the Admin Panel and on the Server

You can try disabling all modules in the "**Modules**" section (make sure to note the initial state) and check if the site runs faster.

If it does, gradually re-enable the modules in batches of 3–5 and monitor when the slowdown occurs. Once you identify the problematic module, analyze it further to find the cause of the lag.

Also, if present, you can delete the module located at `\wp-content\plugins\premiumbox\moduls\courselogs` on the server, as it may be causing significant system load.

If these recommendations don’t resolve the issue, contact your hosting provider’s support team and ask them to perform diagnostics and provide information about the server load.

---

<details>

<summary>Increasing the Maximum Upload File Size</summary>

If needed, you can set a custom maximum file size for uploads via the user account or in requests (for example, images used for invoice or identity verification).

The default limit is 2 megabytes.

If you are using ISP Manager, log in as the root user, go to the "**PHP Settings**" section:

![PHP Settings](../../.gitbook/assets/image%20(1517).png)

Select the PHP version your site uses and open its settings:

![PHP Version Settings](../../.gitbook/assets/image%20(1519).png)

</details>

Set the desired value for the "**Max file size**" option and save the changes. Then restart the server.

If you are not using the ISP Manager control panel, open your php.ini file, locate the directives below, set your values accordingly, and restart the server.

```ini
upload_max_filesize = 128M      — maximum size of a single uploaded file  
post_max_size = 128M            — maximum size of all files uploaded in one request  
memory_limit = 256M             — PHP memory limit  
max_execution_time = 300        — maximum script execution time in seconds  
max_input_time = 300            — maximum time in seconds a script can spend parsing input data  
```

- **upload_max_filesize** — set this to a value larger than your backup file size  
- **post_max_size** — set this to a value larger than your backup file size  
- **memory_limit** — set this to a value larger than your backup file size  
- **max_execution_time** — set this to 0 (unlimited)

If you encounter errors after increasing the file size limits, please refer to the [official PHP guide on common file upload pitfalls](https://www.php.net/manual/ru/features.file-upload.common-pitfalls.php) for troubleshooting.

---

<details>

<summary>Setting the status to "<strong>Under Review</strong>"</summary>

1. In the settings of **all** **active** merchant modules, locate the block titled "**Working with request statuses**." For every option in this block, select "**Under Review**" from the dropdown menu and save your changes.

<img src="../../.gitbook/assets/Добавить мерчант ‹ Обменник — WordPress - Google Chrome_240501160623.png" alt="" data-size="original">

2. In the settings of **all** **active** auto-payout modules, disable payouts for requests with the status "**Under Review**" by selecting "**No**" for the highlighted option below.

<img src="../../.gitbook/assets/Добавить автовыплату ‹ Обменник — WordPress - Google Chrome_240501160808.png" alt="" data-size="original">

</details>

---

<details>

<summary>Quick reference for configuring DNS records to enable email on your domain</summary>

Occasionally, you may need to troubleshoot certain aspects of email verification. This involves checking various DNS records and queries.

</details>

Here is a naturalistic English translation of the given text:

---

[A brief cheat sheet](https://www.netmeister.org/blog/email-dns-records.html) that you can use next time you forget which records are used to verify SPF, DKIM, DMARC, etc.

</details>

### Module "**QR Generator**":

{% file src="../../.gitbook/assets/qr_adress.zip" %}

### The file class-form.php for different script versions:

Version 2.6:

{% file src="../../.gitbook/assets/class-form.php" %}

Version 2.5:

{% file src="../../.gitbook/assets/class-form (1).php" %}

[^1]: phpMyAdmin in ISP Manager can be installed via "Settings - Software Configuration - check the box for 'MySQL Administration Web Interface' - then click the 'Install' button above the table.

[^2]: Merchant logs

[^3]: Auto payout logs