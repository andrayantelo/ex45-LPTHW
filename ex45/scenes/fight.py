import scene as sc
from ..utils import cool_print
import textwrap
from ..characters import Villain


class Fight(sc.Scene):
    
    def __init__(self):
        super(Fight, self).__init__()
        self.swipe_text = textwrap.dedent("""
        Piet takes a swipe at his enemy.""")
        self.kick_text = textwrap.dedent("""
        Piet kicks at his enemy with his hind legs.""")
        self.bite_text = textwrap.dedent("""
        Piet sinks his teeth into one of his enemy's limbs and doesn\'t 
        let go.
        """)
        self.fight_text = textwrap.dedent("""
        Piet punches his enemy in the face.""")
        self.attack_text = textwrap.dedent("""
        Piet lunges forward to attack.""")
        self.look_text = textwrap.dedent("""
        Piet looks into the eyes of his enemy and nearly wets himself.""")
        self.sniff_text = textwrap.dedent("""
        The stench of Piet's own fear wafts through the air.""")
        self.play_text = textwrap.dedent("""
        Attempting to distract the enemy, Piet gets into a playful stance.
        The enemy laughs then quickly snarls and Piet recoils in fear.""")
        self.sleep_text = textwrap.dedent("""
        No time to sleep now! Must fight!""")
        self.backyard_fight_text = textwrap.dedent("""
        Piet may be small but he thinks he is the biggest dog in the world.
        \"I can take that cat,\" Piet thinks arrogantly to himself. Piet puffs 
        up his chest and lets out a loud bark. The cat looks at him incredulously,
        as if it's about to laugh. Then charges Piet, claws out.
        """)
        self.tunnel_fight_text = textwrap.dedent("""
        Piet barks loudly but the spider is unfazed. The spider begins to advance.
        """)
        self.enemy = Villain()

        
    #def parse_command(self, command):
     #   super(Fight, self).parse_command(command)
     #   
     #   if any(w in words for w in ('attack', 'strike', 'charge', 'rush')):
     ##       action = ATTACK
      #  return action
        
    #def process_action(self, command, player):
    #    super(Fight, self).process_action(command, player)
    #    
    #    if any(w in action for w in (FIGHT, SWIPE, KICK, BITE, ATTACK)):
    #        player.attack(self.cat)
                
    def enter(self, player):
        print "Type 'medpack' to use a medpack"
        player.display_items()
        player.fight_scene_count = player.fight_scene_count + 1
        
        if player.fight_scene_count == 1:
            cool_print(self.backyard_fight_text)
            self.enemy.name_villain('Cat')
        elif player.fight_scene_count == 2:
            cool_print(self.tunnel_fight_text)
            self.enemy.name_villain('Spider')
        
        while True:
            if player.status == 0:
                return 'death'
            elif self.enemy.status == 0 and player.fight_scene_count == 1:
                print 'You have defeated the enemy!'
                self.enemy.status = 3
                return 'enchantedforest'
            elif self.enemy.status == 0 and player.fight_scene_count == 2:
                print "You have defeated the enemy!"
                self.enemy.status = 3
                return 'river'
                
            player.health_status()
            command = str(raw_input("Type a command.\n> "))
            
            action = self.parse_command(command)
            self.process_action(command, player)
            
            if any(w in action for w in (sc.ATTACK, sc.FIGHT, sc.BITE, sc.SWIPE, sc.KICK)):
                player.attack(self.enemy)
            elif action not in [sc.ATTACK, sc.FIGHT, sc.BITE, sc.SWIPE, sc.KICK, sc.HEALTH,
                                 sc.ITEMS, sc.MEDPACK, sc.HEADLAMP]:
                self.enemy.damage_player(player)
            elif player.headlamp_state == False:
                self.enemy.damage_player(player)
                print "\"I can't see!\""
                # I want to piet to miss all his hits when headlamp is off
                continue
            if player.status == 0:
                print "%s has defeated you!" % self.enemy.name
                return 'death'
