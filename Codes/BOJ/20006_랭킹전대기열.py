import sys

input = sys.stdin.readline


class Player:
    def __init__(self, level, name):
        self.level = level
        self.name = name


class Room:
    def __init__(self, master: Player):
        self.master_level = master.level
        self.room_manager = MANAGER
        self.players = [master]

    def put_in(self, player):
        self.players.append(player)

    def print_room(self):
        status = "Started!" if len(self.players) == m else "Waiting!"
        print(status)
        players = sorted(self.players, key=lambda player: player.name)
        for player in players:
            print(f"{player.level} {player.name}")


class Manager:
    def __init__(self):
        self.rooms = []

    def is_accessable_room(self, player: Player, room: Room):
        if len(room.players) == m:
            return False

        return player.level - 10 <= room.master_level <= player.level + 10

    def print_result(self):
        for room in self.rooms:
            room.print_room()

    def apply_join(self, player):
        for room in self.rooms:
            if self.is_accessable_room(player, room):
                room.put_in(player)
                return

        new_room = Room(player)
        self.rooms.append(new_room)


MANAGER = Manager()
p, m = map(int, input().split())

for _ in range(p):
    level, name = input().split()
    player = Player(int(level), name)
    MANAGER.apply_join(player)

MANAGER.print_result()
