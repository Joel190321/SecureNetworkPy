# 🛡️ SecureNetworkPy  
🔍 **Verifica la seguridad de tu conexión a Internet con Python.**  

---

## 📌 Descripción  
**SecureNetworkPy** analiza diferentes aspectos de la seguridad de tu conexión a Internet y proporciona un nivel de seguridad basado en:  

- ✅ **Disponibilidad de conexión a Internet**  
- ✅ **Uso de HTTPS en la navegación**  
- ✅ **Resolución de DNS confiables (Google y Cloudflare)**  
- ✅ **Detección de proxies o VPNs**  

📢 Si la conexión es segura, se mostrará un mensaje de **felicitación**.  
⚠️ Si no es segura, aparecerá una **advertencia** al usuario.  

---

## 🚀 Requisitos  
Asegúrate de cumplir con los siguientes requisitos antes de ejecutar el script:  

- 🔹 Tener **Python 3** instalado en tu sistema.  
- 🔹 Instalar las dependencias necesarias ejecutando:  

```bash
pip install requests tkinter
```

##🔧 Instalación y Uso
1️⃣ Clona este repositorio

```bash
git clone https://github.com/Joel190321/SecureNetworkPy.git
cd SecureNetworkPy
```

2️⃣ Ejecuta el script
```bash
python secure_network.py
```

📌 El programa analizará la seguridad de tu conexión y mostrará una alerta o un mensaje de éxito en caso de que sea segura


#🛠️ Estructura del Código
El script está organizado en funciones clave para cada verificación de seguridad:

- 🔹 check_internet_connection(): Verifica si hay acceso a Internet.
- 🔹 check_https(url): Confirma si la conexión usa HTTPS.
- 🔹 check_dns(): Analiza si se están usando DNS confiables.
- 🔹 check_proxy_or_vpn(): Detecta proxies o VPNs.
- 🔹 check_connection_security(): Evalúa la seguridad y la clasifica.
- 🔹 show_congratulations(): Muestra un mensaje de éxito si la conexión es segura.
- 🔹 main(): Ejecuta todas las verificaciones y muestra el resultado final.

---

#🏗️ Contribuciones
🚀 ¡Este proyecto es open-source y cualquier contribución es bienvenida!

---

Si deseas mejorar el código, sigue estos pasos:
- 1️⃣ Haz un fork del repositorio.
- 2️⃣ Crea una nueva rama para tu mejora.
- 3️⃣ Envía un Pull Request con los cambios.

