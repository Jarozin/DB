class BaseGenerator:
    def __init__(self) -> None:
        self.params = []

        self.id = 0

    def reset_id(self):
        self.id = 0

    def get_header(self):
        return self.params

    def generate_record(self):
        return self.params
