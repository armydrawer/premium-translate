# Adding a New Language

By default, Premium Exchanger only supports two languages: Russian and English.

You can also add new languages:

To do this, add the appropriate filter to the hooks plugin at the end of the file `wp-content/plugins/premiumhook/premiumhook.php`. In the "**Plugins**" section, activate the "**Premium Exchanger hooks**" plugin:

<figure><img src="../../../../ru/.gitbook/assets/Screenshot_52 (1).png" alt=""><figcaption></figcaption></figure>

Data is added according to the [ISO 3166-1](https://en.wikipedia.org/wiki/ISO_3166-1) standard.

After adding a language through the filter, additional input fields will appear in the admin panel. However, that’s not all—our plugin, theme, and WordPress still don’t recognize the new language, so all text will default to English.

You will need to download the translation program [Poedit](https://poedit.net/download).\
The program has two modes: paid and free. Either mode will work for our purposes, but the paid version allows you to automatically translate all strings from the file.

### Localization for WordPress (Basic WordPress Options)

1. Use any search engine to find the necessary WordPress version, for example, by searching for "WordPress in Kazakh." Download the appropriate distribution.
2. In the downloaded distribution, open the folder `wp-content/languages/` and copy the localization files to your site.

These files will have a prefix; for example, in the Kazakh version, they are:

* `kk_KZ.po`
* `kk_KZ.mo`
* `kk_KZ.php`

### Localization of the Premium Exchanger Theme (Client Side)

1. Open the theme folder: `wp-content/themes/your_theme_name/lang/`.
2. Download the files `ru_RU.po` and `ru_RU.mo`, then rename them to your prefix. You should end up with files named `kk_KZ.po` and `kk_KZ.mo`.
3. Open the `kk_KZ.po` file in Poedit.
4. Click on the line you want to translate. The original English text will appear on the left, and the text for your language version will appear on the right.
5. After making your changes, save the file and upload it to the folder mentioned above. Your theme is now localized.

### Localization of the Premium Exchanger Plugin (Admin Panel)

1. Open the plugin folder: `wp-content/plugins/premiumbox/languages/`.
2. Download the files `pn-ru_RU.po` and `pn-ru_RU.mo`, then rename them to your prefix. You should end up with files named `pn-kk_KZ.po` and `pn-kk_KZ.mo`.
3. Open the `pn-kk_KZ.po` file in Poedit.
4. Click on the line you want to translate. The original English text will appear on the left, and the text for your language version will appear on the right.
5. After making your changes, save the file and upload it to the folder mentioned above. The plugin is now localized as well.

### Localization of the Premium Exchanger Framework (Admin Panel)

1. Open the framework folder: `wp-content/plugins/premiumbox/premium/languages/`.
2. Download the files `pn-ru_RU.po` and `pn-ru_RU.mo`, then rename them to your prefix. You should end up with files named `pn-kk_KZ.po` and `pn-kk_KZ.mo`.
3. Open the `pn-kk_KZ.po` file in Poedit.
4. Click on the line you want to translate. The original English text will appear on the left, and the text for your language version will appear on the right.
5. After making your changes, save the file and upload it to the folder mentioned above. The framework is now localized as well.

After completing all these steps, add a flag icon with the appropriate prefix—`kk_KZ_eng.png` (make sure it’s in **\_eng.png** format) to the plugin section `wp-content/plugins/premiumbox/flags/`.

{% hint style="warning" %}
After adding new languages, be sure to check that the **Premium Exchanger hooks** plugin is activated in the **"Plugins"** section, or activate it if it has been disabled.\
![](<../../../../ru/.gitbook/assets/image (563) (1).png>)
{% endhint %}
