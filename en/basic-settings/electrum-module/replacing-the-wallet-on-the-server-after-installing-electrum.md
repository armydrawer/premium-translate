# Replacing the Wallet on the Server After Installing Electrum

If the installation and configuration of the Electrum module were performed by the specialists at Premium Exchanger, you’ll need to replace the test wallet on the server with the one you created after the work is completed.

***

### 1. [Download](https://download.electrum.org/4.3.3/) and install Electrum on your computer:

* [electrum-4.4.6-setup.exe](https://download.electrum.org/4.4.6/electrum-4.4.6-setup.exe) — Installable version for Windows
* [electrum-4.4.6-portable.exe](https://download.electrum.org/4.4.6/electrum-4.4.6-portable.exe) — Portable version for Windows
* [electrum-4.4.6.dmg](https://download.electrum.org/4.4.6/electrum-4.4.6.dmg) — Installable version for macOS
* [Electrum-4.4.6.tar.gz](https://download.electrum.org/4.4.6/Electrum-4.4.6.tar.gz) — Installable version for Linux

{% hint style="danger" %}
**Important:** Make sure to download version 4.4.6 specifically. When launching the application, decline any prompts to update to the latest version.
{% endhint %}

***

### 2. Create a new wallet by following the app’s instructions.

<details>

<summary>Steps to Create a New Wallet</summary>

1. Select "Standard Wallet."\
   ![](<../../.gitbook/assets/image (1316)_eng.png>)
2. Generate a new seed phrase.\
   ![](<../../.gitbook/assets/image (1317)_eng.png>)
3. Write down the seed phrase in a secure location.\
   ![](<../../.gitbook/assets/image (1318)_eng.png>)
4. Enter the full seed phrase to confirm.\
   ![](<../../.gitbook/assets/image (1319)_eng.png>)
5. <mark style="color:red;">Make sure</mark> to set a wallet password (at least 16 characters, using Latin letters and numbers) and write it down securely.\
   ![](<../../.gitbook/assets/image (1320)_eng.png>)

</details>

***

### 3. Open the installed Electrum app on your computer and go to the "**File**" -> "**Open**" menu.

***

### 4. A folder containing your wallet files will open. Locate the wallet file with the name you assigned during setup.

<figure><img src="../../.gitbook/assets/image (1357)_eng (1).png" alt="" width="482"><figcaption></figcaption></figure>

**Note:** You may have multiple wallets in this folder. Select the correct wallet file, as you’ll need it for uploading to the server in the next step.

{% hint style="warning" %}
By default, the wallet is named **"default\_wallet"**, but you may have given it a custom name during setup.
{% endhint %}

***

### 5. Open the ISP Manager panel in your browser and log in. Once logged in as the user created for the site (**not root**), navigate to the "File Manager" section in the sidebar.

<figure><img src="../../.gitbook/assets/image (1359)_eng.png" alt="" width="330"><figcaption></figcaption></figure>

***

### 6. Upload the wallet file you created (e.g., `default_wallet`) to the appropriate directory:

* For receiving funds: `electrum_in/Electrum-4.4.6/electrum_data/wallets/`
* For sending funds: `electrum_out/Electrum-4.4.6/electrum_data/wallets/`

If a warning appears stating that a file with the same name already exists, click "**Replace**."

<figure><img src="../../.gitbook/assets/image (1360)_eng.png" alt="" width="384"><figcaption></figcaption></figure>

***

### 7. In the directory `Electrum/Electrum-4.4.6/`, update the wallet password in the file **`start_or_restart_electrum_daemon.sh`**, which was previously uploaded to your server. If the password for the test wallet and your new wallet is the same, you can skip this step.

***

### 8. <mark style="color:red;">Restart the server</mark>.

***

After completing these steps, the test wallet on the server will be replaced with the wallet you created.
