# Working with the Plugin During Activation

The hook code needs to be placed at the end of the file `wp-content/plugins/premiumhook/premiumhook.php`. In the "**Plugins**" section, you need to activate the "**Premium Exchanger hooks**" plugin.

When you activate the plugin, several important actions take place. One of these is the creation of pages in your website's database.

During plugin activation, there is a useful hook available:

```php
do_action('pn_plugin_activate');
```

This hook allows you to execute your own custom actions.

For example, if you want to send an email upon activation, you can create a hook in our plugin like this:

```php
add_action('pn_plugin_activate', 'myhook_pn_bd_activated');
function myhook_pn_bd_activated() {

    // Your custom action upon plugin activation

}
```

For instance, if you want to send yourself an email every time the plugin is activated, you can include a mail-sending function within the hook:

```php
add_action('pn_plugin_activate', 'myhook_pn_bd_activated');
function myhook_pn_bd_activated() {

    wp_mail('test@mail.ru', 'Test title', 'Test content');

}
```

Now, every time the plugin is activated, you will receive an email notification.