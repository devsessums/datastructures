'''
class name: Object

class use: This is a class meant for creating pseudo classes.

Object properties:
    obj_type - str - pseudo type name
    attrs - dict - attributes for pseudo-class

An example for using this class is to create a pseudo class "ball" with attributes of
color, size, and rubber.

> ball1 = Object('ball', color='red', size=2, rubber=True)
or
> ball1 = Object('ball')
> ball1.update_attrs(color='red', size=2, rubber=True)
or
> ball1 = Object()
> ball1._obj_type = 'ball'
> ball1.update_attrs(color='red', size=2, rubber=True)
or
> ball1 = Object('ball', {'color':'red', 'size':2, 'rubber':True})

'''

class Object():
    def __init__(self, obj_type='default', dct={}, **kwargs):
        if dct and kwargs:
            raise TypeError('Use dictionary or kwargs, not both')

        elif type(dct) != dict:
            raise TypeError("Argument not of type dict")

        else:
            self.obj_type = obj_type
            if dct:
                self.attrs = dct
            else:
                self.attrs = kwargs


    @property
    def obj_type(self):
        return _obj_type

    @obj_type.setter
    def obj_type(self, name):
        if type(name) != str:
            raise TypeError("Object._obj_type needs to be of type str.")
        self._obj_type = name

    @property
    def attrs(self):
        return _attrs

    @attrs.setter
    def attrs(self, dct):
        if type(dct) != dict:
            raise TypeError("Object._attrs needs to be of type dict.")
        self._attrs = dct

    def update_attrs(self, dct=None, **attrs):
        if dct and attrs:
            raise TypeError("Use dictionary or kwargs, not both.")

        elif type(dct) != dict and not attrs:
            raise TypeError("Argument to update attributes must be type dict or kwargs")

        else:
            if dct:
                for attr in dct:
                    if attr in self._attrs:
                        self._attrs[attr] = dct[attr]
                    else:
                        self._attrs[attr] = dct[attr]
            else:
                for attr in attrs:
                    if attr in self._attrs:
                        self._attrs[attr] = attrs[attr]
                    else:
                        self._attrs[attr] = attrs[attr]

    def delete_attrs(self, attrs):
        if type(attrs) != list:
            raise TypeError("Attributes to delete need to be type list")
        else:
            for attr in attrs:
                if type(attr) != str and type(attr) != int and type(attr) != tuple:
                    raise TypeError("Attribute key types accepted are str, int, or tuple.")

                elif attr not in self._attrs:
                    raise AttributeError("No attribute {} in Object._attrs".format(attr))

                else:
                    del self._attrs[attr]

    def __eq__(self, obj):
        if type(self) != type(obj):
            return False

        elif self._obj_type != obj._obj_type:
            return False

        elif len(self._attrs) != len(obj._attrs):
            return False

        else:
            for attr in self._attrs:
                if attr not in obj._attrs:
                    return False
                else:
                    if self._attrs[attr] != obj._attrs[attr]:
                        return False
            return True


    def __str__(self):
        __str__ = ""
        __str__ += "Class/Type: Object\n"
        __str__ += "Object type name: {}\n".format(self._obj_type)
        __str__ += "Number of attributes: {}\n".format(len(self._attrs))
        __str__ += "Attributes{\n"
        for attr in self._attrs:
            __str__ += "\t{}: {}\n".format(attr, self._attrs[attr])
        __str__ += '}\n'
        return __str__
