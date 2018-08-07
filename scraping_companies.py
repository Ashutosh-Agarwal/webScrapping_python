from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'http://www.iato.in/members/lists'

#opening connection and grabing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#html parsing
page_soup = soup(page_html,"html.parser")

#grabs each line
containers = page_soup.tbody.findAll("tr")

#Creating CSV file and write data into it.
filename = "companies.csv"
f = open(filename, 'w')

headers = "Company_Name, Contact_Name, Designation, Street_Address, City, State, Pincode, Email, Phone, Mobile,Website,Employee_Size\n"
f.write(headers)

for container in containers:
    table_row = container.findAll("td")
    hyperlink = table_row[1].a["href"]

    #opening connection and grabing the page of each company
    uClient = uReq(hyperlink)
    page_html = uClient.read()
    uClient.close()

    #html parsing
    page_soup = soup(page_html,"html.parser")

    #grabs each line
    sub_containers = page_soup.findAll("div",{"class":"post-content"})
    
    length = len(sub_containers)
    for i in range(length):
        CD = False
        if(sub_containers[i].h6.text == "Contact Details:"):
            CD = True
            break
            
    if(CD == True):   
        info = sub_containers[i].findAll("p")

        str = ""
        for j in range(0,12,1):
            if (j <10):
                str+=info[j].text.split(':')[1].strip().replace(","," ")+","
            elif(j==11):
                str+=info[j].text.split(':')[1].strip().replace(",","")+"\n"
        print(str)
        f.write(str)
    else:
        str = ""
        for j in range(0,12,1):
            add = table_row[2].text.split('-')
            if (j ==0):
                str+=container.a.text+","
            elif(j==4):
                if(len(add)>0):
                    str+=add[0]+','
            elif(j==5 ):
                if(len(add)>1):
                    str+=add[1]+','
            elif(j==6 ):
                if(len(add)>2):
                    str+=add[2]+','
            else:
                str+=","
        print(str+"\n")
        f.write(str+"\n")

f.close()
    
