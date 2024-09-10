
# Запросы и ответы

- Создание пользователя `POST /users/create`

Request example:
```json
{
  "first_name": "string",
  "last_name": "string",
  "email": "string",
  "sport": "string"
}
```

Response example:
```json
{
  "id": "number",
  "first_name": "string",
  "last_name": "string",
  "email": "string",
  "contests": [
  	"number",
    ...
  ]
}
```

- Получение данных по определенному пользователю `GET /users/<user_id>`

Response example:
```json
{
  "id": "number",
  "first_name": "string",
  "last_name": "string",
  "email": "string",
  "contests": [
  	"number",
    ...
  ]
}
```

- Создание соревнования `POST /contests/create`

Request example:
```json
{
  "name": "string",
  "sport": "string",
  "participants": [
  	"number",
    "number"
  ]
}
```

Response example:
```json
{
  "id": "number",
  "name": "string",
  "sport": "string",
  "status": "STARTED",
  "participants": [
  	"number",
    "number"
  ],
  "winner": null
}
```

- Получение данных по определенному соревнованию `GET /contests/<contest_id>`

Response example:
```json
{
  "id": "string",
  "name": "string",
  "sport": "string",
  "status": "string",
  "participants": [
  	"number",
    "number"
  ],
  "winner": "number"
}
```

- Завершает соревнование `POST /contests/<contest_id>/finish`

Request example:
```json
{
  "winner": "number"
}

Response example:
```json
{
  "id": "string",
  "name": "string",
  "sport": "string",
  "status": "FINISHED",
  "participants": [
  	"number",
    "number"
  ],
  "winner": "number"
}
```

- Получение соревнований конкретного пользователя `GET /users/<user_id>/contests`

Response example:
```json
{
  "contests": [
  	{
    	"id": "string",
        "name": "string",
        "sport": "string",
        "status": "FINISHED",
        "participants": [
          "number",
          "number"
  		],
  		"winner": "number"
    }
    {
    	...
    }
  ],
}
```

- Генерирует список пользователей, отсортированному по количеству соревнований `GET /users/leaderboard`

Значение `asc` обозначет `ascending` (по возрастанию), параметр `desc` обозначет `descending` (по убыванию)

Request example:
```json
{
  "type": "list",
  "sort": "asc/desc"
}
```

Response example:
```json
{
  "users": [
    {
      "id": "number",
      "first_name": "string",
      "last_name": "string",
      "email": "string",
      "contests": [
        "number",
        ...
      ]
    },
    {
    	...
    }
  ],
}
```

- Получение графика пользователей по количеству соревнований `GET /users/leaderboard`

Request example:
```json
{
  "type": "graph",
}
```

Response example:
```html
<img src="path_to_graph">
```

- Объекты храняться в runtime
