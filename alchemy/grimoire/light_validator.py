from . import light_spellbook


def validate_ingredients(ingredients: str) -> str:
    lowered_ingredients = ingredients.lower()
    is_valid = False
    for allowed in light_spellbook.light_spell_allowed_ingredients():
        if allowed in lowered_ingredients:
            is_valid = True
            break
    keyword = "VALID" if is_valid else "INVALID"
    return f"{ingredients} - {keyword}"
