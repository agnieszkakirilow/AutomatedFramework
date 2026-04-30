class BaseProviderClass():
    def __init__(self, input_values):
        super().__init__()
        self.values = input_values

    def get(self, item_name):
        return self.values(item_name)