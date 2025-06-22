def calculate_average(numbers: list[float]) -> int | None:
    if not numbers:
        return None
    average = sum(numbers) / len(numbers)
    return int(average)
