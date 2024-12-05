import requests
import os
from dotenv import load_dotenv

load_dotenv()


def get_input(day):
    """
    Fetches the input data for the given day of Advent of Code.
    Requires the AOC_SESSION_COOKIE environment variable to be set.
    """
    session_cookie = os.environ.get('AOC_SESSION_COOKIE')
    if not session_cookie:
        raise ValueError("Session cookie not found. Please set the AOC_SESSION_COOKIE environment variable.")

    url = f'https://adventofcode.com/2024/day/{day}/input'
    response = requests.get(url, cookies={"session": session_cookie})
    if response.status_code != 200:
        raise Exception(f"Failed to fetch input data: HTTP {response.status_code}")
    return response.text.rstrip()
