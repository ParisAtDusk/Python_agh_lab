import json as js

class Person:
    def __init__(self, first_name, last_name, address, post_code, pesel):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.post_code = post_code
        self.pesel = pesel

    def to_json(self, file_path):
        """
        Save Person instance as JSON file
        """
        data = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "address": self.address,
            "post_code": self.post_code,
            "pesel": self.pesel
        }
        with open(file_path, "w", encoding="utf-8") as json_file:
            js.dump(data, json_file, ensure_ascii=False, indent=4)

    @classmethod
    def from_json(cls, file_path):
        """ 
        Load from JSON and create a new Person instance
        :param file_path: Path to JSON file
        :return: New instance of person based on JSON data
        """
        with open(file_path, "r", encoding="utf-8") as json_file:
            data = js.load(json_file)
        return cls(
            data["first_name"],
            data["last_name"],
            data["address"],
            data["post_code"],
            data["pesel"]
        )

grzegB = Person("Grzegorz", "Brzeczyszczykiewicz", "Cracow, Nowa Huta", "31-999", "01234567890")    # make grzegorz
grzegB.to_json("per_A.json")    # Save grzegorz

per_B = Person.from_json("per_B.json")  # load jan from file
print(per_B.__dict__)   # print jan

print(Person.from_json("per_A.json").__dict__) # load and print grzegorz
