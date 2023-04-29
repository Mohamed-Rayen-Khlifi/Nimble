import Nimble
print("""\n\n			######		      Welcome to NIMBLE SHARP 			######""")
print("""			###### A programming language built by Joumene, Roua and Rayen! ######\n""")
result = input("""To start using Nimble#, please type S 
To quit Nimble#, please type Q\n
Your answer: """)
if result == "S":
	while True:
			text = input('Nimble# ')
			if text.strip() == "": continue
			result, error = Nimble.run('<stdin>', text)

			if error:
				print(error.as_string())
			elif result:
				if len(result.elements) == 1:
					print(repr(result.elements[0]))
				else:
					print(repr(result))
elif result == "Q":
	quit
else:
	print("Please specify a valid option (S/Q)")