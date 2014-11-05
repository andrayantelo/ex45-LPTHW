import scene as sc
from ..utils import cool_print
import textwrap

class EnchantedForestPartTwo(sc.Scene):
    
    def __init__(self):
        super(EnchantedForestPartTwo, self).__init__()
        self.enchantedforest2_text = textwrap.dedent(
        """ \n
        Piet decides to continue following the trail. Piet walks and 
        walks all day long. At one point he passes a small creek he gets
        a drink of water. Suddenly, Piet hears running footsteps.
        He could tell they were human. Piet runs towards the sound and comes
        across a man running. 'Whoa!' the man exclaims in surprise at the
        sight of Piet. Piet jumps up on the man and cries excitedly. 'Hey,
        there, Puppy! Where are your owners?' The man asks gently. The man 
        picks Piet up and takes a look at his collar. 'Don't worry, boy, 
        I'll get you home soon.' The man takes Piet home and gives him some 
        food. The man had a dog at home too and Piet was excited to play. 
        After a couple of hours there is a knock at the door. When the man 
        opens the door Piet hears a familiar sound. 'It's my owner!' Piet 
        sprints to the door and leaps into his owner's arms. He lickes his face
        all over. 'Piet, where have you been!' His owner exclaimed. Piet
        barked excitedly and spun around in a circle. He was going home.
        """)
        
        
    def enter(self, player):
        super(EnchantedForestPartTwo, self).enter(player)
        
        cool_print(self.enchantedforest2_text)
        
        return 'home'
