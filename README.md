🛡️ SecureNetworkPy
🔍 Verifica la seguridad de tu conexión a Internet mediante Python.

📌 Descripción
Este proyecto analiza diferentes aspectos de la seguridad de tu conexión a Internet y proporciona un nivel de seguridad basado en:

✅ Disponibilidad de conexión a Internet
✅ Uso de HTTPS en la navegación
✅ Resolución de DNS confiables (Google y Cloudflare)
✅ Detección de proxies o VPNs

Si la conexión es segura, se muestra una ventana de felicitación. Si no, se alerta al usuario con un mensaje de advertencia.

🚀 Requisitos
Asegúrate de tener Python 3 instalado en tu sistema. Luego, instala las dependencias necesarias:

bash
Copiar
Editar
pip install requests tkinter
🔧 Instalación y Uso
1️⃣ Clona este repositorio:

bash
Copiar
Editar
git clone https://github.com/Joel190321/SecureNetworkPy.git
cd SecureNetworkPy
2️⃣ Ejecuta el script:

bash
Copiar
Editar
python secure_network.py
🖼️ Capturas de Pantalla
💡 Si la conexión es segura, verás:

⚠️ Si la conexión no es segura, verás:

🛠️ Estructura del Código
📌 Funciones principales:

check_internet_connection(): Verifica si hay acceso a Internet.
check_https(url): Verifica si la conexión es a través de HTTPS.
check_dns(): Analiza si se está utilizando servidores DNS confiables.
check_proxy_or_vpn(): Intenta detectar si la conexión pasa por un proxy o VPN.
check_connection_security(): Evalúa los resultados y clasifica el nivel de seguridad.
show_congratulations(): Muestra un mensaje de éxito si la conexión es segura.
main(): Ejecuta todas las verificaciones y muestra el resultado final.
📜 Licencia
MIT License - Siéntete libre de mejorar este proyecto y contribuir.

💡 ¿Ideas o mejoras? ¡Abre un issue o un pull request! 🚀
