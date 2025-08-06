class ChaiUtils:
    @staticmethod
    def clean_ingredients(text): # type: ignore
        return [item.strip() for item in text.split(",")]  # type: ignore

raw = " water , milk , ginger, honey "
cleaned = ChaiUtils.clean_ingredients(raw)
print(cleaned)