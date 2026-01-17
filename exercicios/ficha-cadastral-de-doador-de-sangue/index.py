# Cadastro de doadores de sangue

print("Cadastro de doadores de sangue")
input_name = input("Por favor, digite seu nome completo: ")
input_weight = float(input("Por favor, digite seu peso em quilos: "))
input_height = int(input("Por favor, digite sua altura em centímetros: "))
input_birth = int(input("Por favor, digite seu ano de nascimento: "))

# Armazenando os dados em variáveis
name = input_name
height = input_height
weight = input_weight
birth = input_birth
age = 2022 - birth

# Verificando os requisitos para doação de sangue
min_age = "Sim" if weight > 50 else "Não"
max_age = "Sim" if age >= 16 else "Não"

# Montando o questionário
blood_donor_questionnaire = f"""
    \tNOME: {name.upper()}
    \n\tPESO: {weight} kg
    \n\tALTURA: {height} cm
    \n\tIDADE: {age} anos
    \n\tPOSSUI PESO MÍNIMO PARA DOAR?: {min_age}
    \n\tPOSSUI IDADE MÍNIMA PARA DOAR: {max_age}
    \n\t"""
# Exibindo o questionário
print("-"*30)
print(blood_donor_questionnaire)
print("-"*30)