# from datetime import datetime
# import sys
#TODO:// MAKE STATE FUNCTION THAT GETS THE STATE AND CONVERTS IT INTO A PROPER FORMAT

state = input("State:")

        
#global variables, these should work fine inside of my functions
yes = ["Y","y","Yes","yes","YES"]
no = ["N","n","No","no","NO"]

norulesapply = "No state-specific rules apply in your case. yay!"
notrelevant = "'s rules arent relevant to you! yay!"
staterules = state + " Rules\n---------------------------------------------------------------------------------------------"
#hmm should i put the state lists in here or in a constant. eh right now its easier to put them in here
def get_state(state):
    state = state.upper()
    state_restrictions_short = ['CA', 'DC', 'GA', 'HI', 'IN', 'KS', 'KY', 'MD','MA', 'MI', 'MT', 'NH', 'NM', 'NY', 'PA', 'VI', 'WA', 'WI']
    st_restrictions = ['CALIFORNIA', 'DISTRICT OF COLUMBIA', 'GEORGIA', 'HAWAII', 'INDIANA', 'KANSAS', 'KENTUCKY', 'MARYLAND', 'MASSACHUSETTS',
    'MICHIGAN', 'MONTANA', 'NEW HAMPSHIRE', 'NEW MEXICO', 'NEW YORK', 'PENNSYLVANIA', 'U.S. VIRGIN ISLANDS', 'WASHINGTON', 'WISCONSIN']
    #makes state(now capitalized) into its state abbreviation
    if state in state_restrictions_short:
        return state
    if state in st_restrictions:
        index = st_restrictions.index(state)
        state = state_restrictions_short[index]
        return state
        #state is now in correct format now i turn it into a function call and pass it too my switcher function
    else:
        print("This state has no restrictions - program quitting, feel free to restart")
        sys.exit()
        #this function might be out of scope but i can figure it out later
        
def pos_loc():
    while True:
        threenums = [1,2,3]
        pos_locat = input(f"Is (1) the position location in {state},(2) the address location in {state} \nor (3) are both the position and the address in {state}:\n")
        pos_locat = int(pos_locat)
        if int(pos_locat) in threenums:
            return pos_locat
        else:
            print("Input 1,2 or 3")


# for i in range(0,len(st_restrictions)):
#     st_restrictions[i] = state_restrictions_short[i]
# #makes st_restrictions == state_restrictiosn sh0rt- effectively turning all long versions of states into abbreviations    


def CA():
    #tests position location rules -raises enter1or2 if invalid response
    SF = input("Is the position in San Francisco?:")
    print("\n\n")
    if int(pos_location) == 1:
        print(staterules)
        print("Do not report dismeanor marijuana cases outside of a 2 year scope")
        #maybe put in something later where i can just ask questions about whether its a misdemeanor marijuana or not and if the answer is no i cam move on
        #eventually it would be great to get to a point where i can just have people enter info in a certain format, or fill in a form of some type and then
        #i can spit out the correct answer
        # break
    elif int(pos_location) == 2:
        print(staterules)
        print("Rule 1: Only report convictions and active pending cases / warrants (do not report non-convictions / alternates \n(deferrals / diversions in which individual is on probation)")
        print("Rule 2: Do not report out of 7 year scope")
        print("Rule 3:  Do not report 1203.4 case status or dispositions")
        # break
    elif int(pos_location) == 3:
        print(staterules)
        print("Rule 1: Only report convictions and active pending cases / warrants (do not report non-convictions / alternates, (deferrals / diversions in which individual is on probation))")
        print("Rule 2: Do not report out of 7 year scope.")
        print("Rule 3: Do not report 1203.4 case status or dispositions.")
        print("Rule 4: Do not report dismeanor marijuana cases outside of a 2 year scope.")
        # break
        # break
        # else:
        #     print("Enter 1, 2, or 3!")
        #     pos_location = input("Is (1) the position location in california,(2) the address location in California \n or (3) are both the position and the address in California \n")
    # tests and instructs for the marijuana scope rule    -raises customError if invalid response
    while True:
        if SF in yes:
            marijuana = input("Is the disposition a non-felony marijiana conviction?: ")
            if marijuana in yes:
                print("Do not report non-felony marijuana convictions -  Exception: Report if the disposition is within the past 2 \n years and the individual was under age 21 at the time of conviction")
            else:
                print("Continue on")
            break
        elif SF in no:
            break
        else:
            print("Enter Y or N!")
    return
def DC(): 
    if pos_location == 1 or pos_location == 3:
        print(f"{state} Rules:\n Do not report out of a 10 year scope")
        return
def GA():
    print(f"{state} Rules:\n-Do not report First Offender Act case status or disposition")
    return
def HI():
    if pos_location == 1 or pos_location == 3:
        print(f"{state} Rules:")
        print("Rule 1: Only report convictions and active pending cases / warrants (do not report non-convictions / alternates \n(deferrals / diversions in which individual is on probation))\n")
        print("Rule 2: Do not report FELONY charges outside 7 year (may only use incarceration for the 7 years scope - \n NOT probation or parole - otherwise use disposition date)\n ")
        print("Rule 3: Do not report: MISDEMEANOR charges outside 5 year (may only use incarceration for the 5 year \n scope - NOT probation or parole - otherwise use disposition date)\n")
    elif pos_location == 2:
        print(f"{state} Rules:")
        print(norulesapply)
    return
