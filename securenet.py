import requests
import socket
import tkinter as tk
from tkinter import messagebox


def check_internet_connection():
    try:
        requests.get("https://www.google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False


def check_https(url):
    try:
        response = requests.get(url)
        return response.url.startswith('https')
    except requests.RequestException:
        return False


def check_dns():
    try:
       
        dns_servers = ['8.8.8.8', '1.1.1.1']
        resolver = socket.getaddrinfo('www.google.com', 80)
        for res in resolver:
            if res[4][0] in dns_servers:
                return True
        return False
    except socket.error:
        return False


def check_proxy_or_vpn():
    try:
        
        proxy = requests.get('https://api.ipify.org?format=json').json()
        vpn = requests.get('https://ipinfo.io/json').json()
        if 'proxy' in proxy or 'vpn' in vpn:
            return True
        return False
    except requests.RequestException:
        return False


def check_connection_security():
    if not check_internet_connection():
        return "No hay conexión a Internet."

    security_level = 0

    if check_https("https://www.google.com"):
        security_level += 1

    if check_dns():
        security_level += 1

    if check_proxy_or_vpn():
        security_level += 1

    if security_level == 0:
        return "Conexión no segura."
    elif security_level == 1:
        return "Conexión segura."
    elif security_level == 2:
        return "Conexión muy segura."
    else:
        return "Conexión extremadamente segura."


def show_congratulations():
    
    root = tk.Tk()
    root.title("Verificación de Seguridad")
    root.geometry("400x200")  

    
    canvas = tk.Canvas(root, width=400, height=200, bg="lightgreen")
    canvas.pack()

    
    canvas.create_text(
        200,  
        100,  
        text="¡Felicidades! Conexión segura.",
        font=("Arial", 16, "bold"),
        fill="darkgreen"
    )

 
    root.mainloop()


def main():
    result = check_connection_security()
    print(result)  

    
    if "segura" in result.lower():
        show_congratulations()
    else:
        
        root = tk.Tk()
        root.withdraw()  
        messagebox.showwarning("Advertencia", result)


if __name__ == "__main__":
    main()