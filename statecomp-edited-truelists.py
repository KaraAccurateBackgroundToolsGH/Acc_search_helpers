import datetime
from datetime import date
from rich import print
from rich.console import Console
from rich.panel import Panel
import sys

#TODO: EDIT CONSISTANCY OF IF RESIDENCY STRINGS

console = Console()
rules = lambda n: [False for _ in range(n)]
NR7years,noaltdispos,NR10yrscope,NRfel7yr,NRmisd5year,NRfirstoff,NRconvoD2A,NR7yr_exc20k,NRmsd3yrdispo,weirdmarylandrule,NRadjournment,NR7r_exc25k,NRpendalt,prob3years,GbnotG  = rules(15)

#ruleslisthere just to make things a bit easier. hmm maybe i should just make them strings, then i can just say if state == rule title.
ruleslist = [NR7years,noaltdispos,NR10yrscope,NRfel7yr,NRmisd5year,NRfirstoff,NRconvoD2A,NR7yr_exc20k,NRmsd3yrdispo,weirdmarylandrule,
NRadjournment,NR7r_exc25k,NRpendalt,prob3years,GbnotG]

# state = input("Enter the state (be careful of spelling - im too lazy at the moment to do something that can handle mispellings)\n Side note 2: if the state is in the US virgin islands just type VI or US Virgin islands:\n: ")
state = input("Enter the state:")
#i could put this on the bottom after I run get_state but for now i should make it a const
PRB = ["P","R","B"]
while True:
    pos_res = input(f"Is (P) the position location in {state}, (R) the residency location in {state} or (B) both?:")
    pos_res = pos_res.upper()
    if pos_res in PRB:
        break

pos_res = PRB.index(pos_res) + 1

    


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


def CA():
    NR7years,noaltdispos =  [True, "NR7years"],[True,"noaltdispos"]
    #get input whether the position is in SF, and whether the MJ rule applies, if it applies it prints the MJ rule, otherwise returns "no"
    def SF():
        # gets a yes or no answer regarding whether the position is in SF
        def get_SF():
            while True:
                SF = input("Is the position in San Francisco?: ")
                if SF in yes or SF in no:
                    return SF
                else:
                    print("Enter Y or N!")
        #asks questions applicability non-felony marijuana convictions,if the SF marijuana rule isnt applicable it returns "no"
        def yes_SF(SF):
            marijuana = input("Is the disposition a non-felony marijiana conviction?: ")
            if marijuana in yes:
                console.print(Panel.fit("Do not report non-felony marijuana convictions -  Exception: Report if the disposition is within the past 2 \n years and the individual was under age 21 at the time of conviction",style="bold red"))
                return
            else:
                print("Continue on")
                return("no")
        #gets the SF y/n answer, if getSF is yes than it does a function to see if the SF marijuana rule is applicable
        SF = get_SF()
        if SF in yes:
            return yes_SF(SF)
        # return "no"
    #takes position/residence info and spits out rules according to that input
    if pos_res == 1:
        if SF() == "no":
            console.print(Panel.fit("Do not report dismeanor marijuana cases outside of a 2 year scope",style="bold red"))
        return
    #returns NR7years and noaltdispo
    elif pos_res == 2:
        console.print(Panel.fit("Rule 1: \n Only report convictions and active pending cases / warrants (do not report non-convictions / alternates \n (deferrals / diversions in which individual is on probation))\n",style="bold red"))
        console.print(Panel.fit("Rule 2: \n Do not report out of 7 year scope\n",style="bold red"))
        console.print(Panel.fit("Rule 3: \n Do not report 1203.4 case status or dispositions",style="bold red"))
        return NR7years,noaltdispos
    #returns NR7years and noaltdispo
    elif pos_res == 3:
        Sanfran = SF() 
        console.print(Panel.fit("Rule 1: \n Only report convictions and active pending cases / warrants (do not report non-convictions / alternates \n (deferrals / diversions in which individual is on probation))\n",style="bold red"))
        console.print(Panel.fit("Rule 2: \n Do not report out of 7 year scope\n",style="bold red"))
        console.print(Panel.fit("Rule 3: \n Do not report 1203.4 case status or dispositions\n",style="bold red"))
        if Sanfran == "no":
            console.print(Panel.fit("Rule 4: \n Do not report dismeanor marijuana cases outside of a 2 year scope",style="bold red"))
        return NR7years,noaltdispos 
