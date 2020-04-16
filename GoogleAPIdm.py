#-------------------------------------------------------------------------------
# Name:        GoogleAPIdm
# Purpose:     Automatically accesses Google Premium Streets API and performs
#              distance matrix requests at user-specified origins and
#              destinations.
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
import requests, json
import time

#change your api_key
api_key = ''
x = []
oid,origin,did,dest,time,dist = [],[],[],[],[],[]
counter = 0
# change the range
for n in range(473,543):
    Source = str(Ori.loc[n,'geometry'].y) + ',' + str(Ori.loc[n,'geometry'].x)

    for m in range(139,209):
        if counter>38500:
            break
        Dest = str(Des.loc[m,'geometry'].y) + ',' + str(Des.loc[m,'geometry'].x)
        url ='https://maps.googleapis.com/maps/api/distancematrix/json?'
        url2 = url +'&origins=' + Source + '&destinations=' + Dest + '&key=' + api_key
        r = requests.get(url2)
        #x.append(r.json())
        t = r.json()
        a = float(t['rows'][0]['elements'][0]['duration']['text'].split(' ')[0])
        print a,n,m
        oid.append(n)
        did.append(m)
        origin.append(Source)
        dest.append(Dest)
        time.append(a)
        dist.append(float(t['rows'][0]['elements'][0]['distance']['text'].split(' ')[0]))
        counter+=1


df = pd.DataFrame([oid,origin,did,dest,time,dist]).T
df.columns=["OriginID","OriginCoords","DestinationID","DestinationCoords","TimeInMin","DistInKm"]
df.to_csv("ODMatrixTime.csv")
