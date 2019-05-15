from copy import deepcopy

f = open("input0.txt", "r")

x = f.readline()

Airport_info=x.split();

Landing_positions=int(Airport_info[0])
No_of_Gates=int(Airport_info[1])
TakeOff_positions=int(Airport_info[2])

# print (Landing_positions)
# print (No_of_Gates)
# print (TakeOff_positions)

No_Of_planes= int(f.readline())



class Planes:


    def __init__(self, R, M,S, O,C):
        self.Time_In_Air = R
        self.Time_To_Reach_Gate = M
        self.Time_to_Unload=S
        self.Time_To_TakeOff=O
        self.Max_WaCiting_Time=C
        self.domain_Land_time = []
        self.domain_Takeoff_time = {}
        self.LandTime=0
        self.TakeOfftime=0
        self.dict1={}
        self.dict2={}
        self.dict3={}

Plane_List=[]

for i in range(No_Of_planes):
    a=f.readline()
    plane_information = a.split()

    Plane_List.append(Planes(int(plane_information[0]), int(plane_information[1]), int(plane_information[2]), int(plane_information[3]),int(plane_information[4])))

f.close()



for i in range(len(Plane_List)):

    for j in range(Plane_List[i].Time_In_Air+1):
        list=[]
        Plane_List[i].domain_Land_time.append(j)
        for k in range(j+Plane_List[i].Time_To_Reach_Gate+Plane_List[i].Time_to_Unload,j+Plane_List[i].Time_To_Reach_Gate+Plane_List[i].Max_WaCiting_Time+1):
            list.append(k)
            Plane_List[i].domain_Takeoff_time[j] = list



Landingpositions = [[] for _ in range(Landing_positions)]


Gates=[[] for _ in range(No_of_Gates)]


Takoffposition=[[] for _ in range(TakeOff_positions)]