def DC(): 
    NR10yrscope = [True,"NR10yrscope"]
    if pos_res == 1 or pos_res == 3:
        console.print(Panel.fit("If position is in DC do not report out of a 10 year scope",style="bold red"))
    return NR10yrscope
def GA():#TODO - make a first offender rule.
    NRfirstoffender = [True,"NRfirstoff"]
    while True:
        firstoff = input ("Is this a first offender act?")
        if firstoff in yes:
            console.print(Panel.fit("Do not report First Offender Act case status or disposition",style="bold red"))
            return NRfirstoffender
        elif firstoff in no:
            return
def HI():
    NRpendalt,NR7years = [True,"NRpendalt"],[True,"NR7years"]
    while True:
        if pos_res == 1 or pos_res == 3:
            console.print(Panel.fit("Rule 1: Only report convictions and active pending cases / warrants (do not report non-convictions / alternates \n(deferrals / diversions in which individual is on probation))\n",style="bold red"))
            console.print(Panel.fit("Rule 2: Do not report FELONY charges outside 7 year (may only use incarceration for the 7 years scope - \n NOT probation or parole - otherwise use disposition date)\n ",style="bold red"))
            console.print(Panel.fit("Rule 3: Do not report: MISDEMEANOR charges outside 5 year (may only use incarceration for the 5 year \n scope - NOT probation or parole - otherwise use disposition date)\n",style="bold red"))
            return NRpendalt, NR7years
        elif pos_res == 2:
            console.print(Panel.fit("No rules apply to you",style="bold red")) #remove this late
        else:
            print("Enter Y or N")
    return
def IN():
    NRconvoD2A = [True,"NRconvoD2A"]
    while True:
        residenceIN = input("Is the candidates residence in Indiana?: ")
        if residenceIN in ("Y","y","Yes","yes","YES"):
            console.print(Panel.fit("Do not report Class D felony convictions that have been entered or converted to Class A \n misdemeanor convictions, only report the misdemeanor",style="bold red"))
            return NRconvoD2A
        elif residenceIN in ("N","n","No","no","NO"):
            console.print(Panel.fit("This rule isnt relevant to you!",style="bold red"))
        else:
            print("Enter Y or N")
    return
def KS():
    NR7yr_exc20k = [True,"NR7yr_exc20k"]
    console.print(Panel.fit("Do not report out of 7 year scope, unless candidate makes $20,000 or more annually",style="bold red"))
    return NR7yr_exc20k
def KY():
    NRpendalt = [True,"NRpendalt"]
    V = input("Was the offense committed in Kentucky?")
    while True:
        if V in yes:
            console.print(Panel.fit("Only report convictions and warrants (do not report pending or alternate \n(diversion, dismissed, or any related dispositions))\n",style="bold red"))
            return NRpendalt
        elif V in no:
            print("Continue on!")
            break
        else:
            print("Enter Y or N")
    return
def MD():
    weirdmarylandrule = [True,"weirdmarylandrule"]
    while True:
        V = input("Was the position in Montogomery County MD?:")
        if V in yes:
            console.print(Panel.fit("Do not report misdemeanor conviction if disposition date is more than 3 years.",style="bold red"))
            V1 = input("Was the offense also in maryland only?")
            if V1 in yes:
                console.print(Panel.fit("Do not report 1st offense (misdemeanor conviction or pending offense) of :  (i) trespass under §§ 6-402 \nor 6-403  OR (ii)  disturbance of the peace under § 10-201 OR (iii) assault in the second degree \nunder § 3-203 of the Criminal Law Article of the Maryland Code,\n refer to WI Package Review for Montgomery County, MD.",style="bold red"))
                return weirdmarylandrule
            else:
                print("Continue on!")
            break
        elif V in no:
            print("Continue on!")
            break
        else:
            print("Enter Y or N")
    return
def MA():
    NR7years = [True,"NR7years"]
    console.print(Panel.fit("Do not report outside of 7 year scope",style="bold red"))
    return NR7years
def MI():
    noaltdispos = [True,"noaltdispos"]
    if pos_res == 1 or pos_res == 3:
        console.print(Panel.fit("Do not report misdemeanor alternate disposition (e.g. diversion, deferral, ...)",style="bold red"))
        return noaltdispos
    return
