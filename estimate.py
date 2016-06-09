#!/usr/bin/env python

def estimate():

	print('Please enter the amount of records you intend to ingest and process: ')
	process_estimate = 0 #initialize estimate variable

	while True: 
		try:
			X = input("Records: ")
			X = X.lower() 
			X = X.replace(',', '') #remove comma from user input
			if X == "stop": #ends loop
				break
			else: 
				X = int(X)
				if X <= 0: #input must be >0
					print ("%s is not a valid input, please input a non-negative number greater than zero. Type 'stop' to cancel." % X)
				else:
					while True:
						try: 
							user_confirm = input("You input %s. Is this correct? (Y/N): " % X)
							user_confirm = user_confirm.lower()
							if user_confirm == "y" or user_confirm == "yes":
								#ingestion and processing time in seconds for each step of data ingestion process
								I_Step_1 = 0
								I_Step_2 = X * 2.44459229701e-05
								I_Step_3 = X * 0
								I_Step_4 = X * 0.000706894605885
								I_Step_5 = X * 0.00327880941836
								I_Step_6 = X * 0.00109415876894
								I_Step_7 = X * 1.73158621038e-05
								I_Step_8 = X * 0.000618889283193
								I_Step_9 = X * 0.000914481235106
								I_Step_10 = X * 0.000500326556788
								I_Step_11 = X * 2.13901825988e-05
								I_Step_12 = X * 0.00125366841632
								I_Step_13 = 0
								I_Step_14 = 0
								I_Step_15 = 0
								I_Step_16 = 0
								Ingestion = (I_Step_1 + I_Step_2 + I_Step_3 + I_Step_4 + I_Step_5 + I_Step_6 + I_Step_7 + I_Step_8 + I_Step_9 + I_Step_10 + I_Step_11 + I_Step_12 + I_Step_13 + I_Step_14 + I_Step_15 + I_Step_16)
								#Member Re-Matching
								"""MR_Step_1 = 
								MR_Step_2 = 
								MR_Step_3 = 
								MR_Step_4 =
								MR_Step_5 = 
								MR_Step_6 =
								MR_Step_7 =
								Member_Rematching = MR_Step_1 + MR_Step_2 + MR_Step_3 + MR_Step_4 + MR_Step_5 + MR_Step_6 + MR_Step_7"""

								#sum of ingestion and processing steps
								process_estimate = (Ingestion) / 3600
								#present time estimate in optimized format
								if process_estimate < 1:
									process_estimate = process_estimate * 60
									print("The estimated time to ingest and process %s records is %d minutes" % (X, process_estimate))
									return

								else:
									process_estimate = float(process_estimate)
									print("The estimated time to ingest and process %s records is %.2f hours" % (X, round(process_estimate,2)))
									return

							elif user_confirm == "stop":
								return

							elif user_confirm == "n" or user_confirm == "no":
								print("Please input the correct amount of records. Type 'stop' to cancel.")
								break
							else:
								print("Please input Y or N")
						except ValueError:
							print ("Please input Y or N")
		except ValueError:
			print("%s is not a valid input, please input a number" % X)
	


estimate();