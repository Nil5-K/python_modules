from enum import Enum
from pydantic import BaseModel, model_validator, Field, ValidationError
from datetime import datetime


class Ranks(str, Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Ranks
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime = Field(default_factory=datetime.now)
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validate_space_mission(self) -> 'SpaceMission':
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")
        has_leader = False
        for member in self.crew:
            if member.rank in (Ranks.CAPTAIN, Ranks.COMMANDER):
                has_leader = True
                break
        if not has_leader:
            raise ValueError("Must have at least one Commander or Captain")
        if self.duration_days > 365:
            experienced_count = sum(
                1 for member in self.crew if member.years_experience >= 5
            )
            if experienced_count < len(self.crew) * 0.5:
                raise ValueError(
                    "Long missions (> 365 days) require at "
                    "least 50% experienced crew (5+ years)"
                )
        for member in self.crew:
            if not member.is_active:
                raise ValueError("All crew members must be active")
        return self


def print_crew(_space_mission: SpaceMission) -> None:
    print("========================================")
    print(f"Mission: {_space_mission.mission_name}")
    print(f"ID: {_space_mission.mission_id}")
    print(f"Destination: {_space_mission.destination}")
    print(f"Duration: {_space_mission.duration_days} days")
    print(f"Budget: ${_space_mission.budget_millions}M")
    print(f"Crew size: {len(_space_mission.crew)}")
    print("Crew members:")
    for member in _space_mission.crew:
        print(f"- {member.name} ({member.rank.value}) - "
              f"{member.specialization}")
    print("========================================\n")


def main() -> None:
    print("Space Mission Crew Validation")
    space_mission = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        duration_days=900,
        crew=[
            CrewMember(
                member_id="CM001",
                name="Sarah Connor",
                rank=Ranks.COMMANDER,
                age=42,
                specialization="Mission Command",
                years_experience=15
            ),
            CrewMember(
                member_id="CM002",
                name="John Smith",
                rank=Ranks.LIEUTENANT,
                age=35,
                specialization="Navigation",
                years_experience=8
            ),
            CrewMember(
                member_id="CM003",
                name="Alice Johnson",
                rank=Ranks.OFFICER,
                age=29,
                specialization="Engineering",
                years_experience=5
            )
        ],
        budget_millions=2500.0
    )
    print_crew(space_mission)

    print("Expected validation error:")
    try:
        invalid_mission = SpaceMission(
            mission_id="M2024_TEST",
            mission_name="Test Mission",
            destination="Moon",
            duration_days=30,
            crew=[
                CrewMember(
                    member_id="CM004",
                    name="Bob Wilson",
                    rank=Ranks.CADET,
                    age=25,
                    specialization="Engineering",
                    years_experience=2
                )
            ],
            budget_millions=50.0
        )
        print_crew(invalid_mission)
    except ValidationError as e:
        print(f"{e.errors()[0]['msg']}")


if __name__ == "__main__":
    main()
