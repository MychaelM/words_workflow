import httpx
import os
from dotenv import load_dotenv

load_dotenv()

def print_words(words: list[str]):
  for word in words:
    word_dict = fetch_word(word)
    definitions = word_dict['results'][0]['definition']
    synonyms = word_dict['results'][0]['synonyms']
    print(f'{definitions} {synonyms}')

def fetch_word(word: str):
  return httpx.get(f'https://wordsapiv1.p.rapidapi.com/words/{word}', headers={'x-rapidapi-key': os.getenv('RAPID_KEY'), 'x-rapidapi-host': "wordsapiv1.p.rapidapi.com"}).json()

print_words(['hello', 'apple'])