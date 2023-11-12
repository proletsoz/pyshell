import subprocess

services = ["torrserver.service", "jackett.service"]


def start_service(service_name):
    subprocess.run(["sudo", "systemctl", "start", service_name])
    print(f"Service {service_name} started.")


def stop_service(service_name):
    subprocess.run(["sudo", "systemctl", "stop", service_name])
    print(f"Service {service_name} stopped.")


def toggle_kodi():
    if subprocess.run(["pgrep", "kodi"]).returncode == 0:
        subprocess.run(["pkill", "kodi"])
        print("Kodi closed.")
    else:
        subprocess.run(["kodi", "&"])
        print("Kodi opened.")


def toggle_services():
    for service in services:
        if subprocess.run(["sudo", "systemctl", "is-active", "--quiet", service]).returncode == 0:
            stop_service(service)
        else:
            start_service(service)


# Закрытие Kodi перед переключением сервисов и вызов toggle_services
toggle_services()

# Вызов функции toggle_kodi для открытия/закрытия Kodi в зависимости от ее текущего состояния
toggle_kodi()
