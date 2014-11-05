import scene as sc
from ..utils import cool_print
import textwrap


class Clearing(sc.Scene):
    
    def __init__(self):
        super(Clearing, self).__init__()
        self.clearing_text = textwrap.dedent(
        """ \n
        The clearing is large and covered in dirt and shrubs. Piet sees
        a small tunnel to the left and a dirt trail on the right.
        """)
        self.trail_text = textwrap.dedent("""
        Piet heads over to the trail.""")
        self.tunnel_text = textwrap.dedent("""
        Piet heads over to the tunnel entrance.""")
        
    def enter(self, player):
        super(Clearing, self).enter(player)
        
        cool_print(self.clearing_text)
        
        while True:
            command = str(raw_input("Type a command.\n> "))
            
        
            action = self.parse_command(command)
            self.process_action(command, player)
            
            if action == sc.TRAIL:
                return 'trail'
            if action in [sc.TUNNEL, sc.ENTER]:
                return 'tunnel'
