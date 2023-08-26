import math 

input = 1
output_desire = 0
input_weight = 0.5

learning_rate = 0.01

def activation(sum):
    if sum >= 0:
        return 1
    else:
        return 0

print("entrada", input, "desejado", output_desire)

error = math.inf


while not error  == 0:
    sum = input * input_weight
    output = activation(sum)
    print("saida", output)
    error = output_desire - output
    print("err0", error)


    if not error ==  0:
        input_weight = input_weight + (learning_rate * input * error)
print("Se entrou aqui a rede aprendeu")