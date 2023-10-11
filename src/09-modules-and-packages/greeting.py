def get_full_name(first_name, last_name):
    return f"{first_name} {last_name}"

def get_greeting(greet_message, full_name):
    return f"{greet_message}, {full_name}"

class Greeter:
    def __init__(self, greet_message):
        self.greet_message = greet_message
        
    def get_greeting(self, full_name):
        return get_greeting(self.greet_message, full_name)
