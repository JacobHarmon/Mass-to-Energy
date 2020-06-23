class Application:
	
	SpeedOfLight = 3000000000.0
	
	def __init__(self):
		# Variables
		Mass = 0.0
		
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
			print("\nWhat amount of mass do you want? (kg)\n")
			
			try:
				Input = float(input("-> "))
				Mass = Input
			except:
				print("You didn't put a number.")
				exit()
			
			print("\nThe amount of Energy to make the amount of Mass you have selected is:")
			print(str(Mass * pow(self.SpeedOfLight, 2)) + " joules")
					
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
			
			try:
				Input = float(input("-> "))
				Mass = Input
			except:
				print("You didn't put a number.")
				exit()
			
			# Initial Velocity
			print("What is the initial velocity. (m/s)")
			
			try:
				Input = float(input("-> "))
				InitialVelocity = Input
			except:
				print("You didn't put a number.")
				exit()
			
			# Final Velocity
			print("What is the final velocity. (m/s)")
			
			try:
				Input = float(input("-> "))
				FinalVelocity = Input
			except:
				print("You didn't put a number.")
				exit()
			
			# Time Took
			print("How long did it take for Initial Velocity to reach Final Velocity. (m/s)")
			
			try:
				Input = float(input("-> "))
				TimeTook = Input
			except:
				print("You didn't put a number.")
				exit()
			
			# Printing out Math
			print("The amount of energy to make mass with other energy states is: ")
			print(str(pow(Mass, 2) * pow(self.SpeedOfLight, 4) + pow((FinalVelocity - InitialVelocity) / TimeTook, 2) + pow(self.SpeedOfLight, 2))  + "joules")
		else:
			print("What you select is not option.")
			exit()

app = Application()

