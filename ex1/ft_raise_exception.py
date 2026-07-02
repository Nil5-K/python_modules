def input_temperature(temp_str: str) -> int:
    temp = int(temp_str)
    if temp >= 0 and temp <= 40:
        return temp
    else:
        if temp < 0:
            raise Exception(f"{temp} is too cold for plants (min 0°C)")
        else:
            raise Exception(f"{temp} is too hot for plants (max 40°C)")


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")

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

    print("\nInput data is '100'")
    try:
        print(f"Temperature is now {input_temperature('100')}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")

    print("\nInput data is '-50'")
    try:
        print(f"Temperature is now {input_temperature('-50')}°C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")


if __name__ == "__main__":
    test_temperature()
    print("\nAll tests completed - program didn't crash!")
