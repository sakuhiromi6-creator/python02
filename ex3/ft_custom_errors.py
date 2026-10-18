class GardenError(Exception):
    def __init__(self, message: str = "Error Garden") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Error plant") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Error Water") -> None:
        super().__init__(message)


def plant_error() -> None:
    raise PlantError("The tomato plant is wilting!")


def water_error() -> None:
    raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===")
    print()
    print("Testing PlantError...")
    try:
        plant_error()
    except PlantError as error:
        print(f"Caught PlantError: {error}")
    print()
    print("Testing WaterError...")
    try:
        water_error()
    except WaterError as error:
        print(f"Caught WaterError: {error}")
    print()
    print("Testing catching all garden errors...")
    try:
        plant_error()
    except GardenError as error:
        print(f"Caught GardenError: {error}")
    try:
        water_error()
    except GardenError as error:
        print(f"Caught GardenError: {error}")
    print()
    print("All custom error types work correctly!")


test_custom_errors()
