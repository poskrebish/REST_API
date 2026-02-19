# REST API на Flask

Простое REST API для управления задачами с функциями CRUD.

## Возможности
- **Получение всех задач** - GET /tasks
- **Получение одной задачи** - GET /tasks/{id}
- **Создание задачи** - POST /tasks
- **Обновление задачи** - PUT /tasks/{id}
- **Удаление задачи** - DELETE /tasks/{id}

## Технологии
- Python 3.8+
- Flask 2.3.3
- JSON для обмена данными

## Установка и запуск

1. **Клонируйте репозиторий:**
```bash
git clone https://github.com/poskrebish/REST_API.git
cd REST_API
```
2. **Установите зависимости:**
```bash
pip install -r requirements.txt
```
3. **Запустите сервер:**
```bash
python app.py
```
4. **Откройте в браузере:**
```bash
[python app.py](http://localhost:5000/tasks)
```

## Примеры использования
**Создать задачу (через curl)**
```bash
curl -X POST http://localhost:5000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Выучить REST API", "completed": false}'
```
**Создать задачу (через Python)**
```bash
import requests

response = requests.post(
    'http://localhost:5000/tasks',
    json={'title': 'Выучить REST API', 'completed': False}
)
print(response.json())
```
**Обновить задачу**
```bash
curl -X PUT http://localhost:5000/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"completed": true}'
```

## Статус-коды ответов
- 200 OK - Запрос выполнен успешно
- 201 Created - Задача создана
- 404 Not Found - Задача не найдена
