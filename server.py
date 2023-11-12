import subprocess

services = ["torrserver.service", "jackett.service"]


def is_service_active(service_name):
    try:
        output = subprocess.check_output(
            ["systemctl", "is-active", service_name]).decode().strip()
        return output == "active"
    except subprocess.CalledProcessError:
        return False


def start_services(services):
    try:
        subprocess.run(["sudo", "systemctl", "start"] + services, check=True)
        print("Services started:", ", ".join(services))
    except subprocess.CalledProcessError as e:
        print(f"Error starting services: {e}")


def stop_services(services):
    try:
        subprocess.run(["sudo", "systemctl", "stop"] + services, check=True)
        print("Services stopped:", ", ".join(services))
    except subprocess.CalledProcessError as e:
        print(f"Error stopping services: {e}")


def toggle_services():
    active_services = [
        service for service in services if is_service_active(service)]
    if len(active_services) == len(services):
        stop_services(services)
    else:
        start_services(services)


# Call the toggle_services function to toggle the services
toggle_services()
