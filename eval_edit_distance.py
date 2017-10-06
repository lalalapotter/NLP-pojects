import numpy as np
import sys

f = open("vocab.txt", "r+")
sys.stdin = f
vocab_list = input(f)
print(vocab_list[1:10])