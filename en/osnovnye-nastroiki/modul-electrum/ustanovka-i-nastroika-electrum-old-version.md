# Installing and Configuring Electrum (Old Version)

{% hint style="info" %}
**System Requirements for the Module Installed on the Server:**

- Operating System: **Ubuntu 20.x** or **22.x**. **Other OS are not supported**.
- Control Panel: **ISP Manager 6 Lite**
- **Premium Exchanger v2.4** or higher

**System Requirements for the Application Installed on a Computer:**

- Operating System: **Linux/Windows (8.1 and higher)/macOS (10.13 and higher)/Android (5.0 and higher)**
{% endhint %}

---

## Installing Required Modules on the Server via ISP Manager 6 Lite

1. Log in to the ISP Manager control panel using your <mark style="color:red;">**root user**</mark> credentials.
2. Navigate to the "**Administration**" -> "**Shell Client**" section.

<figure><img src="../../.gitbook/assets/изображение (126).png" alt="" width="330"><figcaption></figcaption></figure>

3. Right-click on the blank screen and select "**Paste from browser**" from the context menu.

<figure><img src="../../.gitbook/assets/изображение (178).png" alt="" width="563"><figcaption></figcaption></figure>

4. Enter the command below in the opened window, click "**OK**," and then press **Enter** to execute the command.

```
sudo apt-get install libsecp256k1-0 python3-cryptography -y
```

5. Wait for the command to complete.

<figure><img src="../../.gitbook/assets/изображение (38).png" alt=""><figcaption></figcaption></figure>

---

## Verifying Shell Client Access for the Website User

6. Go to the "**Users**" section.

<figure><img src="../../.gitbook/assets/изображение (136).png" alt="" width="325"><figcaption></figcaption></figure>

7. Click on the username under which the website operates.

<figure><img src="../../.gitbook/assets/изображение (183).png" alt=""><figcaption></figcaption></figure>

8. In the "**Access**" block, check if the **"Shell Access"** checkbox is ticked. If it is not, tick it and save the user settings.

<figure><img src="../../.gitbook/assets/изображение (104).png" alt="" width="563"><figcaption></figcaption></figure>

---

## Installing Electrum on Your Computer and Creating a Wallet

