from datetime import datetime
# from rich import console.print
from rich.console import Console
# import tkinter as tk
import sys

console = Console()
# window = tk.Tk
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
["AHOLD S&S","AHOLD S + S","AHOLD STOP & SHOP","AHOLD STOP"], ["AL AIR","ALASKA"], ["AMAZON","AMZ","AMAZON SALESFORCE"],
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
    NRcontfind,NR_ARD, NRret = [True,"NRcontfind "],[True,"NR_ARD "],[True,"NRret "]
    console.console.print("Do not report continued without finding (basically a deferral)",style="bold red")
    console.print("Do not report accelerated rehabilitation program(ARD)",style="bold red")
    console.print("Do not report retired",style="bold red")
    return NRcontfind,NR_ARD, NRret 
def aholdfresh(): 
    Ractwarr, Ractpend, NRaltdispo = [True,"Ractwarr "],[True,"Ractpend "],[True,"NRaltdispo "]
    NRfel_an_gam,NRmis_an_gam, NRtraff = [True,"NRfel_an_gam "],[True,"NRmis_an_gam "],[True,"NRtraff "]
    console.print("Report ACTIVE WARRANTS",style="bold red")
    console.print("Report ACTIVE / PENDING CHARGES",style="bold red")
    console.print("Do not report NON-CONVICTIONS / ALTERNATE DISPOSITIONS (including diversions, deferrals, etc.) ",style="bold red")
    console.print("Do not report FELONY CHARGES involving animals or gambling",style="bold red")
    console.print("Do not report MISDEMEANOR charges involving animals, gambling, alcohol, false ID, or licensing",style="bold red")
    console.print("Do not report Traffic-related charges regardless of charge level",style="bold red")
    return Ractwarr, Ractpend, NRaltdispo,NRfel_an_gam,NRmis_an_gam, NRtraff
def aholdretail(): 
    Ractwarr, Ractpend, NRaltdispo = [True,"Ractwarr "],[True,"Ractpend "],[True,"NRaltdispo "]
    console.print("Report ACTIVE WARRANTS",style="bold red")
    console.print("Report ACTIVE / PENDING CHARGES",style="bold red")
    console.print("Do not report NON-CONVICTIONS / ALTERNATE DISPOSITIONS (including diversions, deferrals, etc.) ",style="bold red")
    return Ractwarr, Ractpend, NRaltdispo
def aholdstop(): 
    Ractwarr, Ractpend, NRaltdispo = [True,"Ractwarr "],[True,"Ractpend "],[True,"NRaltdispo "]
    console.print("Report ACTIVE WARRANTS",style="bold red")
    console.print("Report ACTIVE / PENDING CHARGES",style="bold red")
    console.print("Do not report NON-CONVICTIONS / ALTERNATE DISPOSITIONS (including diversions, deferrals, etc.) ",style="bold red")
    return Ractwarr, Ractpend, NRaltdispo
def AlAir(): 
    Rnosal = [True,"Rnosal"]
    console.print("Report NO SALARY VERIFICATION - $25,000 ALREADY VERIFIED")
    return Rnosal
