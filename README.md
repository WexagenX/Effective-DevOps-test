# Effective Mobile — DevOps тестовое задание

Простое приложение с Python-бэкендом за Nginx reverse proxy,
развёрнутое в Docker Compose.

## Как запустить
Предварительно должен быть установлен Docker!
```bash
git clone https://github.com/WexagenX/Effective-DevOps-test
cd effective-devops
docker compose up -d --build
```
Проверка после билда:

```bash
 curl http://localhost 
 ```
или Открой http://localhost — должно вернуть:
```bash 
Hello from Effective Mobile!
```
## Архитектура

Internet → Nginx:80 → Backend:8080 → ответ

Nginx принимает запросы снаружи, бэкенд недоступен напрямую с хоста —
только через внутреннюю Docker-сеть.

## Стек

- Python 3.12-slim — бэкенд
- nginx:alpine — reverse proxy
- Docker Compose — оркестрация

## Структура
```bash
.
├── backend/
│   ├── Dockerfile          # Python backend (non-root + healthcheck)
│   └── app.py              # Простой HTTP-сервер на Python
├── nginx/
│   ├── Dockerfile          # Кастомный образ на базе nginx:alpine
│   └── nginx.conf          # Конфигурация reverse-proxy
├── docker-compose.yml      # Оркестрация сервисов + отдельная сеть
├── .env                    
├── .gitignore
├── .dockerignore
└── README.md
```
## Что реализовано

- Оба контейнера запускаются без root
- Healthcheck на каждый сервис
- Изолированная сеть между контейнерами
- Минимальные образы + .dockerignore

## О тестовом задании

Данный проект выполнен согласно рекомендациям тестового задания, соблюдено ТЗ и рекомендации:

- Non-root пользователи в обоих контейнерах
- Healthcheck в каждом сервисе
- Изолированная effective-mobile-net сеть
- Минимальный размер образов + .dockerignore
- .env файл
- Чистая структура проекта согласно ТЗ
- Полный харденинг Docker

Автор: WexagenX Авдеев Кирилл
Дата выполнения: 06.04.2026
