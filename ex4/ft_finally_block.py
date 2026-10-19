class GardenError(Exception):
    def __init__(self, message: str = "Error Garden") -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str = "Error plant") -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str = "Error Water") -> None:
        super().__init__(message)


def water_plant(plant_name: str) -> None:
    if plant_name != plant_name.capitalize():
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")
    print(f"Watering {plant_name}: [OK]")


def test_watering_system() -> None:
    print("=== Garden Watering System ===")
    print()
    print("Testing valid plants...")
    print("Opening watering system")
    try:
        water_plant("Tomato")
        water_plant("Lettuce")
        water_plant("Carrots")
    except PlantError as error:
        print(f"Caught PlantError: {error}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")
    
    print()
    print("Testing invalid plants...")
    print("Opening watering system")
    try:
        water_plant("Tomato")
        water_plant("lettuce")
    except PlantError as error:
        print(f"Caught PlantError: {error}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")
    print()
    print("Cleanup always happens, even with errors!")



test_watering_system()