#!/bin/bash

# Выводим приветствие
echo "Добро пожаловать! Этот скрипт проверит наличие Python и pip на вашей системе и установит их, если необходимо."

# # Проверяем, является ли текущий пользователь администратором (root)
# if [[ $EUID -ne 0 ]]; then
#    echo "Этот скрипт должен быть запущен с правами администратора." 
#    exit 1
# fi

# Проверяем наличие пакетного менеджера
if command -v apt >/dev/null 2>&1; then
    echo "Обнаружен пакетный менеджер apt. Выполняем обновление пакетного списка."
    # Если apt доступен, обновляем пакетный список
    apt update
    echo "Пакетный список обновлён. Выполняем установку Python и pip."
    # Устанавливаем Python и pip, если их нет
    if ! command -v python3 >/dev/null 2>&1 || ! command -v pip3 >/dev/null 2>&1; then
        apt install -y python3 python3-pip
        echo "Python и pip успешно установлены."
    else
        echo "Python и pip уже установлены на вашей системе."
    fi
elif command -v yum >/dev/null 2>&1; then
    echo "Обнаружен пакетный менеджер yum. Выполняем установку Python и pip."
    # Если yum доступен, устанавливаем Python и pip (предполагая, что это CentOS или Fedora), если их нет
    if ! command -v python3 >/dev/null 2>&1 || ! command -v pip3 >/dev/null 2>&1; then
        yum install -y python3 python3-pip
        echo "Python и pip успешно установлены."
    else
        echo "Python и pip уже установлены на вашей системе."
    fi
elif command -v pacman >/dev/null 2>&1; then
    echo "Обнаружен пакетный менеджер pacman. Выполняем установку Python и pip."
    # Если pacman доступен, устанавливаем Python и pip (предполагая, что это Arch Linux или Manjaro), если их нет
    if ! command -v python3 >/dev/null 2>&1 || ! command -v pip3 >/dev/null 2>&1; then
        pacman -S --noconfirm python python-pip
        echo "Python и pip успешно установлены."
    else
        echo "Python и pip уже установлены на вашей системе."
    fi
else
    # Если ни apt, ни yum, ни pacman не доступны, выводим сообщение об ошибке
    echo "Пакетный менеджер не найден. Установка Python и pip невозможна."
    exit 1
fi