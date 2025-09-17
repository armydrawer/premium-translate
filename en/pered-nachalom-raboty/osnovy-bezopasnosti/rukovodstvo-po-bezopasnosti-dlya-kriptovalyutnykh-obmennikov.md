# Cryptocurrency Exchange Security Guide

{% hint style="warning" %}
### ⚠️ IMPORTANT: Security is Priority #1

**Golden Rule**: Security must be fully set up and all systems thoroughly checked before launching the exchange. **Security takes precedence over convenience.**

_Security in the cryptocurrency space is not paranoia—it's a necessity. Follow all recommendations strictly._  
\
The guidelines below are based on 10 years of experience from an exchange administrator who also leads our training program.
{% endhint %}

---

### 1. 🖥️ Computer/Laptop Security

#### Key Principles for Using Your Computer:

* ❌ **DO NOT visit** suspicious websites  
* ❌ **DO NOT download** unknown software  
* ✅ Use your computer **exclusively for work**  
* ✅ It is recommended to use **macOS** (a more secure operating system)  

#### Antivirus Protection:

**Recommended Antivirus:** Use a paid antivirus with **data encryption features**, such as ESET NOD32, Kaspersky Internet Security, or Dr. Web. The key is ensuring the antivirus has the necessary tools to protect your information.

* ⚠️ **Important**: Purchase the license only via VPN/proxy (avoid using a Russian IP address).  
* When buying NOD32, avoid the Russian PRO32 version (it is less reliable).  

**Disk Encryption:**

1. **Create an encrypted disk** using your antivirus software.  
2. Store **ALL work-related data** exclusively on the encrypted disk.  
3. **DO NOT store** data on regular Windows drives.  
4. Create **backup copies** on encrypted USB drives.  

#### Handling USB Drives:

1. **Always format** new USB drives before use.  
2. Format them on a **separate computer** (not your work device).  
3. **Encrypt** USB drives using the same antivirus software.  
4. ⚠️ **Warning**: Even brand-new USB drives can carry viruses.  

---

### 2. 🌐 Browser Configuration

#### Mandatory Security Settings:

**Disable the following:**

* ❌ Password manager  
* ❌ Password auto-save  
* ❌ Payment methods  
* ❌ Automatic login  
* ❌ ALL extensions (except those essential for work)  

**Enable the following:**

* ✅ **Enhanced protection** in the "Security" section.  
* ✅ All available privacy features.  

**Extensions:**

* Use **minimal extensions** (only a VPN for work, if necessary).  
* **DO NOT install** even official extensions unless absolutely required.  
* The only exception: tools for document handling (e.g., PDF readers).  

---

### 3. 🔐 Payment System Security

#### Two-Factor Authentication (2FA):

**Mandatory for all services:**

* **Crypto exchanges and wallets:** Enable the highest level of protection for all services, including two-factor authentication (2FA) via an app (e.g., Google Authenticator) and linking to an email address or phone number.  
* **Email accounts:** Use 2FA via phone or an authenticator app.  

**"Lock and Key Separate" Rule:**

* **DO NOT use** 2FA on the same device where your wallet is accessed.  
* Use **different devices** for different security functions.  
* Have **dedicated work phones** exclusively for 2FA.  

#### Work Phones:

* Use **at least 1–2 dedicated** work phones.  
* **DO NOT use** them for personal calls or messages.  
* **Never share** work phone numbers with others.  
* Consider **replacing your phone number** in existing services with a work number.  

---

### 4. 🖥️ Server and Admin Panel Security

#### Server Access:

**SSH Keys:**

* **DO NOT store** access keys on your desktop.  
* Store keys on an **encrypted disk** or **separate USB drive**.  
* **DO NOT share** keys with anyone (except trusted technical specialists).  
* If sharing keys via Telegram, **delete messages immediately** after the recipient confirms receipt.  

**2FA Setup for the Server:**

1. **Enable 2FA** for ROOT access.  
2. **Enable 2FA** for user access.  
3. **Save QR codes** and keys on an encrypted storage device.  
4. **Change passwords** after completing setup.  

#### Password Requirements:

* **At least 15 characters long**  
* Include **uppercase and lowercase Latin letters**  
* Include **numbers**  
* Include **1–2 special characters** (e.g., `@, #, !`)  

---

### 5. 📧 Telegram and Email Security

#### Setting Up a Work Telegram Account:

* **Install Telegram separately** for work purposes only.  
* **Enable 2FA.**  
* Set up **code words** for added security.  
* Install Telegram on both your work phone and laptop.  

#### Sharing Confidential Information:

1. **Only share information** with trusted technical specialists.  
2. **Immediately delete** files after the recipient confirms receipt.  
3. **Delete messages** from both your and the recipient's chat history.  
4. **DO NOT leave passwords** in message history.  

#### Work Email:

* Use a **dedicated email address** for work only.  
* Choose a **reliable email provider** for work purposes (this email will be used for **server notifications**). Suitable options include Gmail, ProtonMail, or Yandex.Mail.  
* **2FA via phone** is mandatory.  

---

### 6. 📋 Data Storage Structure

#### Recommended File Organization:

```
📁 Work (on an encrypted disk)
├── 📁 Server
│   ├── 📁 Server Access
│   │   ├── SSH Keys
│   │   ├── 2FA QR Codes
│   │   └── Passwords
│   └── 📁 Admin Panel Settings
├── 📁 Payment Systems
│   ├── 📁 Exchanges
│   ├── 📁 Wallets
│   └── 📁 2FA Codes
└── 📁 Backups
```

---

### 7. ✅ Security Checklist

#### Verify Before Starting Work:

**Computer:**

* ✅ Antivirus is installed and updated.  
* ✅ An encrypted disk has been created.  
* ✅ All work data is stored on the encrypted disk.  
* ✅ Browser is configured (password saving disabled, protection enabled).  
* ✅ Minimal extensions are installed.  

**Accounts and Services:**

* ✅ 2FA is enabled everywhere possible.  
* ✅ Dedicated work phones are set up.  
* ✅ A work-specific Telegram account is created.  
* ✅ Strong passwords are set for all accounts.  

**Server:**

* ✅ 2FA is enabled for ROOT access.  
* ✅ 2FA is enabled for user access.  
* ✅ SSH keys are stored securely.  
* ✅ Passwords have been changed after setup.  

**General Rules:**

* ✅ Backups of the website and database are created.  
* ✅ All confidential data has been deleted from chats.  
* ✅ The "lock and key separate" rule is followed.  

---

### ⚠️ Common Mistakes and How to Avoid Them

#### Beginner Mistakes:

1. **Neglecting basic security** due to "inconvenience."  
2. **Using one device** for all functions.  
3. **Storing passwords in browsers** or unencrypted files.  
4. **Installing unnecessary extensions** for "convenience."  

#### Experienced User Mistakes:

1. **Overconfidence** leading to skipped security checks.  
2. **Occasional protocol violations.**  
3. **Using personal devices** for work tasks.  

---

### 🚨 In Case of a Security Breach

#### If Data is Compromised:

1. **Immediately change** all passwords.  
2. **Revoke access** to all services.  
3. **Check balances** on all wallets.  
4. **Create new wallets** if necessary.  
5. **Reinstall systems** from scratch.  

#### Remember:

* **Recovering stolen cryptocurrency is nearly impossible.**  
* **Investing time in security is better than losing funds.**  
* **Every protocol violation** is a potential risk of total loss.  