def amz(): 
    NR_ARD, NractKT,NR1stoffGA,NRaltdispoHI,NRret,NR10yrDC = [True,"NR_ARD "],[True,"NractKT"],[True,"NR1stoffGA"],[True,"NRaltdispoHI"],[True,"NRret "],[True,"NR10yrDC"]
    NR7yr25k,Raltdisp_probmet,RscpMSD, NRmjCA, RmjSF = [True,"NR7yr25k"],[True,"Raltdisp-probmet"],[True,"RscpMSD"],[True,"NRmjCA"],[True,"RmjSF"]
    NRyrfelHI,NR5yrmisHI,NoprobDCNV= [True,"NRyrfelHI"],[True,"NR5yrmisHI"],[True,"NoprobDCNV"]
    
    console.print("Do not report  accelerated rehabilitation program (ard)",style="bold red")
    console.print("Do not report ACTIVE WARRANTS if offense is located in Kentucky (KY); OR candidate residence location in U.S. Virgin Islands (VI)",style="bold red")
    console.print("Do not report first offender act based on the candidate residence location in georgia (ga) -- not offense location",style="bold red")
    console.print("Report pending or alternate dispositions (including diversions, deferrals, etc.) based on the candidate position location in hawaii (hi), montgomery county (md), or pennsylvania (pa); or residence in new mexico (nm); or position and residence in new york (ny)",style="bold red")
    console.print("Do not report retired",style="bold red")
    console.print("Do not report out of 10 year scope based on the Candidate residence location in district of Columbia (dc) -- not position location",style="bold red")
    console.print("Do not report out of 7 year scope, unless candidate makes $25,000 or more annually based on the candidate residence location only in new york (ny) -- not position location",style="bold red")
    console.print("You can report non-convictions / alternate dispositions (including diversions, deferrals, etc.) where the sentenced probationary period has been met.",style="bold red")
    console.print("Report scope for misdemeanor convictions (or active warrants on convictions) is determined by disposition date, jail, probation (where permitted), prison, or parole duration, as applicable.",style="bold red")
    console.print("Do not report misdemeanor marijuana cases outside of 2 year scope based on the candidate residence location in california (ca) -- not position location",style="bold red")
    console.print("Report non-felony marijuana convictions if position is located in san francisco, ca (still need to consider california statewide requirement above)",style="bold red")
    console.print("Do not report felony charges outside 7 year (may only use incarceration for the 7 years scope - not probation or parole - otherwise use disposition date) if current residence or position is located in hawaii",style="bold red")
    console.print("Do not report: misdemeanor charges outside 5 year (may only use incarceration for the 5 year scope - not probation or parole - otherwise use disposition date) if current residence or position is located in hawaii",style="bold red")
    console.print("Probation is not permitted to be used for scope if the candidate’s residence and/or position location are in district of columbia (dc) and nevada (nv).",style="bold red")
    console.print("any sentencing that is a result of a probation violation / revocation should not be used to bring a case into scope if candidate's residence and/or position location are in ca, hi, ks, ma, md, nm, ny, wa, and madison wi (dane county).this includes jail or an active warrant issued only when it is from a probation violation or revocation.if the final disposition is updated, that can still bring the case into scope (ex: probation revoked, disposition updated to guilty).",style="bold red")
    return NractKT,NR1stoffGA,NRaltdispoHI,NR10yrDC,NRret,NR_ARD,NR7yr25k,Raltdisp_probmet,RscpMSD, NRmjCA, RmjSF,NRyrfelHI,NR5yrmisHI,NoprobDCNV
def AmElec(): 
    NRmsd,Nrdivdef = [True,"NRmsd"],[True,"Nrdivdef"]
    console.print("Do not report any dismdemeanor charges",style="bold red")
    console.print("Do not report diversion/deferral",style="bold red")
    return NRmsd,Nrdivdef
def AmMult():
    Ract7yr,Rpendnegcr,NRaltdispo,NR_CAmj = [True,"Ract7yr"],[True,"Rpendnegcr"],[True,"Ractpend "],[True,"NR_CAmj"]
    console.print("Report active warrants within 7 years involving neglect, cruelty, sex crimes, endangerment, trespassing, or violence",style="bold red")
    console.print("Report pending charges involving neglect, cruelty, sex crimes, endangerment, trespassing, or violence",style="bold red")
    console.print("Do not report non-convictions / alternate dispositions (including diversions, deferrals, etc.) ",style="bold red")
    console.print("If position/residence is located in California do not report marijuana possesion offenses",style="bold red")
    return Ract7yr,Rpendnegcr,NRaltdispo,NR_CAmj
def BaHealth(): 
    Ractwarr,Ractpend,Nraltdisexcdef = [True,"Ractwarr "],[True,"Ractpend "],[True,"Nraltdisexcdef"]
    console.print("Report active warrants",style="bold red")
    console.print("Report active / pending charges",style="bold red")
    console.print("Do not report non-convictions / alternate dispositions - exception: report if the disposition includes the word 'deferral' or 'deferred' except if position / residence is in CA",style="bold red")
    return Ractwarr,Ractpend,Nraltdisexcdef 
