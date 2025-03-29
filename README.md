# 🚀 Proyecto TCP Cliente y Servidor en Python

Este proyecto implementa un servidor y un cliente TCP en Python que se comunican a través de `localhost` en el puerto `5000`. El servidor convierte los mensajes recibidos a mayúsculas y maneja la desconexión cuando recibe el mensaje `"DESCONEXION"`.

---

## 📋 Requisitos
- **Python 3.6** o superior
- **Virtualenv** (opcional pero recomendado)

---

## 📂 Estructura del Proyecto
```plaintext
TCPTEST/
├── server/
│   └── server.py
├── client/
│   └── client.py
└── utils/
    └── util.py
```


## ⚙️ Instalación y Ejecución

### Paso 1: Clonar el repositorio
```bash
git clone https://github.com/mauricioruiz1997/TCPKosmos.git
cd TCPKosmos
```
### Paso 2: Entorno virtual
```bash
python3 -m venv venv
source venv/bin/activate    # MacOS/Linux
.\venv\Scripts\activate     # Windows
```

### Paso 3: Ejecutar el servidor
* Abre una terminal

* Navega al directorio del proyecto

* Ejecuta el siguiente comando: 
```bash
python server/server.py
```
* El servidor mostrará: "Servidor TCP iniciado en localhost:5000"


### Paso 4: Ejecutar el cliente (en terminal aparte)
* Abre otra terminal

* Navega al directorio del proyecto

* Ejecuta el siguiente comando: 
```bash
python client/client.py
```

* Envia un mensaje




## ⚠️ Consideraciones Importantes
```bash
El puerto predeterminado es 5000 (verifica que esté disponible)
Diseñado para pruebas en entorno local (127.0.0.1)
Requiere permisos de red en el sistema
```