class GardenError(Exception):
	def __init__(self, message="Unknown garden error"):
		super().__init__(message)

class PlantError(GardenError):
	def __init__(self, message="Unknown plant error"):
		super().__init__(message)

def water_plant(plant_name):
	if plant_name == plant_name.capitalize():
		print(f"Watering {plant_name}: [OK]")
	else:
		raise PlantError(f"Invalid plant name to water: {plant_name}")

def test_watering_system():
	print("=== Garden Watering System ===")

	print("\nTesting valid plants...")
	try:
		print("Opening watering system")
		water_plant("Tomato")
		water_plant("Lettuce")
		water_plant("Carrots")
	except PlantError as e:
		print(f"Caught {e.__class__.__name__}: {e}")
		print(".. ending tests and returning to main")
		return
	finally:
		print("Closing watering system")

	print("\nTesting invalid plants...")
	try:
		print("Opening watering system")
		water_plant("Tomato")
		water_plant("lettuce")
	except PlantError as e:
		print(f"Caught {e.__class__.__name__}: {e}")
		print(".. ending tests and returning to main")
		return
	finally:
		print("Closing watering system")

if __name__ == "__main__":
	test_watering_system()
	print("\nCleanup always happens, even with errors!")
