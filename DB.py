class DB:
    def _init_(self, name, address):
        self.name = name
        self.address = address

    def _str_(self):
        return "Name:{},Address:{}".format(self.name, self.address)
