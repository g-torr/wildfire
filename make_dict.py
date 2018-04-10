import pickle
def load_dict(name):
        with open('dict-' + name + '.pkl', 'rb') as f:
                return pickle.load(f)
def save_dict(obj, name ):
    with open('dict-'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f,protocol=2)
dic={}
titles=["District_code","District_name","Country","Parish","private_shrub_burnt","public_shrub_burnt","tot_shrub_burnt","private_forest_burnt","public_forest_burnt","tot_forest_burnt","tot_burnt","agricultural_burnt","type","cause","ignition_date","ignition_time", "ignition_hour","ignition_min","extinction_date","extinction_time","extinction_hour","extinction_min","duration","flag1","flag2","flag3","flag4","time_intervation","day_of_the_week"]

with open('./PortugalWildfireData/PRFD_1980_2005_17Nov11.txt', 'r') as f:
    for line in f:
        a=line.strip("\n").split("\t")
        for i in arange(0,len(titles)):
            dic.setdefault(titles[i], []).append(a[i]) #this dictionary contains a list, now I want a dictionary of arrays
fire={}
types=[int,np.unicode,np.unicode,np.unicode,float,float,float,float,float,float,float,float,int,int,int,float,int,int,int,float,int,int,float,int,int,int,int,unicode,int]
for i in arange(0,len(titles)):
    fire[titles[i]]=np.array(dic[titles[i]],dtype=types[i])
save_dict(fire,"fire")
