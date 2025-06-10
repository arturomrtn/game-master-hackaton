## Arquitectura

Componentes principales:

🔁 n8n: Orquestador de flujos lógicos.

🧠 OpenAI Assistant: Control de decisiones del Game Master.

💾 Supabase: Almacenamiento de personajes.

🐍 Microservicio Python: Lógica de combate.

💬 Telegram: Entrada/salida de mensajes del jugador.

## Microservicio: Combat Service

- **Tecnología**: Flask (Python)
- **Funcionalidad**: Simula un combate entre jugador y enemigo según las reglas de Knave.
- **Endpoint en producción**: https://combat-service-knave-cc775ec144bb.herokuapp.com/combat
- **Input**: JSON con datos del jugador y del enemigo.
- **Output**: Resultado del combate, registros por turno, HP restante, y ganador.
- **Integración**: N8N llamará este servicio desde un nodo HTTP cuando se inicie un combate.

El microservicio se encarga de lógica determinista, es decir: todo lo que no necesita creatividad ni interpretación. Debe ser exacto, rápido y robusto.                         
