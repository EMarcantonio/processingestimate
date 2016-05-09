#!/usr/bin/env python

def estimate():
	print "Please enter the amount of records you intend to ingest and process: "
	process_estimate = 0 #initialize estimate variable
	count = 0
	while True: 
		try:
			X = raw_input('Records: ')
			X = X.lower()
			X = X.replace(',', '')
			if X == "stop":
				break
			else: 
				X = int(X)
				if X < 0:
					print "%s is not a valid input, please input a non-negative number" % X
				else:
					user_confirm = raw_input("You input %s. Is this correct? (Y/N): " % X)
					user_confirm = user_confirm.lower()
					if user_confirm == "y":
						Step_1 = 1
						Step_2 = X * 0.00153
						Step_3 = X * 0.000765
						Step_4 = X * 0.002296
						Step_5 = X * 0.002296
						Step_6 = X * 0.002296
						Step_7 = X * 0.000765
						Step_8 = X * 0.00459
						Step_9 = X * 0.000383
						Step_10 = X * 0.00306
						Step_11	 = X * 0.0153
						Step_12 = 300
						Step_13 = 0
						Step_14 = X * 0.000383

						process_estimate = (Step_1 + Step_2 + Step_3 + Step_4 + Step_5 + Step_6 + Step_7 + Step_8 + Step_9 + Step_10 + Step_11 + Step_12 + Step_13 + Step_14) / 3600
						if process_estimate < 1:
							process_estimate = process_estimate * 60
							print "The estimated time to ingest and process %s records is %d minutes" % (X, process_estimate)
							break
						else:
							process_estimate = float(process_estimate)
							print "The estimated time to ingest and process %s records is %.2f hour(s)" % (X, round(process_estimate,2))
							break

					elif user_confirm == "stop":
						break

					else:
						print "Please input the correct amount of records. Type 'stop' to cancel."
					


		except ValueError:
			print "%s is not a valid input, please input a number" % X
	


estimate();