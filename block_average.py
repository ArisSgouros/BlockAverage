################################################################################
# MIT License
#
# Copyright (c) 2023 ArisSgouros
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
################################################################################

import sys
import math
import numpy as np

# Computes the absolute deviation from the mean
def cmad(data, axis=None):
    return np.mean(np.absolute(data - np.mean(data, axis)), axis)

with open(sys.argv[1]) as f:
    data = f.read().splitlines()

data_len = len(data)

# data can only be proccesed in powers of two. The largest data
# data chunk will be proccesed and the rest will be ignored
iter = int(math.log(data_len,2))
nmax = 2**iter

# define the blocks
blocks = [[0 for x in range(0,2**y)] for y in range(iter,0,-1)]

# make the main block
for n in range(nmax):
    blocks[0][n] = float(data[n])

# calculate the block averages
for it in range(1,iter):
    for n in range(0,len(blocks[it])):
        blocks[it][n] = 0.5 * ( blocks[it-1][2*n+1] + blocks[it-1][2*n] )

print('File lines:      ', data_len)
print('processed lines: ', nmax)
print('mean:            ', np.mean(blocks[iter-1]))
print('blocklen, mad, std, stdEst, stdEstErr')

# calculate the std, its estimate and the error of the estimate
for block in blocks:
    mad = cmad(block)
    std = np.std(block,ddof=1)
    blockLen = len(block)
    stdEst = std/(blockLen-1)**0.5
    stdEstErr = stdEst / (2*(blockLen-1))**0.5
    print(blockLen, mad, std, stdEst, stdEstErr)
