import scene as sc
from ..utils import cool_print
import textwrap
 

class Home(sc.Scene):
    
    def __init__(self):
        super(Home, self).__init__()
        self.home_text = textwrap.dedent("""
        Piet has returned home with his owners.""")
        self.sniff_text = textwrap.dedent("""
        Piet sniffs around the living room and finds a long lost treat!
        He quickly gobbles it up before his owners see.""")
        self.look_text = textwrap.dedent("""
        Piet looks around the room and sees his owners relaxing on the couch.
        """)
        self.jump_text = textwrap.dedent("""
        Piet jumps up on the couch next to his owners. His owners tell him
        to get off the couch. Then they tell him that he can't come up 
        without being told to come up. They pat the couch and Piet excitedly
        jumps up on the couch with them.""")
        self.play_text = textwrap.dedent("""
        Piet grabs his ball and begins to play. His owners laugh joyfully 
        at him.""")
        self.run_text = textwrap.dedent("""
        Piet runs around the room barking happily.""")
        self.stand_text = textwrap.dedent("""
        Piet stands still.""")
        self.sleep_text = textwrap.dedent("""
        Piet curls up in his bed and takes a nap.""")
        self.scratch_text = textwrap.dedent("""
        Piet begins to scratch at the carpet. \"No!\" his owners yell at him.
        Piet stops and looks sheepish.""")
        self.givewristwatch_text = textwrap.dedent("""
        Piet suddenly remembers his owner's wristwatch and brings it to him.
        His owner exclaims in surprise, "Good boy! I've been looking for my
        watch!" Then they hug.""")
        self.giving_amount = []
        
    def enter(self, player):
        super(Home, self).enter(player)
        
        cool_print(self.home_text)
        print "To quit type 'quit'"
        while True:
            command = str(raw_input("Type a command.\n> "))
            
        
            action = self.parse_command(command)
            
            if action == sc.GIVE and len(self.giving_amount) < 1 and 'wristwatch' in player.items:
                self.giving_amount.append(1)
                cool_print(self.givewristwatch_text)
                player.items.remove('wristwatch')
                continue
                
            self.process_action(command, player)
