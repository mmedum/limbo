# limbo

## Architecture

High-level architecture drawing

![alt text](imgs/architecture.png "Architecture")

## API

### Root

Returning a small hello world

**Definition**

`GET /`

**Response**
- `200 OK` on success

```json
{
    "hello": "world"
}
```

### Health

Returning ok for representing the service is up and alive.

**Definition**

`GET /health`

**Response**
- `200 OK` on success

```json
{
    "health": "ok"
}
```

### Metrics

Returning metrics about the service

**Definition**

`GET /metrics`

**Response**
- `200 OK` on success

```json
{
    "metrics": "ok"
}
```

### Mail

Submit of emails to the service

**Definition**

`POST /v1/mail`

**Request Body**

| Key | Value type | Description  |
| --- | --- | --- |
| from | string | email address for the sender |
| to | list of strings | list of emails that should recieve the message |
| cc | list of strings | list of emails that should be cc on the message |
| bcc | list of strings | list of emails that should be bcc on the message |
| subject | string | subject of the message |
| message | string | contents of the message |

```json
{
    "from": "email@email.com",
    "to": ["email@email.com", "email@email.com"],
    "cc": ["email@email.com"],
    "subject": "Hello",
    "message": "World!",
}
```

**Response**
- `200 OK` on success

```json
{
    "Message": "submitted"
}
```
