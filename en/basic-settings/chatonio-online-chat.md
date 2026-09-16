# Chatonio online-chat

[Chatonio](https://chatonio.com/) is a customer support service with a web chat and the ability to use AI to handle customer inquiries. Premium Exchanger provides a dedicated module for connecting the Chatonio widget to the website.

Once connected, the widget is displayed on the exchange website pages. The main chat settings - appearance, greeting, button position, knowledge base, operator settings, and other parameters - are configured in the Chatonio account. Premium Exchanger is responsible directly for connecting the widget to the website.

### 1. Creating a Project and Web Chat in Chatonio <a href="#ibbn56b33jcw" id="ibbn56b33jcw"></a>

1. Go to[ ](https://chatonio.com/)[chatonio.com](https://chatonio.com/) and register or sign in to your existing account.
2. In the Chatonio panel, create a project for your exchange website.
3. In the project, create a channel of the Web Chat type.
4. In the channel settings, specify the exchange website domain in the “URLs and domains” section.\
   <br>

<figure><img src="../.gitbook/assets/image (901).png" alt=""><figcaption></figcaption></figure>



The domain must be specified together with the website scheme, for example https://site.com.

After saving the settings, access from the new domain may take some time to become available.

&#x20;

### 2. Activating the Chatonio Module in Premium Exchanger <a href="#snvs5k3hz2l5" id="snvs5k3hz2l5"></a>

Activate the module in:

Modules → Modules

<figure><img src="../.gitbook/assets/image (916).png" alt=""><figcaption></figcaption></figure>

\
If you do not see the Chatonio module in the list of available modules, you will need to [update Premium Exchanger to the latest version](https://premium.gitbook.io/main/en/basic-settings/faq/updating-script-files-on-the-server/how-to-update-files-on-the-server#script-modules).

### 3. Getting the Chatonio Channel ID <a href="#id-96p8yjbz5i1" id="id-96p8yjbz5i1"></a>

Open the settings of the created web chat in your Chatonio account. In the **“Web Chat Widget”** section, select the **“ID Only”** tab and copy the entire contents of the **“Channel ID”** field.

<figure><img src="../.gitbook/assets/image (951).png" alt=""><figcaption></figcaption></figure>

### 4. Connecting Chatonio in Premium Exchanger <a href="#uktah7upxqxg" id="uktah7upxqxg"></a>

After activating the module, go to the exchange website admin panel:

Settings → General Settings

Find the Chatonio Channel ID field and paste the ID you copied earlier into it.

<figure><img src="../.gitbook/assets/image (936).png" alt=""><figcaption></figcaption></figure>

Save the changes.

{% hint style="info" %}
The Chatonio Channel ID field is multilingual. However, when using a single channel for the entire website, it is sufficient to specify the identifier in one language. It will be used across all language versions of the website.

Using separate Channel IDs for different languages makes sense if inquiries should be sent to different Chatonio channels, for example, to different operators.

If the Chatonio Channel ID field is left empty, the Chatonio widget will not be displayed on the website.
{% endhint %}

After saving the settings, open the exchange website and make sure that the chat button appears and that the chat opens correctly.

### 5. Configuring the Widget Appearance and Behavior <a href="#k2vll2rcyti" id="k2vll2rcyti"></a>

The appearance and behavior of the web chat are configured directly in your Chatonio account. In particular, you can configure:

* appearance and color scheme
* chat button position
* greeting
* operator and AI operation
* knowledge base
* widget visibility on specific URLs

{% hint style="info" %}
If another chat service, such as Jivo, is already used on the website, we recommend disabling it after connecting Chatonio. Otherwise, buttons for both services will be displayed on the website at the same time.
{% endhint %}

### Additional Settings <a href="#id-7zh7vthdmx7e" id="id-7zh7vthdmx7e"></a>

#### Light and Dark Theme <a href="#ju1nbvyruiw7" id="ju1nbvyruiw7"></a>

If the website uses a switch between light and dark themes, configure the corresponding widget color scheme in Chatonio.

<figure><img src="../.gitbook/assets/image (938).png" alt=""><figcaption></figcaption></figure>

#### Button Position <a href="#evvzeyrmnln7" id="evvzeyrmnln7"></a>

By default, the chat button may be located in the bottom-right corner of the page. If other website elements are already located in this area, change the button position or set the required offsets in the Chatonio settings.

<figure><img src="../.gitbook/assets/image (940).png" alt=""><figcaption></figcaption></figure>

#### Hiding the Chat on Specific Pages <a href="#id-1x41ocwx54f2" id="id-1x41ocwx54f2"></a>

To control the widget display on specific pages, use the URL visibility settings in the channel settings under “URLs and domains”.

<figure><img src="../.gitbook/assets/image (943).png" alt=""><figcaption></figcaption></figure>

There is no need to configure a separate exception for this in the Premium Exchanger admin panel.

&#x20;
