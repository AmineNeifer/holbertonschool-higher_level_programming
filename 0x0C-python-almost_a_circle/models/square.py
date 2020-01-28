#!/usr/bin/python3


from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
    
    def __str__(self):
        return "[Square] ({}) {}/{} - \
{}".format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        count = 0
        if len(args) != 0:
            for i in args:
                if count == 0:
                    self.id = i
                elif count == 1:
                    self.size = i
                elif count == 2:
                    self.x = i
                elif count == 3:
                    self.y = i
                count += 1
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        dicc = {}
        dicc['x'] = self.x
        dicc['y'] = self.y
        dicc['size'] = self.size
        dicc['id'] = self.id
        return dicc
