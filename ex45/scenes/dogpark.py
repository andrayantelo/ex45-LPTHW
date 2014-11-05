import scene as sc
from ..utils import cool_print
import textwrap


class DogPark(sc.Scene):
    
    def __init__(self):
        super(DogPark, self).__init__()
        self.dogpark_text = textwrap.dedent(
        """ \n
        Piet arrives on the other side of the river and sees that he has
        reached his favorite dog park in the whole wide world. He could see dogs
        running around playing with their owners. In his excitement, he jumps 
        out of the boat before anchoring it. The boat floats away but Piet
        was too distracted by all the other dogs to notice or care.
        """)
        self.play_text = textwrap.dedent(
        """ \n
        Piet sniffs at the nearest dogs and begins to play with them. 
        He is having so much fun he forgets all about his owners. Eventually, 
        the humans begin to notice that Piet is there all by himself. One 
        human takes it upon herself to make sure Piet gets home. She takes a 
        look at his collar. About half an hour later Piet hears a familiar sound.
        "Piet!" Piet whips his head around and sure enough it's his owner calling
        him. Piet sprints towards his owner and leaps into his arms. He
        was so happy to finally have found him. He takes the wristwatch out
        of his purse and drops it in front of his owner. "Oh good boy! I 
        thought I had lost this forever!' Piet's owner puts his wristwatch on, 
        then he picks Piet up and they go back home.
        """)
        self.look_text = textwrap.dedent(
        """ \n
        Piet looks around and sees a dog treat nestled in the grass.
        He gobbles it up hungrily.
        """)
        self.sniff_text = textwrap.dedent("""
        Piet can smell hundreds of different dogs.""")
        self.run_text = textwrap.dedent("""
        Piet picks a random dog and starts running wildly around behind it. 
        They begin a long game of chase.""")
        self.jump_text = textwrap.dedent("""
        Piet jumps over another dog.""")
        
        
    def enter(self, player):
        super(DogPark, self).enter(player)
        
        cool_print(self.dogpark_text)
        
        while True:
            command = str(raw_input("Type a command.\n> ")) 
                       
        
            action = self.parse_command(command)
            self.process_action(command, player)
            
            if action == sc.PLAY:
                return 'home'
