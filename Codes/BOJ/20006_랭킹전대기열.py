import sys

input = sys.stdin.readline


class Manager:
    def __init__(self):
        self.rooms = []

    def print_result(self):
        for room in self.rooms:
            room.print_room()

    def apply_join(self, player):
        for room in self.rooms:
            if player.is_accessable_room(room):
                room.put_in(player)
                return

        new_room = Room(self, player)
        self.rooms.append(new_room)


class Room:
    def __init__(self, room_manager, master):
        self.master_level = master.level
        self.room_manager = room_manager
        self.players = [master]

    def put_in(self, player):
        self.players.append(player)

    def print_room(self):
        status = "Started!" if len(self.players) == m else "Waiting!"
        print(status)
        players = sorted(self.players, key=lambda player: player.name)
        for player in players:
            print(f"{player.level} {player.name}")


class Player:
    def __init__(self, level, name):
        self.level = level
        self.name = name

    def is_accessable_room(self, room: Room):
        if len(room.players) == m:
            return False

        return self.level - 10 <= room.master_level <= self.level + 10


room_manager = Manager()

p, m = map(int, input().split())

for _ in range(p):
    level, name = input().split()
    player = Player(int(level), name)
    room_manager.apply_join(player)

room_manager.print_result()
