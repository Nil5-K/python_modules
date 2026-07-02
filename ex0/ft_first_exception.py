def input_temperature(temp_str):
    return int(temp_str)


def test_temperature():
    print("=== Garden Temperature ===")

    print("\nInput data is '25'")
    try:
        print(f"Temperature is now {input_temperature('25')}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")

    print("\nInput data is 'abc'")
    try:
        print(f"Temperature is now {input_temperature('abc')}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")


if __name__ == "__main__":
    test_temperature()
    print("\nAll tests completed - program didn't crash!")
