# Проверяем, существует ли служба jackett.service
if systemctl list-units --full -all | grep -Fq "$service_name"; then
  echo "Jackett is already installed. Exiting."
  exit 0
else
  echo "Jackett is not installed. Installing..."
  # Ваш остальной код для установки Jackett
  release=$(curl -s https://api.github.com/repos/Jackett/Jackett/releases/latest | grep '"tag_name":' | cut -d '"' -f 4)
  curl -LJO "https://github.com/Jackett/Jackett/releases/download/$release/$f"
  tar -xzf "$f" --strip-components=1 && rm -f "$f"
  sudo /opt/Jackett*/install_service_systemd.sh
  systemctl status "$service_name"
  echo -e "\nVisit http://127.0.0.1:9117"
fi