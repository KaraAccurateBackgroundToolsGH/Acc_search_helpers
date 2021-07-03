from datetime import datetime
#you know i might be able to just plug data into an excel spreadsheet and it can spit out things back for me.
#TODO:// MAKE STATE FUNCTION THAT GETS THE STATE AND CONVERTS IT INTO A PROPER FORMAT

state = input("Enter the state (be careful of spelling - im too lazy at the moment to do something that can handle mispellings)\n Side note 2: if the state is in the US virgin islands just type VI or US Virgin islands:\n: ")

#global variables, these should work fine inside of my functions
yes = ["Y","y","Yes","yes","YES"]
no = ["N","n","No","no","NO"]

#hmm should i put the state lists in here or in a constant. eh right now its easier to put them in here
def get_state(state):
    state = state.upper()
    state_restrictions_short = ['CA', 'DC', 'GA', 'HI', 'IN', 'KS', 'KY', 'MD','MA', 'MI', 'MT', 'NH', 'NM', 'NY', 'PA', 'VI', 'WA', 'WI']
    st_restrictions = ['CALIFORNIA', 'DISTRICT OF COLUMBIA', 'GEORGIA', 'HAWAII', 'INDIANA', 'KANSAS', 'KENTUCKY', 'MARYLAND', 'MASSACHUSETTS',
    'MICHIGAN', 'MONTANA', 'NEW HAMPSHIRE', 'NEW MEXICO', 'NEW YORK', 'PENNSYLVANIA', 'U.S. VIRGIN ISLANDS', 'WASHINGTON', 'WISCONSIN']
    
    #makes state(now capitalized) into its state abbreviation
    if state in st_restrictions:
        index = st_restrictions.index(state)
        state = state_restrictions_short[index]
        #state is now in correct format now i turn it into a function call and pass it too my switcher function
    return state
        #this function might be out of scope but i can figure it out later
        
        
# for i in range(0,len(st_restrictions)):
#     st_restrictions[i] = state_restrictions_short[i]
# #makes st_restrictions == state_restrictiosn sh0rt- effectively turning all long versions of states into abbreviations    
    

def CA():
    #tests position location rules -raises enter1or2 if invalid response
    SF = input("Is the position in San Francisco?: ")
    while True:
        pos_location = input("Is (1) the position location in california,(2) the address location in California \n or (3) are both the position and the address in California \n")
        if pos_location == 1:
            print("Do not report dismeanor marijuana cases outside of a 2 year scope")
            #maybe put in something later where i can just ask questions about whether its a misdemeanor marijuana or not and if the answer is no i cam move on
            #eventually it would be great to get to a point where i can just have people enter info in a certain format, or fill in a form of some type and then
            #i can spit out the correct answer
            break
        elif pos_location == 2:
            print("Rule 1: \n Only report convictions and active pending cases / warrants (do not report non-convictions / alternates \n (deferrals / diversions in which individual is on probation))\n")
            print("Rule 2: \n Do not report out of 7 year scope\n")
            print("Rule 3: \n Do not report 1203.4 case status or dispositions")
            break
        elif pos_location == 3:
            print("Rule 1: \n Only report convictions and active pending cases / warrants (do not report non-convictions / alternates \n (deferrals / diversions in which individual is on probation))\n")
            print("Rule 2: \n Do not report out of 7 year scope\n")
            print("Rule 3: \n Do not report 1203.4 case status or dispositions\n")
            print("Rule 4: \n Do not report dismeanor marijuana cases outside of a 2 year scope")
            break

        else:
            print("Enter 1, 2, or 3!")
            pos_location = input("Is (1) the position location in california,(2) the address location in California \n or (3) are both the position and the address in California \n")
    # tests and instructs for the marijuana scope rule    -raises customError if invalid response
    while True:
        if SF in yes:
            marijuana = input("Is the disposition a non-felony marijiana conviction?: ")
            if marijuana in no:
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
    print("If position is in DC do not report out of a 10 year scope")
    return
def GA():
    print("Do not report First Offender Act case status or disposition")
    return
