from test_stuff.tryhard import studentlayer


studentlayer.erik.increase_term()
studentlayer.erik.increase_term()

erik_firstname = studentlayer.erik.get_firstname()
erik_latname = studentlayer.erik.get_lastname()
erik_semester = studentlayer.erik.get_term()

print(erik_firstname + " " + erik_latname + ": Semester (" + str(erik_semester) + ")")