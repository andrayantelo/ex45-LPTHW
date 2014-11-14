import random

class Character(object):
    
    def __init__(self):
        self.items = []
        self.status = 3
        self.fight_scene_count = []
        self.name = 'name'
        
    def health_status(self):
        heart = u'\u2764'
        empty_heart = u'\u2661'
        print "%s\'s current health status:" % self.name
        if self.status == 3:
            print heart, heart, heart
        if self.status == 2: 
            print heart, heart, empty_heart
        if self.status == 1:
            print heart, empty_heart, empty_heart
        if self.status == 0:
            print empty_heart, empty_heart, empty_heart
        return self.status

class Player(Character):
    
    def __init__(self):
        super(Player, self).__init__()
        self.items = []
        self.status = 3
        self.fight_scene_count = 0
        self.name = 'Piet'
        self.headlamp_state = False
        self.player_in_dark = False
        
    
    def obtain_item(self, thing):
        self.items.append(thing)
        return self.items
    
    def display_items(self):
        print "You currently have the following items:"
        print self.items
        
    def attack(self, villain):
        if self.headlamp_state == False and self.player_in_dark:
            print "Piet missed!"
        else:
            print "attack method worked"
            if villain.status > 1:
                villain.status = villain.status - 1
            elif villain.status == 1:
                villain.status = villain.status - 1
                print "You have slain the villain!"
        villain.health_status()
        
    def use_medpack(self):
        medpack = 'medpack'
        if medpack in self.items and self.status != 3:
            print "Piet uses a medpack."
            self.status = self.status + 1
            self.items.remove('medpack')
        elif self.status == 3:
            print "Health status is full."
        elif medpack not in self.items:
            print "%s has no medpacks." % self.name
            
    def use_sword(self, villain):
        if self.headlamp_state == False and self.player_in_dark:
            print "Piet missed!"
        else:
            sword_text = textwrap.dedent("""
            Piet pulls out his sword and grips it in his mouth. He slashed 
            the sword at his enemy.""")
            sword = 'sword'
            if sword in self.items:
                print sword_text
                villain.status = villain.status - 1
            else:
                print "Piet doesn't have a sword."
            
    def eat_treat(self):
        treat_text = textwrap.dedent("""
        Piet gets out a treat and gobbles it up in 2.5 seconds.""")
        treat = 'treat'
        if treat in self.items:
            print treat_text
            self.items.remove(treat)
        else:
            print "Piet doesn't have any treats!"
            
    def use_headlamp(self):
        print self.headlamp_state
        off_text = textwrap.dedent("""
        Piet switches his headlamp off.""")
        on_text = textwrap.dedent("""
        Piet switches his headlamp on.""")
        headlamp = 'headlamp'
        if headlamp not in self.items:
            print "Piet does not have a headlamp."
        else:
            if self.headlamp_state == False:
                print on_text
                self.headlamp_state = True
            elif self.headlamp_state == True:
                print off_text
                self.headlamp_state = False
        
        return self.headlamp_state
        
    def use_ball(self):
        if 'ball' in self.items:
            print "Piet takes out a ball and tosses it in the air."
        else:
            print "Piet doesn't have a ball."
        
class Villain(Character):
     
    def __init__(self):
        super(Villain, self).__init__()
        self.name = 'name'
        
    def name_villain(self, name):
        self.name = name
        return self.name # is this necessary?
        
    def damage_player(self, player):
        attacks = ['swipe', 'hit', 'kick', 'punch', 'scratch', 'bite']
        current_attack = random.choice(attacks)
        print "%s has hit you with a %s attack!" %(self.name, current_attack)
        player.status = player.status - 1
        return player.status
