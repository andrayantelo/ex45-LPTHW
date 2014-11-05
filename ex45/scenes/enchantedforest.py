import scene as sc
from ..utils import cool_print
import textwrap



class EnchantedForest(sc.Scene):
    
    def __init__(self):
        super(EnchantedForest, self).__init__()
        self.enchanted_text = textwrap.dedent(
        """ \n
        On the other side of the backyard's fence Piet finds himself at the border
        of the Enchanted Forest. All the dogs referred to the forest as \"The
        Enchanted Forest\" on account of all the strange things that happened
        to the dogs that dared to enter it alone, but he had often heard 
        his owners refer to it with the words \"The Greenbelt\". Piet stops at 
        the edge of the woods and contemplates his options. He could go back
        into the yard now that the cat was gone, but his owners weren't 
        there anyway.
        """)
        self.back_text = textwrap.dedent(
        """ \n
        Piet turns around and heads back inside like a coward. The cat
        was no longer in the yard. Who knew where his owners were. Piet 
        sat down and cried.
        """)
        self.forward_text = textwrap.dedent(
        """ \n
        'I will find my owners!' Piet thinks to himself, determined to
        find them. Piet enters the Enchanted Forest and walks along the dirt
        past trees and shrubs. Eventually he reaches a large clearing.
        """)
        self.original_sniff = self.sniff_text
        self.sniff_text = textwrap.dedent(
        """ 
        Piet finds a medpack nestled in the dirt. Acquired medpack!
        """)
        self.original_look = self.look_text
        self.look_text = textwrap.dedent(
        """ \n
        Piet notices something shiny near some rocks. It's a small
        sword with a handle shaped perfectly to be held in a dog's mouth.
        You have acquired a sword!
        """)
        self.bark_text = textwrap.dedent(
        """ \n
        Piet barks three times and waits. At first he does not hear 
        anything and then he hears a loud hissing. His barking has attracted
        a large Coral Snake!
        """)
        self.items = ['medpack', 'sword']
        
        
    def enter(self, player):
        super(EnchantedForest, self).enter(player)
        
        cool_print(self.enchanted_text)
        
        while True:
            command = str(raw_input("Type a command.\n> "))
            
        
            action = self.parse_command(command)
            self.process_action(command, player)
            
            if action in [sc.BARK, sc.BACK]:
                return 'death'
            elif action == sc.FORWARD:
                return 'clearing'
            elif action == sc.SNIFF and 'medpack' in self.items:
                self.items.remove('medpack')
                player.items.append('medpack')
                self.sniff_text = self.original_sniff
            elif action == sc.LOOK and 'sword' in self.items:
                self.items.remove('sword')
                player.items.append('sword')
                self.look_text = self.original_look
