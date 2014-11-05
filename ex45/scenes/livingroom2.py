import scene as sc
from ..utils import cool_print
import textwrap

class LivingRoom2(sc.Scene):
    
    def __init__(self):
        super(LivingRoom2, self).__init__()
        self.living2_text = textwrap.dedent("""
        Piet is back in the living room.
        """)
        self.wristwatch_text = textwrap.dedent("""
        Piet grabs his owner's wristwatch and places it in his purse.""")
        self.gather_text = textwrap.dedent("""
        Piet picks up his toy and places it in his purse.""")
        self.sleep_text = textwrap.dedent(
        """ \n
        Piet whimpered at the door a little bit. Then he curled up into
        a little ball and shut his eyes. 'Maybe if I go to sleep the time
        will go faster and when I wake up they will be home,' he thought as
        he drifted off to sleep.
        """)
        self.play_text = textwrap.dedent(
        """ \n
        Piet attacks his chew toy and plays with it a little. Then
        he gets bored and looks back at the front door.
        """)
        self.scratch_text = textwrap.dedent(
        """ \n
        Piet scratches at the door but gets tired of it quickly. He
        already knew that didn't bring his owners back.
        """)
        self.look_text = textwrap.dedent("""
        Piet looks out the window and sees the cat staring back at him.
        """)
        self.jump_text = textwrap.dedent("""
        Piet musters up all of his strength and sprints
        forward leaping out the open window.
        """)
        self.dig_text = textwrap.dedent("""
        There is nowhere to dig!"""
        )
        self.items = ['medpack', 'wristwatch']
        self.treats_amount = []
        
    def enter(self, player):
        super(LivingRoom2, self).enter(player)
        
        cool_print(self.living2_text)
        
        while True:
            command = str(raw_input("Type a command.\n> "))
            
        
            action = self.parse_command(command)
            
            if action == sc.SNIFF and len(self.treats_amount) < 1:
                self.treats_amount.append(1)
                print textwrap.dedent("""
                Piet finds a hidden treat!""")
                player.items.append('treat')
                continue
            
            if action == sc.GATHER:
                if 'wristwatch' not in player.items:
                    print self.wristwatch_text
                    player.items.append('wristwatch')
                    continue
                else:
                    self.process_action(command, player)
                    player.items.append('ball')
                    continue
                    
            self.process_action(command, player)
            
            if action == sc.JUMP:
                return 'backyard'
