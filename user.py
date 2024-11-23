"""Module to generate random users"""

import logging
from faker import Faker
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
logging.basicConfig(filename=BASE_DIR / "user.log",
                    filemode="w",
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")
fake = Faker(locale="fr_FR")


def get_user() -> str:
    """Generates a random first and last name

    Returns:
        str: A first name and a last name in a string
    """
    first_name = fake.first_name()
    last_name = fake.last_name()
    
    logging.info(f"Generating {first_name} {last_name}.")
    return f"{first_name} {last_name}"


def get_users(nbr: int) -> list[str] | None:
    """Generates a list of random first and last names

    Args:
        nbr (int): Number of first and last names to generate

    Returns:
        list[str]: First and last name in a list of strings
    """
    logging.info(f"Generating a list of {nbr} users.")
    try:
        return [get_user() for _ in range(nbr)]
    except TypeError:
        logging.error("An integer is expected as a parameter")
