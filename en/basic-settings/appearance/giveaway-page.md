# "Giveaway" Page

The "Giveaway" module allows the administrator to set up and manage the promotional section of the contest on the currency exchange website. This section encourages users to leave feedback about the service by participating in weekly prize draws.

{% hint style="info" %}
How to work with the module:

1. **Activate the section**: Set the giveaway display to "show"
2. **Basic settings**: Fill in the title, description, and configure the participation button
3. **Set the timer**: Specify the end date for the current giveaway
4. **Statistics**: Update the number of reviews and the total prize pool
5. **Rules**: Edit the HTML content with detailed participation conditions
6. **Platforms**: Configure the list of recommended sites for reviews
7. **Save**: Click the "Save" button after making changes
{% endhint %}

To configure the text for the banner, go to "**Appearance**" ➔ "**Homepage**" ➔ "**Banners**".

<figure><img src="../../.gitbook/assets/image (2042)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

In the settings for the "**Giveaway**" page under the "**Pages**" section, make sure to select the appropriate template (Promo page template) for the page to display correctly.

<figure><img src="../../.gitbook/assets/image (2125) (1).png" alt="" width="253"><figcaption></figcaption></figure>

To set up the text on the Giveaway page (`https://your_domain/promo/`), go to "**Appearance**" ➔ "**Giveaway**".

<figure><img src="../../.gitbook/assets/image (2207) (1).png" alt="" width="563"><figcaption></figcaption></figure>

### **Displaying the Giveaway**

* **Function**: Enable/disable the giveaway section on the public website
* **Options**: `hide` / `show`
* **Action**: Select the desired option and click the **Save** button

### **Configuring Giveaway Content**

**Giveaway Title**

* Field for bilingual input (Russian/English)
* Example: "Leave a Review"
* Displayed as the main call to action

**Giveaway Description**

* Brief description of participation conditions
* Example: "Participate in the giveaway every week!"
* Supports both Russian and English languages

**Participation Button**

* **Button Link**: URL to the feedback form
* **Button Text**: Text on the button (Russian/English)
* **Image**: Path to the image for visual styling
  * Format: `/wp-content/themes/newexchanger2.0/images/promo/promo.svg`

### **Timer Settings**

**Timer Title**

* Text above the countdown
* Example: "Until the contest ends"
* Bilingual support

**End Date**

* Input format: `DD.MM.YYYY`
* Example: `16.11.2024`
* Automatic countdown to the specified date

### **Review Statistics Block**

**Reviews Block Title**

* Name of the section with statistics
* Example: "Reviews"

**Number of Reviews**

* Numeric field to display the current count
* Format: `00000` (five-digit number with leading zeros)

### **Prize Pool Block**

**Bank Block Title**

* Name of the section with prize information
* Example: "Contest Bank"

**Total Prize Amount**

* Display the total prize amount
* Format: `00000 ₽` (with currency indication)

### Advanced Settings

### **Giveaway Rules**

Block with an HTML editor for detailed description of participation conditions:

**Available HTML Tags**:

* `div`, `span`, `br`, `p` - structural elements
* `a` - links
* `img` - images
* `b`, `i`, `u`, `del` - text formatting
* `ul`, `ol`, `li` - lists
* `H2`, `H3` - headings

**Special Variables**:

* Anti-spam
* Text color
* Year
* Registration link
* Login link
* Image

**Example of Rules Structure**:

```
<h2>Winning money is very easy</h2>
<ul>
  <li><span>Make an exchange on our site</span> <a href="">Exchange</a></li>
  <li><span>Leave a review about our service, including your application number</span> <a href="" class="review">Leave a Review</a></li>
  <li><span>Check your email, open the message from BestChange, and activate your review by following the link</span></li>
</ul>
<p>You can check the giveaway results <a href="">on our Telegram channel</a>. You can participate in the giveaway an unlimited number of times! Good luck!</p>
<div>
  <p>Last week's winner</p>
  <p class="user_mail">p****rii@gmail.com</p>
</div>
```

### **List of Review Platforms**

HTML block with a list of recommended sites for posting reviews:

**Categories of Platforms**:

1. **Review Sites**:
   * mywot.com
   * trustpilot.com
   * webproverka.com
2. **Forums**:
   * mmgp.com
   * forum.bits.media
   * bitcointalk.org
3. **Monitoring Sites**:
   * kurs.expert
   * pro-obmen.ru

**List Structure**:

```
<h2>List of Platforms for Posting Reviews</h2>
<ul>
  <h3>Review Sites:</h3>
  <li><span>mywot.com</span><a href="domain">Leave a Review</a></li>
  <li><span>trustpilot.com</span><a href="domain">Leave a Review</a></li>
</ul>
```

Links should be inserted according to HTML markup rules in the [A](https://htmlbook.ru/html/A) tag within quotes.

```
Example:  <a href="https://your_domain/">Exchange</a>
```

<figure><img src="../../.gitbook/assets/brave_q2JReC6Ejm (1).png" alt="" width="563"><figcaption></figcaption></figure>

Also, don't forget to add the translated text in English.

<figure><img src="../../.gitbook/assets/image (2045)_eng.png" alt="" width="563"><figcaption></figcaption></figure>
