# FPY_Diplom_My_cloud
Дипломный проект по профессии «Fullstack-разработчик на Python»

Запуск

Создайте виртуальное окружение
(В программе VSCode комбинация клавиш Ctrl+Shirft+P. В строке поиска наберите 
Python: Create Environment и выберите "Venv Creates .venv virtual environments in current workspace
Появится предложение сразу же установить зависимости из файла requirements.txt в виртуальное окружение,
соглашаемся и шаг с установкой зависимостей можно пропустить
)

python -m venv .venv

Активируйте его

.venv/Scripts/activate

Установите зависимости

pip install -r requirements.txt

либо используйте (установите при необходимости) pipenv

pip install pipenv

и установите зависимости из файла Pipfile

pipenv install




Что сделано...
Установлены Django и React
Установка и подключение БД PostgreSQL myclouddb
Скрестил Django и React на одном порту.
Создал первичные тестовые модели "Пользователи" и "Файлы". Связь один-ко-многим 