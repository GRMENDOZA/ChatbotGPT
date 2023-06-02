import openai
import json
import os

def chatGPT(question = "",phoneNumber =""):

    # export OPENAI_API_KEY="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"
    
    pathConversation = f'../database/{phoneNumber}.json'
    part1 = "sk-lQ3PhpomKiZ6XqZI5KnoT3"
    part2 = "BlbkFJj6IAd8FpQogkCVrchDpX"
    openai.api_key = part1+part2
    flagError = 0

    messages = []
    if os.path.exists(pathConversation):
        conversationFile = open(pathConversation)
        messages = json.load(conversationFile)
        conversationFile.close()
        # print(messages)
    else:
        context = {"role": "system", "content": "Hola"}
        messages = [context]

    if question.lower() in ["new","nuevo","nueva","nueva conversacion","hola"]:
        messages = [{"role": "system",
            "content": "Hola"}]
    
    messages.append({"role": "user", "content": question})

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages)
        response_content = response.choices[0].message.content

    except BaseException as error:
        msg = error
        flagError = 1

    if flagError == 0:
        messages.append({"role": "assistant", "content": response_content})
        conversationFile = open(pathConversation,'w')
        conversationFile.write(json.dumps(messages))
        conversationFile.close()
    else:
        response_content = "Rate limit reached for default-gpt-3.5-turbo in organization org-SQkzws9FsPgYdhHNc8hJq9VH on requests per min. Limit: 3 / min. Please try again in 20s. Contact support@openai.com if you continue to have issues. Please add a payment method to your account to increase your rate limit. Visit https://platform.openai.com/account/billing to add a payment method."

    return response_content