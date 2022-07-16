import sys, math

input = sys.stdin.readline


class Item:
    def __init__(self, r, c, t, s):
        self.y = r
        self.x = c
        self.t = t
        self.s = s


class Monster:
    def __init__(self, r, c, s, w, a, h, e, is_boss):
        self.y = r
        self.x = c
        self.name = s
        self.damage = w
        self.defense = a
        self.max_hp = h
        self.cur_hp = h
        self.exp = e
        self.is_boss = is_boss

    def get_damaged(self, dmg: int):
        self.cur_hp -= dmg
        if self.cur_hp <= 0:
            self.die()

    def die(self):
        game_manager.obj_destroyed(self.y, self.x)


class Trap:
    def __init__(self):
        self.name = "SPIKE TRAP"


class Player:
    def __init__(self):
        self.max_hp = 20
        self.cur_hp = 20
        self.damage = 2
        self.defense = 2
        self.level = 1
        self.exp = 0
        self.weapon = 0
        self.armor = 0
        self.accessories = []

    def heal(self, num):
        self.cur_hp = min(self.max_hp, self.cur_hp + num)

    def get_damaged(self, dmg: int, from_who: Monster or Trap):
        self.cur_hp -= dmg
        if self.cur_hp <= 0:
            self.cur_hp = 0
            self.die(from_who)

    def die(self, from_who: Monster or Trap):
        self.cur_hp = 0
        if "RE" in self.accessories:
            self.cur_hp = self.max_hp
            game_manager.player_y = start_y
            game_manager.player_x = start_x
            self.accessories.remove("RE")
        else:
            # 게임 종료
            game_manager.game_over(f"YOU HAVE BEEN KILLED BY {from_who.name}..")

    def get_exp(self, exp: int):
        if "EX" in self.accessories:
            exp = math.floor(exp * 1.2)
        self.exp += exp
        if self.exp >= self.level * 5:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.exp = 0
        self.max_hp += 5
        self.damage += 2
        self.defense += 2
        self.cur_hp = self.max_hp

    def get_item(self, item: Item):
        if item.t == "O":
            if len(self.accessories) < 4 and item.s not in self.accessories:
                self.accessories.append(item.s)
                if item.s == "DX":
                    game_manager.set_trap_damage(1)
        elif item.t == "W":
            self.weapon = item.s
        elif item.t == "A":
            self.armor = item.s

        game_manager.obj_destroyed(item.y, item.x)

    def trap(self):
        self.get_damaged(game_manager.trap_damage, Trap())

    def win(self, monster: Monster):
        self.get_exp(monster.exp)
        if "HR" in self.accessories:
            self.heal(3)

        if monster.is_boss:
            game_manager.game_over("YOU WIN!")


