from nose.tools import *
from ex45.characters import Character
from ex45.characters import Player
from ex45.characters import Villain

def test_obtain_item():
    a_player = Player()
    item = 'sword of fury'
    a_player.obtain_item(item)
    assert_in(item, a_player.items)

def test_attack():
    a_player = Player()
    a_villain = Villain()
    
    a_player.attack(a_villain)
    assert_equal(a_villain.status, a_villain.health_status())
    
def test_no_medpack():
    a_player = Player()
    a_player.use_medpack()
    assert_equal(a_player.status, 3)

def test_medpack():
    a_player = Player()
    a_player.status = 2
    a_player.items.append('medpack')
    a_player.use_medpack()
    assert_equal(a_player.status, 3)
    assert_notin('medpack', a_player.items)


