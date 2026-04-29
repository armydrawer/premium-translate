# PayPlay

{% hint style="danger" %}
<mark style="color:red;">Перед настройкой автовыплат обязательно прочитайте</mark> [<mark style="color:blue;">предупреждение о рисках</mark>](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/preduprezhdenie-o-riskakh)<mark style="color:blue;">!</mark>
{% endhint %}

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat)
{% endhint %}

## Настройки в личном кабинете мерчанта

{% hint style="warning" %}
Для обсуждения условий и подключения, свяжитесь с [представителем сервиса](https://t.me/am_payplay).

**Дисклеймер**: при подключении вашего сайта к тому или иному сервису, пожалуйста, самостоятельно оценивайте возможные риски сотрудничества.
{% endhint %}

Зарегистрируйтесь на сервисе PayPlay с помощью представителя сервиса и авторизуйтесь в личном кабинете мерчанта.

## Настройки модуля

В панели администратора создайте нового мерчанта в разделе "**Автовыплаты**" ➔ "**Добавить автовыплату".**

Выберите PayPlay в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../.gitbook/assets/изображение (3) (1).png" alt=""><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/изображение (2) (1).png" alt=""><figcaption></figcaption></figure>

**Домен** — оставьте поле пустым

**API ключ** — API ключ, отображаемый в настройках ЛК PayPlay

<figure><img src="https://premium.gitbook.io/main/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FNZSV6TzmYmXOsEsIfx2M%252F%25D0%25B8%25D0%25B7%25D0%25BE%25D0%25B1%25D1%2580%25D0%25B0%25D0%25B6%25D0%25B5%25D0%25BD%25D0%25B8%25D0%25B5.png%3Falt%3Dmedia%26token%3D2556172d-e1f8-4af1-a4c3-ae6c84c0bca9&#x26;width=768&#x26;dpr=3&#x26;quality=100&#x26;sign=3f3877&#x26;sv=2" alt="" width="563"><figcaption></figcaption></figure>

**Slug** — ID платежной страницы, отображаемый в ЛК PayPlay

<figure><img src="https://premium.gitbook.io/main/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FPIVatFPaHcf3qvT9Dr3z%252F%25D0%25B8%25D0%25B7%25D0%25BE%25D0%25B1%25D1%2580%25D0%25B0%25D0%25B6%25D0%25B5%25D0%25BD%25D0%25B8%25D0%25B5.png%3Falt%3Dmedia%26token%3D19a11c12-1a38-4ecb-aca4-5b62992e41fe&#x26;width=768&#x26;dpr=3&#x26;quality=100&#x26;sign=13a2a2f8&#x26;sv=2" alt="" width="563"><figcaption></figcaption></figure>

Обратите внимание, что для модуля автовыплаты необходимо указывать ссылку для вебхука для корректной проверки выплаты по заявке. Скопируйте ссылку в настройках модуля автовыплаты

<figure><img src="../../../.gitbook/assets/изображение.png" alt=""><figcaption></figcaption></figure>

и вставьте её в указанное на скриншоте ниже поле в настройках ЛК PayPlay

<figure><img src="../../../.gitbook/assets/изображение (5).png" alt="" width="563"><figcaption></figcaption></figure>

После сохранения вебхука обязательно выберите методы для работы с ним и сохраните изменения.

<figure><img src="../../../.gitbook/assets/изображение (4).png" alt="" width="540"><figcaption></figcaption></figure>

## Особые поля

<figure><img src="../../../.gitbook/assets/изображение (1) (1).png" alt="" width="476"><figcaption></figcaption></figure>

**Код валюты** — выберите необходимый способ для выплаты средств клиенту

* **Доп. поля** — использование кода валюты, указанного в [доп.поле](https://premium.gitbook.io/main/osnovnye-nastroiki/valyuty-i-napravleniya-obmena/dopolnitelnye-polya#dopolnitelnye-polya-dlya-valyuty) для валюты "**Получаю**" или в направлении обмена или [доп.поля для направления обмена](https://premium.gitbook.io/main/osnovnye-nastroiki/valyuty-i-napravleniya-obmena/dopolnitelnye-polya#dopolnitelnye-polya-dlya-napravleniya-obmena)
* **Коды валют** — выбор кода валюты вручную (в этом случае модуль будет работать только с указанной валютой)

<figure><img src="../../../.gitbook/assets/изображение (3).png" alt="" width="462"><figcaption></figcaption></figure>

**Сеть** — выберите подходящую сеть для валюты выплаты

* **Доп. поля** — использование кода валюты, указанного в [доп.поле](https://premium.gitbook.io/main/osnovnye-nastroiki/valyuty-i-napravleniya-obmena/dopolnitelnye-polya#dopolnitelnye-polya-dlya-valyuty) для валюты "**Получаю**" или в направлении обмена или [доп.поля для направления обмена](https://premium.gitbook.io/main/osnovnye-nastroiki/valyuty-i-napravleniya-obmena/dopolnitelnye-polya#dopolnitelnye-polya-dlya-napravleniya-obmena)
* **Коды валют** — выбор кода валюты вручную (в этом случае модуль будет работать только с указанной валютой)

## Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-merchantov-avtovyplat).<br>
