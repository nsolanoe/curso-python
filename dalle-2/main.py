import openai
#from decouple import config

openai.api_key = "."
while True:
    prompt = input("Detalla: ")
    if prompt == "salir":
       break 
    response = openai.Image.create(
        prompt = prompt,
        n = 1,
        size = "1024x1024"
    )
    image_url = response['data'][0]['url']
    print(image_url)

    