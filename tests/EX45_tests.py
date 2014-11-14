from nose.tools import *
from ex45.ex45 import Map
from ex45.ex45 import Engine
import ex45.ex45
import ex45.scenes as sc
#from characters import Player

def test_map():
    a_map = Map("introduction")
    assert_is_instance(a_map.next_scene("introduction"), sc.Introduction)
    assert_is_instance(a_map.next_scene("living_room"), sc.LivingRoom)
    assert_is_instance(a_map.next_scene("backyard"), sc.Backyard)
    assert_is_instance(a_map.next_scene("enchantedforest"), sc.EnchantedForest)
    assert_is_instance(a_map.next_scene("clearing"), sc.Clearing)
    assert_is_instance(a_map.next_scene("trail"), sc.Trail)
    assert_is_instance(a_map.next_scene("tunnel"), sc.Tunnel)
    assert_is_instance(a_map.next_scene("inside_tunnel"), sc.InsideTunnel)
    assert_is_instance(a_map.next_scene("enchantedforest_2"), sc.EnchantedForestPartTwo)
    assert_is_instance(a_map.next_scene("river"), sc.River)
    assert_is_instance(a_map.next_scene("dogpark"), sc.DogPark)
    assert_is_instance(a_map.next_scene("death"), sc.Death)
    assert_is_instance(a_map.next_scene("fight"), sc.Fight)
    assert_is_instance(a_map.next_scene("home"), sc.Home)

def test_initialize_start_scene():
    a_map = Map("introduction")
    assert_equal(a_map.start_scene, "introduction")

def test_opening_scene():
    a_map = Map("introduction")
    opening_scene = a_map.opening_scene()
    assert_is_instance(opening_scene, sc.Introduction)
    assert_equal(opening_scene, a_map.next_scene('introduction'))

def test_engine():
    a_map = Map("introduction")
    an_engine = Engine(a_map)
    assert_is_instance(an_engine.game_map, Map)
    assert_equal(an_engine.game_map, a_map)
    
#def test_play():
#    a_player = Player()
#    a_map = Map("introduction")
#    an_engine = Engine(a_map)
    
def setup():
    print "SETUP!"
    
def teardown():
    print "TEAR DOWN!"
    
def test_basic():
    print "I RAN!"
