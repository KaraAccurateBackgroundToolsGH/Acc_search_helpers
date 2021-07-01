from datetime import datetime
# from rich import print
from rich.console import Console
import sys

console = Console()
#TODO:// MAKE PERLS FOR ALL THE SPECIAL CLIENTS
#TODO ADD EXTRA ALTS FOR AMAZON VENDORS YOU ENCOUNTER
#NOTE CLIENT EQUIVILANCY FUNCTION WORKS FINE,
client = input("Client:")
client = client.upper()
        
#global variables, these should work fine inside of my functions
yes = ["Y","y","Yes","yes","YES"]
no = ["N","n","No","no","NO"]

#the goal is to turn alternate input into the clients list
#so im going to make a list with alternate values for clients and then say if client is in list it equals x items in the official client list
#i think i can make this into a dictionary or a list of lists. okay cool the list of list thing totally works.


alts_list = [["ACCURATENOW","ACCURATE","ACC"], ["AHOLD","AHOLD FRESH"], ["AHOLD RETAIL","AHOLD RET","AHOLD R"],
["AHOLD S&S","AHOLD S + S","AHOLD STOP & SHOP","AHOLD STOP"], ["AL AIR","ALASKA"], ["AMAZON","AMZ"],
["AMERICAN ELECTRIC","AMERICAN ELECTRIC POWER","AM ELEC"], ["AMERICAN MULTI","AMERICAN MULTI CINEMA","AM MULTI","AMERICAN CINEMA"],
["BANNER","BH"], ["CALY"], ["CPS","CPS EN"], ["F5","F5 NET"], ["FPI","FPI MAN"], ["FRESH DIR","FRESH"],["HORIZON","HOR"],
["JCP","JCP PROCUREMENT","JCP PROCUREMENT INCC"], ["MOLSON","MOLSON COORS","MILLER","MILLERCOORS","MOLSON COORS INT."], ["MUN"], 
["NAVISTAR","NAVISTAR INC","NAVISTAR INC."] , ["NEW BALANCE","NEW BALANCE ATH"], ["ON","ON-SEMI"], ["PUBLIC STOR","PS"], ["RENEW","RENEW FIN"],
["SKYG"], ["STARBUCKS","STBK"], ["DISNEY","WALT DISNEY CO.","THE WALT DISNEY CO","WALT DISNEY COMPANY"], ["UBER","UBR","RAZIER"], 
["UNION","UNION B"], ["VIA"]]



clients = ["ACCURATENOW OFFICE","AHOLD FRESH FORMATS","AHOLD RETAIL BUSINESS SERVICES","AHOLD STOP AND SHOP",
"ALASKA AIR","AMAZON","AMERICAN ELECTRIC POWER SERVICE","AMERICAN MULTI-CINEMA",
"BANNER HEALTH","CALYPSO","CPS ENERGY","F5 NETWORKS","FPI MANAGEMENT","FRESH DIRECT","HORIZON AIR",
"JCP PROCUREMENT, INC.","MOLSON COORS / MILLERCOORS /MOLSON COORS INT.","MUNICH","NAVISTAR, INC.",
"NEW BALANCE ATHLETICS","ON SEMICONDUCTOR","PUBLIC STORAGE","RENEW FINANCIAL ","SKYGEN",
"STARBUCKS CORPORATION","THE WALT DISNEY COMPANY","UBER/RAZIER","UNION BANK","VIACOM"]

#takes any input from the alts list and matches it to the apporpriate official client name
def get_client(client):
    for i in range(0,28):
        if client in alts_list[i]:
            client = clients[i]
            return client




def accnow(): 
    print("Do not report continued without finding (basically a deferral)")
    print("Do not report accelerated rehabilitation program(ARD)")
    print("Do not report retired")
def aholdfresh(): 
    print("Report ACTIVE WARRANTS")
    print("Report ACTIVE / PENDING CHARGES")
    print("Do not report NON-CONVICTIONS / ALTERNATE DISPOSITIONS (including diversions, deferrals, etc.) ")
    print("Do not report FELONY CHARGES involving animals or gambling")
    print("Do not report MISDEMEANOR charges involving animals, gambling, alcohol, false ID, or licensing")
    print("Do not report Traffic-related charges regardless of charge level")
def aholdretail(): 
    print("Report ACTIVE WARRANTS")
    print("Report ACTIVE / PENDING CHARGES")
    print("Do not report NON-CONVICTIONS / ALTERNATE DISPOSITIONS (including diversions, deferrals, etc.) ")
