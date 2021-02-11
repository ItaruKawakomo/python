# MIT License

# Copyright (c) 2021 Vasily Denisenko, Sergey Kuznetsov

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import sys
import turtle
from random import randrange



def dir_inverse(char):
	if char == 'L':
		return 'R'
	elif char == 'R':
		return 'L'
	elif char == 'F':
		return 'F'
	else:
		return ''



def generate_dragon(order, use_order_char = 0):
	s_prev = 'F'

	if use_order_char == 1:
		s_prev = s_prev + 'O'
	if order == 0:
		return s_prev
	
	for ord in range(order):
		s_cur = s_prev + 'L'
		for i in range(s_prev.__len__()):
			s_cur = s_cur + dir_inverse(s_prev[s_prev.__len__() - i - 1])
		if use_order_char == 1:
			s_cur = s_cur + 'O'
		s_prev = s_cur
		
	return s_cur
	
	
	
def draw_dragon(turtl, instr, step):
	for i in range(instr.__len__()):
		if instr[i] == 'F':
			turtl.forward(step)
		elif instr[i] == 'R':
			turtl.right(90)
		elif instr[i] == 'L':
			turtl.left(90)
		elif instr[i] == 'O':
			turtl.color((randrange(32, 224), randrange(32, 224), randrange(32, 224)))
		else:
			return
	

def main():
	if __name__ == '__main__':
		screen = turtle.getscreen()
		screen.colormode(255)
		t = turtle.Turtle()
		t.speed(0)
		t.hideturtle()

		order = int(sys.argv[1])
		if order < 0:
			print('Incorrect order')
			sys.exit()

		STEP = 20
		if order > 8:
			STEP = STEP / 1.41421356**(order - 8)

		instructions = generate_dragon(order, use_order_char = 1)
		draw_dragon(t, instructions, STEP)

		input()
		
main()
