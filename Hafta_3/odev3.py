row=""
for a in range(1,10):
    for i in range(1,10):
        islem=f"{i} x {a} = {i*a}"
        row=row+islem+(" "*(15-len(islem)))
    print(row)
    row=""
        