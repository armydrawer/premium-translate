# FireKassa Card/Link

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере - воспользуйтесь [инструкцией](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-merchantov)
{% endhint %}

## Настройки в личном кабинете мерчанта

Пройдите регистрацию на сайте [Vanilapay](https://web.vanilapay.com/) (при работе с RUB) или на сайте [Gamepay](https://web.gampay.cc/) (при работе с UAH).

Зайдите в личный кабинет, раздел "**Сайты**" -> "**Список сайтов**" и добавьте новый сайт.

<figure><img src="../../../.gitbook/assets/image (749).png" alt=""><figcaption></figcaption></figure>

Заполните указанные поля, кроме "**URL уведомлений**" и "**URL уведомлений для выплат**" и нажмите "**Добавить**".

<figure><img src="../../../.gitbook/assets/image (750).png" alt="" width="563"><figcaption></figcaption></figure>

В открывшемся окне перейдите на вкладку "**API**".

<figure><img src="../../../.gitbook/assets/image (751).png" alt=""><figcaption></figcaption></figure>

Обновите **API Bearer Token** и **API Sign Token**, нажав **"Изменить"** на каждой строке поочередно.

<figure><img src="../../../.gitbook/assets/image (752).png" alt=""><figcaption></figcaption></figure>

Скопируйте ключи и сохраните их в текстовый файл.

## Настройки модуля

В панели администратора создайте нового мерчанта в разделе "**Мерчанты**" -> "**Добавить мерчант".**

*   **FireKassa Card** — если вы хотите, чтобы номер кошелька/карты выдавался непосредственно на вашем сайте.\


    <figure><img src="../../../.gitbook/assets/image (753).png" alt=""><figcaption><p>Firekassa Card</p></figcaption></figure>
*   **FireKassa Link** — если вы хотите, чтобы пользователь переходил к оплате на сайт платежной системы.\


    <figure><img src="../../../.gitbook/assets/image (754).png" alt=""><figcaption><p>Firekassa Link</p></figcaption></figure>

{% hint style="info" %}
Для обоих вариантов формата оплаты действуют лимиты на стороне мерчанта, которые следует уточнить у технической поддержки FireKassa.
{% endhint %}

Выберите подходящий модуль в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/image (1421).png" alt=""><figcaption></figcaption></figure>

**API url** — укажите URL сервиса, с которым будете работать:\
• **https://admin.gampay.cc** — при работе с UAH (альтернативный URL - **https://web.gampay.cc)**\
• **https://admin.vanilapay.com** — при работе с RUB (альтернативный URL - **https://web.vanilapay.com)**

**API ключ** — **API Bearer Token** из личного кабинета Firekassa

**Секретный ключ** — **API Sign Token** из личного кабинета Firekassa

### Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).

## Особые поля

**Тип (Firekassa Card):**

<figure><img src="../../../.gitbook/assets/image (649).png" alt=""><figcaption></figcaption></figure>

* **Тип** — выбор банка для приема средств (RUB, UAH)

{% hint style="warning" %}
Список банков и платежных систем для этой опции подгружается по API от мерчанта — если какого-то типа не хватает, обратитесь к мерчанту за его включением
{% endhint %}

### **Выполнение требований Firekassa**

Требование мерчанта — передача номера телефона клиента, который он должен вводить в форме обмена. Для этого в настройках направления (вкладка "**Доп. поля**") установите галочку напротив поля "**Телефон**" (убедитесь, что поле обязательно для заполнения — в форме обмена должна отображаться <mark style="color:red;">красная звездочка</mark> для этого поля)

<figure><img src="../../../.gitbook/assets/изображение (43).png" alt="" width="563"><figcaption></figcaption></figure>

После этого поле для ввода номера телефона будет отображаться в форме обмена для этого направления.

<figure><img src="../../../.gitbook/assets/изображение (63).png" alt="" width="349"><figcaption></figcaption></figure>
