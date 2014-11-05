import scene as sc
from ..utils import cool_print
import textwrap


class Tunnel(sc.Scene):
    
    def __init__(self):
        super(Tunnel, self).__init__()
        self.tunnelscene_text = textwrap.dedent(
        """ \n
        Piet walks over to the entrance of the tunnel. A loud squawk sound
        makes Piet freeze in his tracks. A large hawk swoops down and blocks
        the tunnel entrance. Piet swallows audibly and takes a
        step back. 'If you wish to use the tunnel you must correctly solve 
        this riddle.' the Hawk screeches. Piet nods slowly.
        
        'What gets wetter and wetter the more it dries?' The hawk cackles 
        as Piet looks at it stumped.
        """)
        self.fight_text = textwrap.dedent("""
        The hawk does not wish to fight. Besides Piet would be dead in a second.""")
        self.play_text = textwrap.dedent("""
        The hawk does not wish to play.""")
        self.towel_text = textwrap.dedent(
        """ \n
        The hawk squealed in excitement. 'That's a first!' He squawked
        as he tossed something at Piet. Piet sniffed at it. It was a small 
        head lamp, and it fit perfectly around Piet's head. 'Thanks, Mr. 
        Hawk,' Piet said politely. The Hawk rolled it's eyes and stepped 
        aside so that Piet could enter the dark tunnel. 
        """)
        self.wrong_guess = textwrap.dedent(""" 
        Sorry, Dog, that's the wrong answer!""")
        self.last_guess = textwrap.dedent(
        """ \n
        'Sorry, Dog, that's the wrong answer!' The hawk cackles. Then 
        he swoops in and grabs Piet with his enormous claws. Piet shrieks
        as the hawk carries him off to a large nest where hungry baby hawks
        are waiting.
        """)
        self.enter_text = """
        You can't enter yet."""
        self.guesses = []
        
        self.items = ['head lamp']
        
    def enter(self, player):
        super(Tunnel, self).enter(player)
        
        cool_print(self.tunnelscene_text)
        
        while True:
            command = str(raw_input("Type a command.\n> "))
            self.guesses.append(1)
            
            if len(self.guesses) == 3:
                cool_print(self.last_guess)
                return 'death'
        
            action = self.parse_command(command)
            self.process_action(command, player)
            
            if action == sc.TOWEL:
                player.items.append('headlamp')
                return 'inside_tunnel'
            else:
                cool_print(self.wrong_guess)
                numberofguesses = 3 - len(self.guesses)
                print "%s guesses left!" % numberofguesses
