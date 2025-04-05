# 🎉 Events API

REST API для управления мероприятиями, тегами и категориями, построенный с использованием **FastAPI**, **SQLAlchemy**, **Alembic** и **PostgreSQL**.
Проект реализует архитектуру с применением паттернов Repository и Unit of Work (UoW) для управления взаимодействием с базой данных. 

---

## 📁 Структура проекта
```
.
├── alembic/                # Миграции Alembic
│   ├── versions/           # Файлы отдельных миграций
│   └── env.py              # Конфигурация окружения для Alembic
├── event_app/              # Исходный код приложения
│   ├── api/                # API-слой
│   │   ├── endpoins/       # Роутеры FastAPI
│   │   └── schemas/        # Pydantic-схемы
│   ├── core/               # Конфигурация и настройки проекта
│   ├── db/                 # Подключение к базе данных, декларация моделей
│   ├── repo/               # Реализация паттерна Repository для работы с БД
│   ├── services/           # CRUD-сервисы
│   └── utils/              # Реализация паттерна Unit of Work (UoW)
├── .env                    # Переменные окружения
├── alembic.ini             # Конфигурация Alembic
├── Dockerfile              # Инструкция сборки Docker-образа
├── docker-compose.yml      # Docker Compose для запуска
├── main.py                 # Точка входа в приложение
├── requirements.txt        # Зависимости проекта
└── README.md               # Документация проекта
```

---

## ⚙️ Установка локально

### 1. Клонируй репозиторий

```bash
git clone https://github.com/your-username/events-api.git
cd events-api
```

### 2. Создай и настрой .env файл

```
DB_HOST=localhost
DB_PORT=5432
DB_USER=postgres
DB_PASS=yourpassword
DB_NAME=events
```

### 3. Установи зависимости

```bash
python3 -m venv venv
source venv/bin/activate  # Для Windows используйте venv\Scripts\activate
pip install -r requirements.txt
```

### 4. Применить миграции

```bash
alembic upgrade head
```

### 5. Запуск

```bash
uvicorn main:app --reload
```

---

## 🧪 Примеры запросов

- GET /events/ — список мероприятий

- POST /events/ — создать мероприятие


Документация Swagger доступна по адресу:
```
http://localhost:8000/docs
```


