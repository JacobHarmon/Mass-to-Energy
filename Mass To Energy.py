SpeedOfLight = 3000000000.0

# Variables
Mass = 0.0

def InputDataFloat():
		try:
			Input = float(input("-> "))
			return Input
		except:
			print("You tried to put a non-number.")
			exit()
if __name__ == "__main__":
	################
	# Start screen #
	################
	print("\n|01------------------10|")
	print("|0- |Mass to Energy| -0|")
	print("|01------------------10|\n")
		
	print("|1| Mass to Energy in Rested Energy State")
	print("|2| Mass to Energy at Other Energy States\n")

	try:
		Input = int(input("-> "))
	except ValueError:
		print("You didn't use a number.")
		exit()

	###############
	# Do the Math #
	###############
	if(Input == 1): 	# Energy at a rested state
		print("\nWhat amount of mass do you want? (kg)")
		Mass = InputDataFloat()

		print("\nThe amount of Energy to make the amount of Mass you have selected is:")
		print(str(Mass * pow(SpeedOfLight, 2)) + " joules")
		
	elif(Input == 2):	# Energy at different state
		# Variables
		InitialVelocity = 0.0
		FinalVelocity = 0.0
		TimeTook = 0.0
		
		##############################
		# Energy at different states #
		##############################
		# Mass
		print("What amount of mass do you want? (kg)")
		Mass = InputDataFloat()
		
		# Initial Velocity
		print("What is the initial velocity. (m/s)")
		IntiailVelocity = InputDataFloat()
		
		# Final Velocity
		print("What is the final velocity. (m/s)")
		FinalVelocity = InputDataFloat()
		
		# Time Took
		print("How long did it take for Initial Velocity to reach Final Velocity. (m/s)")
		TimeTook = InputDataFloat()
		
		# Printing out Math
		if(TimeTook != 0):
			print("The amount of energy to make mass with other energy states is: ")
			print(str(pow(Mass, 2) * pow(SpeedOfLight, 4) + pow(((FinalVelocity - InitialVelocity) / TimeTook) * Mass, 2) * SpeedOfLight) + "joules")
		else:
			print("You can't divide by 0.")
	else:
		print("What you select is not option.")
		exit()

