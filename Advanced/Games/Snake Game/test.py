dict = {
    (0, 0): "hi",
    (20, 50): "hello",
}

dict[(60, 70)] = "yeah"

del dict[(0, 0)]

print(dict)