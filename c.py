import requests as req


def download():
    link = "https://erp.psit.in/assets/img/Simages/"
    for i in range(26991,27000): 
        r2 = req.get(link+str(i)+".jpg")
        if r2.status_code == 200:
            with open ("links.txt","a+")as f:
                f.write(link+str(i)+".jpg\n")
        else:
            print("Link not found")
    f.close()
download()
#"images/"+str(i)+".jpg"