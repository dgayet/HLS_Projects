output_file = open("output.txt", "w")


test_index = 100
sample = x_test_nn_bin[test_index]

#print(x_test_nn_bin[test_index])

for i in sample:
    print(i, end=",", file=output_file)
output_file.close()

print(y_test_bin[test_index])


print(np.argmax(y_pred[test_index]))
