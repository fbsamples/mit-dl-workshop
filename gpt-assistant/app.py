import openai
import yaml
import string
import questionary

openai.api_key_path = 'apikey'

with open('prompts.yaml') as f:
    PROMPTS = yaml.safe_load(f)


def fill_prompt(task):
    prompt = PROMPTS[task]
    print(f"\nPrompt template: {prompt}\n")    
    placeholders = {v[1]: "" for v in string.Formatter().parse(prompt) if v[1] is not None}
    for plac in placeholders.keys():
        placeholders[plac] = questionary.text(f"{plac}: ").ask()
    prompt = prompt.format(**placeholders)
    return prompt


def ask_gpt(prompt):
    print("\nGenerating response....\n")
    response = openai.Completion.create(
        model="text-davinci-003",
        temperature=0.75,
        max_tokens=650,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        prompt=prompt
    )
    gpt_answer = response['choices'][0]['text']
    return gpt_answer


if __name__ == "__main__":
    choices = PROMPTS.keys()
    print("\n\n")
    action = questionary.select("What do you want to do?", choices=choices).ask()
    if action == "freetext":
        prompt = questionary.text("Ask GPT: ").ask()
    else:
        prompt = fill_prompt(action)
    response = ask_gpt(prompt)
    print(response)


