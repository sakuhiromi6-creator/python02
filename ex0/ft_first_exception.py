def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    print()
    print("Input data is '25'")
    temp_right = input_temperature("25")
    print(f"Temperature is now {temp_right}°C")
    print()
    print("Input data is 'abc'")
    try:
        input_temperature("abc")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")
    print()
    print("All tests completed - program didn't crash!")


test_temperature()
