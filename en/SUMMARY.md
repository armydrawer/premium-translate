# Table of contents

* [Premium Exchanger Administrator Guide](README.md)
  * [Changelog](mainpage/changelog.md)

## Getting Started

* [Recommendations](pered-nachalom-raboty/rekomendacii/README.md)
  * [Choosing a Server](pered-nachalom-raboty/rekomendacii/vybor-servera.md)
  * [Recommendations from BestChange](pered-nachalom-raboty/rekomendacii/rekomendacii-ot-bestshange.md)
* [Security Basics](pered-nachalom-raboty/osnovy-bezopasnosti/README.md)
  * [General Security Measures](pered-nachalom-raboty/osnovy-bezopasnosti/obshie-mery-bezopasnosti.md)
  * [How to Avoid Scammers](pered-nachalom-raboty/osnovy-bezopasnosti/kak-ne-stat-zhertvoi-moshennika.md)
  * [Securing the Exchange Control Panel](pered-nachalom-raboty/osnovy-bezopasnosti/kak-obezopasit-panel-upravleniya-obmennikom.md)
  * [How to Protect the Server](pered-nachalom-raboty/osnovy-bezopasnosti/kak-zashitit-server.md)
  * [How to Secure Accounts in Payment Systems](pered-nachalom-raboty/osnovy-bezopasnosti/kak-zashitit-akkaunty-v-platezhnykh-sistemakh.md)
  * [Changing Passwords for Server Users](pered-nachalom-raboty/osnovy-bezopasnosti/smena-parolei-dlya-polzovatelei-servera.md)
  * [How to Password Protect a Website](pered-nachalom-raboty/osnovy-bezopasnosti/kak-zakryt-sait-parolem.md)
* [Script License](getting-started/script-license/README.md)
  * [Purchasing a License](getting-started/script-license/purchasing-a-license.md)
  * [Renewing a License](getting-started/script-license/renewing-a-license.md)
* [Script Installation Instructions](getting-started/script-installation-instructions.md)
* [Script Update Instructions](getting-started/script-update-instructions/README.md)
  * [Updating from Version 2.6 to 2.7](getting-started/script-update-instructions/updating-from-version-2.6-to-2.7.md)
  * [Updating from Version 2.5 to 2.6](getting-started/script-update-instructions/updating-from-version-2.5-to-2.6.md)
  * [Updating from Version 2.4 to 2.5](getting-started/script-update-instructions/updating-from-version-2.4-to-2.5.md)
  * [Updating from Version 2.3 to 2.4](getting-started/script-update-instructions/updating-from-version-2.3-to-2.4.md)
  * [List of Updates](getting-started/script-update-instructions/list-of-updates.md)

## Main Settings

Currencies and Exchange Directions
* Creating a New Currency
* Creating a New Exchange Direction
* Currency Exchange Rates
   * Currency Rates from File
   * Currency Rates Parser (Parsers 2.0)
   * Bestchange Parser (old)
   * Bestchange API Parser (new, starting from v2.6)
* Currency Reserves
   * Reserves from File
   * Reserves from Another Currency
      * Reserving Conversion when Using a Merchant
      * Examples of Setting Up Complex Reserves Using Formulas
   * Setting Manual Reserves for a New Currency
* Additional Fields
Verification
* Identity Verification (KYC)
* Payment Details Verification
* Email Confirmation
* Phone Number Confirmation
Appearance
* Exchange Directions Table Types
* Main Page Customization
* Client Dashboard
* Website and Admin Panel Translation
   * Adding a New Language
   * Editing Translation and Text Changes
* News on the Website
* "Requests" Section
* "Pages" Section
* Request Statuses
   * Text Templates in Requests
* "Site Rules", "AML/KYC/KYT Verification Rules" Pages
* "Giveaway" Page
* Website Notifications
Merchants and Auto Payouts
* Internal Accounts
   * Internal Account (Merchant Receiving Module)
   * Internal Account (Auto Payout Module)
   * Exchange Involving User's Internal Account
