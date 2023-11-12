#!/bin/bash

services=("torrserver.service" "jackett.service")

is_service_active() {
    local service_name=$1
    systemctl is-active --quiet "$service_name"
    return $?
}

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
        if is_service_active "$service"; then
            stop_service "$service"
        else
            start_service "$service"
        fi
}

# Вызов функции toggle_kodi для открытия/закрытия Kodi в зависимости от ее текущего состояния
toggle_kodi

# Закрытие Kodi перед переключением сервисов и вызов toggle_services
toggle_services