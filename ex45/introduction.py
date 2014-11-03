from scene import *

class Introduction(Scene):
    
    def __init__(self):
        super(Introduction, self).__init__()
        self.intro_text = textwrap.dedent(
        """\n\n
        Once upon a time there lived a little black and white dog
        named Piet. He was a small poodle/schnauzer mix with soft curly
        fur and a big heart. He had two lovely owners who loved him very
        much. Piet was very protective of his owners and his friends. He 
        was a very loyal dog. Some say, he was the most loyal dog in the 
        world.""")
        self.dig_text = textwrap.dedent("""
        There is nowhere to dig.""")
        
    def enter(self, player):
        super(Introduction, self).enter(player)
        cool_print(self.intro_text)
        
        print "To check health status type \"health status\""
        print "To check item inventory type \"display items\""
        print "To quit type 'quit'"
        print "Type 'continue' to continue"
        
        while True:
            command = str(raw_input("\n> "))
            
        
            action = self.parse_command(command)
            self.process_action(command, player)
            if action == CONTINUE:
                return 'living_room'
