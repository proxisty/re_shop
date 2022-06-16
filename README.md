re_shop
====
Установка
----
#### 1)Установить виртуальное окружение:

virtualenv venv

cd venv

.\Scripts\activate

cd ..

pip install -r requirements.txt

#### 2) Создать базу данных postgresql. Пример через psql:

create database remii;

create user remiii_user WITH PASSWORD 'remii';

ALTER ROLE remii_user SET client_encoding TO 'utf8';

ALTER ROLE remii_user SET default_transaction_isolation TO 'read committed';

ALTER ROLE remii_user SET timezone TO 'Asia/Vladivostok';

GRANT ALL PRIVILEGES ON DATABASE remiii TO remii_user;

#### 3) Мигразия и импорт данных

python manage.py migrate

python manage.py loaddata db.json

Данные для входа:
#### 1) Вход по http://127.0.0.1:8000/admin/ . Логин: remii; Пароль: remii
#### 1) Вход по http://127.0.0.1:8000/store . Почта: proxy_none@mail.ru; Пароль: gbajynbq176
----
Выполнено:
----
#### 1) каталог (иерархическое дерево категорий)
Использована библиотека django-mptt в моделе category
![image](https://user-images.githubusercontent.com/42601425/173991351-f8681129-8359-493e-84da-d336d80fe188.png)
#### 2) товар связанный с категорией каталога, например с изображением и «спецификацией» (Filefield)
Товар (модель product) связан с моделью category. Есть возможность выбирать товары по категориям.
#### 3) корзина \ заказ набор товаров, изменение статусов заказов, завершение
Логика: Пользователь логинится -> добавляет товары -> Заходит в корзину и регистрирует товар -> Администратор через админ панель меняет статус заявки
![image](https://user-images.githubusercontent.com/42601425/173993460-38763acf-80f7-426c-869c-efe63fc670fa.png)
![image](https://user-images.githubusercontent.com/42601425/173993515-16f2c6b9-84e3-4496-8b02-ca565a2604eb.png)
![image](https://user-images.githubusercontent.com/42601425/173993581-7b89484d-fd54-4686-be33-9f9e7da834c2.png)
![image](https://user-images.githubusercontent.com/42601425/173993728-c244ff90-d4e4-43dc-932e-6111be2d1ad1.png)
![image](https://user-images.githubusercontent.com/42601425/173993797-c1c111cc-13b3-4bca-9b4a-56f810f07c96.png)
#### 4) - промо абстракция для объединения между собой товаров в “акцию”, с дополнительными условиями.
Реализована модель с методами в discount.py и отображением в админ окне. Но не реализован gui для пользователя
![image](https://user-images.githubusercontent.com/42601425/173994020-5c28cd9e-76a8-44df-a513-0f2f6428fef7.png)
#### 4) Представления Class / Function Based View; Бизнес логику вынести в модели, или в отдельные модули на уровне моделей. Минимизировать ее во view; Пара форм, с нестандартной инициализацией или валидацией; Добавить модели в админку, подобрать кастомные представления (в списке), фильтры, поиск, сортировку — по смыслу моделей. Например для заказа полезно будет кол-во товаров, для категории товары внутри, а для товара действующая акция / акции на товар.
Выполнено
#### 4) Написать миграцию данных, на «несуществующую проблему», и обратную миграцию; Далее как бонусы, в свободной форме для демонстрации возможностей, жирным выделил наиболее интересные с точки зрения django.
Не выполнено





