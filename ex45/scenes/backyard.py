import scene as sc
from ..utils import cool_print
import textwrap
          

class Backyard(sc.Scene):
    
    def __init__(self):
        super(Backyard, self).__init__()
        self.backyard_text = textwrap.dedent(
        """ \n
        Piet lands clumsily on his four paws and looks back up at the
        open window. The window is low enough to the ground that he could
        easily go back inside if he wanted to. Piet feels reassured at this
        thought as he turns around to face the backyard. The backyard is 
        quite large. Much bigger than the living room. The lawn is overgrown
        and there is a gigantic cracked bird fountain in the middle.  Piet 
        begins to march forward sniffing at the ground but stops short when
        he hears a loud noise. 
        'HISSSSSSSSSSS'
        Piet looks up. A large spotted cat eyes him menacingly. This was the 
        largest cat Piet had ever seen in his entire life. The cat has the look
        of a seasoned war veteran. There were scars etched in the fur of its
        face and it had a few bald spots. The cat arches its back and stares
        at Piet with wide eyes.
        """)
        self.fight_text = textwrap.dedent("""
        Piet decides he can fight this cat.
        """)
        self.run_text = textwrap.dedent(
        """ \n
        Piet decides to run past the cat. Piet is one of the fastest 
        dogs in the neighborhood, frequently outrunning other dogs at the
        dog park. His owners also liked to take him jogging with them which
        kept Piet in tip top shape! Piet began to run towards the cat, which 
        catches the cat off gaurd. The cat freezes in place mid-swipe. Just 
        as Piet is about to crash into the cat he veers left and flies past
        it towards the back fence. Piet takes a literal leap of faith and flies
        over the fence landing on the other side. The cat speeds off to 
        the neighbor's yard.
        """)
        self.inside_text = textwrap.dedent(
        """ \n
        Piet jumps back inside through the open window. The cat looks 
        at Piet for a minute safely inside then curls up and lays down in 
        the grass staring at Piet. Piet realizes the cat was going to stay
        there all day waiting for him. 
        """
        )
        self.nothing_text = textwrap.dedent(
        """ \n
        Piet stands in front of the cat frozen in fear. The cat swipes
        at Piet with its claws. Piet yelps as the cat continues to swipe.
        Eventually, the cat leaves Piet alone to die.
        """)
        self.look_text = textwrap.dedent("""
        Piet looks around but sees nothing he could use as a weapon.""")
        self.sniff_text = textwrap.dedent("""
        Piet sniffs the air but can only smell cat.""")
        self.play_text = textwrap.dedent(""" 
        Piet attemps to play with the cat but the cat swipes at him with it's
        claws and barely misses Piet's face.""")
        self.bark_text = textwrap.dedent("""
        Piet barks loudly but the cat is unfazed.""")
        self.items = []
        self.number_of_fights = []
        
    def enter(self, player):
        super(Backyard, self).enter(player)
        
        cool_print(self.backyard_text)
        
        while True:
            command = str(raw_input("Type a command.\n> "))
            
        
            action = self.parse_command(command)
            self.process_action(command, player)
            if action == sc.RUN:
                return 'enchanted_forest'
            elif action == sc.NOTHING:
                return 'death'
            elif action == sc.INSIDE:
                return 'living_room'
            elif action in [sc.FIGHT, sc.SWIPE, sc.ATTACK, sc.KICK, sc.BITE, sc.CONTINUE]:
                return 'fight'
