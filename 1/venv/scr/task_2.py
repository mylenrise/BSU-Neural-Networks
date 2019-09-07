import numpy as np

def sigmoid(x):
    s = 1/(1+np.exp(-x))
    return s

input=[[0,0],[0,1],[1,1],[1,0]]

w1=0.45
w2=1.88
w3=-0.12
w4 = -0.4
w5 = 2.6
w6 = -2.2
n=4

def learn(I1,I2):
    H1input = I1 * w1 + I2 * w3  # 0.45
    H1output = sigmoid(H1input)  # 0.61

    H2input = I1 * w2 + I2 * w4  # 0.78
    H2output = sigmoid(H2input)  # 0.69

    O1input = H1output * w5 + H2output * w6  # -0.672
    O1output = sigmoid(O1input)  # 0.33
    return (O1output)

if __name__ == '__main__':

    O1ideal = []  # (0xor1=1)
    output=[]
    for pair in input:
        output.append(learn(pair[0], pair[1]))
    for pair in input:
        O1ideal.append(pair[0]^pair[1])
    Error=0
    for i in range(n):
        Error+=((O1ideal[i]-output[i])**2)
    Error/=n
    print("Error: ",Error)

  #  Error = ((O1ideal - O1output) ** 2) / n  # 0.45

   # print(O1ideal)
    #Результат — 0.33, ошибка — 45%.