# Palindrone validator

import collections
import pytest

@pytest_fixture
def test_pelindrone_validator(e_word):

    check = e_word.isnumeric()

    print(check)

    assert check is False, "This is a number. Please enter text values."

    pd = collections.deque(e_word)
    ee = collections.deque(e_word)

    print(pd)
    print(ee)

    rev_pd = pd.reverse()
    print(pd)

    print(type(e_word))

    if pd == ee:
        print("equal")
    else:
        print("not equal")


enter_word = "Bye"

test_pelindrone_validator(enter_word)
