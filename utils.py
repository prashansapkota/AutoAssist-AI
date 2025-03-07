
import os
from dotenv import load_dotenv, find_dotenv

def load_env():
    """Load environment variables from a .env file."""
    _ = load_dotenv(find_dotenv())

def get_openai_api_key():
    """Retrieve the OpenAI API key from environment variables."""
    load_env()
    openai_api_key = os.getenv("OPENAI_API_KEY")
    return openai_api_key

def get_serper_api_key():
    """Retrieve the Serper API key from environment variables."""
    load_env()
    serper_api_key = os.getenv("SERPER_API_KEY")
    return serper_api_key

def pretty_print_result(result):
    """Format the result to ensure no line exceeds 80 characters."""
    parsed_result = []
    for line in result.split('\n'):
        if len(line) > 80:
            words = line.split(' ')
            new_line = ''
            for word in words:
                if len(new_line) + len(word) + 1 > 80:
                    parsed_result.append(new_line)
                    new_line = word
                else:
                    if new_line == '':
                        new_line = word
                    else:
                        new_line += ' ' + word
            parsed_result.append(new_line)
        else:
            parsed_result.append(line)
    return "\n".join(parsed_result)
