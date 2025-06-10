# ⚔️ Game Master Automatizado 

## 📌 Descripción
Este proyecto implementa un sistema de juego de rol (tipo Knave) donde un jugador puede interactuar con un Game Master automatizado a través de Telegram. El flujo completo se gestiona con n8n, que se encargaa la comunicación entre el jugador, una IA basada en OpenAI, una base de datos Supabase y un microservicio de combate en Python.

## 🎯 Características
- Crear, usar o borrar personajes.
- Iniciar combates y obtener resultados realistas.
- Todo el flujo se ejecuta por Telegram.
- Respuestas prediseñadas y basadas en decisiones automatizadas.

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