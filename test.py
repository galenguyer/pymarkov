from pymarkov import PyMarkov

chain = PyMarkov('test.txt')
for i in range(0, 100):
    print(chain.generate())