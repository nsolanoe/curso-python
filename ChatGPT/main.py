import openai
#from decouple import config

openai.api_key = "."



while True:
    fecha_nacimiento = input("Ingresa tu fecha de nacimiento: ") 
    
    prompt = "signo sodiacal en" + fecha_nacimiento
    
    if prompt == "salir":
        break
   
    completion = openai.Completion.create(
     engine = "text-davinci-003",
     prompt = prompt, 
     max_tokens = 1024
    )
    
    print(completion.choices[0].text)