def Cal(): 
    NRaltdispo, Ractwarr, Ractpend = [True,"NRaltdispo "],[True,"Ractwarr "],[True,"Ractpend "]
    console.print("Do not report non-convictions / alternate dispositions (including diversions, deferrals, etc.) ",style="bold red")
    console.print("Report active warrants",style="bold red")
    console.print("Report active / pending charges",style="bold red")
    return NRaltdispo, Ractwarr, Ractpend
def CpsEn(): 
    RepALLconv = [True,"RepALLconv"]
    console.print("Report all convictions regardless of scope",style="bold red")
    return RepALLconv
def F5(): 
    NRaltdispo, NRmisd5year, NRmj2yr = [True,"NRaltdispo "],[True,"NRmisd5year"],[True,"NRmj2yr"]
    console.print("Do not report non-convictions / alternate dispositions (including diversions, deferrals, etc.) ",style="bold red")
    console.print("Do not report misdemeanor charges outside 5 year scope",style="bold red")
    console.print("Do not report marijuana charges outside 2 year scope",style="bold red")
def FPI(): 
    NR_ARD,NRactwarr,NRactpend,NRadjwith,NRbailbond,NR_ARD,Nrdivdef = [True,"NR_ARD "],[True,"NRactwarr"],[True,"NRactpend"],[True,"NRadjwith"],[True,"NR_ARD "],[True,"Nrdivdef"]
    NRabeyplea,NRjudpray,NRfeldefadj = [True,"NRabeyplea"],[True,"NRjudpray"],[True,"NRfeldefadj"]
    
    console.print("Do not report accelerated rehabilitation program (ard)",style="bold red")
    console.print("Do not report active warrants",style="bold red")
    console.print("Do not report active / pending charges",style="bold red")
    console.print("Do not report adjudication withheld",style="bold red")
    console.print("Do not report bail / bond forfeiture",style="bold red")
    console.print("Do not report accelerated rehabilitation program (ard)",style="bold red")
    console.print("Do not report diversion / deferral",style="bold red")
    console.print("Do not report plea in abeyance",style="bold red")
    console.print("Do not report prayer for judgment",style="bold red")
    console.print("Do not report retired",style="bold red")
    console.print("Do not report felony deferred adjudication",style="bold red")
    
    return NR_ARD,NRactwarr,NRactpend,NRadjwith,NRbailbond,NR_ARD,Nrdivdef,NRabeyplea,NRjudpray,NRfeldefadj 
def FreshDir(): 
    NoSalVerNY = [True,"NoSalVerNY"]
    console.print("If position/residence if location in NY only - NO SALARY VERIFICATION - $25,000 ALREADY VERIFIED",style="bold red")
    return NoSalVerNY
def Horizon(): 
    NoSalVer  = [True,"NoSalVer"]
    console.print("No salary verification needed - $25,000 already verified",style="bold red")
    return NoSalVer
def JCP(): 
    NRabeyplea,NRjudpray,R_ALLfel = [True,"NRabeyplea"] , [True,"NRjudpray"],[True,"R_ALLfel"]
    console.print("Do not report plea in abeyance",style="bold red")
    console.print("Do not report prayer for judgment ",style="bold red")
    console.print("Report felony convictions involving theft, sex, or violence regardless of scope",style="bold red")
def MoCoors (): 
    NR7yrdispo = [True,"NR7yrdispo"]
    console.print("Do not report out of 7 year scope from disposition date. (do not consider any sentencing. use of disposition date rather than sentencing date is intentional.)",style="bold red")
    return NR7yrdispo
def Munich(): 
    NRmsd = [True,"NRmsd"]
    console.print("Do not report any misdemeanor charges",style="bold red")
    return NRmsd
