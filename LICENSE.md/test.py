import BinaryInteger as b_i

x_1 = b_i.BinaryInteger("00000000000000001111111111111111")
x_2 = b_i.BinaryInteger("00000000111111110000000011111111")
x_3 = b_i.BinaryInteger("00001111000011110000111100001111")
x_4 = b_i.BinaryInteger("00110011001100110011001100110011")
x_5 = b_i.BinaryInteger("01010101010101010101010101010101")

x_1x_2 = b_i.BinaryInteger.multiply(x_1,x_2)
x_2x_3 = b_i.BinaryInteger.multiply(x_2,x_3)
x_3x_4 = b_i.BinaryInteger.multiply(x_3,x_4)
x_1x_4 = b_i.BinaryInteger.multiply(x_1, x_4)
b = b_i.BinaryInteger.add(x_1x_2,x_2x_3)
bent_1 = b_i.BinaryInteger.add(b, x_3x_4)
bent_2 = b_i.BinaryInteger.add(x_2x_3, x_1x_4)
print(bent_1.toString())
print(bent_2.toString())
print(bent_1.distance_from(bent_2))