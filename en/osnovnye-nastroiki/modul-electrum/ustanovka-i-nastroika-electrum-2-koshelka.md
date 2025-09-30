# Installing and Configuring Electrum (2 Wallets)

{% hint style="info" %}
**System Requirements for the Module Installed on the Server:**

- Operating System: **Ubuntu 20.x** or **22.x**. **Other OS versions are not supported**.
- Control Panel: **ISP Manager 6 Lite**
- **Premium Exchanger v2.4** or higher

**System Requirements for the Application Installed on the Client Device:**

- Operating System: **Linux/Windows (8.1 and higher)/macOS (10.13 and higher)/Android (5.0 and higher)**
{% endhint %}

---

## Installing Required Modules on the Server via ISP Manager 6 Lite

1. Log in to the ISP Manager control panel using the <mark style="color:red;">**root user**</mark> credentials.
2. Navigate to the "**Administration** -> **Shell Client**" section.

<figure><img src="../../.gitbook/assets/изображение (126)_eng.png" alt="" width="330"><figcaption></figcaption></figure>

3. Right-click on the blank screen and select "**Paste from browser**" from the context menu.

<figure><img src="../../.gitbook/assets/изображение (178)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

4. Enter the command below in the opened window, click "**OK**," and then press **Enter** to execute the command:

```
sudo apt-get install libsecp256k1-0 python3-cryptography -y
```

5. Wait for the command to complete.

<figure><img src="../../.gitbook/assets/изображение (38)_eng.png" alt=""><figcaption></figcaption></figure>

---

## Verifying Shell Client Access for the Website User

6. Go to the "**Users**" section.

<figure><img src="../../.gitbook/assets/изображение (136)_eng.png" alt="" width="325"><figcaption></figcaption></figure>

7. Click on the username under which the website operates.

<figure><img src="../../.gitbook/assets/изображение (183)_eng.png" alt=""><figcaption></figcaption></figure>

8. In the "**Access**" block, check if the **"Shell Access"** checkbox is selected. If not, select it and save the user settings.

<figure><img src="../../.gitbook/assets/изображение (104)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

---

## Installing Electrum on Your Computer and Creating Wallets

