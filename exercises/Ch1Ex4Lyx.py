participants = 52
trials = 200
experimental_sessions = 3.0
trials_pp = trials * experimental_sessions
var1 = "task difficulty (easy, difficult)"
var2 = "time (limited, unlimited)"

print "In total,", participants, "participants",\
      "participated in the study."
print "A", design, "between subjects design was employed."
print "The study examined the interaction of two",\
      "independent variables,", var1, "and",\
       var2 + "."
print "Participants were tested in",\
       experimental_sessions, "experimental sessions."
print "Each session consisted of", trials,"trials."
print "In total, each partcipant thus completed",\
       trials_pp, "trials."