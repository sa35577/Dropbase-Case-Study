import plotly.express as px
import csv
with open('Revenues.csv', mode = 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    firstTime = True
    headers = []
    lst = []
    lst1 = []
    cnt = 0
    for row in csv_reader:
        print(row)
        print()
        for i in row:
            if firstTime:
                try:
                    headers.append(int(i))
                except:
                    pass
            print(f'\'{i}\',')
        
        if firstTime:
            headers = headers[1:]
            firstTime = False
            print(headers)
        for head in headers:
            #print(row[head])
            lst1.append(int(row[str(head)]))
            
        lst.append(lst1)
        lst1 = []
        cnt += 1
    
    
        

fig = px.scatter(x=headers, y = lst[0], trendline = "ols") #trendline = "ols" is LOBF, uses linear regression

#fig.update_xaxes(type='category')
fig.show()
