import json as js
from dataclasses import dataclass, asdict

@dataclass
class Person:
    first_name: str
    last_name: str
    address: str
    post_code: str
    pesel: str

    def to_json(self, file_path):
        """
        Save Person instance as JSON file
        """
        data = asdict(self)     # Simplified data saving 
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


grzegB = Person("Grzegorz", "Brzeczyszczykiewicz", "Cracow, Nowa Huta", "31-999", "01234567890")  # make Grzegorz
grzegB.to_json("per_A.json")  # Save Grzegorz

per_B = Person.from_json("per_B.json")  # load another person from file
print(per_B)  # Print the person instance

print(Person.from_json("per_A.json"))  # Load and print Grzegorz
