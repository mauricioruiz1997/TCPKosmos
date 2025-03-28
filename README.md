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
git clone https://github.com/tu-usuario/tu-proyecto.git
cd TCPTEST
```
### Paso 2: Entorno virtual
```bash
python3 -m venv venv
source venv/bin/activate    # MacOS/Linux
.\venv\Scripts\activate     # Windows
```

### Paso 3: Ejecutar el servidor
```bash
python server/server.py
```

### Paso 4: Ejecutar el cliente (en terminal aparte)
```bash
python client/client.py
```

## 🧪 Modo de Uso

### Envío de mensajes normales:
```bash
[Cliente]  Ingrese mensaje: hola mundo
[Servidor] Respuesta: HOLA MUNDO
```
### Desconexión:
```bash
[Cliente]  Ingrese mensaje: DESCONEXION
[Servidor] Conexión cerrada con ('127.0.0.1', 54322)
```

## ⚠️ Consideraciones Importantes
```bash
El puerto predeterminado es 5000 (verifica que esté disponible)
Diseñado para pruebas en entorno local (127.0.0.1)
Requiere permisos de red en el sistema
```