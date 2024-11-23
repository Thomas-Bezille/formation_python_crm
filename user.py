from faker import Faker


fake = Faker(locale="fr_FR")

def get_user() -> str:
    """Generates a random first and last name

    Returns:
        str: A first name and a last name in a string
    """
    return f"{fake.first_name()} {fake.last_name()}"


def get_users(nbr: int) -> list[str]:
    """Generates a list of random first and last names

    Args:
        nbr (int): Number of first and last names to generate

    Returns:
        list[str]: First and last name in a list of strings
    """
    return [get_user() for _ in range(nbr)]
