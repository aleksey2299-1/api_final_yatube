## API публикации

Доступ к публикациям пользователей и возможностью подписки через API.
Аутентификация осуществляется через Bearer token.


### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

`git clone git@github.com:aleksey2299-1/api_final_yatube.git
cd api_final_yatube`

Cоздать и активировать виртуальное окружение:

`python3 -m venv env
source env/bin/activate
python3 -m pip install --upgrade pip`

Установить зависимости из файла requirements.txt:

`pip install -r requirements.txt`

Выполнить миграции:

`python3 manage.py migrate`

Запустить проект:

`python3 manage.py runserver`


### Как начать?

Посмотреть все публикации: `localhost:8000/api/v1/posts/`

Конкретная публикация: `localhost:8000/api/v1/posts/<номер_поста>/`


Посмотреть все комментарии к посту: `localhost:8000/api/v1/posts/<номер_поста>/comments/`

Конкретнай комментарий к посту `localhost:8000/api/v1/posts/<номер_поста>/comments/<номер_комментария>/`


Посмотреть все группы: `localhost:8000/api/v1/groups/`

__Чтобы самому создавать посты, комментарии и подписываться на авторов нужно зарегистрироваться:__

`localhost:8000/api/v1/users/` в теле запроса передать username и password

`localhost:8000/api/v1/jwt/create/` получить token

`localhost:8000/redoc/` остальная документация и примеры запросов API
