import os
import random

class PyMarkov:
    nodes = {}

    def __init__(self, filename:str):
        if filename is None:
            raise Exception('filename argument cannot be None')
        if not os.path.exists(filename):
            raise Exception(f'file {filename} does not exist')
        fd = open(filename, 'r', encoding='UTF-8')
        text = fd.readlines()
        fd.close()

        for line in text:
            t_line = line.strip().split(' ')
            for i in range(0, len(t_line) - 1):
                if t_line[i] not in self.nodes:
                    self.nodes[t_line[i]] = [t_line[i+1]]
                else:
                    self.nodes[t_line[i]].append(t_line[i+1])
            if t_line[-1] not in self.nodes:
                self.nodes[t_line[-1]] = ['<EOF>']
            else:
                self.nodes[t_line[-1]].append('<EOF>')


    def generate(self):
        tokens = ''
        prev_token = random.choice(list(self.nodes.keys()))
        tokens = tokens + prev_token + ' '
        while True:
            next_token = random.choice(self.nodes[prev_token])
            if next_token == '<EOF>':
                break
            else:
                tokens = tokens + next_token + ' '
                prev_token = next_token
        return tokens


if __name__ == '__main__':
    print('This is a library and not meant to be called directly. ' + \
        'Please import it using "import pymarkov"')
