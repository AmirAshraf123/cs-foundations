
from data_structures.hashmap.hashmap import HashMap

def test_set_and_get():
    hm = HashMap()
    hm.set("a", 1)
    hm.set("b", 2)
    assert hm.get("a") == 1
    assert hm.get("b") == 2

def test_overwrite_key():
    hm = HashMap()
    hm.set("x", 10)
    hm.set("x", 20)
    assert hm.get("x") == 20

def test_delete():
    hm = HashMap()
    hm.set("key", "value")
    assert hm.delete("key") is True
    assert hm.get("key") is None
    assert hm.delete("missing") is False
