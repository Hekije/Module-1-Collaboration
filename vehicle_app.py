"""
Name: Henry Escoto
Date: 09/15/2025
SDEV 220

For this assignment, I created a Python program to practice using classes
and inheritance. I made a Vehicle class and then an Automobile class that
inherits from it. The program asks the user for details about a car (like
year, make, model, doors, and roof type) and then prints everything back
in a nice format.

* I made some upgrades to the program which in my opinion makes it better, here
is a list of the changes made: *

- Multiple cars: I wanted the program to handle more than one car, this lets me enter
  a few and review them together.
- Input validation: stops bad inputs so the object data stays clean.
- Helper prompt functions: This helps keeping the main logic readable and avoids
  copy/paste issues.
- Type Hints: makes the code easier to understand.
- _str_: one-liner print for automobile to avoid print() spam.
- to_dict/save to JSON: just a quick way to persist a session, it's nice for testing and sharing.

"""

from typing import List, Dict
import json

# ---------- Base & Subclass ----------

class Vehicle:
    def __init__(self, vehicle_type: str) -> None:
        self.vehicle_type: str = vehicle_type  # for example, "car", "truck", etc.

class Automobile(Vehicle):
    def __init__(self, vehicle_type: str, year: str, make: str, model: str, doors: int, roof: str) -> None:
        super().__init__(vehicle_type)
        self.year: str = year
        self.make: str = make
        self.model: str = model
        self.doors: int = doors         # validated as 2 or 4
        self.roof: str = roof           # validated as "solid" or "sun roof"

    def __str__(self) -> str:
        return (
            f"Vehicle type: {self.vehicle_type}\n"
            f"Year: {self.year}\n"
            f"Make: {self.make}\n"
            f"Model: {self.model}\n"
            f"Number of doors: {self.doors}\n"
            f"Type of roof: {self.roof}"
        )

    # Tiny serializer
    def to_dict(self) -> Dict[str, object]:
        return {
            "vehicle_type": self.vehicle_type,
            "year": self.year,
            "make": self.make,
            "model": self.model,
            "doors": self.doors,
            "roof": self.roof,
        }

# ---------- Input helpers (keeping main clean) ----------

def prompt_nonempty(prompt: str) -> str:
    """Ask until the user types something non-empty."""
    while True:
        val = input(prompt).strip()
        if val:
            return val
        print("Please enter something (can't be empty).")

def prompt_choice(prompt: str, choices: List[str]) -> str:
    """Ask until the user picks a valid option (case-insensitive display)."""
    choices_display = "/".join(choices)
    while True:
        val = input(f"{prompt} ({choices_display}): ").strip().lower()
        if val in choices:
            return val
        print(f"Please choose one of: {choices_display}")

def prompt_int_choice(prompt: str, valid_ints: List[int]) -> int:
    """Ask until the user types one of the valid integers."""
    valid_display = "/".join(str(v) for v in valid_ints)
    while True:
        raw = input(f"{prompt} ({valid_display}): ").strip()
        if raw.isdigit():
            num = int(raw)
            if num in valid_ints:
                return num
        print(f"Please enter {valid_display}.")

# ---------- Program flow ----------

def add_car() -> Automobile:
    print("\nEnter car details:")
    vehicle_type = "car"  # we’re storing only “car” for Vehicle
    year = prompt_nonempty("Year: ")
    make = prompt_nonempty("Make: ")
    model = prompt_nonempty("Model: ")
    doors = prompt_int_choice("Number of doors", [2, 4])
    roof = prompt_choice("Type of roof", ["solid", "sun roof"])
    return Automobile(vehicle_type, year, make, model, doors, roof)

def print_cars(cars: List[Automobile]) -> None:
    if not cars:
        print("\nNo cars recorded yet.")
        return
    print("\n===== Your Cars =====")
    for i, car in enumerate(cars, start=1):
        print(f"\n[{i}]")
        print(car)

def save_cars_to_json(cars: List[Automobile], filename: str = "cars.json") -> None:
    data = [c.to_dict() for c in cars]
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"\nSaved {len(cars)} car(s) to {filename}")

def main() -> None:
    cars: List[Automobile] = []

    print("Car Collector (multi-entry) — with validation + save to JSON")
    while True:
        cars.append(add_car())
        again = prompt_choice("Add another car?", ["y", "n"])
        if again == "n":
            break

    print_cars(cars)

    # Optional save
    save = prompt_choice("\nSave to JSON file?", ["y", "n"])
    if save == "y":
        save_cars_to_json(cars)

    print("\nDone. Thanks!")

if __name__ == "__main__":
    main()