import os
import openai


python_code = input('enter code')

openai.api_key = os.getenv("OPENAI_KEY")

response = openai.ChatCompletion.create(
  model="gpt-4",
  messages=[
    {
      "role": "system",
      "content": "You will be provided with a piece of Python code, and your task is to find and fix bugs in it."
    },
    {
      "role": "user",
      "content": "import Random\na = random.randint(1,12)\nb = random.randint(1,12)\nfor i in range(10):\n    question = \"What is \"+a+\" x \"+b+\"? \"\n    answer = input(question)\n    if answer = a*b\n        print (Well done!)\n    else:\n        print(\"No.\")"
    }
  ],
  temperature=0.52,
  max_tokens=8000,
  top_p=1,
  frequency_penalty=0.75,
  presence_penalty=0.34,
  stop=["--stop"]
)