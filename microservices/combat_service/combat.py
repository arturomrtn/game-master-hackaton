# combat.py - Lógica de combate Knave adaptado a OSR

import random

def roll_die(sides):
    return random.randint(1, sides)

class Character:
    def __init__(self, name, hp, attack_bonus, defense):
        self.name = name
        self.hp = hp
        self.attack_bonus = attack_bonus
        self.defense = defense

    def is_alive(self):
        return self.hp > 0

class Enemy:
    def __init__(self, name, hd, ac, attack_bonus):
        self.name = name
        self.hp = hd * 4  # adaptación básica: HD × 4
        self.attack_bonus = attack_bonus
        self.defense = ac  # AC en OSR se convierte directamente a Defense

    def is_alive(self):
        return self.hp > 0

def simulate_combat(player, enemy):
    log = []
    turns = []

    # Crear instancias
    player_char = Character(
        name=player["name"],
        hp=player["hp"],
        attack_bonus=player["attack_bonus"],
        defense=player["defense"]
    )

    enemy_char = Enemy(
        name=enemy["name"],
        hd=enemy["hd"],
        ac=enemy["ac"],
        attack_bonus=enemy["attack_bonus"]
    )

    # Iniciativa: 1-3 enemigo empieza, 4-6 jugador
    initiative_roll = roll_die(6)
    player_turn = initiative_roll >= 4
    log.append(f"Iniciativa: {'Jugador' if player_turn else 'Enemigo'} empieza")

    while player_char.is_alive() and enemy_char.is_alive():
        turn_data = {}
        if player_turn:
            roll = roll_die(20) + player_char.attack_bonus
            if roll >= enemy_char.defense:
                damage = roll_die(6)
                enemy_char.hp -= damage
                action = f"Jugador ataca con {roll} y hace {damage} de daño."
            else:
                action = f"Jugador falla con un ataque de {roll}."
            turn_data["actor"] = "player"
        else:
            roll = roll_die(20) + enemy_char.attack_bonus
            if roll >= player_char.defense:
                damage = roll_die(6)
                player_char.hp -= damage
                action = f"Enemigo ataca con {roll} y hace {damage} de daño."
            else:
                action = f"Enemigo falla con un ataque de {roll}."
            turn_data["actor"] = "enemy"

        turn_data["log"] = action
        turns.append(turn_data)
        log.append(action)
        player_turn = not player_turn

    result = "victory" if player_char.is_alive() else "defeat"

    return {
        "result": result,
        "player_remaining_hp": max(player_char.hp, 0),
        "enemy_remaining_hp": max(enemy_char.hp, 0),
        "turns": turns,
        "log": log
    }
