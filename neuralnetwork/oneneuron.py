input = 1
output_desire = 0
input_weight = 0.5
sum = (input * input_weight)

 
def activation(sum):
    if sum >= 0:
        return 1
    else:
        return 0

print("entrada", input, "desejado", output_desire)
output = activation(sum)
print("saida", output)
error = output_desire - output