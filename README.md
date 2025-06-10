# ⚔️ Game Master Automatizado 

## 📌 Descripción

Este proyecto implementa un sistema de juego de rol (tipo Knave) donde un jugador puede interactuar con un Game Master automatizado a través de Telegram. El flujo completo se gestiona con n8n, que se encarga de la comunicación entre el jugador, una IA basada en OpenAI, una base de datos Supabase y un microservicio de combate en Python. 

✅ Funcionalidades implementadas

- Extracción y limpieza de mensajes desde Telegram

- Identificación del jugador por nombre o chat ID

- Verificación de existencia del personaje

- Creación de personaje con valores por defecto

- Llamada HTTP a un microservicio de combate

- Actualización de personaje tras el combate

- Devolución del resultado al jugador vía Telegram

En algunas pruebas, donde añadi otro nodo de el flujo llegó hasta el final, ejecutando el combate y devolviendo el mensaje correctamente

🚧 Limitaciones actuales

- El chat_id no siempre se vincula bien al nombre del personaje, lo que genera errores en algunos caminos del flujo

- El flujo completo depende mucho del orden en que el jugador interactúa y tengo mezclados algunos nodos hardcodeados para test con otros dinámicos.

- Algunas rutas pueden perder información entre nodos (por ejemplo, el name), provocando errores silenciosos.

- No se maneja aún un control de sesión persistente entre usuario y personaje

## 🔧 Tecnologías Usadas

- 🧠 OpenAI GPT-3.5
- 🔄 n8n (Interfaz visual low-code)
- 💾 Supabase (Base de datos PostgreSQL + REST)
- 🐍 FastAPI (Microservicio de combate)
- 💬 Telegram Bot API

## 🚀 Cómo Funciona

1. El jugador envía un mensaje por Telegram.
2. n8n recibe el mensaje y lo analiza.
3. El asistente IA responde de forma estructurada.
4. Según la respuesta, el flujo llama a Supabase o al microservicio.
5. El jugador recibe una respuesta con la siguiente acción a realizar.
