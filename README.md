EN
# Chat App with Sockets and Threading

This is a chat application based on sockets designed to enable real-time communication between multiple clients connected to a central server. It uses threading in Python to handle simultaneous connections.

---

## 📋 What is this application?

This is a real-time chat application that allows:
- Multiple clients to connect to a server.
- Messages to be exchanged between connected clients.
- Each client connection to be managed in a separate thread for seamless communication.

---

## 🎯 Purpose

The goal of this application is to demonstrate how to use Python's built-in `socket` and `threading` libraries to build a simple and functional networking solution. It is ideal for learning basic concepts of networking and concurrency in Python.

---

## 🛠️ How does it work?

1. **Server**:
   - Listens for incoming connections on a specific IP address and port.
   - Manages each client in a separate thread to allow multiple simultaneous connections.
   - Broadcasts messages sent by one client to all other connected clients.

2. **Client**:
   - Connects to the server by specifying its IP address and port.
   - Sends a nickname to identify the user.
   - Allows real-time message sending and receiving.

---

## 🚀 How to Use

### Requirements

- Python 3.8 or higher installed on your system.
- Network connection to enable communication between the server and clients.

## Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/your-repository.git

## Execution
### Step 1: Start the Server
   1. Open a terminal
   2. Navigate to the project directory:
      ```bash
      cd your-repository
   3. Run the program in sever mode.
      ```
      python app.py
   4. You will see the message:
      ```
      [SERVER] Waiting for connections on 0.0.0.0:5555
   This indicates the server is ready to accept connections.
### Step 2: Connect as a Client
   1. Open another terminal (you can use the same device or another device on the same network).
   2. Run the program in client mode:
      ```
      python app.py
   3. Select the client options:
      ```
      Select mode:
      1. Server
      2. Client
      Option: 2
   4. Enter the server's IP address when prompted:
      ```
      Enter server IP: <SERVER_IP>
   5. Enter a nickname to identify yourself:
      ```
      Enter your nickname: <YOUR_NICKNAME>
   6. Start chatting by typing messages in the terminal. Messages will be broadcast to all connected clients.
### Exit the Chat
Type `exit` in the client to disconnect from the server.

---

🧪 ## Example Usage
   1. Server running:
      ```
      [SERVER] Waiting for connections on 0.0.0.0:5555
      [NEW CLIENT] Connected from ('192.168.0.10', 54321)
   2. Messages exchanged between clients:
      - Client 1:
        ```
        [nickname1] Hello, how are you?
      - Client 2:
        ```
        [nickname1] Hello, how are you?
---

⚠️ ## Common Errors and Solutions
   1. ConnectionRefusedError:
      - Make sure the server is running before trying to connect as a client.
   2. TimeoutError:
      - Verify that the server IP address is correct.
      - Ensure both devices are on the same network.
   3. Unexpected disconnection:
      - if a client disconnects abruptly, the server will remove the connection and allow others to continue functioning.
---
🛡️ ## Security Notes.
   - This code does not implement encryption, meaning messages are sent in plain thext. ###Do not use it on public networks or production enviroments.###
   - Consider implementing SSL/TLS for secure communication if deploying in a more serious context.
---
📄 ## License
This project is licensed under the MIT License. You can use, modify, and distribute the code under the terms of this license.
---
Thank you for exploring this chat application! 💬 If you have suggestions or improvements, feel free to contribute to the project. 🚀

---
---

ES
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

## Ejecución
### Paso 1: Iniciar el Servidor
   1. Abre una terminal.
   2. Ejecuta el programa en modo servidor:
      ```bash
      cd your-repository
   3. Ejecuta el programa en modo servidor:
      ```
      python app.py
   4. Verás el siguiente mensaje:
      ```
      [SERVER] Waiting for connections on 0.0.0.0:5555
   Esto indica que el servidor está listo para aceptar conexiones.
   
### Step 2: Conectarse como cliente
   1. Abre otra terminal (puedes usar el mismo dispositivo o uno en la misma red).
   2. Ejecuta el programa en modo cliente:
      ```
      python app.py
   3. Selecciona la opción de cliente:
      ```
      Select mode:
      1. Server
      2. Client
      Option: 2
   4. Ingresa la dirección IP del servidor cuando se te solicite:
      ```
      Enter server IP: <SERVER_IP>
   5. Ingresa un apodo para identificarte:
      ```
      Enter your nickname: <YOUR_NICKNAME>
   6. Comienza a chatear escribiendo mensajes en la terminal. Los mensajes se enviarán a todos los clientes conectados.
### Salir del chat
Escribe `exit` en el cliente para desconectarte del servidor.

---

🧪 ## Ejemplo de Uso
   1. Servidor en ejecución:
      ```
      [SERVER] Waiting for connections on 0.0.0.0:5555
      [NEW CLIENT] Connected from ('192.168.0.10', 54321)
   2. Mensajes intercabiados entre clientes:
      - Cliente 1:
        ```
        [nickname1] Hello, how are you?
      - Cliente 2:
        ```
        [nickname1] Hello, how are you?
---

⚠️ ## Errores Comunes y Soluciones
   1. ConnectionRefusedError:
      - Asegúrate de que el servidor esté corriendo antes de conectarte como cliente.
   2. TimeoutError:
      - Verifica que la IP del servidor sea correcta.
      - Asegúrate de que ambos dispositivos estén en la misma red.
   3. Desconexión inesperada:
      - Si un cliente se desconecta abruptamente, el servidor eliminará la conexión y permitirá que otros sigan funcionando.
---
🛡️ ## Notas de Seguridad
   - Este código no implementa cifrado, lo que signidica que los mensajes se envían en texto plano. ###No lo utilices en redes públicas o en entornos de producción.###
   - Considera usar SSL/TSL para protefer la comunicación si deseas implementarlo en un entorno más serio.
---
📄 ## Licencia
Este proyecto está bajo la Licencia MIT. Puedes usar, modificar y distribuir el código bajo los términos de esta licencia.
---
¡Gracias por explirar esta aplicación de chat en consola! 💬 Si tienes alguna sugerencia o mejora, no dudes en contribuir al proyecto. 🚀
