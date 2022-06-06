from Practice import Person
from Practice import Generator
def test_person():
    p = Person('some', 'example','gender', 'age')
    assert p.name == 'some'
    assert p.surname == 'example'
    # assert p.age == '2000-01-01'


def test_person_full():
    p = Person('some', 'example', 'female', '1990-10-10')
    assert p.name == 'some'
    assert p.surname == 'example'
    assert p.gender == 'female'
    assert p.age == '1990-10-10'


def test_person_getinfo():
    p = Person('some', 'example', 'female', '1990-10-10')
    assert isinstance(p.get_info(), str)


def test_gen_single_types():
    g = Generator()
    p = g.generate_one()
    assert isinstance(p, Person)
    assert isinstance(p.name, str)
    assert isinstance(p.surname, str)
    assert isinstance(p.gender, str)
    assert isinstance(p.age, str)


def test_gen_1000_type():
    g = Generator()
    plist = g.generate_1000()
    assert isinstance(plist, list)
    assert isinstance(plist[0], Person)
    assert len(plist) == 1000


def test_gen_10_000_type():
    g = Generator()
    plist = g.generate_10000()
    assert isinstance(plist, list)
    assert isinstance(plist[0], Person)
    assert len(plist) == 10000