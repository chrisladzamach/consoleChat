# Chat App con Sockets y Threading

Esta es una aplicación de chat basada en sockets diseñada para permitir la comunicación en tiempo real entre múltiples clientes conectados a un servidor central. Utiliza threading en Python para manejar múltiples conexiones simultáneamente.

---

## 📋 ¿Qué es esta aplicación?

Es una aplicación de chat en tiempo real que permite:
- Conectar múltiples clientes a un servidor.
- Intercambiar mensajes entre los clientes conectados.
- Gestionar cada conexión de cliente en un hilo separado para garantizar la fluidez de las comunicaciones.

---

## 🎯 Propósito

Esta aplicación tiene como objetivo demostrar cómo se pueden usar las bibliotecas integradas de Python, como `socket` y `threading`, para construir una solución de red simple y funcional. Es ideal para aprender conceptos básicos de redes y concurrencia en Python.

---

## 🛠️ ¿Cómo funciona?

1. **Servidor**:
   - Escucha conexiones entrantes en una dirección IP y puerto específicos.
   - Maneja cada cliente en un hilo independiente para permitir múltiples conexiones simultáneas.
   - Difunde los mensajes enviados por un cliente a todos los demás clientes conectados.

2. **Cliente**:
   - Se conecta al servidor especificando su IP y puerto.
   - Envía un nickname para identificar al usuario.
   - Permite enviar y recibir mensajes en tiempo real.

---

## 🚀 Guía de Uso

### Requisitos

- Python 3.8 o superior instalado en tu sistema.
- Conexión de red para comunicación entre servidor y clientes.

### Instalación

1. Clona este repositorio en tu máquina local:
   ```bash
   git clone https://github.com/tuusuario/tu-repositorio.git
