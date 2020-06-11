import requests as req
import time
import multiprocessing 


def download():
    link = "https://erp.psit.in/assets/img/Simages/"
    for i in range(26900,27000): 
        
        r2 = req.get(link+str(i)+".jpg")
        if r2.status_code == 200:
            with open ("images/"+str(i)+".jpg",'wb')as f:
                f.write(r2.content)
        else:
            print("Link not found")
        
if __name__=="__main__":
    start = time.process_time()
    process = multiprocessing.Process(target=download)
    process1 = multiprocessing.Process(target=download)
    process2 = multiprocessing.Process(target=download)
    process3 = multiprocessing.Process(target=download)
    process4 = multiprocessing.Process(target=download)
    process5 = multiprocessing.Process(target=download)
    process6 = multiprocessing.Process(target=download)
    process7 = multiprocessing.Process(target=download)
    process8 = multiprocessing.Process(target=download)
    processq = multiprocessing.Process(target=download)
    processw = multiprocessing.Process(target=download)
    processe = multiprocessing.Process(target=download)
    processr = multiprocessing.Process(target=download)
    processt = multiprocessing.Process(target=download)
    processy = multiprocessing.Process(target=download)
    processu = multiprocessing.Process(target=download)
    
    process.start()
    process1.start()
    process2.start()
    process3.start()
    process4.start()
    process5.start()
    process6.start()
    process7.start()
    process8.start()
    processq.start()
    processw.start()
    processe.start()
    processr.start()
    processt.start()
    processy.start()
    processu.start()
    
    
    
    process.join()
    process1.join()
    process2.join()
    process3.join()
    process4.join()
    process5.join()
    process6.join()
    process7.join()
    process8.join()
    processq.join()
    processw.join()
    processe.join()
    processr.join()
    processt.join()
    processy.join()
    processu.join()
    
    print(time.process_time() - start)