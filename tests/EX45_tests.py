from nose.tools import *
from ex45.ex45 import Map
from ex45.ex45 import Engine
import ex45.ex45
import ex45.scenes as sc

def test_map():
    a_map = Map("introduction")
    assert_is_instance(a_map.scenes.get("introduction"), sc.Introduction)
    assert_is_instance(a_map.scenes.get("living_room"), sc.LivingRoom)
    assert_is_instance(a_map.scenes.get("backyard"), sc.Backyard)
    assert_is_instance(a_map.scenes.get("enchantedforest"), sc.EnchantedForest)
    assert_is_instance(a_map.scenes.get("clearing"), sc.Clearing)
    assert_is_instance(a_map.scenes.get("trail"), sc.Trail)
    assert_is_instance(a_map.scenes.get("tunnel"), sc.Tunnel)
    assert_is_instance(a_map.scenes.get("inside_tunnel"), sc.InsideTunnel)
    assert_is_instance(a_map.scenes.get("enchantedforest_2"), sc.EnchantedForestPartTwo)
    assert_is_instance(a_map.scenes.get("river"), sc.River)
    assert_is_instance(a_map.scenes.get("dogpark"), sc.DogPark)
    assert_is_instance(a_map.scenes.get("death"), sc.Death)
    assert_is_instance(a_map.scenes.get("fight"), sc.Fight)
    assert_is_instance(a_map.scenes.get("home"), sc.Home)

def test_start():
    a_map = Map("introduction")
    assert_equal(a_map.start_scene, "introduction")

def test_next_scene():
    a_map = Map("introduction")
    assert_is_instance(a_map.next_scene("backyard"), sc.Backyard)

def test_opening_scene():
    a_map = Map("introduction")
    assert_is_instance(a_map.opening_scene(), sc.Introduction)

def test_engine():
    a_map = Map("introduction")
    an_engine = Engine(a_map)
    assert_is_instance(an_engine.game_map, Map)
    
def setup():
    print "SETUP!"
    
def teardown():
    print "TEAR DOWN!"
    
def test_basic():
    print "I RAN!"
