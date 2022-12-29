# kopeyka-coin
 Самостабилизирующаяся криптовалюта на алгоритмах POS и POW


## Сервер TCP

Сервер принимает от клиента данные в формате JSON.
Пример:
```json
{
    "action": "status"
}
```
Ответ сервера:
```json
{
    "status": 200, 
    "message": "I'm OK", 
    "blocks": 1
}
```

### Действия

- status
- lastblock
- exit
- get_user
- get_task
- send_task