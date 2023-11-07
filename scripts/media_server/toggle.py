import subprocess

services = ["torrserver.service", "jackett.service"]


def is_service_active(service_name):
    try:
        return subprocess.run(["sudo", "systemctl", "is-active", service_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True).stdout.decode().strip() == "active"
    except subprocess.CalledProcessError:
        return False


def start_service(service_name):
    try:
        subprocess.run(["sudo", "systemctl", "start",
                       service_name], check=True)
        print(f"Service {service_name} started.")
    except subprocess.CalledProcessError as e:
        print(f"Error starting service {service_name}: {e}")


def stop_service(service_name):
    try:
        subprocess.run(["sudo", "systemctl", "stop", service_name], check=True)
        print(f"Service {service_name} stopped.")
    except subprocess.CalledProcessError as e:
        print(f"Error stopping service {service_name}: {e}")


def toggle_services():
    for service in services:
        if is_service_active(service):
            stop_service(service)
        else:
            start_service(service)


# Call the toggle_services function to toggle the services
toggle_services()
