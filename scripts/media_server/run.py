import subprocess

services = ["torrserver.service", "jackett.service"]


def is_service_active(service_name):
    try:
        return subprocess.run(["sudo", "systemctl", "is-active", service_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True).stdout.decode().strip() == "active"
    except subprocess.CalledProcessError:
        return False


def run_service(service_name):
    if not is_service_active(service_name):
        try:
            subprocess.run(["sudo", "systemctl", "start",
                           service_name], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Ошибка: {e}")


def get_service_status(service_name):
    try:
        result = subprocess.run(
            ["systemctl", "status", service_name], capture_output=True, text=True, check=True)
        print(f"{result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка: {e}")


for service in services:
    if not is_service_active(service):
        run_service(service)
    get_service_status(service)

# Команда для запуска Kodi
kodi_command = "kodi"

# Запускаем Kodi с помощью subprocess
subprocess.Popen(kodi_command, shell=True)
