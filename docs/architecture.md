## Microservicio: Combat Service

- **Tecnología**: Flask (Python)
- **Funcionalidad**: Simula un combate entre jugador y enemigo según las reglas de Knave.
- **Endpoint en producción**: https://combat-service-knave.herokuapp.com/combat
- **Input**: JSON con datos del jugador y del enemigo.
- **Output**: Resultado del combate, registros por turno, HP restante, y ganador.
- **Integración**: N8N llamará este servicio desde un nodo HTTP cuando se inicie un combate.
