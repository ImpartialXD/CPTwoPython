class Q1:
    def __init__(self, numbers):
        self.numbers = numbers

    def calculate_average(self):
        if not self.numbers:
            return 0
        return sum(self.numbers) / len(self.numbers)

    def print_average(self):
        avg = self.calculate_average()
        nums_str = " , ".join(str(n) for n in self.numbers)
        print(f"The average of {nums_str} is: {int(avg)}")


class Q2:
    def __init__(self, list_one, list_two):
        self.list_one = list_one
        self.list_two = list_two

    def find_same_numbers(self):
        return sorted(set(self.list_one) & set(self.list_two))

    def print_same_numbers(self):
        print(f"List One: {self.list_one}")
        print(f"List Two: {self.list_two}")
        same = self.find_same_numbers()
        same_str = ", ".join(str(n) for n in same)
        print(f"\nAll same numbers on both List: {same_str}")


class Q3:
    def __init__(self, persons):
        self.persons = persons

    def filter_by_age(self, max_age):
        return [p for p in self.persons if p.age < max_age]

    def print_filtered(self, max_age):
        filtered = self.filter_by_age(max_age)
        print(f"Person with the lower age than {max_age}")
        for p in filtered:
            print(f"Name: {p.name} Age: {p.age}")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def Activity():
    # 1. Average Calculator
    avg_calc = Q1([10, 15, 20, 30])
    avg_calc.print_average()
    print()

    # 2. Same Numbers Finder
    list_one = [1, 20, 3, 6, 8, 9, 10, 7, 12, 21, 18]
    list_two = [10, 2, 30, 15, 8, 21, 13, 18, 28, 25, 16]
    same_finder = Q2(list_one, list_two)
    same_finder.print_same_numbers()
    print()

    # 3. Person Age Filter
    persons = [
        Person("Kurt", 15),
        Person("Carl", 23),
        Person("JK", 45),
        Person("James", 60),
        Person("Kelvin", 39),
        Person("Haze", 18),
        Person("Gaze", 10),
        Person("Soap", 20),
        Person("Price", 23),
        Person("McQueen", 80),
        Person("Bascreveil", 50)
    ]
    age_filter = Q3(persons)
    # print_filtered is the input of the max age to filter the persons
    age_filter.print_filtered(39)

# Run the Activity function
if __name__ == "__main__":
    Activity()