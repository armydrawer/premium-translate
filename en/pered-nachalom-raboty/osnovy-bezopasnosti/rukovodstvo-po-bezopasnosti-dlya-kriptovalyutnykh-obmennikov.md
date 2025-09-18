---
layout:
  width: default
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
---

# Security Guide for Cryptocurrency Exchanges

{% hint style="warning" %}
### ⚠️ IMPORTANT: Security is Priority #1

**The main rule**: Set up all security measures first, check all systems, and only then start operating the exchange. **Security is more important than convenience.**

_Security is not paranoia; it is a necessity in the cryptocurrency space. Follow all recommendations strictly._\
\
The recommendations in this article are based on 10 years of experience as an exchange administrator, who also leads our training program.
{% endhint %}

***

### 1. 🖥️ Computer/Laptop Security

#### Basic Principles for Working with a Computer:

* ❌ **DO NOT visit** suspicious websites
* ❌ **DO NOT download** unknown software
* ✅ Use the computer **only for work**
* ✅ It is recommended to use **macOS** (a more secure system)

#### Antivirus Protection:

**Recommended Antivirus:** It is advisable to use a paid antivirus with **data encryption features**. Examples include ESET NOD32, Kaspersky Internet Security, or Dr. Web. The key is to have **the necessary features for information protection**.

* ⚠️ **Important**: Purchase the license only through VPN/proxy (not from a Russian IP)
* When buying NOD32, avoid the Russian version PRO32 (less reliable)

**Disk Encryption:**

1. **Create an encrypted disk** using the antivirus
2. **Store ALL work data** only on the encrypted disk
3. **DO NOT store** data on regular Windows disks
4. Create **backup copies** on encrypted USB drives

#### Working with USB Drives:

1. **Always format** new flash drives before use
2. Format on a **separate computer** (not the work one)
3. **Encrypt** the flash drives with the same antivirus
4. ⚠️ **Danger**: Even new flash drives can contain viruses

***

### 2. 🌐 Browser Configuration

#### Mandatory Security Settings:

**Disable:**

* ❌ Password manager
* ❌ Auto-save passwords
* ❌ Payment methods
* ❌ Automatic login
* ❌ ALL extensions (except those necessary for work)

**Enable:**

* ✅ **Enhanced protection** in the "Security" section
* ✅ All available privacy features

**Extensions:**

* **Minimum extensions** (only VPN for work, if necessary)
* **DO NOT install** even official extensions without extreme necessity
* The only exception: programs for working with documents (PDF)

***

### 3. 🔐 Payment System Security

#### Two-Factor Authentication (2FA):

**Mandatory for all services:**

* **Exchanges and wallets:** Maximum security levels must be set for all used services, including two-factor authentication (2FA) via an app (e.g., Google Authenticator) and linking to an email/phone number.
* **Email**: 2FA via phone or authenticator

**"Lock separately, key separately" rule:**

* **DO NOT use** 2FA on the same device where the wallet is open
* **Different devices** for different security functions
* **Separate work phones** only for 2FA

#### Work Phones:

* **At least 1-2 separate** work phones
* **DO NOT use** for personal calls/messages
* **Do not share** work phone numbers with anyone
* You can **replace the number** in existing services with the work number

***

### 4. 🖥️ Server and Admin Panel Security

#### Server Access:

**SSH Keys:**

* **DO NOT store** access keys on the desktop
* Store keys on a **encrypted disk** or **separate flash drive**
* **DO NOT share** keys with anyone (except trusted technical specialists)
* When sending keys via Telegram: **immediately delete** messages after the recipient has read them

**Setting up 2FA for the server:**

1. **Enable 2FA** for ROOT access
2. **Enable 2FA** for user access
3. **Save QR codes** and keys on an encrypted medium
4. **Change passwords** after training is completed

#### Password Requirements:

* **Minimum 15 characters**
* **Uppercase and lowercase Latin letters**
* **Numbers**
* **At least 1-2 special characters** (`@, #, !`, etc.)

***

### 5. 📧 Telegram and Email Security

#### Setting Up Work Telegram:

* **Separate installation** only for work
* **2FA enabled**
* **Code words** configured
* **Installed on work phone and laptop**

#### Transmitting Confidential Information:

1. **Transmit information only** to trusted technical specialists
2. **Immediately delete** files after the recipient has read the message
3. **Delete messages from both your and the recipient's accounts**
4. **DO NOT leave** passwords in message history

#### Work Email:

* **Separate email** only for work
* **Use a reliable email service for work** (the email will be used for **sending notifications from the server**). Suitable options include Gmail, ProtonMail, or Yandex.Mail.
* **2FA via phone** is mandatory

***

### 6. 📋 Data Storage Structure

#### Recommended File Structure:

```
📁 Work (on encrypted disk)
├── 📁 Server
│   ├── 📁 Server Access
│   │   ├── SSH Keys
│   │   ├── 2FA QR Codes
│   │   └── Passwords
│   └── 📁 Panel Settings
├── 📁 Payment Systems
│   ├── 📁 Exchanges
│   ├── 📁 Wallets
│   └── 📁 2FA Codes
└── 📁 Backups
```

***

### 7. ✅ Security Checklist

#### Before Starting Work, Check:

**Computer:**

* ✅ Antivirus is installed and updated
* ✅ An encrypted disk has been created
* ✅ All work data is on the encrypted disk
* ✅ Browser is configured (password saving disabled, protection enabled)
* ✅ Minimum extensions

**Accounts and Services:**

* ✅ 2FA is enabled everywhere possible
* ✅ Separate work phones are set up
* ✅ Work Telegram is created
* ✅ Strong passwords are set everywhere

**Server:**

* ✅ 2FA for ROOT access
* ✅ 2FA for user access
* ✅ SSH keys are stored in a secure location
* ✅ Passwords changed after training

**General Rules:**

* ✅ Backups of the site and database are created
* ✅ All confidential data is deleted from chats
* ✅ The "lock separately, key separately" rule is followed

***

### ⚠️ Common Mistakes and How to Avoid Them

#### Novice Mistakes:

1. **Neglecting basic security** due to "inconvenience"
2. **Using one device** for all functions
3. **Storing passwords in the browser** or unencrypted files
4. **Installing unnecessary extensions** "for convenience"

#### Experienced User Mistakes:

1. **Overconfidence** and skipping checks
2. **One-time violations** of security protocols
3. **Using personal devices** for work tasks

***

### 🚨 In Case of an Incident

#### If a Data Breach Occurs:

1. **Immediately change** all passwords
2. **Revoke access** to all services
3. **Check balances** of all wallets
4. **Create new wallets** if necessary
5. **Reinstall** systems from scratch

#### Remember:

* **Recovering stolen cryptocurrency is nearly impossible**
* **It's better to spend time on security than to lose funds**
* **Every protocol violation** is a risk of total loss
