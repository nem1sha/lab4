class Australopithecus:
    level = 1

    def __init__(self):
        self.hp = 100
        self.weight = 50
        self.high = 150
        self.intellect = 10

    def loot(self):
        print('STICKS', 'BONES', 'STONES')

    def hunt(self, other):
        print('ATTACK!!!')
        if self.weight > other.weight:
            print('BOOTY!!!')
        else:
            print('DIED...')

    def life_style(self):
        gregariousness = ['HERD', 'HUNT']
        return gregariousness


class HomoHabilis:
    level = 2

    def __init__(self):
        self.hp = 100
        self.weight = 55
        self.high = 150
        self.intellect = 30

    def loot(self):
        print('STONE TOOLS')

    def life_style(self):
        hunting = ['GROUP PROTECTION ', 'HUNTING']
        return hunting


class HomoErectus:
    level = 3

    def __init__(self):
        self.hp = 100
        self.weight = 60
        self.high = 160
        self.intellect = 60

    def loot(self):
        print('STONE TOOLS', 'FIRE')

    def life_style(self):
        live_in_case = 'CASE'
        return live_in_case


class Neanderthalensis:
    level = 4

    def __init__(self):
        self.hp = 100
        self.weight = 65
        self.high = 165
        self.intellect = 85

    def loot(self):
        print('COMPLEX TOOLS')

    def life_style(self):
        tribe = 'TRIBAL RELATIONS'
        return tribe

    def speech(self):
        non_articulate_speech = 'ЯУМЕТЬГОВОРИТЬ! ААААААрррррр...'
        return non_articulate_speech


class HomoSapiens:
    level = 5

    def __init__(self):
        self.hp = 100
        self.weight = 70
        self.high = 180
        self.intellect = 100

    def loot(self):
        return True

    def life_style(self):
        live = ['SOCIAL LABOR', 'DOMESTICATION', 'RITES']
        return live

    def speech(self):
        articulate_speech = 'Я УМЕЮ ГОВОРИТЬ'
        return articulate_speech


class Human(Australopithecus, HomoHabilis, HomoErectus, Neanderthalensis, HomoSapiens):

    def __init__(self):
        HomoSapiens.__init__(self)

    def upright_posture(self):
        return True


human_first = Australopithecus
human_second = HomoHabilis
human_third = HomoErectus
human_fourth = Neanderthalensis
human_fifth = HomoSapiens
human_main = Human
humans = [human_first, human_second, human_third, human_fourth, human_fifth]

print(human_first.hunt(human_first, human_third))

print(human_second.life_style())

print(human_third.loot())

print(human_main.life_style())

for human in humans:
    print(human.level)


