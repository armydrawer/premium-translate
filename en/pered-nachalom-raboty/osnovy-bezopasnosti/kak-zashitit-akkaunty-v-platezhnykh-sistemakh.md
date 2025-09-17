# How to Protect Accounts in Payment Systems

{% hint style="info" %}
_<mark style="color:red;">A</mark>_<mark style="color:red;">ctivating automatic payouts is done at your own risk. The script developer is not responsible for the safety of your funds in payment system accounts, although every effort has been made on their part to ensure their security. We strongly advise against enabling automatic payouts unless absolutely necessary. Active automatic payouts significantly increase the risk of losing your money in a given payment system in the event of a website or hosting/server breach where your site is hosted.</mark>
{% endhint %}

When setting up and connecting payment systems, it is crucial to exercise extreme caution. Pay special attention to the security of merchant keys, API passwords, and their safekeeping. A leak of this information could result in the theft of your funds.

We strongly recommend enabling all available identity verification measures for each payment system you connect, such as SMS authorization, SMS confirmation for transactions, email confirmation, IP address restrictions for API access and personal accounts, and so on. Each payment system has its own set of security features, so it’s a good idea to clarify these details directly with the technical support team of the respective system.

For payment systems, it is advisable to use a completely new mobile phone number specifically for SMS confirmations and to keep it anonymous—use it exclusively for SMS verification purposes.

If your website operates in automatic mode with operator confirmation, make use of the [security code](https://premium.gitbook.io/rukovodstvo-polzatelya/navigaciya/nastroiki/kod-bezopasnosti).