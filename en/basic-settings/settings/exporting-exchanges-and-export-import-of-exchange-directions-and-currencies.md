# Exporting Exchanges and Export/Import of Exchange Directions and Currencies

{% hint style="warning" %}
All imported files must use the [**Windows-1251**](https://ru.wikipedia.org/wiki/Windows-1251) encoding. Otherwise, the files will not be recognized during import, and the information will not be saved on the server.

Please use the same encoding (Windows-1251) and data separators (semicolon) as in the files exported from the section.

<img src="../../.gitbook/assets/image (839) (1).png" alt="" data-size="original">
{% endhint %}

You can activate the "**Export/Import**" module in the site management panel under "**Modules" → "Modules"**.

## Exporting Exchanges

In the management panel under "**Modules" → "Export Exchanges"**, you can:

<figure><img src="../../.gitbook/assets/image (1061)_eng.png" alt=""><figcaption></figcaption></figure>

* Export (download) all exchanges created in your exchange platform to a CSV file. You can open the CSV file using Microsoft Excel, for example.

## **Export/Import of Exchange Directions**

In the management panel under "**Modules" → "Export/Import Exchange Directions"**, you can:

<figure><img src="../../.gitbook/assets/image (1002)_eng.png" alt=""><figcaption></figcaption></figure>

* Export (download) all exchange directions created in your exchange platform to a CSV file. You can open the CSV file using Microsoft Excel, for example.
* Import (upload) exchange directions from a CSV file into your exchange platform.

{% hint style="danger" %}
The CSV file must adhere to a specific structure. Export your previously created currencies/exchange directions as an example of the CSV file.

One of the parameters in the file is the ID — this is the internal number of the currency/exchange direction in your exchange platform.

* If the ID in the CSV file matches the ID in the exchange platform during import, the data for those currencies/directions will be overwritten with the values specified in the file for that ID.
* If the file contains IDs for currencies/directions that do not yet exist in the exchange platform, new IDs will be assigned to those directions from the file (for example, if the highest ID in the exchange platform was 350, the currencies/directions from the file will be assigned IDs 351 and so on).

If your goal is to update existing exchange directions in the exchange platform, the IDs in the file and the exchange platform must match.

If your goal is to create new exchange directions in the exchange platform, the IDs in the file must be unique.
{% endhint %}

{% hint style="info" %}
When importing a CSV file, it is not technically possible to pass the following parameters in the file: "**Exchange Completion Time, Exchange Description, Payment Instructions, Information After Payment Confirmation, Information After Payment Completion, and others**".

For each new exchange direction created, the values of these parameters will automatically be set to those specified in the "**Exchange Directions"** → "**Exchange Direction Templates"** section.
{% endhint %}

{% hint style="info" %}
If the CSV file contains currency names that were not previously in your exchange platform, they will be created automatically. For existing currencies, the names used in the CSV file must match those in your exchange platform.
{% endhint %}

## **Export/Import of Currencies**

In the site management panel under "**Modules" → "Export/Import Currencies"**, you can:

<figure><img src="../../.gitbook/assets/image (968) (1).png" alt=""><figcaption></figcaption></figure>

* Export (download) all currencies created in your exchange platform to a CSV file. You can open the CSV file using Microsoft Excel, for example.
* Import (upload) currencies from a CSV file into your exchange platform.
