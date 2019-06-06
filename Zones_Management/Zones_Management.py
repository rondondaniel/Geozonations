import pandas as pd

Folder="D:/Documents/Zone management/"

def dms2dd( dms ):  
    if dms.endswith("N"):
        deg = float(str(dms)[0:2])  
        min = float(str(dms)[4:6])  
        sec = float(str(dms)[7:9])  
        dd = deg + (min / 60) + (sec / 3600)
    elif dms.endswith("W") or dms.endswith("E"):         
        deg = float(str(dms)[0:3])  
        min = float(str(dms)[5:7])  
        sec = float(str(dms)[8:10])  
        dd = deg + (min / 60) + (sec / 3600)
        if dms.endswith("W"):
            dd=dd*(-1)
    else:
        print "nah!"
        dd=0
    return dd

def readdms(Name):
    Zone=Folder+ZoneName+".csv"
    data=pd.read_csv(Zone)
    return data

def convert(dframe):
    for index, row in dframe.iterrows():        
        Lat=dms2dd(row["Lat"])
        Log=dms2dd(row["Log"])
        row["Lat"]=Lat
        row["Log"]=Log
        print str(row["Log"])+","+str(row["Lat"]) 
    return dframe


if __name__ == "__main__":

    ZoneName=raw_input("Enter file name: ");
    dms=readdms(ZoneName)
    df=pd.DataFrame(dms)
    print df
    df_dd=convert(df)
    #writeKML(df_dd)
    

    
        
