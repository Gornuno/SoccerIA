import google.generativeai as genai
import os

from google.generativeai.types.generation_types import GenerateContentResponse

ABSOLUTE_FILEPATH = os.path.dirname(__file__)

MODEL_NAME = 'gemini-1.5-pro-latest'
GENERATION_CONFIG = {
  'temperature': 1,
  'candidate_count': 1,
}

SAFETY_SETTINGS = [
  {
    'category': 'HARM_CATEGORY_HARASSMENT',
    'threshold': 'BLOCK_NONE'
  },
  {
    'category': 'HARM_CATEGORY_HATE_SPEECH',
    'threshold': 'BLOCK_NONE'
  },
  {
    'category': 'HARM_CATEGORY_SEXUALLY_EXPLICIT',
    'threshold': 'BLOCK_LOW_AND_ABOVE'
  },
  {
    'category': 'HARM_CATEGORY_DANGEROUS_CONTENT',
    'threshold': 'BLOCK_NONE'
  },
]

SYSTEM_INSTRUCTION_FILEPATH = os.path.join(ABSOLUTE_FILEPATH, 'system_instructions/instrucsocceria.txt')

def run_setup() -> None:
    #insira aqui a sua API KEY
    GOOGLE_API_KEY="suaApiKey"
    genai.configure(api_key=GOOGLE_API_KEY)

def read_file(filepath) -> str:
    try:
        with open(filepath, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print("File not found Exception!")
        return ''
    except Exception as e:
        print("Unknown Exception: ", e)
        return ''


def write_file(content, file_extension='.md') -> None:
    with open('output'+file_extension, 'w', encoding='utf-8') as f:
        f.write(content)


def list_models() -> None:
    print('LIST OF MODELS \n')
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)


def get_model(model=MODEL_NAME,
              generation_config= GENERATION_CONFIG,
              safety_settings = SAFETY_SETTINGS,
              system_instruction = read_file(SYSTEM_INSTRUCTION_FILEPATH)):
    return genai.GenerativeModel(model_name=model,
                                 generation_config=generation_config,
                                 safety_settings=safety_settings,
                                 system_instruction=system_instruction)

def generate_text_with_google_api(prompt):
    run_setup()
    model = get_model()
    response: GenerateContentResponse = model.generate_content(prompt)
    return response.text
