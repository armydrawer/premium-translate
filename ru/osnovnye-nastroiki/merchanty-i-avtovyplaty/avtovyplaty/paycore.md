# Paycore

{% hint style="danger" %}
Перед настройкой автовыплат обязательно прочитайте [предупреждение о рисках!](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/preduprezhdenie-o-riskakh)
{% endhint %}

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat)
{% endhint %}

## Настройки в личном кабинете мерчанта

{% hint style="warning" %}
Для обсуждения условий и подключения, свяжитесь с [представителем сервиса](https://t.me/Paycore_pw).

**Дисклеймер**: при подключении вашего сайта к тому или иному сервису, пожалуйста, самостоятельно оценивайте возможные риски сотрудничества.
{% endhint %}

После получения реквизитов для входа от [представителя сервиса](https://t.me/Paycore_pw), авторизуйтесь в [ЛК PayCore](https://paycore.pw/admin) и пройдите верификацию.\
После прохождения верификации запросите у представителя сервиса API-ключ для подключения.

## Настройки модуля

В панели администратора создайте нового мерчанта в разделе "**Мерчанты**" ➔ "**Добавить автовыплату".**

Выберите Paycore в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../.gitbook/assets/image (13).png" alt=""><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/image (2272).png" alt=""><figcaption></figcaption></figure>

**Домен** — оставьте поле пустым

**API ключ** — API ключ, выданный вам представителем Paycore

## Особые поля

При выплате средств с использованием мерчанта Finora **необходимо** использовать дополнительное поле в форме обмена для заполнения его клиентом при создании заявки.

В панели администратора в разделе "**Валюты**" ➔ выбрать нужную валюту ➔ "**Настройка полей**" необходимо произвести следующую настройку. Сохраните изменения.

{% hint style="success" %}
Номер РФ состоит из 12 символов с учетом знака "+" (Пример: +79991234567)
{% endhint %}

<figure><img src="https://premium.gitbook.io/main/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FA0q5PJ9k3a0GtMmZ4lYa%252F%25D0%25B8%25D0%25B7%25D0%25BE%25D0%25B1%25D1%2580%25D0%25B0%25D0%25B6%25D0%25B5%25D0%25BD%25D0%25B8%25D0%25B5.png%3Falt%3Dmedia%26token%3D3e7545f4-09c9-4d9d-a7e4-45e2a4581268&#x26;width=768&#x26;dpr=3&#x26;quality=100&#x26;sign=82144600&#x26;sv=2" alt=""><figcaption></figcaption></figure>

В инструкции в модуле автовыплаты обязательно добавьте шорткод "**Ссылка на оплату**" — это необходимо для отображения ссылки в заявке, по которой будет переходить клиент для выбора метода получения им средств и банка на платежной странице сервиса.

<figure><img src="../../../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>

После этого вставьте следующий блок текста в поле:

```html
<h2>Текст</h2>
<br>
<div style="text-align: center;">
<a href="{tx_url}" target="_blank" class="btn-new">Перейти к
подтверждению</a>
</div>
[else]
<h2>Текст</h2>
```

и скорректируйте текст, используя первый шорткод, чтобы в итоге получился формат:

```html
[if_url_xxxxxxxxxxxxxxxxxxxxxxxxxxxxx]
<h2>Ваш текст</h2>
<br>
<div style="text-align: center;">
<a href="{tx_url}" target="_blank" class="btn-new">Перейти к
подтверждению</a>
</div>
[else]
<h2>Текст</h2>
[/if_url_xxxxxxxxxxxxxxxxxxxxxxxxxxxxx]
```

<figure><img src="../../../.gitbook/assets/image (2271).png" alt=""><figcaption><p>Отображение вышеуказанного шаблона на странице заявки</p></figcaption></figure>

Также обязательно отметьте статус "**Ожидание подтверждения от модуля автовыплат**" в разделе "**Настройки обменника**" ➔ "**Настройки статуса**" — это необходимо для корректной работы модуля автовыплаты (если раздел не отображается в боковой панели — активируйте модуль "**Профессиональная настройка статусов**" в разделе "**Модули**", а затем проведите указанную настройку).

<figure><img src="../../../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>

## Порядок создания и проведения платежа <a href="#poryadok-sozdaniya-i-provedeniya-platezha" id="poryadok-sozdaniya-i-provedeniya-platezha"></a>

От клиента потребуется указать номер телефона, привязанный к банковскому счету,\
на который он собирается получить средства и сумму платежа.

<figure><img src="../../../.gitbook/assets/изображение (184).png" alt=""><figcaption></figcaption></figure>

После указания этих данных, клиенту необходимо нажать кнопку "**Создать платеж**". Следующий шаг – выбрать метод выплаты.

Небольшая справка по методам оплаты:

Банк ВТБ, Т-Банк, Сбер — прямой банковский шлюз (пополнение через приложение банка).

СБП QR — прием платежей со всех банков РФ.

<figure><img src="https://premium.gitbook.io/main/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FXfFadZg2BSIr04zqaBOS%252F%25D0%25B8%25D0%25B7%25D0%25BE%25D0%25B1%25D1%2580%25D0%25B0%25D0%25B6%25D0%25B5%25D0%25BD%25D0%25B8%25D0%25B5.png%3Falt%3Dmedia%26token%3D3ca00c46-ed0e-4f90-a81e-dbe26518e4ec&#x26;width=768&#x26;dpr=3&#x26;quality=100&#x26;sign=1fcd5861&#x26;sv=2" alt=""><figcaption><p>Страница с выбором метода оплаты</p></figcaption></figure>

После выбора нужного метода выплаты необходимо пройти верификацию. Верификация включает в себя 3 шага:

1. Фото главного разворота паспорта
2. Фото разворота с регистрацией (пропиской)
3. Селфи (без паспорта)

<figure><img src="https://premium.gitbook.io/main/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FtlS9aPyVCDjIRNZ14Pon%252F%25D0%25B8%25D0%25B7%25D0%25BE%25D0%25B1%25D1%2580%25D0%25B0%25D0%25B6%25D0%25B5%25D0%25BD%25D0%25B8%25D0%25B5.png%3Falt%3Dmedia%26token%3Ddb95c361-64b4-44c7-9e72-675dc6c60cc9&#x26;width=768&#x26;dpr=3&#x26;quality=100&#x26;sign=ec7b8432&#x26;sv=2" alt=""><figcaption><p>Страница верификации</p></figcaption></figure>

Для верификации можно сделать фотографии прямо в браузере или загрузить их из\
галереи.\
После успешно пройденной верификации – заявка будет выплачена с баланса ЛК.

## Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).<br>
