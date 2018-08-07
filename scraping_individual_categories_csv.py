from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'http://bharathlisting.com/'

#opening connection and grabing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#html parsing
page_soup = soup(page_html,"html.parser")


#grabs each line
containers = page_soup.findAll('div',{'class':'main-cat-name'}, limit = None)
for i in range(1,60,1):
    Category = containers[i].text.strip()

    #opening new file
    filename = 'bharathlisting/'+Category+'.csv'
    f = open(filename, 'w')

    headers = "Category,Company_Name,Address,Pincode,Phone,Website,Email,Name\n"
    f.write(headers)
    
    hyperlink_cat = containers[i].a["href"]
    hp = hyperlink_cat
    page = 1
    a,b = "",""
    while True:
        #opening connection and grabing the page
        uClient = uReq(hp)
        page_html = uClient.read()
        uClient.close()

        #html parsing
        page_soup = soup(page_html,"html.parser")

        if(page>1):
            a = sub_containers[0]

        #grabs each line
        sub_containers = page_soup.findAll("div",{"class":"item-description"})
        
        if sub_containers != []:
            b = sub_containers[0]
        else:
            break

        if a!=b:
            page+=1

            #main section for data retreival
            add_containers = page_soup.findAll('div',{"class":"item-addr"})
            pin_containers = page_soup.findAll('span',{"class":"pcClass"})
            tel_containers = page_soup.findAll('div',{"class":"item-phone"})

            for item in range(len(sub_containers)):
                data = ""
                Company = sub_containers[item].a.text.replace(',','')
                Company = Company.replace('\u200b','')
                Company = Company.replace('\uff08','')
                Company = Company.replace('\uff09','')
                Address = add_containers[item].strong.text.strip().replace(',',' ')
                Address = Address.replace('\u2003','')
                Address = Address.replace('\u200e','')
                Address = Address.replace('\u060c','')
                Address = Address.replace('\uff0c','')
                Address = Address.replace('\ufeff','')
                Address = Address.replace('\u200b','')
                Pincode = pin_containers[item].text.strip()
                
                if(item<len(tel_containers)):
                    Telephone = tel_containers[item].text.strip().replace('\t\t\t\t\t\t\t\t\t',' ')
                else:
                    Telephone = ''
                hyperlink_item = sub_containers[item].a["href"]

                #opening connection and grabing the page
                uClient = uReq(hyperlink_item)
                page_html = uClient.read()
                uClient.close()

                #html parsing
                page_soup_item = soup(page_html,"html.parser")

                #grabs each line
                Website =""
                web = page_soup_item.findAll('a',{"rel":"nofollow"})
                if(web!=[]):
                    Website = web[0].text.strip()
                
                Email =""
                mail = page_soup_item.findAll('div',{"class":"custom-field custom-field-1"})
                if(mail!=[]):
                    Email = mail[0].a.text.strip()
                
                try:
                    data += Category+','+Company+','+Address+','+Pincode+','+Telephone+','+Website+','+Email+'\n'
                    print(data.encode('utf8'))
                    f.write(data)
                except Exception:
                    Address = ''
                    data2 = Category+','+Company+','+Address+','+Pincode+','+Telephone+','+Website+','+Email+'\n'
                    print(data2.encode('utf8'))
                    f.write(data2)
            
            if (len(sub_containers)==20):
                hp = hyperlink_cat[:-1]+str(page)
        else:
            break
    f.close()
        
                

  
