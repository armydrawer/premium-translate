# Using Electrum on a Computer (Wallet Synchronization)

If you want to use the **Electrum** wallet on your computer as well, keep the following points in mind:

* The wallet on the server and the wallet on your computer do not automatically synchronize incoming transactions. For example, if new addresses are created on the server wallet and funds are received there, these addresses will not automatically appear on the computer wallet. If you need detailed information about incoming transactions on your computer wallet, you’ll need to manually synchronize it. Instructions on how to do this are provided below.
* The balance displayed in the computer wallet may be incorrect until a spending transaction is made directly from the exchange. While this issue is not widespread or fully confirmed, it has been observed during testing.

Download Electrum for your operating system from the [official website](https://download.electrum.org/4.4.6/) (**make sure to use the latest version, 4.4.6**).

Install the software and create a new wallet by following the [instructions (steps 9–12)](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/modul-electrum/ustanovka-i-nastroika-electrum#ustanovka-electrum-na-kompyuter-i-sozdanie-koshelka).

## Wallet Synchronization

1. In the ISP Manager control panel, go to the **"Sites"** section, select the desired site with a single click, and click on **"Log in as owner"**.

    <figure><img src="../../.gitbook/assets/изображение (94)_eng.png" alt=""><figcaption></figcaption></figure>

2. Open the **"File Manager"** section.

    <figure><img src="../../.gitbook/assets/изображение (67)_eng.png" alt="" width="330"><figcaption></figcaption></figure>

3. Navigate to the directory `/Electrum/Electrum-X.X.X/electrum_data/wallets/`, where `X.X.X` represents the version number of the wallet installed on the server (in this case, version 4.4.6).

    <figure><img src="../../.gitbook/assets/image (1475)_eng.png" alt=""><figcaption></figcaption></figure>

4. Download the `default_wallet` file to your computer.

    <figure><img src="../../.gitbook/assets/image (1476)_eng.png" alt=""><figcaption></figcaption></figure>

5. Replace the `electrum_data\wallets\default_wallet` file on your computer with the `default_wallet` file you downloaded from the server. Then, restart **Electrum** on your computer. After completing these steps, the wallets will be synchronized.