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
        self.gather_text = textwrap.dedent(""" 
                The only thing around to pick up is the wristwatch. Piet gingerly
                grasps it in his mouth and places it in his dog purse which he
                wears around his neck.
                 """)
        self.original_sniff = self.sniff_text
        self.sniff_text = textwrap.dedent("""
                Piet sniffs around the living room and finds a medpack
                hidden behind the couch. He places it in his purse.
                """)
        self.items = ['medpack', 'wristwatch']
        self.enter = self.enter1
        
    def exit_livingroom(self):

        self.living_text = textwrap.dedent("""
        Piet is back in the living room.
        """)
        self.wristwatch_text = textwrap.dedent("""
        Piet grabs his owner's wristwatch and places it in his purse.""")
        self.gather_text = textwrap.dedent("""
        Piet picks up his toy and places it in his purse.""")
        self.look_text = textwrap.dedent("""
        Piet looks out the window and sees the cat staring back at him.
        """)
        self.jump_text = textwrap.dedent("""
        Piet musters up all of his strength and sprints
        forward leaping out the open window.
        """)
        self.sniff_text = textwrap.dedent("""
                Piet finds a hidden treat!""")
        self.items += ['ball', 'treat']
        self.enter = self.enter2
        
    def enter1(self, player):
        super(LivingRoom, self).enter(player)
        
        cool_print(self.living_text)
        
        while True:
            command = str(raw_input("Type a command.\n> "))
            
        
            action = self.parse_command(command)
            
            if action == sc.SNIFF and 'medpack' in self.items:
                self.items.remove('medpack')
                player.items.append('medpack')
            
            elif action == sc.GATHER and 'wristwatch' in self.items:
                self.items.remove('wristwatch')
                player.items.append('wristwatch')
                
            self.process_action(command, player)
            
            if action == sc.JUMP:
                self.exit_livingroom()
                return 'backyard'
                
    def enter2(self, player):
        super(LivingRoom, self).enter(player)
        
        
        while True:
            command = str(raw_input("Type a command.\n> "))
            
        
            action = self.parse_command(command)
            
            if action == sc.SNIFF and 'treat' in self.items:
                self.items.remove('treat')
                player.items.append('treat')
                self.process_action(command, player)
                self.sniff_text = self.original_sniff
            
            elif action == sc.GATHER:
                if 'wristwatch' not in player.items:
                    print self.wristwatch_text
                    player.items.append('wristwatch')
                    self.process_action(command, player)
                else:
                    self.process_action(command, player)
                    player.items.append('ball')
                    self.process_action(command, player)
            
            else:
                self.process_action(command, player)
                    
            if action == sc.JUMP:
                return 'backyard'
                
         
                
                
            

                
