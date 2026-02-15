import random

def generate_personas(human_name: str, age: int, location: str, temperament: str):
    names_pool = ["Arjun", "Riya", "Sam", "Meera", "Dev", "Sara", "Sanjay"]

    selected = random.sample(names_pool, 3)

    personas = []

    for name in selected:
        personas.append({
            "name": name,
            "age": age,
            "location": location,
            "temperament": temperament,
            "style": "witty, emotionally intelligent, culturally aware, humorous but respectful"
        })

    return personas
