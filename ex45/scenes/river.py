import scene as sc
from ..utils import cool_print
import textwrap


class River(sc.Scene):
    
    def __init__(self):
        super(River, self).__init__()
        self.river_text = textwrap.dedent(
        """ \n
        Piet emerges from the tunnel into the blinding sunlight. He shuts
        his headlamp off and puts it away in his purse. He has emerged into a
        very small clearing with a river right in front of him.
        """)
        self.swim_text = textwrap.dedent(
        """ \n
        Piet leaps into the water and begins to swim across. The current
        was really strong and Piet struggled to swim to the other side. Eventually,
        Piet had no strength left and he let the river carry him far far away.
        Piet was never to be seen or heard of again. 
        """)
        self.look_text = textwrap.dedent(
        """ \n
        Piet looks around and finds a small dog size boat anchored to 
        the river bed.
        """)
        self.boat_text = textwrap.dedent(
        """ \n
        Piet leaps into the boat pulls up the anchor. Then he grabs a 
        paddle with his mouth and begins to paddle across the river.
        """)
        self.drink_water = textwrap.dedent("""
        Piet takes a couple of sips of the fresh river water.
        """)
        
    def enter(self, player):
        super(River, self).enter(player)
        player.player_in_dark = False
        player.headlamp_state = False
        
        cool_print(self.river_text)
        
        while True:
            command = str(raw_input("Type a command.\n> "))            
        
            action = self.parse_command(command)
            self.process_action(command, player)
            
            if action == sc.SWIM:
                return 'death'
            elif action == sc.LOOK:
                player.items.append('boat')
            elif action == sc.BOAT and 'boat' in player.items:
                cool_print(self.boat_text)
                return 'dogpark'
            elif action == sc.DRINK:
                player.status = player.status + 1
