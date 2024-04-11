import logging

from event_bus import Events
from event_system.event import register


class EnemyManager:

    def __init__(self, enemies):
        self.enemies = enemies
        register(Events.ENEMY_OOB.name, self.on_enemy_oob)

    def on_enemy_oob(self, enemy):
        logging.debug(f"{enemy} is oob")
        self.enemies.remove(enemy)
