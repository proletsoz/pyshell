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

toggle_services() {
    for service in "${services[@]}"; do
        if is_service_active "$service"; then
            stop_service "$service"
        else
            start_service "$service"
        fi
    done
}

# Call the toggle_services function to toggle the services
toggle_services
