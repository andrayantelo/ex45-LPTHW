import scene as sc
from ..utils import cool_print
import textwrap


class LivingRoom(sc.Scene):
    
    def __init__(self):
        super(LivingRoom, self).__init__()
        self.living_text = textwrap.dedent(
        """ \n
        One lovely Sunday morning, Piet was napping peacefully 
        in his dog bed dreaming about the dog park. He jolted awake when 
        he heard the sound of house keys jingling and ran towards
        the front door. The door clicked shut softly just as he got there
        and Piet knew that his owners had just left him home alone. Despite
        having several rooms, the only room available to Piet in the house
        is the living room. Piet stared at the front door for a bit and
        then noticed that his owner had forgotten his wristwatch.
        """)
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
        self.look_text = textwrap.dedent(
        """ \n
        Piet looks around the living room and notices that the window
        looking out at the backyard is open. Piet's ears perk up as he runs
        over to the window. He stops short in front of the window and looks 
        out hesitantly. A soft cool breeze beckons him and he could hear birds
        chirping in the trees and leaves rustling in the wind. He sniffs
        the air and smells all sorts of wonderful smells. 
        """)
        self.jump_text = textwrap.dedent("""
        Piet goes and retrieves his dog purse then
        he turns to face the window. He musters up all of his strength and sprints
        forward leaping out the open window.
        """)
        self.dig_text = textwrap.dedent("""
        There is nowhere to dig!"""
        )
        self.items = ['medpack', 'wristwatch']
        self.amount_sniff_commands = []
        self.amount_gather_commands = []
        
    def enter(self, player):
        super(LivingRoom, self).enter(player)
        
        cool_print(self.living_text)
        
        while True:
            command = str(raw_input("Type a command.\n> "))
            
        
            action = self.parse_command(command)
            
            if action == sc.SNIFF and len(self.amount_sniff_commands) < 1:
                self.amount_sniff_commands.append(1)
                print textwrap.dedent("""
                Piet sniffs around the living room and finds a medpack
                hidden behind the couch. He places it in his purse.
                """)
                player.items.append('medpack')
                continue
            
            if action == sc.GATHER and len(self.amount_gather_commands) < 1:
                self.amount_gather_commands.append(1)
                print textwrap.dedent(""" 
                The only thing around to pick up is the wristwatch. Piet gingerly
                grasps it in his mouth and places it in his dog purse which he
                wears around his neck.
                 """)
                player.items.append('wristwatch')
                continue
                
            self.process_action(command, player)
            
            if action == sc.JUMP:
                return 'backyard'
                
