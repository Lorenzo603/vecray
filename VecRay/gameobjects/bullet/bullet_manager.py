import logging

from event_bus import Events
from event_system.event import register
from gameobjects.bullet.bullet import Bullet


class BulletManager:

    def __init__(self):
        self.bullets = []
        register(Events.BULLET_OOB.name, self.on_bullet_oob)

    def spawn_bullet(self, x, y):
        self.bullets.append(Bullet(x, y))

    def on_bullet_oob(self, bullet):
        self.bullets.remove(bullet)
