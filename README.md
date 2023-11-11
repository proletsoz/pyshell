# Cкрипты для автоматизации
## Скрипт для теста
### Shell
```bash -c "$(curl -fsSL https://raw.githubusercontent.com/proletsoz/pyshell/main/test.sh)"```
## Инсталятор Python
### Shell
```sudo bash -c "$(curl -fsSL https://raw.githubusercontent.com/proletsoz/pyshell/main/python.sh)"```
## Запуск медиа сервера
Работает как переключатель. Запускает torserver и jackett.
### Python
```wget -O - https://raw.githubusercontent.com/proletsoz/pyshell/main/server.py | python3```
### Shell
```wget -O - https://raw.githubusercontent.com/proletsoz/pyshell/main/server.sh | bash```
