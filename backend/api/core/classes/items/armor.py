
class Armor():
    def __init__(
        self,
        head,
        head_wear,
        body,
        body_wear
    ) -> None:
        self.head = head
        self.head_wear = head_wear
        self.body = body
        self.body_wear = body_wear

    def as_json(self):
        return {
            'head': self.head,
            'head_wear': self.head_wear,
            'body': self.body,
            'body_wear': self.body_wear,
        }
