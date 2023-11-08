import subprocess

# Проверка состояния службы torrserver.service
try:
    status_command = ["systemctl", "is-active", "torrserver.service"]
    status_output = subprocess.run(
        status_command, capture_output=True, text=True).stdout.strip()

    if status_output in ["active", "inactive"]:
        print("Служба torrserver.service уже установлена")
    else:
        # Команда для выполнения
        install_command = [
            "curl", "-s", "https://raw.githubusercontent.com/YouROK/TorrServer/master/installTorrServerLinux.sh", "|", "sudo", "bash"]

        # Выполнение команды с использованием subprocess
        subprocess.run(install_command, check=True)
        print("Команда успешно выполнена")

except subprocess.CalledProcessError as e:
    print("Произошла ошибка при выполнении команды:", e)

except Exception as e:
    print("Произошла ошибка при проверке состояния службы torrserver.service:", e)