* Merchants
   * Merchant Diagnostics
   * Adding or Creating a Merchant Copy
   * General Merchant Settings
   * Using Own Cards/Wallets/Accounts
   * Various Merchant Platforms (ABCEx, Alfabit Crypto, ArchEx, etc.)
* Auto Payouts
   * Risk Warning!
   * Adding or Creating an Auto Payout Copy
   * General Auto Payout Settings
   * Various Auto Payout Platforms (ABCEx, Alfabit Crypto, Binance, etc.)
Trade Actions Module
* Installing the Trade Actions Module
   * General Module Settings
* Error Diagnostics
* Creating Trade Actions
   * Trade Action Parameters
   * Various Trade Actions Platforms (ABCEx, Beribit, Binance, etc.)
Electrum Module
* Installing and Configuring Electrum (2 Wallets)
* Using on Computer (Wallet Synchronization)
* Updating Electrum on Server (for version 4.3.3 and below)
* Creating Additional Wallet (for Auto Payout)
* Removing Electrum from Server
* Replacing Wallet on Server after Installing Electrum
* Installing and Configuring Electrum (old version)
Affiliate Program
* Partner Banners
* Earnings and Affiliate Percentage
AML Verification
* Configuration in v.2.7
* Configuration in v.2.6 and below
   * AMLBot
   * BitOK
   * CoinKyt
   * Getblock
Settings
* Request Archiving
* Bank Card Validator
* Cryptocurrency Wallet Validator
* Displaying Confirmation Count in Request
* Two-Factor Authentication (2FA) in Admin Panel
* X19 Interface (Webmoney)
* Nginx and PHP-FPM Configuration with ISP Manager
* Logging
   * Authorization Log
   * Merchant and Auto Payout Log
   * Parsers 2.0 Log
   * Server Error Log
   * Telegram Messages Log
   * Request Status Log
   * AML Log
   * API Log
   * Email Log
   * Trade Actions Log
   * Admin Actions Logging
   * Logging Settings
* Exchange Settings
* Control Panel Screen Settings
* General Settings
* Module Descriptions
   * Module Table
* Card Type Determination
* Security Passwords
* Website Operation via HTTPS Connection
* Unpaid Request Deletion Timer
* Website Functionality during Non-Working Hours
* Hooks
* Hash and Transaction Link
* Exchange Export and Exchange/Import of Exchange Directions and Currencies
* SEO
   * Google Tag Manager
Telegram Bot for Exchanges
* Bot Creation
* Bot Settings
* Diagnostics
Notifications to Admins and Clients
* Telegram Notifications
* Email Notifications
* SMS Notifications
Financial Statistics
FAQ
* Diagnosing and Resolving Errors when Working with the Script
* Adding IP Addresses to Cloudflare Whitelist
* Replacing SSH Authorization Keys on Server
* Changing Domain Name for License
* Restoring Access to Exchange Control Panel
* Changing Exchange Control Panel Address
* Changing Admin Password
* Finding Website Root Folder on Server
* Finding "Developer News" Section
* Transferring Website
* Checking Installed IonCube Version on Server
   * Updating ionCube Loader
* Updating Files on Server
* Updating WordPress
* Updating OpenSSH on Server
* Checking PHP Version Used for Website
   * Updating PHP
* Calculating Exchange Discount, Affiliate Reward
* Clearing Cache in Cloudflare
* Creating Website Backup
* Creating Cron Job on Server
* Installing Online Chat
* Installing Plugin
   * Working with Plugin Activation
* Requirements for Exchanges from Monitoring Services

* [Premium Exchanger API](api-premium-exchanger/README.md)
  * [API v1](api-premium-exchanger/api-v1.md)
  * [Affiliate Program API (old version of API)](api-premium-exchanger/api-partnerskoi-programmy-staraya-versiya-api.md)