class GameManager:
    def __init__(self, player_y, player_x):
        self.player_y = player_y
        self.player_x = player_x
        self.turn_cnt = 0
        self.obj_matrix = [[None] * m for _ in range(n)]
        self.trap_damage = 5
        self.playing = True

    def turn(self, cmd):
        self.turn_cnt += 1
        self.player_move(cmd)
        if self.obj_matrix[self.player_y][self.player_x] == "^":
            player.trap()

    def player_move(self, cmd):
        if cmd == "L":
            ny, nx = self.player_y, self.player_x - 1
        elif cmd == "R":
            ny, nx = self.player_y, self.player_x + 1
        elif cmd == "U":
            ny, nx = self.player_y - 1, self.player_x
        elif cmd == "D":
            ny, nx = self.player_y + 1, self.player_x

        if ny >= n or ny < 0 or nx >= m or nx < 0:
            return
        if grid[ny][nx] == "#":
            return

        self.player_y = ny
        self.player_x = nx

        if grid[ny][nx] == "B":
            player.get_item(self.obj_matrix[ny][nx])
            self.obj_destroyed(ny, nx)

        elif grid[ny][nx] == "&":
            if not self.battle(player, self.obj_matrix[ny][nx]):
                return
        elif grid[ny][nx] == "M":
            if not self.battle_boss(player, self.obj_matrix[ny][nx]):
                return

    def set_trap_damage(self, dmg):
        self.trap_damage = dmg

    def game_over(self, message):
        self.playing = False
        if player.cur_hp > 0:
            grid[self.player_y][self.player_x] = "@"

        for row in grid:
            print("".join(row))
        print(f"Passed Turns : {self.turn_cnt}")
        print(f"LV : {player.level}")
        print(f"HP : {player.cur_hp}/{player.max_hp}")
        print(f"ATT : {player.damage}+{player.weapon}")
        print(f"DEF : {player.defense}+{player.armor}")
        print(f"EXP : {player.exp}/{player.level * 5}")
        print(message)

    def battle_boss(self, player: Player, boss: Monster):
        first_dmg = player.damage + player.weapon
        if "CO" in player.accessories:
            if "DX" in player.accessories:
                first_dmg *= 3
            else:
                first_dmg *= 2

        # 전투 첫 턴
        boss.get_damaged(max(1, first_dmg - boss.defense))
        if boss.cur_hp <= 0:
            player.win(boss)
            return True

        if "HU" in player.accessories:
            player.heal(player.max_hp)
        else:
            player.get_damaged(
                max(1, boss.damage - player.defense - player.armor), boss
            )

        if player.cur_hp <= 0:
            boss.cur_hp = boss.max_hp
            return False

        # 남은 전투 시작
        damage_give = max(1, player.damage + player.weapon - boss.defense)
        damage_get = max(1, boss.damage - player.defense - player.armor)

        cnt_win = math.ceil(boss.cur_hp / damage_give)
        cnt_lose = math.ceil(player.cur_hp / damage_get)
        # 이김
        if cnt_win <= cnt_lose:
            player.get_damaged((cnt_win - 1) * damage_get, boss)
            player.win(boss)
            boss.die()
            return True
        # 짐
        else:
            boss.cur_hp = boss.max_hp
            player.die(boss)
            return False

    def battle(self, player: Player, monster: Monster):
        first_dmg = player.damage + player.weapon
        if "CO" in player.accessories:
            if "DX" in player.accessories:
                first_dmg *= 3
            else:
                first_dmg *= 2

        # 전투 첫 턴
        monster.get_damaged(max(1, first_dmg - monster.defense))
        if monster.cur_hp <= 0:
            player.win(monster)
            return True

        player.get_damaged(
            max(1, monster.damage - player.defense - player.armor), monster
        )
        if player.cur_hp <= 0:
            monster.cur_hp = monster.max_hp
            return False

        # 남은 전투 시작
        damage_give = max(1, player.damage + player.weapon - monster.defense)
        damage_get = max(1, monster.damage - player.defense - player.armor)

        cnt_win = math.ceil(monster.cur_hp / damage_give)
        cnt_lose = math.ceil(player.cur_hp / damage_get)

        # 이김
        if cnt_win <= cnt_lose:
            player.get_damaged((cnt_win - 1) * damage_get, monster)
            player.win(monster)
            monster.die()
            return True
        # 짐
        else:
            monster.cur_hp = monster.max_hp
            player.die(monster)
            return False

    def obj_destroyed(self, r, c):
        self.obj_matrix[r][c] = None
        grid[r][c] = "."

    def play(self, commands):
        for cmd in commands:
            self.turn(cmd)
            if not self.playing:
                break
        else:
            self.game_over("Press any key to continue.")


n, m = map(int, input().split())
grid = [list(input().rstrip()) for _ in range(n)]
commands = input().rstrip()

traps = []

box_cnt = 0
monster_cnt = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == "B":
            box_cnt += 1
        elif grid[i][j] == "&":
            monster_cnt += 1
        elif grid[i][j] == "M":
            monster_cnt += 1
        elif grid[i][j] == "@":
            start_y, start_x = (i, j)
        elif grid[i][j] == "^":
            traps.append((i, j))

game_manager = GameManager(start_y, start_x)
player = Player()

for i, j in traps:
    game_manager.obj_matrix[i][j] = "^"

for _ in range(monster_cnt):
    # s: 이름, w: 공격력, a: 방어력, h: 체력, e: 경험치
    r, c, s, w, a, h, e = input().split()
    r, c, w, a, h, e = map(int, (r, c, w, a, h, e))
    game_manager.obj_matrix[r - 1][c - 1] = Monster(
        r - 1, c - 1, s, w, a, h, e, grid[r - 1][c - 1] == "M"
    )

for _ in range(box_cnt):
    # t: w=무기, a=방어구, o=장신구, s: 공격력 | 방어력 | 이름
    r, c, t, s = input().split()
    r, c = map(int, (r, c))
    if t != "O":
        s = int(s)
    game_manager.obj_matrix[r - 1][c - 1] = Item(r - 1, c - 1, t, s)

grid[start_y][start_x] = "."
game_manager.play(commands)
