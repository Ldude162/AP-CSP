import random as rndm

hp = 100
enemyHP = 100


while hp > 0 and enemyHP > 0:
	atkOrDef = input('Would you like to attack or defend? Say "a" to attack and "h" to heal.')
	if atkOrDef == 'a':
		random = rndm.randrange(10)
		enemyAtk = rndm.randrange(3)
		enemyHP = enemyHP - random
		print("You attacked for", random, "damage! The enemy's health is now", enemyHP)
		random = rndm.randrange(10)
		if enemyAtk <= 1 and enemyHP > 10:
			hp = hp -random
			print('The enemy attacked you for', random, "damage. You now have", hp, "health.")
		elif enemyAtk == 2 or enemyHP <= 10:
			enemyHP = enemyHP + random
			print('The enemy healed for', random, 'health. They are on', enemyHP, 'HP, and you are on', hp, "HP.")
	elif atkOrDef == 'h':
		random = rndm.randrange(15)
		enemyAtk = rndm.randrange(3)
		hp = hp + random
		print("You healed for", random, "HP! Your health is now", hp)
		if enemyAtk <= 1:
			random = rndm.randrange(12)
			hp = hp - random
			print('The enemy attacked you for', random, "damage. You now have", hp, "health. Their health is", enemyHP)
		elif enemyAtk == 2:
			random = rndm.randrange(15)
			enemyHP = enemyHP + random
			print('The enemy healed for', random, 'health. They are on', enemyHP, 'HP, and you are on', hp, "HP.")
	else:
		print("I'm sorry, I couldn't figure out what that was. Make sure you are typing the letters a or d!")
		continue
if hp > 0:
	print("You won!")
elif enemyHP > 0:
	print("You lost...")
else:
	print("what.")
		

		
	
