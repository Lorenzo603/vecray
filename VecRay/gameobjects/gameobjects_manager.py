
class GameObjectsManager:

    def __init__(self):
        self.gameobjects = []

    def add_gameobject(self, go):
        self.gameobjects.append(go)

    def remove_gameobject(self, go):
        self.gameobjects.remove(go)
