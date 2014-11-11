from nose.tools import *
from ex45.ex45 import Map
import ex45.ex45
import ex45.scenes as sc

def test_map():
    a_map = Map("introduction")
    assert_equal(a_map.scenes.get("introduction"), sc.Introduction())
    assert_equal(a_map.scenes.get("living_room"), sc.LivingRoom())
    assert_equal(a_map.scenes.get("backyard"), sc.Backyard())
    assert_equal(a_map.scenes.get("enchantedforest"), sc.EnchantedForest())
    assert_equal(a_map.scenes.get("clearing"), sc.Clearing())
    assert_equal(a_map.scenes.get("trail"), sc.Trail())
    assert_equal(a_map.scenes.get("tunnel"), sc.Tunnel())
    assert_equal(a_map.scenes.get("inside_tunnel"), sc.InsideTunnel())
    assert_equal(a_map.scenes.get("enchantedforest_2"), sc.EnchantedForestPartTwo())
    assert_equal(a_map.scenes.get("river"), sc.River())
    assert_equal(a_map.scenes.get("dogpark"), sc.DogPark())
    assert_equal(a_map.scenes.get("death"), sc.Death())
    assert_equal(a_map.scenes.get("fight"), sc.Fight())
    assert_equal(a_map.scenes.get("home"), sc.Home())

def setup():
    print "SETUP!"
    
def teardown():
    print "TEAR DOWN!"
    
def test_basic():
    print "I RAN!"
