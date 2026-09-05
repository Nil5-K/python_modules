from pydantic import BaseModel, Field, ValidationError
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime = Field(default_factory=datetime.now)
    is_operational: bool = Field(default=True)
    notes: str | None = Field(max_length=200, default=None)


def print_station(_space_station: SpaceStation) -> None:
    status = ("Operational"
              if _space_station.is_operational
              else "Not Operational"
              )
    print("========================================")
    print(f"ID: {_space_station.station_id}")
    print(f"Name: {_space_station.name}")
    print(f"Crew: {_space_station.crew_size} people")
    print(f"Power: {_space_station.power_level}%")
    print(f"Oxygen: {_space_station.oxygen}%")
    print(f"Status: {status}")
    if _space_station.notes:
        print(f"Notes: {_space_station.notes}")
    print("========================================\n")


def main() -> None:
    print("Space Station Data Validation")
    space_station = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen=92.3
    )
    print_station(space_station)

    print("Expected validation error:")
    try:
        invalid_space_station = SpaceStation(
            station_id="ISS002",
            name="International Space Station",
            crew_size=23,
            power_level=85.5,
            oxygen=92.3
        )
        print_station(invalid_space_station)
    except ValidationError as e:
        print(f"{e.errors()[0]['msg']}")


if __name__ == "__main__":
    main()


#  Create a virtual environment and install pydantic
# python3 -m venv venv
# source venv/bin/activate
# pip install pydantic

#  If there is a mypy issue:
# pip install mypy
# which mypy
# pip show mypy

#  Clear Shell cache
# hash -r         (bash)
# rehash          (zsh)
