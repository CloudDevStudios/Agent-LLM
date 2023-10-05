import os


class CustomPrompt:
    def add_prompt(self, prompt_name, prompt):
        # if prompts folder does not exist, create it
        if not os.path.exists("prompts"):
            os.mkdir("prompts")
        # if prompt file does not exist, create it
        if not os.path.exists(os.path.join("prompts", f"{prompt_name}.txt")):
            with open(os.path.join("prompts", f"{prompt_name}.txt"), "w") as f:
                f.write(prompt)
        else:
            raise Exception("Prompt already exists")

    def get_prompt(self, prompt_name):
        with open(os.path.join("prompts", f"{prompt_name}.txt"), "r") as f:
            prompt = f.read()
        return prompt

    def get_prompts(self):
        return [
            file.replace(".txt", "")
            for file in os.listdir("prompts")
            if file.endswith(".txt")
        ]

    def delete_prompt(self, prompt_name):
        os.remove(os.path.join("prompts", f"{prompt_name}.txt"))

    def update_prompt(self, prompt_name, prompt):
        with open(os.path.join("prompts", f"{prompt_name}.txt"), "w") as f:
            f.write(prompt)
