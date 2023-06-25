# wiki

Wiki
Спроєктуйте онлайн-енциклопедію, подібну до Вікіпедії.

Передумови
Вікіпедія – це безкоштовна онлайн-екнциклопедія, що складається з багатьох статей на різні теми.

Щоб переглянути кожну статтю енциклопедії, вам потрібно зайти на сторінку цієї статті. Зайшовши, наприклад, на https://en.wikipedia.org/wiki/HTML, ви побачите статтю, присвячену HTML. Зверніть увагу, що назву потрібної статті (HTML) вказано у маршруті /wiki/HTML. Зауважте також, що наповнення сторінки мусить бути в HTML, щоб його відобразив ваш браузер.

Насправді було би дуже стомливо писати кожну сторінку Вікіпедії в HTML. Натомість зручно було б зберігати статті енциклопедії за допомогою більш легкої та зручної мови розмітки. Вікіпедія використовує мову розмітки Wikitext, але ми зберігатимемо статті для цього проекту, використовуючи мову розмітки Markdown.

Прочитайте посібник з Markdown від GitHub, щоб зрозуміти, як працює синтаксис Markdown. Зверніть особливу увагу на те, як виглядає синтаксис Markdown для заголовків, шрифтових виділень, посилань та списків.

Представивши кожну енциклопедичну статтю окремим файлом Markdown, ми зробимо наші статті більш зручними для написання та редагування. Однак, коли користувач переглядатиме нашу статтю, ми повинні будемо конвертувати Markdown у HTML, перш ніж відображати її користувачу.

Перший крок
Завантажте вихідний код і розпакуйте його.
Пояснення
У у завантаженому коді знаходиться Django-проєкт під назвою wiki, в якому міститься один застосунок encyclopedia.

Спочатку відкрийте encyclopedia/urls.py, де визначено URL-конфігурацію для цього застосунку. Зверніть увагу, що ми вже надали вам один типовий маршрут, пов’язаний з функцією views.index.

Далі зазирніть до encyclopedia/util.py. Вам не потрібно буде нічого змінювати в цьому файлі, але зверніть увагу на три функції, які можуть стати в пригоді для взаємодії зі статтями енциклопедії. list_entries повертає список назв всіх збережених статей енциклопедії. save_entry зберігатиме нову статтю, отримавши її назву і Markdown- наповнення. get_entry шукатиме статтю за її назвою, повертаючи її Markdown-наповнення, якщо стаття існує, або None якщо стаття відсутня. Будь-які представлення, що ви напишете, можуть використовувати ці функції для взаємодії зі статтями енциклопедії.

Кожна стаття буде збережена як файл Markdown всередині директорії entries/. Якщо ви зайдете до неї зараз, ви побачити, що ми попередньо створили кілька статей для прикладу. Можете додати ще!

Тепер давайте зазирнемо до encyclopedia/views.py. . Зараз тут лише одне представлення – index. Це представлення повертає шаблон encyclopedia/index.html, надаючи йому список усіх статей енциклопедії (отриманих за допомогою util.list_entries, яку ми бачили визначеною в util.py).

Ви можете знайти цей шаблон, подивившись в encyclopedia/templates/encyclopedia/index.html. Цей шаблон наслідує від базового файлу layout.html і вказує, яким має бути заголовок сторінки і що має бути в тілі сторінки. В цьому випадку там буде маркований (невпорядкований) список усіх статей енциклопедії. layout.html, тим часом, визначає більш загальну структуру сторінки: у кожної сторінки є бічна панель з полем пошуку (яке поки не працює), посилання на головну сторінку і посилання (що поки теж не працюють) на створення нової сторінки чи відвідання випадкової сторінки.

Специфікація завдання
Завершіть реалізацію вашої енциклопедії Wiki з урахуванням наступних вимог:

• Сторінка статті: Перехід на /wiki/TITLE, де TITLE - це назва енциклопедичної статті, має відобразити сторінку, що показує вміст цієї статті.
Представлення має отримувати вміст статті за допомогою виклику відповідної функції util.
Якщо стаття, яку хоче відкрити користувач, не існує, йому має бути показана сторінка помилки, де буде зазначено, що потрібну статтю не знайдено.
Якщо стаття існує, користувач має побачити сторінку, що відображає вміст статті. Назва сторінки має містити назву статті.
Сторінка index: Змініть index.html так, щоб замість того, щоб побачити звичайний перелік назв усіх сторінок в енциклопедії, користувач міг натиснути на назву статті, щоб перейти безпосередньо на сторінку цієї статті.
Пошук: Дозвольте користувачу набрати запит у полі пошуку на бічній панелі, щоб відшукати статтю в енциклопедії.
Якщо запит збігається з назвою статті, користувач має бути направлений на сторінку цієї статті.
o Якщо запит не збігається з назвою статті, користувач має бути направлений на сторінку результатів пошуку, яка відображає список всіх статей енциклопедії, що містять цей запит в підрядку. Наприклад, якщо пошуковий запит був ytho, в результатах пошуку повинен з'явитися Python.
Натискання на будь-яку назву статті в результатах пошуку має переносити користувача на сторінку цієї статті.
Нова сторінка: Натискання на «Create New Page» на бічній панелі має переносити користувача на сторінку, де він зможе створити нову енциклопедичну статтю.
Користувач повинен мати змогу ввести назву сторінки і у textarea ввести Markdown-наповнення для сторінки.
Користувач повинен мати змогу натиснути кнопку для збереження своєї нової сторінки.
Коли сторінку збережено, у випадку, якщо енциклопедична стаття з наданою назвою вже існує, користувач має отримати повідомлення про помилку.
В іншому випадку енциклопедичну статтю має бути збережено на диск, а користувача треба перенести на сторінку цієї нової статті.
Редагування сторінки: На сторінці кожної статті користувач повинен мати можливість натиснути на посилання, що перенесе його на сторінку, де він зможе змінити Markdown-наповнення у textarea.
textarea має бути попередньо заповнена наявним Markdown-наповненням сторінки (іншими словами, наявний вміст має бути початковим значенням value у textarea).
Користувач повинен мати змогу натиснути кнопку, щоб зберегти впроваджені до статті зміни.
Після збереження статті користувача має бути перенаправлено назад на сторінку цієї статті.
Випадкова сторінка: Настискання на «Random Page» на бічній панелі має перенести користувача на випадкову статтю енциклопедії.
Конвертування Markdown у HTML: На сторінці кожної статті будь-яке Markdown-наповнення має бути конвертоване в HTML перед тим, як відобразити його для користувача. Щоб виконати це конвертування, ви можете використати пакет python-markdown2, який встановлюється за допомогою pip3 install markdown2.
Завдання для впевнених: якщо вам це до снаги, спробуйте впровадити конвертування Markdown у HTML без використання зовнішніх бібліотек зі збереженням заголовків, виділеного шрифту, маркованих списків, посилань та параграфів. Вам може допомогти використання регулярних виразів у Python.