def aholdstop(): 
    print("Report ACTIVE WARRANTS")
    print("Report ACTIVE / PENDING CHARGES")
    print("Do not report NON-CONVICTIONS / ALTERNATE DISPOSITIONS (including diversions, deferrals, etc.) ")
def AlAir(): 
    print("Report NO SALARY VERIFICATION - $25,000 ALREADY VERIFIED")
def amz(): 
    print("Do not report  accelerated rehabilitation program (ard)")
    print("Do not report ACTIVE WARRANTS if offense is located in Kentucky (KY); OR candidate residence location in U.S. Virgin Islands (VI)")
    print("Do not report first offender act based on the candidate residence location in georgia (ga) -- not offense location")
    print("Report pending or alternate dispositions (including diversions, deferrals, etc.) based on the candidate position location in hawaii (hi), montgomery county (md), or pennsylvania (pa); or residence in new mexico (nm); or position and residence in new york (ny)")
    print("Do not report retired")
    print("Do not report out of 10 year scope based on the Candidate residence location in district of Columbia (dc) -- not position location")
    print("Do not report out of 7 year scope, unless candidate makes $25,000 or more annually based on the candidate residence location only in new york (ny) -- not position location")
    print("You can report non-convictions / alternate dispositions (including diversions, deferrals, etc.) where the sentenced probationary period has been met.")
    print("Report scope for misdemeanor convictions (or active warrants on convictions) is determined by disposition date, jail, probation (where permitted), prison, or parole duration, as applicable.")
    print("Do not report misdemeanor marijuana cases outside of 2 year scope based on the candidate residence location in california (ca) -- not position location")
    print("Report non-felony marijuana convictions if position is located in san francisco, ca (still need to consider california statewide requirement above)")
    print("Do not report felony charges outside 7 year (may only use incarceration for the 7 years scope - not probation or parole - otherwise use disposition date) if current residence or position is located in hawaii")
    print("Do not report: misdemeanor charges outside 5 year (may only use incarceration for the 5 year scope - not probation or parole - otherwise use disposition date) if current residence or position is located in hawaii")
    print("Probation is not permitted to be used for scope if the candidate’s residence and/or position location are in district of columbia (dc) and nevada (nv).")
    print("any sentencing that is a result of a probation violation / revocation should not be used to bring a case into scope if candidate's residence and/or position location are in ca, hi, ks, ma, md, nm, ny, wa, and madison wi (dane county).this includes jail or an active warrant issued only when it is from a probation violation or revocation.if the final disposition is updated, that can still bring the case into scope (ex: probation revoked, disposition updated to guilty).")
def AmElec(): 
    print("Do not report any dismdemeanor charges")
    print("Do not report diversion/deferral")
def AmMult():
    print("Report active warrants within 7 years involving neglect, cruelty, sex crimes, endangerment, trespassing, or violence")
    print("Report pending charges involving neglect, cruelty, sex crimes, endangerment, trespassing, or violence")
    print("Do not report non-convictions / alternate dispositions (including diversions, deferrals, etc.) ")
    print("If position/residence is located in California do not report marijuana possesion offenses")
def BaHealth(): 
    print("Report active warrants")
    print("Report active / pending charges")
    print("Do not report non-convictions / alternate dispositions - exception: report if the disposition includes the word 'deferral' or 'deferred' except if position / residence is in CA")
def Cal(): 
    print("Do not report non-convictions / alternate dispositions (including diversions, deferrals, etc.) ")
    print("Report active warrants")
    print("Report active / pending charges")
def CpsEn(): 
    print("Report all convictions regardless of scope")
def F5(): 
    print("Do not report non-convictions / alternate dispositions (including diversions, deferrals, etc.) ")
    print("Do not report misdemeanor charges outside 5 year scope")
    print("Do not report marijuana charges outside 2 year scope")
def FPI(): 
    print("Do not report accelerated rehabilitation program (ard)")
    print("Do not report active warrants")
    print("Do not report active / pending charges")
    print("Do not report adjudication withheld")
    print("Do not report bail / bond forfeiture")
    print("Do not report accelerated rehabilitation program (ard)")
    print("Do not report accelerated rehabilitation program (ard)")
    print("Do not report diversion / deferral")
    print("Do not report plea in abeyance")
    print("Do not report prayer for judgment ")
    print("Do not report retired")
    print("Do not report felony deferred adjudication")
