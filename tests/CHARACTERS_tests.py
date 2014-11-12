from nose.tools import *
from ex45.characters import Character
from ex45.characters import Player
from ex45.characters import Villain

def test_character():
    a_character = Character()
    a_character.items = ['test']
    assert_equal(a_character.items, ['test'])
