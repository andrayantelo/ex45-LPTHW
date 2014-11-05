import scene as sc
from ..utils import cool_print
import textwrap


class Death(sc.Scene):
    
    def __init__(self):
        self.death_text = textwrap.dedent("""
        Unfortunately, the decisions Piet has made have led him to his
        untimely death. Game over!
        """)
        
    def enter(self, player):
        cool_print(self.death_text)
        sys.exit()
        
