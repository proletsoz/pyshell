#!/bin/bash

services=("torrserver.service" "jackett.service")

start_service() {
    local service_name=$1
    sudo systemctl start "$service_name"
    echo "Service $service_name started."
}

stop_service() {
    local service_name=$1
    sudo systemctl stop "$service_name"
    echo "Service $service_name stopped."
}

toggle_kodi() {
    if pgrep kodi; then
        pkill kodi
        echo "Kodi closed."
    else
        kodi &
        echo "Kodi opened."
    fi
}

toggle_services() {
    for service in "${services[@]}"; do
        sudo systemctl is-active --quiet "$service" && stop_service "$service" || start_service "$service" &
    done
    wait
}

# Закрытие Kodi перед переключением сервисов и вызов toggle_services
toggle_services

# Вызов функции toggle_kodi для открытия/закрытия Kodi в зависимости от ее текущего состояния
toggle_kodi