def HI():
    while True:
        pos_loc = input("Is the position location in Hawaii?: ")
        if pos_loc in ("Y","y","Yes","yes","YES"):
            print("Rule 1: Only report convictions and active pending cases / warrants (do not report non-convictions / alternates \n(deferrals / diversions in which individual is on probation))\n")
            print("Rule 2: Do not report FELONY charges outside 7 year (may only use incarceration for the 7 years scope - \n NOT probation or parole - otherwise use disposition date)\n ")
            print("Rule 3: Do not report: MISDEMEANOR charges outside 5 year (may only use incarceration for the 5 year \n scope - NOT probation or parole - otherwise use disposition date)\n")
            break
        elif pos_loc in ("N","n","No","no","NO"):
            print("Dont worry about any rules then!")
            break
        else:
            print("Enter Y or N")
    return
def IN():
    while True:
        residenceIN = input("Is the candidates residence in Indiana?: ")
        if residenceIN in ("Y","y","Yes","yes","YES"):
            print("Do not report Class D felony convictions that have been entered or converted to Class A \n misdemeanor convictions, only report the misdemeanor")
            break
        elif residenceIN in ("N","n","No","no","NO"):
            print("This rule isnt relevant to you!")
            break
        else:
            print("Enter Y or N")
    return
def KS():
    print("Do not report out of 7 year scope, unless candidate makes $20,000 or more annually")
    return
def KY():
    V = input("Was the offense committed in Kentucky?")
    while True:
        if V in yes:
            print("Only report convictions and warrants (do not report pending or alternate \n(diversion, dismissed, or any related dispositions))\n")
            break
        elif V in no:
            print("Continue on!")
            break
        else:
            print("Enter Y or N")
    return
def MD():
    while True:
        V = input("Was the position in Montogomery County MD?:")
        if V in ("Y","y","Yes","yes","YES"):
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
    print("If the position is in Michigan do not report misdemeanor alternate disposition (e.g. diversion, deferral, ...)")
    return
def MT():
    print("If the residency is in Montana do not report out of a 7 year scope.")
    return
def NH():
    print("If the residency is in New Hampshire do not report out of 7 year scope, unless candidate makes $20,000\n or more annually")
    return
def NM():
    print("If residency is in New Mexico:")
    print("Rule 1:Only report convictions and active pending cases / warrants (do not report non-convictions \n / alternates (deferrals / diversions in which individual is on probation))")
    print("Rule 2: Do not report outside of a 7 year scope.")
    return
def NY():
        print("Rule 1: Only report convictions and active pending cases / warrants (do not report non-convictions \n / alternates (deferrals / diversions in which individual is on probation))")
        print("Rule 2: Do not report Adjournment in contemplation of dismissal (ACD) disposition)")
        print("Rule 3:Do not report out of 7 year scope, unless candidate makes $25,000 or more annually")
def PA():
    posloc == True
    #placeholder for when later I'll probably parameterize the position location/ residency as a constant or global var so 
    #users dont have to specify every time. I can just as a question as posR"= ()
    if posloc == True:
        print("If the residency is in Pennsylvania only report convictions and warrents \n(do not report pending or alternate (diversion, dismissed, or any related dispositions))")
def VI():
    print("If residency is in the US Virgin Islands only report convictions and warrants (do not report pending or alternate \n (diversion, dismissed, or any related dispositions))")
    return
def WA():
    print("If the candidate has residency in Washington and makes >$20,000 annually do not report out of 7 year scope")
    return
    #TODO edit this later so i can input the pos_res variable into the function def
def WI():
    Madison = input("Is the position in Madison, WI? (enter Y/N):")
    if Madison in ("Y","y"):
        ("Only report 3 years from when the individual has been placed on probation (start date) / disposition \ndate, paroled (start of parole), released from incarceration, or paid a fine")
    if pos_res in ("R","r","B","b"):
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
    print(Switch_func())

pos_res = input("Is (P) the position location in the state you entered, (R) the residency location in the state you entered or (B) both?:")
#the statement above is for in the future where I start only listing rules depending on whether pos_res is.
get_state(state)
state_cases(state)
