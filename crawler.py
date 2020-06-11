import requests as req
import time
import multiprocessing as mp

def download(s,e):
    link = "https://erp.psit.in/assets/img/Simages/"
    for i in range(s,e): 
        r2 = req.get(link+str(i)+".jpg")
        if r2.status_code == 200:
            with open ("images/"+str(i)+".jpg",'wb')as f:
                f.write(r2.content)
        else:
            print("Link not found")


if __name__=="__main__":
    start = time.process_time()
    cores = 8
    pool = mp.Pool(cores)
    tasks = []
    l=26900
    u=27000
    for i in range(u,l,cores):
        tasks.append([i,i+cores-1])
    for task in tasks:
        s,e = task[0],task[1]
        pool.apply_async(download, args = (s,e))
        
    pool.close()
    pool.join()
    print(time.process_time() - start)
