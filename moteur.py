def determiner_initiative(vitesse_a: int, vitesse_b: int) -> str:
    if vitesse_a >= vitesse_b:
        return "combattant_a"
    return "combattant_b"