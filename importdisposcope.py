import datetime
from datetime import date
from rich import print
from rich.console import Console
from rich.panel import Panel
import sys
# currently  im keeping the true values in usefiledate/useconvodate because this maybe can be moddified later so the user wont have to enter convo/file dates
#TODO: FORMAT THIS TO MAKE IT PRETTIER

def disposcope():

    console = Console()
    dispo = input("Disposition:")
    dispo = dispo.lower()
    
    #TODO// replace this later with your standard get_var function that uses a possessionible list of input values and matches them up to official values on the list. 
    
    if dispo == "convicted" or dispo == "conviction":
        dispo = "convicted/conviction"
    
    #number == 19
    convictions = ["adjudicated","admission","alford plea","convicted/conviction","exparte - admission of guilt ","guilty","guilty - withheld/judgment withheld (id)","guilty in absentia","judgment for state (hi)",
    "judgment of community supervision (tx)","judgment of conviction","no contest","nolo contendere","paid fines","plea by agreement","pled guilty - conviction","responsible","suspended execution of sentencing"]
    
    #count == 29
    abs_non_convs = ["acquittal/acquitted","abandoned","adjournment in contemplation of dismissal (ny)^","charges vacated (wa)","closed-jeopardy or other conviction","complied with law","covered by plea to charge (ny)","dead docket",
    "declined/declined prosecution","dismissed","dismissed with conditions***","dismissed with/without prejudice","dismissed without leave","dropped","first offender act (ga)","judgement set aside (az)","no accusation drawn (ga)","no action (fl)",
    "no bill","no information (fl)","no probable cause","nol pros/nolle prosse/nolle prosequi","non-suit","not criminally responsible","not filed","not guilty","not presented to grand jury","off-docket","plea in bar","prosecution barred","purged",
    "quashed","refused","rejected","remanded to file/passed to file (ms)","set aside (ne)","stricken with leave / stricken off leave (il)","warning (ga)","withdrawn"]
    
    #count == 45
    alt_dispos = ["accelerated misdemeanor program","accelerated rehabilitation disposition (pa)","adjudication withheld","agreed order","article 893 and article 894 (la) Ω","awaiting sentencing","bail/bond forfeiture","chance program",
    "conditional discharge","conditional plea","conditional settlement (ca)","continued for dismissal ","deferred adjudication","deferred dismissed","deferred disposition","deferred guilty","deferred judgment","deferred probation",
    "deferred prosecution","disposition continuance","district attorney probation (la)","diversion granted","drug court","intervention in lieu of conviction","judgment deferred - no conviction","judgment on forfeiture (il)",
    "judgment withheld","non adjudication of guilty - agreed plea","non adjudication of guilty - open plea","passed (tn)","plea in abeyance Ω","prayer for judgment (nc)","prepaid","pre-trial intervention","probation","prosecution diversion",
    "retired","stay of adjudication","stet docket","stipulated order of continuance","supervision","suspended imposition of sentencing","un-adjudicated probation","under advisement","withhold judgment"]
    
    
    
    scope = int(input("Enter the scope if its not 7 years or press enter to skip:") or "7")
    
    
    def match_dispo(dispo):
        if dispo in convictions:
            print("Your Disposition is a CONVICTION, calculate scope from the conviction date")
            useconvodate = [True,"conviction date"]
            return useconvodate
        elif dispo in abs_non_convs:
            print("Disposition is an ABSOLUTE NON-CONVICION n \n  DO NOT REPORT UNLESS STATE OR CLIENT RULES SAY TO")
            abs_non_conv = [True, "absolute non-conviction"] 
            return abs_non_conv
        elif dispo in alt_dispos:
            print("Disposition is an ALTERNATE DISPOSITION,\n   Use the FILE DATE to calculate scope  \n Be sure to check the state/CL guidelines to see if you can report it though, ")
            filedate = input("File_date:")
            usefiledate = [True, "file date"]
            return usefiledate
    
    #//TODO: find a way to get the file date into a format datetime can do subtraction  with
    
    def cal_scope_with_dispo_7year(calculation_date,scope):
        if calculation_date[1] != "absolute non-conviction":
            today = date.today()
                    # input(f"Enter {calculation_date[1]} in YYYY-MM-DD format:")
                    # year,month, day = map(int, date.split('-'))
            inpdate = input(f"Enter {calculation_date[1]} in MM-DD-YYYY format:")
            month, day, year = map(int, inpdate.split('-'))
            CalcDate = datetime.date(year, month, day)
            if today - datetime.timedelta(days= scope *365) <=  CalcDate:
                console.print(Panel.fit(f"Case is within a {scope} year scope, please report it.",style="bold red"))
            else:
                console.print(Panel.fit("Case is out of scope. Report it with the norepo format: \nNot reporting OOS case CASENUMBER (charge_description,level,disposition,year) according to AB GLs.",style="bold red" ))
    
    
    
    calculation_date = match_dispo(dispo) 
    cal_scope_with_dispo_7year(calculation_date,scope)