def FindSolution(Plane_List,Landing_positions,No_of_Gates,Takoffposition,orderlist):
    m=0
    Flag1=True
    Flag2=True
    Flag3=True
    check=True
    if not Plane_List:
        return True
    a=Plane_List[0]
    for i in range(m,len(a.domain_Land_time)):

        Flag1=True
        check=True
        min=100000000
        d = m
        for j in range(len(Landing_positions)):

            if not Landing_positions[j]:
                check=False
                thisdict = {
                    "key": d,
                    "value":d+ a.Time_To_Reach_Gate,
                }
                Landing_positions[j].append((thisdict))
                alpha=j
                break

        for j in range(len(Landing_positions)):
            minhtester1=-1000
            Flag1=True
            d=m

            if check == False:
                break
            for p in Landing_positions[j]:

                if p["key"]>=m and p["value"]<=m+a.Time_To_Reach_Gate:
                    Flag1=False



                    d=abs(p["value"])
                    # if m>(len(a.domain_Land_time)):
                    #     return False

                elif p["key"]<=m  and p["value"]>=m+a.Time_To_Reach_Gate:
                    Flag1=False



                    d = abs( p["value"])




                elif (p["key"]<m) and (m<p["value"]):
                    Flag1=False



                    d = abs(p["value"])


                elif (p["key"]<m+a.Time_To_Reach_Gate) and (m+a.Time_To_Reach_Gate<p["value"]):
                    Flag1=False




                    d = abs( p["value"])
                # if Flag1==True:
                #     d=abs( p["value"])
                if d>minhtester1:
                    minhtester1=d




            if minhtester1<min:
                min=minhtester1
                alpha=j


            if min==0:

                Flag1==True
            if Flag1==True:
                break

        if Flag1==False:
            m=min
            if m>(len(a.domain_Land_time)):
                return False
            continue
        if Flag1==True:
            if check==True:

                thisdict = {
                        "key": min,
                        "value": min + a.Time_To_Reach_Gate,
                    }
                Landing_positions[alpha].append((thisdict))



        if Flag1==True:
            Plane_List[0].dict1 = thisdict

        #Gates

        b=a.domain_Takeoff_time[m][0]
        for q in range(b, a.domain_Takeoff_time[m][len(a.domain_Takeoff_time[m])-1]+1):
            min2 = 100000000
            check2=True
            Flag2=True
            for s in range(len(No_of_Gates)):
                if not No_of_Gates[s]:
                    check2 = False
                    thisdict2 = {
                        "key": m + a.Time_To_Reach_Gate,
                        "value":b,
                    }
                    No_of_Gates[s].append((thisdict2))
                    alpha1=s
                    break
            for s in range(len(No_of_Gates)):
                d=0

                minhtester = -10000
                if check2 == False:
                    break
                for z in No_of_Gates[s]:
                    if z["key"] >= m + a.Time_To_Reach_Gate and z["value"] <=b:
                        Flag2 = False
                        d = abs(z["value"]-(m + a.Time_To_Reach_Gate))
                        # if m>(len(a.domain_Land_time)):
                        #     return False

                    elif z["key"] <= m + a.Time_To_Reach_Gate and z["value"] >= b:
                        Flag2 = False

                        d = abs(z["value"] - (m + a.Time_To_Reach_Gate))




                    elif (z["key"] < m + a.Time_To_Reach_Gate) and (m + a.Time_To_Reach_Gate < z["value"]):
                        Flag2 = False

                        d = abs(z["value"] - (m + a.Time_To_Reach_Gate))



                    elif (z["key"] <b) and (b < z["value"]):
                        Flag2 = False

                        d = abs(z["value"] - (m + a.Time_To_Reach_Gate))


                    if d>minhtester:
                        minhtester=d
                if Flag2==True:
                    if minhtester < min2:
                        min2 = minhtester
                        alpha1 = s
                    break

                if minhtester < min2:
                    min2 = minhtester
                    alpha1 = s


            if min2==0:
                Flag2=True


            if Flag2==False:
                m=min2+m
                if m > (len(a.domain_Land_time)):
                    return False
                break



            if Flag2==True:
                if check2 == True:
                    thisdict2 = {
                        "key": min2 + m + a.Time_To_Reach_Gate,
                        "value": b,
                    }
                    No_of_Gates[alpha1].append((thisdict2))
                min3=100000
                check3=True
                Flag3=True
                for t in range(len(Takoffposition)):
                    if not Takoffposition[t]:
                        check3 = False
                        thisdict3 = {
                            "key": b,
                            "value": b + a.Time_To_TakeOff,
                        }
                        Takoffposition[t].append((thisdict3))
                        alpha2=t
                        break
                for t in range(len(Takoffposition)):
                    d = 0
                    Flag3=True
                    minhtester3 = -10000
                    if check3 == False:
                        break
                    for u in Takoffposition[t]:
                        if u["key"] >= b and u["value"] <= b + a.Time_To_TakeOff:
                            Flag3 = False
                            d = abs(u["value"] - (b ))
                            # if m>(len(a.domain_Land_time)):
                            #     return False


                        elif u["key"] <= b and u["value"] >= b + a.Time_To_TakeOff:
                            Flag3 = False

                            d = abs(u["value"] - (b ))




                        elif (u["key"] < b) and (b < u["value"]):
                            Flag3 = False

                            d = abs(u["value"] - (b ))



                        elif (u["key"] < b + a.Time_To_TakeOff) and (b + a.Time_To_TakeOff < u["value"]):
                            Flag3 = False

                            d = abs(u["value"] - (b ))

                        if d > minhtester3:
                            minhtester3 = d
                    if Flag3 == True:
                        if minhtester3 < min3:
                            min3 = minhtester3
                            alpha2 = t
                        break
                    if minhtester3 < min3:
                        min3 = minhtester3
                        alpha2=t
                if min3 == 0:
                    Flag3 = True
                if Flag3==True:
                    if check3==True:
                        if min3 == 0:
                            Flag3 = True
                            thisdict3 = {
                                "key": thisdict2["value"],
                                "value": thisdict2["value"] + a.Time_To_TakeOff,

                            }
                            Takoffposition[alpha2].append((thisdict3))
                    break
                if Flag3 == False:
                    b = min3 + b
                    No_of_Gates[alpha1].pop()
                    Flag2=False

                    if b > (a.domain_Takeoff_time[m][len(a.domain_Takeoff_time[m]) - 1]+1):
                        Flag2 = False
                        m=b -(a.domain_Takeoff_time[m][len(a.domain_Takeoff_time[m]) - 1])
                        break
                    continue

                if Flag3==True:
                    break
        if b > (a.domain_Takeoff_time[m][len(a.domain_Takeoff_time[m]) - 1]+1):
            Flag2 = False

        if Flag2==False:
            Landing_positions[alpha].pop()
            continue





        if Flag2 == True:
            Plane_List[0].dict2 = thisdict2
        if Flag3==True:
            Plane_List[0].dict3=thisdict3


        orderlist.append(Plane_List[0])
        yeds=Plane_List[0]
        Plane_List.pop(0)
        iloo=FindSolution(Plane_List,Landing_positions,No_of_Gates,Takoffposition,orderlist)
        if iloo ==True:
            return iloo
        Landing_positions[alpha].pop()
        No_of_Gates[alpha1].pop()
        Takoffposition[alpha2].pop()
        orderlist.pop()
        Plane_List.insert(0,yeds)
        m=m+1
        if m>=len(Plane_List[0].domain_Land_time):
            return False
        print (len(orderlist))












ord=[]
FindSolution(Plane_List,Landingpositions,Gates,Takoffposition,ord)
print (Landing_positions)
for i in ord:
    print i.dict1
    print i.dict2
    print i.dict3
f = open("output.txt", "w")
for i in range(No_Of_planes):
    f.write("%d %d \n" % (ord[i].dict1["key"], ord[i].dict2["value"]))

