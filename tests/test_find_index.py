import pytest
from main import get_first_index


ar1 = '111111111110000000000000000'
ar2 = 123
ar3 = ''
ar4 = 'sajf20fj'

class TestGetIndex:
    def test_get_index(self):
        """Return the lowest index of 0"""
        assert get_first_index(ar1) == 11


class TestGetIndexRaise:
    def test_type_raise(self):
        """Return TypeError for not str types"""
        with pytest.raises(TypeError):
            get_first_index(ar2)

    def test_value_raise_empty_str(self):
        """Return ValueError for empty string"""
        with pytest.raises(ValueError):
            get_first_index(ar3)

    def test_value_raise_not_numbers(self):
        """Return ValueError for alphanumeric string"""
        with pytest.raises(ValueError):
            get_first_index(ar4)