def NaInc(): 
    Ractwarr, NRaltdispo ,NRmisdpend = [True,"NRactwarr"],[True,"NRaltdispo "],[True,"NRmisdpend"]
    console.print("Report active warrants",style="bold red")
    console.print("Do not report non-convictions / alternate dispositions (including diversions, deferrals, etc.) ",style="bold red")
    console.print("Do not report misdemeanor pending charges",style="bold red")
    return Ractwarr, NRaltdispo ,NRmisdpend
def NeBalance(): 
    NRmisdAlt = [True,"NRmisdAlt"]
    console.print("Do not report misdemeanor non-convictions / alternate dispositions (including diversions, deferrals, etc.)",style="bold red")
    return NRmisdAlt
def OnSemiconductor():
    NRaltdispo = [True,"NRaltdispo "]
    console.print("Do not report non-convictions / alternate dispositions (including diversions, deferrals, etc.) ",style="bold red")
    return NRaltdispo
def PuStorage(): 
    NR_ARD,NRactwarr,NRactpend,NRadjwith,NRbailbond,NR_ARD,Nrdivdef = [True,"NR_ARD "],[True,"NRactwarr"],[True,"NRactpend"],[True,"NRadjwith"],[True,"NR_ARD "],[True,"Nrdivdef"]
    NRabeyplea,NRjudpray,NRfeldefadj = [True,"NRabeyplea"],[True,"NRjudpray"],[True,"NRfeldefadj"]

    console.print("Do not report accelerated rehabilitation program (ard)",style="bold red")
    console.print("Do not report active / pending charges",style="bold red")
    console.print("Do not report adjudication withheld",style="bold red")
    console.print("Do not report bail / bond forfeiture",style="bold red")
    console.print("Do not report accelerated rehabilitation program (ard)",style="bold red")
    console.print("Do not report diversion / deferral except judgement withheld, suspended imposition of sentence, and stet docket",style="bold red")
    console.print("Do not report plea in abeyance",style="bold red")
    console.print("Do not report prayer for judgment ",style="bold red")
    console.print("Do not report probation before judgement",style="bold red")
    console.print("Do not report retired",style="bold red")
    console.print("Report felony deferred adjudication",style="bold red")
    
    return NR_ARD,NRactwarr,NRactpend,NRadjwith,NRbailbond,NR_ARD,Nrdivdef,NRabeyplea,NRjudpray,NRfeldefadj 
def ReFinancial ():
    NRaltdispo = [True,"NRaltdispo "]
    console.print("Do not report non-convictions / alternate dispositions (including diversions, deferrals, etc.) ",style="bold red")
    return NRaltdispo
def skyg(): 
    NRaltdispo = [True,"NRaltdispo "]
    console.print("Do not report non-convictions / alternate dispositions (including diversions, deferrals, etc.) ",style="bold red")
    return NRaltdispo
def starbucks(): 
    NRmsd3yr = [True,"NRmsd3yr"]
    rule1 = "Do not report misdemeanor charges outside 3 year scope"
    print(rule1)
    return NRmsd3yr
def Disn(): 
    NRactwarr,NRactpend = [True,"NRactwarr"],[True,"NRactpend"]
    console.print("Do not report active warrants",style="bold red")
    console.print("Do not report active / pending charges",style="bold red")
    return NRactwarr,NRactpend 
def UbRazier(): 
    Rtheftalcdrug = [True,"Rtheftalcdrug"]
    console.print("Report theft, alcohol, drug, or insurance / proof of financial responsibility infractions / lower level charges",style="bold red")
    return  Rtheftalcdrug
def UnBank(): 
    R_ALL_DISPOS = [True,"R_ALL_DISPOS"]
    console.print("REPORT ALL DISPOSITIONS",style="bold red")
    return R_ALL_DISPOS
def via(): 
    WeirdViaRule = [True,"WeirdViaRule"]
    console.print("Refer to R Client Specific Rules - Viacom for additional information",style="bold red")
    return WeirdViaRule


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
    # console.print(Switch_func(),style="bold red")
    clientrules = Switch_func()
    # console.print(Switch_func())

client = get_client(client)
client = client_cases(client)
sys.exit(client)

# console.print(client)