# Root folder is ResumeCode
# This should be changed in conjunction with other projects.
''''''
import sys
sys.path.append('C:\\Users\\Sam\\Desktop\\ResumeCode\\')

from DataStructures.Object import Object
''''''
from random import randint

class DiscreteSample():
    def __init__(self, obj_type, n_samples, dct={}, **obj_attrs_vals_dict):
        self.cur = 0
        self.high = n_samples
        self.obj_type = obj_type

        if dct and obj_attrs_vals_dict:
            raise TypeError("Use dictionary or kwargs not both.")

        elif type(dct) != dict:
            raise TypeError("Argument not of type dict")

        else:
            if dct:
                self.obj_attrs_vals = dct
            else:
                self.obj_attrs_vals = obj_attrs_vals_dict

    @property
    def high(self):
        return high

    @high.setter
    def high(self, n_samples):
        if type(n_samples) != int:
            raise TypeError("random_sample parameter n_samples needs to be type int")

        elif n_samples <= 0:
            raise ValueError("parameter n_samples needs to be at least one")

        else:
            self._high = n_samples

    @property
    def obj_type(self):
        return _obj_type

    @obj_type.setter
    def obj_type(self, name):
        if type(name) != str:
            raise TypeError("Object._obj_type needs to be of type str.")
        self._obj_type = name

    @property
    def obj_attrs_vals(self):
        return _obj_attrs_vals

    @obj_attrs_vals.setter
    def obj_attrs_vals(self, dct):
        if type(dct) != dict:
            raise TypeError("Object._attrs needs to be of type dict.")
        self._obj_attrs_vals = dct

    def __iter__(self):
        return self

    def __next__(self):
        if self.cur == self._high:
            raise StopIteration

        else:
            self.cur += 1
            return self.random_sample()


    def random_sample(self):
        rand_sample_obj_attrs = {}

        for attr in self._obj_attrs_vals:
            j = randint(0, len(self._obj_attrs_vals[attr])-1)
            rand_sample_obj_attrs[attr] = self._obj_attrs_vals[attr][j]

        rand_sample_obj = Object(self._obj_type)
        rand_sample_obj.update_attrs(rand_sample_obj_attrs)
        #print(rand_sample_obj)
        return rand_sample_obj
