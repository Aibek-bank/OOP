""" ООП """
# 4 принципа
# 1 принцип: Наследование

# class Game:
#     def __init__(self, game_name, game_year, company, graphics):
#         self.game_name = game_name
#         self.game_year = game_year
#         self.company = company
#         self.graphics = graphics

#     def info(self):
#         print(f'Game - {self.game_name} - {self.game_year} - {self.company} - {self.graphics}')
# # game = Game("CsGo2", "2009", "Walf", "4K")
# # game.info()

# class Roblox(Game):
#     def __init__(self, game_name, game_year, company, graphics, multiplayer):
#         # super().__init__(game_name, game_year, company, graphics)
#         Game.__init__(self, game_name, game_year, company, graphics)
#         self.multiplayer = multiplayer
#         self.name = "Player"
#         self.gender = "None"
#         self.skin = "None"
#         self.hp = 100


#     def info(self):
#         print(f'Game - {self.game_name} - {self.game_year} - {self.company} - {self.graphics} - {self.multiplayer}')

#     def info_player (self):
#         print(f"Игрок - {self.name} - {self.gender} - {self.skin} - {self.hp}XP")

#     def edit_player(self):
#         name = input ("Введите имя игрока: ")
#         gender = input ("Введите пол игрока: ")
#         skin = input ("Введите облик игрока: ")
#         self.name = name
#         self.gender = gender
#         self.skin = skin

# roblox = Roblox("Roblox", 2006, "Roblox Corp.", "ULTRA", "Yes")
# roblox.info()
# roblox.edit_player()
# roblox.info_player()


# class Strike(Roblox):
#     def __init__(self, game_name, game_year, company, graphics, multiplayer):
#         super().__init__(game_name, game_year, company, graphics, multiplayer)

# print(bool("False"))





