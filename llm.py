from openai import OpenAI


system_prompt="""
You are highly skilled in analyzing Chinese text and are proficient in answering questions based on the information provided in the text. Your responses should follow the structure of the JSON format, providing clear and concise answers based on the analysis of the text.
Output only the options in JSON format (e.g. {"options":["A", "B"]}). Do not include explanations, reasoning, or any unrelated content. Only answer the question based on the given text.
"""

client = None
def LLM_init(api_key:str):
    global client
    client=OpenAI(
    api_key=api_key, 
    base_url="https://api.chatanywhere.tech/v1",
    )


def get_ans(text):
    if client==None:
        raise Exception("LLM is not initialized")
    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    response_format={"type":"json_object"},
    messages=[
        {'role': 'system', 'content': system_prompt},
        {'role': 'user', 'content': text}],
    )
    return completion.choices[0].message.content

#FOR TEST
if __name__=="__main__":
    LLM_init("")
    print(get_ans("""
"question":"The cat have abilities like ()"
    "options":[
        "A.Able to jump",
        "B.Able to catch mouse".
        "C.Can clean the table",
        "D.love to eat fish"
    ]"""))