9. [Download](https://download.electrum.org/4.4.6/) and install Electrum on your computer:

- [electrum-4.4.6-setup.exe](https://download.electrum.org/4.4.6/electrum-4.4.6-setup.exe) — Installer for Windows
- [electrum-4.4.6-portable.exe](https://download.electrum.org/4.4.6/electrum-4.4.6-portable.exe) — Portable version for Windows
- [electrum-4.4.6.dmg](https://download.electrum.org/4.4.6/electrum-4.4.6.dmg) — Installer for macOS
- [electrum-4.4.6.tar.gz](https://download.electrum.org/4.4.6/Electrum-sourceonly-4.4.6.tar.gz) — Installer for Linux

10. Create a new wallet by following the app's instructions.

<details>
<summary>Steps to Create a New Wallet</summary>

- Select "Standard Wallet"\
  ![](<../../.gitbook/assets/image (1316).png>)

- Generate a new seed phrase\
  ![](<../../.gitbook/assets/image (1317).png>)

- Write down the seed phrase in a notebook and save the file\
  ![](<../../.gitbook/assets/image (1318).png>)

- Enter the full seed phrase for verification\
  ![](<../../.gitbook/assets/image (1319).png>)

- <mark style="color:red;">It is mandatory</mark> to set a wallet password (at least 16 characters — use Latin letters and numbers) and save the password in a notebook\
  ![](<../../.gitbook/assets/image (1320).png>)

</details>

11. Open the installed Electrum application on your computer and go to the "**File**" -> "**Open**" menu.

<figure><img src="../../.gitbook/assets/image (647).png" alt="" width="403"><figcaption></figcaption></figure>

12. A folder containing your wallet will open. Locate the wallet file with the name you used during setup.

<figure><img src="../../.gitbook/assets/image (1357).png" alt="" width="482"><figcaption></figcaption></figure>

{% hint style="warning" %}
By default, the wallet is named **"default_wallet"**, but you may have given it a custom name during setup.
{% endhint %}

---

## Uploading Files to the Server

13. Go to the "**Sites**" section in ISP Manager.

<figure><img src="../../.gitbook/assets/изображение (190).png" alt="" width="300"><figcaption></figcaption></figure>

14. Select the desired site and click the **"Login as Owner"** button. You will be logged in as the <mark style="color:green;">user created for the site</mark>.

<figure><img src="../../.gitbook/assets/изображение (71).png" alt=""><figcaption></figcaption></figure>

15. Open the "**File Manager**" section in the sidebar.

<figure><img src="../../.gitbook/assets/изображение (115).png" alt="" width="330"><figcaption></figcaption></figure>

16. Upload the files from the **`electrum_installer.zip`** archive you received from us, along with the previously created Electrum wallet file from the "**electrum_data**" folder on your computer, to the opened directory.

<figure><img src="../../.gitbook/assets/image (1356).png" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
If the wallet being uploaded to the server has a name other than **default_wallet**, rename it to **default_wallet** on both the server and your computer. This is necessary for the wallet file to be automatically transferred on the server.
{% endhint %}

The following files must be uploaded to the server:

- `start_or_restart_electrum_daemon.sh`
- `install_electrum.sh`
- `default_wallet` (the Electrum wallet you created earlier)

17. In the root directory, open the **`start_or_restart_electrum_daemon.sh`** file for editing by double-clicking it. In the line <mark style="color:blue;">`4: WALLET_PASSWORD="`</mark><mark style="color:purple;">`your_wallet_password`</mark><mark style="color:blue;">`"`</mark>, replace <mark style="color:purple;">`your_wallet_password`</mark> with the password you set during wallet creation. Save the changes.

<figure><img src="../../.gitbook/assets/image (1385).png" alt=""><figcaption></figcaption></figure>

---

## Installing Electrum on the Server

18. Go to the **"Shell Client"** section while logged in as the <mark style="color:green;">user created for the site</mark>.

<figure><img src="../../.gitbook/assets/изображение (52).png" alt="" width="330"><figcaption></figcaption></figure>

19. Right-click on the blank screen, select **"Paste from browser"**, enter the command **`bash install_electrum.sh`**, and click OK. Then press **Enter** to execute the command.

<figure><img src="../../.gitbook/assets/изображение (36).png" alt="" width="563"><figcaption></figcaption></figure>

20. After the script completes, save the data highlighted in the red box in the screenshot below for further configuration in the Premium Exchanger admin panel.

<figure><img src="../../.gitbook/assets/image (1324).png" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
If you are installing the Electrum module on a server different from the one where the Premium Exchanger script is installed, you will need to fill in the "API Server" field with the IP address of the server where Electrum is installed in the merchant/payout module settings later.

![](<../../.gitbook/assets/image (1351).png>)
{% endhint %}

---

## Adding Cron Jobs

21. Copy the first command to configure the Cron task scheduler on the server. Highlight the corresponding line with the left mouse button, right-click to open the menu, and select "**Copy**."

<figure><img src="../../.gitbook/assets/image (1325).png" alt=""><figcaption></figcaption></figure>

22. Go to the **"Cron Scheduler"** section.

{% hint style="warning" %}
Cron jobs must be added under the <mark style="color:green;">user created for the site</mark>, **not** under the <mark style="color:red;">**root user**</mark>!
{% endhint %}

<figure><img src="../../.gitbook/assets/изображение (75).png" alt="" width="315"><figcaption></figcaption></figure>

23. Click the **"Create Task"** button, paste the copied command into the **"Command"** field, and configure the form as shown in the screenshot below. Click "**Create**."

<figure><img src="../../.gitbook/assets/image (1326).png" alt="" width="488"><figcaption></figcaption></figure>

24. Create a task for the second command. Copy the second command line.

<figure><img src="../../.gitbook/assets/image (1355).png" alt=""><figcaption></figcaption></figure>

Create a new task, paste the command into the appropriate field, and configure the form as shown in the screenshot below. Click "**Create**."

<figure><img src="../../.gitbook/assets/image (1327).png" alt="" width="473"><figcaption></figcaption></figure>

---

## Deleting Files from the Server

25. In the "**File Manager**" section, delete the previously uploaded files from the server:

- `start_or_restart_electrum_daemon.sh`
- `install_electrum.sh`
- `default_wallet`

<figure><img src="../../.gitbook/assets/image (1328).png" alt="" width="563"><figcaption></figcaption></figure>

---

## **Restarting the Server**

26. **Make sure** to restart the server after installation.

{% hint style="danger" %}
After installing Electrum or changing the wallet/password, **you must** restart the server.
{% endhint %}

---

## Continuing Configuration

After installing Electrum on the server, configure the connection to the Electrum wallet in the website control panel:

- [Guide for Configuring a Merchant to Accept BTC](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/electrum)
- [Guide for Configuring a Merchant for BTC Payouts](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/electrum)