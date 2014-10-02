SNIFF = 'sniff'
LOOK = 'look'
NOTHING = 'nothing'
PLAY = 'play'
DIG = 'dig'
BARK = 'bark'
ROLL = 'rollover'
WALK = 'walk'
RUN = 'run'
STAND = 'stand'
FIND = 'find'
SLEEP = 'sleep'
SCRATCH = 'scratch'
FIGHT = 'fight'
INSIDE = 'inside'
BACK = 'back'
FORWARD = 'forward'
ITEMS = 'items'
ENTER = 'enter'
TRAIL = 'trail'
SWORD = 'sword'
SWIM = 'swim'
BOAT = 'boat'
DRINK = 'drink'


def parse_commands(command):
    command_dictionary = {'sniff': self.sniff_text,
                          'look': self.look_text,
                          'nothing': self.nothing_text,
                          'play': self.play_text,
                          'dig': self.dig_text,
                          'bark': self.bark_text,
                          'roll': self.roll_text,
                          'walk': self.walk_text,
                          'run': self.run_text,
                          'stand': self.stand_text,
                          'find': self.find_text,
                          'inside': self.inside_text,
                          'back': self.back_text,
                          'forward': self.forward_text,
                          'items': self.display_items_text,
                          'enter': self.enter_tunneltext,
                          'trail': self.trail_text,
                          'sword': self.use_sword,
                          'swim': self.swim_text,
                          'boat': self.use_boat,
                          'drink': self.drink_water
                          }
                          
    print command_dictionary.get(command)
        
