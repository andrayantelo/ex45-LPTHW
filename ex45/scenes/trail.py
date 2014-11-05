import scene as sc
from ..utils import cool_print
import textwrap


class Trail(sc.Scene):
    
    def __init__(self):
        super(Trail, self).__init__()
        self.trailscene_text = textwrap.dedent(
        """ \n
        Piet heads over to the trail and begins to follow it. He 
        sniffs the ground as he walks but does not smell anything familiar. All 
        the smells were very interesting, of course, but nothing smelled
        remotely like his owners. Piet trudged along for what seemed like 
        hours. Suddenly, Piet noticed that the sun was going down. 
        'Is it really that late already?' he whimpered. Piet laid down to 
        sleep and slept like a log. The next morning he awoke to the sounds 
        of birds chirping in the trees. Piet looked around. Yes, he was still
        in The Enchanted Forest. Piet could either go forward or he could go 
        back the way he came.
        """)
        self.sniff_text = textwrap.dedent("""
        Piet uncovers a medpack!""")
        self.items = ['medpack']
        self.forward_text = textwrap.dedent("""
        Piet continues onward.""")
        self.back_text = textwrap.dedent("""
        Piet retraces his steps.""")
        
    def enter(self, player):
        super(Trail, self).enter(player)
        
        cool_print(self.trailscene_text)
        
        while True:
            command = str(raw_input("Type a command.\n> "))
            
        
            action = self.parse_command(command)
            self.process_action(command, player)
            
            if action == sc.SNIFF:
                player.items.append('medpack')
            if action == sc.FORWARD:
                return 'enchantedforest_2'
            if action == sc.BACK:
                return 'clearing'