9. [Download](https://download.electrum.org/4.4.6/) and install Electrum on your computer:

- [electrum-4.4.6-setup.exe](https://download.electrum.org/4.4.6/electrum-4.4.6-setup.exe) — Installer for Windows
- [electrum-4.4.6-portable.exe](https://download.electrum.org/4.4.6/electrum-4.4.6-portable.exe) — Portable version for Windows
- [electrum-4.4.6.dmg](https://download.electrum.org/4.4.6/electrum-4.4.6.dmg) — Installer for macOS
- [electrum-4.4.6.tar.gz](https://download.electrum.org/4.4.6/Electrum-sourceonly-4.4.6.tar.gz) — Installer for Linux

10. Create 2 wallets (or duplicate an existing wallet by copying its file) following the app instructions.

{% hint style="danger" %}
**Warning!** Do not use the **$** symbol in the wallet password, as it may cause script errors.
{% endhint %}

<details>
<summary>Creating a New Wallet</summary>

Select "Standard Wallet"\
![](<../../.gitbook/assets/image (1316)_eng.png>)

Generate a new seed phrase\
![](<../../.gitbook/assets/image (1317)_eng.png>)

Write down the seed phrase and save it in a file\
![](<../../.gitbook/assets/image (1318)_eng.png>)

Enter the seed phrase for verification\
![](<../../.gitbook/assets/image (1319)_eng.png>)

<mark style="color:red;">Important:</mark> Set a password for the wallet (at least 16 characters, using Latin letters and numbers) and save it in a file.\
![](<../../.gitbook/assets/image (1320)_eng.png>)

</details>

11. Create a second wallet in the same way (or use a duplicate).
12. Open the installed Electrum app on your computer and go to the "**File**" -> "**Open**" menu.

<figure><img src="../../.gitbook/assets/image (647)_eng.png" alt="" width="403"><figcaption></figcaption></figure>

13. In the folder that opens, locate the wallets you created.\
    \
    Name the wallet for receiving funds **default_wallet_in** and the wallet for sending funds **default_wallet_out**. (If you don’t plan to use auto-payouts, you don’t need to create a new module copy in the admin panel. The wallet is only required for proper module installation.)

<figure><img src="../../.gitbook/assets/image (1575)_eng.png" alt=""><figcaption></figcaption></figure>

---

## Uploading Files to the Server

14. Go to the "**Sites**" section in ISP Manager.

<figure><img src="../../.gitbook/assets/изображение (190)_eng.png" alt="" width="300"><figcaption></figcaption></figure>

15. Select your site and click the **"Login as Owner"** button. You will be logged in as the <mark style="color:green;">user created for the site</mark>.

<figure><img src="../../.gitbook/assets/изображение (71)_eng.png" alt=""><figcaption></figcaption></figure>

16. Open the "**File Manager**" section in the sidebar.

<figure><img src="../../.gitbook/assets/изображение (115)_eng.png" alt="" width="330"><figcaption></figcaption></figure>

17. Upload the files from the **`electrum_installer.zip`** archive (provided after [**module payment**](https://premiumexchanger.com/masspayments/)) and the two Electrum wallet files from the "**electrum_data**" folder on your computer.

Files to upload:

- `start_or_restart_electrum_daemon2.sh`
- `install_electrum2.sh`
- `default_wallet_in`
- `default_wallet_out`

{% hint style="danger" %}
If the uploaded wallet files have names other than **default_wallet_in** and **default_wallet_out**, rename them accordingly on both the server and your computer. This is necessary for the automatic transfer of wallet files to the Electrum folder on the server.
{% endhint %}

---

## Installing Electrum on the Server

19. Go to the **"Shell Client"** section, logged in as the <mark style="color:green;">user created for the site</mark>.

<figure><img src="../../.gitbook/assets/изображение (52)_eng.png" alt="" width="330"><figcaption></figcaption></figure>

20. Right-click on the blank screen, select **"Paste from browser"**, enter the command **`bash install_electrum2.sh`**, and click OK. Then press **Enter** to run the command.

<figure><img src="../../.gitbook/assets/image (1579)_eng.png" alt=""><figcaption></figcaption></figure>

21. After the script finishes, save the data highlighted in red in the screenshot below for further module configuration in the admin panel.

<figure><img src="../../.gitbook/assets/image (1580)_eng.png" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
If you are installing Electrum on a server different from the one hosting the Premium Exchanger script, you will need to specify the "API Server" field in the merchant/auto-payout module settings in the admin panel. Enter the IP address of the server where Electrum is installed.

![](<../../.gitbook/assets/image (1351)_eng.png>)
{% endhint %}

---

## Adding Cron Jobs

22. Copy the first command to configure the Cron task scheduler on the server. Highlight the corresponding line with the left mouse button, right-click, and select "**Copy**."

<figure><img src="../../.gitbook/assets/image (575)_eng.png" alt=""><figcaption></figcaption></figure>

23. Go to the **"Cron Scheduler"** section.

{% hint style="danger" %}
Cron jobs must be added under the <mark style="color:green;">user created for the site</mark>, **not** under the <mark style="color:red;">**root user**</mark>!
{% endhint %}

<figure><img src="../../.gitbook/assets/изображение (75)_eng.png" alt="" width="315"><figcaption></figcaption></figure>

24. Click the **"Create Task"** button, paste the command copied in step 22 into the **"Command"** field, and configure the form as shown in the screenshot below.

<figure><img src="../../.gitbook/assets/image (1582)_eng.png" alt="" width="375"><figcaption></figcaption></figure>

Click "**Create**."

25. Create a task for the second command.

<figure><img src="../../.gitbook/assets/image (1327)_eng.png" alt="" width="473"><figcaption></figcaption></figure>

---

## Deleting Files on the Server

26. In the "**File Manager**" section, delete 3 of the 4 previously uploaded files from the server:

- `install_electrum2.sh`
- `default_wallet_in`
- `default_wallet_out`

Do **not** delete the file `start_or_restart_electrum_daemon2.sh`.

<figure><img src="../../.gitbook/assets/image (576)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

---

## **Restarting the Server**

27. **Make sure** to restart the server after installation.

{% hint style="danger" %}
After installing Electrum or changing the wallet/password, you **must** restart the server.
{% endhint %}

---

## Continuing Configuration

After installing Electrum on the server, configure the connection to the Electrum wallets in the admin panel:

- [Instructions for setting up a merchant to receive BTC](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/electrum)
- [Instructions for setting up a merchant for BTC payouts](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/electrum)