def FreshDir(): 
    print("If position/residence if location in NY only - NO SALARY VERIFICATION - $25,000 ALREADY VERIFIED")
def Horizon(): 
    print("No salary verification needed - $25,000 already verified")
def JCP(): 
    print("Do not report plea in abeyance")
    print("Do not report prayer for judgment ")
    print("Report felony convictions involving theft, sex, or violence regardless of scope")
def MoCoors (): 
    print("Do not report out of 7 year scope from disposition date. (do not consider any sentencing. use of disposition date rather than sentencing date is intentional.)")
def Munich(): 
    print("Do not report any misdemeanor charges")
def NaInc(): 
    print("Report active warrants")
    print("Do not report non-convictions / alternate dispositions (including diversions, deferrals, etc.) ")
    print("Do not report misdemeanor pending charges")
def NeBalance(): 
    print("Do not report misdemeanor non-convictions / alternate dispositions (including diversions, deferrals, etc.)")
def OnSemiconductor(): 
    print("Do not report non-convictions / alternate dispositions (including diversions, deferrals, etc.) ")
def PuStorage(): 
    print("Do not report accelerated rehabilitation program (ard)")
    print("Do not report active / pending charges")
    print("Do not report adjudication withheld")
    print("Do not report bail / bond forfeiture")
    print("Do not report accelerated rehabilitation program (ard)")
    print("Do not report diversion / deferral except judgement withheld, suspended imposition of sentence, and stet docket")
    print("Do not report plea in abeyance")
    print("Do not report prayer for judgment ")
    print("Do not report probation before judgement")
    print("Do not report retired")
    print("Report felony deferred adjudication")
def ReFinancial (): 
    print("Do not report non-convictions / alternate dispositions (including diversions, deferrals, etc.) ")
def skyg(): 
    print("Do not report non-convictions / alternate dispositions (including diversions, deferrals, etc.) ")
def starbucks(): 
    # print("Do not report misdemeanor charges outside 3 year scope")
    rule1 = "Do not report misdemeanor charges outside 3 year scope"
    return rule1
def Disn(): 
    print("Do not report active warrants")
    print("Do not report active / pending charges")
def UbRazier(): 
    print("Report theft, alcohol, drug, or insurance / proof of financial responsibility infractions / lower level charges")
def UnBank(): 
    print("REPORT ALL DISPOSITIONS")
def via(): 
    print("Refer to R Client Specific Rules - Viacom for additional information")



def client_cases(client):
    # state_switcher(state)
    #Need to figure out how to take the state arguement and then use it to call state_switcher
    client_switcher = {
        "ACCURATENOW OFFICE": accnow,
        "AHOLD FRESH FORMATS": aholdfresh,
        "AHOLD RETAIL BUSINESS SERVICES": aholdretail,
        "^AHOLD STOP AND SHOP": aholdstop,
        "ALASKA AIR": AlAir,
        "AMAZON": amz,
        "AMERICAN ELECTRIC POWER SERVICE": AmElec,
        "AMERICAN MULTI-CINEMA": AmMult,
        "BANNER HEALTH": BaHealth,
        "CALYPSO": Cal,
        "CPS ENERGY": CpsEn,
        "F5 NETWORKS": F5,
        "FPI MANAGEMENT": FPI,
        "FRESH DIRECT": FreshDir,
        "HORIZON AIR": Horizon,
        "^JCP PROCUREMENT, INC.": JCP,
        "MOLSON COORS / MILLERCOORS /MOLSON COORS INT.": MoCoors,
        "^MUNICH": Munich,
        "NAVISTAR, INC.": NaInc,
        "NEW BALANCE ATHLETICS": NeBalance,
        "ON SEMICONDUCTOR": OnSemiconductor,
        "PUBLIC STORAGE": PuStorage,
        "RENEW FINANCIAL ": ReFinancial ,
        "SKYGEN": skyg,
        "STARBUCKS CORPORATION": starbucks,
        "THE WALT DISNEY COMPANY": Disn,
        "UBER/RAZIER": UbRazier,
        "UNION BANK": UnBank,
        "VIACOM": via
    }
    Switch_func = client_switcher.get(client, lambda: "No special restrictions on entered client.")
    # Execute the function
    console.print(Switch_func(),style="bold red")
    # print(Switch_func())

client = get_client(client)
client = client_cases(client)
sys.exit(client)

# print(client)
