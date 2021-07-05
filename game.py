'''
import random
game_list=['rock','paper','scissors']
computer=c=0
command=p=0
print('score:computer'+ str(c)+':player'+ str(p))
run=True
while run:
	pass
	computer_choice = random.choice(game_list)
	command=input('rock,paper,scisssors or quit:')
	if command == computer_choice:
		print('tie')
	elif command  == 'rock':
		if computer_choice =='scisssors':
			print('player won')
			p+=1
		else:
			print('computer won')
			c+=1
	elif command =='paper':
			if computer_choice == 'rock':
				print('player won')
				p+=1
			else:
				print('computer won')
				c+=0
	elif command =='scisssors':
			if computer_choice == 'paper':
				print('player won')
				p+=1
			else:
				print('computer won')
				c+=1
	elif command == 'quit':
			break
	else:
			print('wrong command')
print('player:'+command)
print('computer'+computer_choice)
print('')
print('score:computer'+str(c)+'player'+str(p))
print('')
'''


import random
game_list=['rock','paper','scissors']
computer=c=0
command=p=0
print('computer score is {0}, player score is {0}'.format(c),(p))
run=True
while run:
	pass
	computer_choice = random.choice(game_list)
	command=input('rock,paper,scisssors or quit:')
	if command  == computer_choice:
		print('tie')
	elif command  =='rock':
		if computer_choice =='scisssors':
			print('player won')
			p+=1
		else:
			print('computer won')
			c+=1
	elif command  =='paper':
			if computer_choice == 'rock':
				print('player won')
				p+=1
			else:
				print('computer won')
				c+=0
	elif command =='scisssors':
			if computer_choice == 'paper':
				print('player won')
				p+=1
			else:
				print('computer won')
				c+=1
	elif command == 'quit':
			break
		
	else:
			print('wrong command')
print('player:'+command)
print('computer'+computer_choice)
print('computer score is {0},player score is {0}'.format(c,p))


