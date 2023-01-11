#!/usr/local/bin/python3

import openai
from colorama import Fore

while True:
    user_input = input(f"{Fore.CYAN}How can I help! ")

    if user_input == 'Exit':
        break
    else:
        try:
            openai.api_key = ("Your Keys Goes here") 
        
            response = openai.Completion.create(
                                    model='text-davinci-003',
                                    prompt=user_input,
                                    max_tokens=3048,
                                    top_p=1.0,
            presence_penalty=0.0)

            print(f"{Fore.YELLOW}{response.choices[0].text}\n") # type:ignore
        except Exception as e:
            print(e)
