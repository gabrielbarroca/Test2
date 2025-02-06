import pytest
from hello_world import check_age, check_nom, demander_nom, demander_age
def test_check_age_happy_flow():
    assert None == check_age(13)  

def test_check_nom_happy_flow():
    assert None == check_nom("")

def test_check_age_exeption():
    with pytest.raises(ValueError):
        check_age("")

def test_demander_nom_happy_flow(monkeypatch):
    inputs = iter(["Gabriel"])
    
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    assert demander_nom() == "Gabriel"

def test_demander_nom_sad_flow(monkeypatch):
    inputs = iter([""])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    with pytest.raises(ValueError):
        check_nom(12)

def test_demander_age_happy_flow(monkeypatch):
    inputs = iter(["abc", 13])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    assert demander_age() == 13 

def test_demander_age_sad_flow(monkeypatch):
    inputs = iter(["abc"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    with pytest.raises(ValueError):
        check_age("")