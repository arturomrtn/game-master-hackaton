# ⚔️ Game Master Automatizado 

## 📌 Descripción

Este proyecto implementa un sistema de juego de rol (tipo Knave) donde un jugador puede interactuar con un Game Master automatizado a través de Telegram. El flujo completo se gestiona con n8n, que se encarga de la comunicación entre el jugador, una IA basada en OpenAI, una base de datos Supabase y un microservicio de combate en Python. 

Endpoint combate en producción: https://combat-service-knave-cc775ec144bb.herokuapp.com/combat
Bot de Telegram: https://t.me/kknave_game_bot
Video demo link: https://www.youtube.com/watch?v=ev3RCl9GF_c

En la versión subida actualmente en la repo el flujo para iniciar el combate no funciona correctamente. Antes de implementar el agente IA, el flujo llegaba al combate sin problemas, después de implementar el agente y añadir más nodos y complejidad al proyecto empecé a ver como parte de la información se perdía por el camino. Luego, en algunos de los tests que hice posteriormente a la entrega del proyecto, donde añadí otro nodo de Telegram, el flujo llegaba hasta el final en ciertas ocasiones, ejecutando el combate y devolviendo logs (aunque no devolviendo todos los logs necesarios), en n8n_workflow/screenshots puede verse un screenshot de esto en una conversación con el bot.

✅ Funcionalidades implementadas

- Implementación de microservice para el combate, creado en Python y desplegado en Heroku

- Implementación de Agente IA de Open AI

- Extracción y limpieza de mensajes desde Telegram

- Identificación del jugador por nombre o chat ID

- Verificación de existencia del personaje

- Creación de personaje con valores por defecto

- Llamada HTTP a un microservicio de combate

- Actualización de personaje tras el combate

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
