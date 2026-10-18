def input_temperature(temp_str: str) -> int:
    numb = int(temp_str)
    if numb < 0:
        raise ValueError(f"{numb}°C is too cold for plants (min 0°C)")
    if numb > 40:
        raise ValueError(f"{numb}°C is too hot for plants (max 40°C)")
    return numb


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")
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
    print("Input data is '100'")
    try:
        input_temperature("100")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")
    print()
    print("Input data is '-50'")
    try:
        input_temperature("-50")
    except ValueError as error:
        print(f"Caught input_temperature error: {error}")
    print()
    print("All tests completed - program didn't crash!")


test_temperature()