def IN():
    while True:
        residenceIN = input("Is the candidates residence in Indiana?: ")
        if residenceIN in yes:
            print(f"{state} Rules:")
            print("Do not report Class D felony convictions that have been entered or converted to Class A \n misdemeanor convictions, only report the misdemeanor")
            break
        elif residenceIN in no:
            print("This rule isnt relevant to you!")
            break
        else:
            print("Enter Y or N")
    return
def KS():
    print(f"{state} Rules:")
    print("Do not report out of 7 year scope, unless candidate makes $20,000 or more annually")
    return
def KY():
    V = input("Was the offense committed in Kentucky?")
    while True:
        if V in yes:
            print("Only report convictions and warrants (do not report pending or alternate \n(diversion, dismissed, or any related dispositions))\n")
            break
        elif V in no:
            print(state + notrelevant)
            break
        else:
            print("Enter Y or N")
    return
def MD():
    while True:
        if pos_location == 1 or pos_location == 3:
            print("Do not report misdemeanor conviction if disposition date is more than 3 years.")
            V1 = input("Was the offense also in maryland only?")
            if V1 in ("Y","y","Yes","yes","YES"):
                print("Do not report 1st offense (misdemeanor conviction or pending offense) of :  (i) trespass under §§ 6-402 \nor 6-403  OR (ii)  disturbance of the peace under § 10-201 OR (iii) assault in the second degree \nunder § 3-203 of the Criminal Law Article of the Maryland Code,\n refer to WI Package Review for Montgomery County, MD.")
            else:
                print("Continue on!")
            break
        elif V in ("N","n","No","no","NO"):
            print("Continue on!")
            break
        else:
            print("Enter Y or N")
    return
def MA():
    print("Do not report outside of 7 year scope")
    return
def MI():
    if pos_location == 1 or pos_location == 3:
        print("Do not report misdemeanor alternate disposition (e.g. diversion, deferral, ...)")
    else:
        print(state + " " + notrelevant)
    return
def MT():
    if pos_location == 2 or pos_location == 3:
        print("Do not report out of a 7 year scope.")
    else:
        print(state + " " + notrelevant)
    return
def NH():
    if pos_location == 2 or pos_location == 3:
        print("Do not report out of 7 year scope, unless candidate makes $20,000\n or more annually")
    else:
        print(state + " " + notrelevant)
    return
def NM():
    print("If residency is in New Mexico:")
    print("Rule 1:Only report convictions and active pending cases / warrants (do not report non-convictions \n / alternates (deferrals / diversions in which individual is on probation))")
    print("Rule 2: Do not report outside of a 7 year scope.")
    return
def NY():
    print(staterules)
    print("Rule 1: Only report convictions and active pending cases / warrants (do not report non-convictions \n / alternates (deferrals / diversions in which individual is on probation))")
    print("Rule 2: Do not report Adjournment in contemplation of dismissal (ACD) disposition)")
    print("Rule 3:Do not report out of 7 year scope, unless candidate makes $25,000 or more annually")
def PA():
    posloc == True
    #placeholder for when later I'll probably parameterize the position location/ residency as a constant or global var so 
    #users dont have to specify every time. I can just as a question as posR"= ()
    if pos_location == 1 or pos_location == 3:
        print("If the residency is in Pennsylvania only report convictions and warrents \n(do not report pending or alternate (diversion, dismissed, or any related dispositions))")
def VI():
    if pos_location == 2 or pos_location == 3:
        print("Only report convictions and warrants (do not report pending or alternate \n (diversion, dismissed, or any related dispositions))")
    else:
        print(state + " " + notrelevant)
    return
def WA():
    if pos_location == 2 or pos_location == 3:
        print("If the makes >$20,000 annually do not report out of 7 year scope")
    return
    #TODO edit this later so i can input the pos_res variable into the function def
def WI():
    Madison = input("Is the position in Madison, WI? (enter Y/N):")
    if Madison in yes:
        ("Only report 3 years from when the individual has been placed on probation (start date) / disposition \ndate, paroled (start of parole), released from incarceration, or paid a fine")
    if pos_location == 2 or pos_location == 3:
        print("Do not report Guilty But Not Guilty Due to Mental Disease/Defect disposition")
        
        
        
        


        
        
def state_cases(state):
    # state_switcher(state)
    #Need to figure out how to take the state arguement and then use it to call state_switcher
    state_switcher = {
        "CA": CA,
        "DC": DC,
        "GA": GA,
        "HI": HI,
        "IN": IN,
        "KS": KS,
        "KY": KY,
        "MD": MD,
        "MA": MA,
        "MI":MI,
        "MT":MT,
        "NH":NH,
        "NM":NM,
        "NY":NY,
        "PA":PA,
        "VI":VI,
        "WA":WA,
        "WI":WI
    }
    
    # Get the function from switcher dictionary
    Switch_func = state_switcher.get(state, lambda: "No special restrictions on entered state.")
    # Execute the function
    Switch_func()

#the statement above is for in the future where I start only listing rules depending on whether pos_res is.
state = get_state(state)
pos_location = pos_loc()
state_cases(state)