def MT():
    NR7years = [True,"NR7years"]
    if pos_res == 2 or pos_res == 3:
        console.print(Panel.fit("Do not report out of a 7 year scope.",style="bold red"))
        return NR7years
    return
def NH():
    NR7years = [True,"NR7years"]
    if pos_res == 2 or pos_res == 3:
        console.print(Panel.fit("Do not report out of 7 year scope, unless candidate makes $20,000\n or more annually",style="bold red"))
        return NR7years
    return
def NM():
    NR7years,NRpendalt = [True,"NR7years"],[True,"NRpendalt"]
    if pos_res == 2 or pos_res == 3:
        console.print(Panel.fit("Rule 1:Only report convictions and active pending cases / warrants (do not report non-convictions \n / alternates (deferrals / diversions in which individual is on probation))",style="bold red"))
        console.print(Panel.fit("Rule 2: Do not report outside of a 7 year scope.",style="bold red"))
        return NR7years,NRpendalt
    return
def NY():
    noaltdispos,NRadjournment,NR7r_exc25k  = [True,"noaltdispos"],[True,"NRadjournment"],[True,"NR7r_exc25k"]
    console.print(Panel.fit("Rule 1: Only report convictions and active pending cases / warrants (do not report non-convictions \n / alternates (deferrals / diversions in which individual is on probation))",style="bold red"))
    console.print(Panel.fit("Rule 2: Do not report Adjournment in contemplation of dismissal (ACD) disposition)",style="bold red"))
    console.print(Panel.fit("Rule 3:Do not report out of 7 year scope, unless candidate makes $25,000 or more annually",style="bold red"))
    return noaltdispos,NRadjournment,NR7r_exc25k
def PA():
    NRpendalt = [True,"NRpendalt"]
    if pos_res == 2 or pos_res == 3:
        console.print(Panel.fit("Only report convictions and warrents \n(do not report pending or alternate (diversion, dismissed, or any related dispositions))",style="bold red"))
        return NRpendalt
def VI():
    NRpendalt = [True,"NRpendalt"]
    if pos_res == 2 or pos_res == 3:
        console.print(Panel.fit("Only report convictions and warrants (do not report pending or alternate \n (diversion, dismissed, or any related dispositions))",style="bold red"))
        return NRpendalt
    return
def WA():
    NR7yr_exc20k = [True,"NR7yr_exc20k"]
    if pos_res == 2 or pos_res == 3:
        console.print(Panel.fit("If the candidat makes >$20,000 annually do not report out of 7 year scope",style="bold red"))
        return NR7yr_exc20k
    return
    #TODO edit this later so i can input the pos_res variable into the function def
def WI():
    prob3years,GbnotG = [True,"prob3years"],[True,"GbnotG"]
    if pos_res == 1:
        Madison = input("Is the position in Madison, WI? (enter Y/N):")
        if Madison in yes:
            console.print(Panel.fit("Only report 3 years from when the individual has been placed on probation (start date) / disposition \ndate, paroled (start of parole), released from incarceration, or paid a fine",style="bold red"))
            return prob3years
    if pos_res == 2:
            console.print(Panel.fit("Do not report Guilty But Not Guilty Due to Mental Disease/Defect disposition",style="bold red"))
            return GbnotG
    if pos_res  == 3:
        Madison = input("Is the position in Madison, WI? (enter Y/N):")
        if Madison in yes:
            console.print(Panel.fit("Only report 3 years from when the individual has been placed on probation (start date) / disposition \ndate, paroled (start of parole), released from incarceration, or paid a fine",style="bold red"))
            console.print(Panel.fit("Do not report Guilty But Not Guilty Due to Mental Disease/Defect disposition",style="bold red"))
            return prob3years,GbnotG
        else:
            console.print(Panel.fit("Do not report Guilty But Not Guilty Due to Mental Disease/Defect disposition",style="bold red"))
            return GbnotG
        
        


        
        
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

# pos_res = input("Is (P) the position location in the state you entered, (R) the residency location in the state you entered or (B) both?:")
#the statement above is for in the future where I start only listing rules depending on whether pos_res is.
get_state(state)
print(state_cases(state))