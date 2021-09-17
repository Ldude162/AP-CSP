import random as rndm

hp = 100
enemyHP = 100

print(hp, enemyHP)
while hp > 0 and enemyHP > 0:
	atkOrDef = input('Would you like to attack or defend? Say "a" to attack and "h" to heal.')
	if atkOrDef == 'a':
		random = rndm.randrange(10)
		enemyHP = enemyHP - random
		print("You attacked for", random, "damage! The enemy's health is now", enemyHP)
		random = rndm.randrange(10)
		hp = hp -random
		print('The enemy attacked you for', random, "damage. You now have", hp, "health.")
	elif atkOrDef == 'h':
		random = rndm.randrange(15)
		hp = hp + random
		print("You healed for", random, "HP! Your health is now", hp)
		random = rndm.randrange(8)
		hp = hp -random
		print('The enemy attacked you for', random, "damage. You now have", hp, "health. Their health is", enemyHP)
	else:
		print("I'm sorry, I couldn't figure out what that was. Make sure you are typing the letters a or d!")
		continue
if hp > 0:
	print("You won!")
elif enemyHP > 0:
	print("You lost...")
else:
	print("what.")
		

		
	
