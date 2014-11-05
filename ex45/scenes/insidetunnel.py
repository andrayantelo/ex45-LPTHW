import scene as sc
from ..utils import cool_print
import textwrap


class InsideTunnel(sc.Scene):
    
    def __init__(self):
        super(InsideTunnel, self).__init__()
        self.inside_tunnel = textwrap.dedent(
        """ \n
        Piet switches on his headlamp and advances into the tunnel. It 
        was pitch black in there. Piet felt relieved that the hawk had given
        him the lamp. He walks cautiously inside the tunnel but did not see 
        much besides a couple of rocks. Slowly, Piet begins to run a little bit. 
        'There doesn't seem to be anything in here anyway! Maybe I can sprint
        to the end' So, Piet begins to sprint, dodging a couple of stones here and there. 
        Suddenly, Piet can see a light at the end of the tunnel. It was still a 
        little distant but it was not far now. With a burst of adrenaline, 
        Piet begins to run just a little faster. Then, without warning, a 
        large object blocks the view of the light at the end of the tunnel. 
        Piet stops running abruptly. He shines his head lamp onto the object.
        It's a giant monster with eight spindly legs. A giant spider monster!
        Piet looks at it in horror.
        """)
        self.fight_text = textwrap.dedent("""
        The fight is on!""")
        self.look_text = textwrap.dedent("""
        Piet looks up into the spider's eight eyes.""")
        self.sniff_text = textwrap.dedent("""
        Piet sniffs and gags at the foul smell.""")
        self.play_text = textwrap.dedent("""
        It doesn't look like the spider wants to play.""")
        self.bark_text = textwrap.dedent("""
        Piet barks feebly.""")
        self.gather_text = textwrap.dedent("""
        Best not to touch the spider.""")
        
    def enter(self, player):
        super(InsideTunnel, self).enter(player)
        
        cool_print(self.inside_tunnel)
        player.headlamp_state = True
        player.player_in_dark = True
        print "Type 'continue' to continue"
        
        while True:
            command = str(raw_input("Type a command.\n> ")) 
                       
        
            action = self.parse_command(command)
            self.process_action(command, player)
            
            if action == sc.NOTHING:
                return 'death'
            elif action in [sc.FIGHT, sc.SWIPE, sc.ATTACK, sc.KICK, sc.BITE, sc.CONTINUE]:
                return 'fight'
