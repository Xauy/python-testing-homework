import unittest

def calculate_average(numbers: list[float]) -> int | None:
    if not numbers:
        print("Tested by Shakhov Dmitriy — пустой список.")
        return None
    average = sum(numbers) / len(numbers)
    rounded = int(average)
    print(f"Tested by Shakhov Dmitriy — среднее знаение: {rounded}")
    return rounded

class TestCalculateAverage(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(calculate_average([1.5, 2.5, 3.5]), 2)

    def test_negative_numbers(self):
        self.assertEqual(calculate_average([-1, -2, -3]), -2)

    def test_empty_list(self):
        self.assertIsNone(calculate_average([]))

if __name__ == "__main__":
    unittest.main()
