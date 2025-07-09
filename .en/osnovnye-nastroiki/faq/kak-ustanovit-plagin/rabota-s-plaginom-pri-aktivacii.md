# Working with the Plugin on Activation

Place the hook code at the end of the file `wp-content/plugins/premiumhook/premiumhook.php`. Then, in the **Plugins** section, activate the plugin called **Premium Exchanger hooks**.

When you activate the plugin, several important actions take place. One of these is the creation of pages in your site's database.

There is a useful hook triggered upon plugin activation:

```
do_action('pn_plugin_activate');
```

You can use this hook to run your own custom actions.

For example, if you want to send an email when the plugin is activated, create a hook in our hooks plugin like this:

```
add_action('pn_plugin_activate', 'myhook_pn_bd_activated');
function myhook_pn_bd_activated() {

    // Your action to perform on plugin activation

}
```

If you want to send yourself an email every time the plugin is activated, add a mail-sending function inside the hook:

```
add_action('pn_plugin_activate', 'myhook_pn_bd_activated');
function myhook_pn_bd_activated() {

    wp_mail('test@mail.ru', 'Test title', 'Test content');

}
```

Now, each time the plugin is activated, you will receive an email notification.