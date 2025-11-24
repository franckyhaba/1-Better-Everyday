jobOpenings = { 
        
        "shop keeper": 50 ,
        "Delivery Driver": 90,
        "Accountant": 5,
        "Law": 2,
        "taxi man": 100 
}
print (jobOpenings)
del jobOpenings ["taxi man"]
print (jobOpenings)

jobOpenings['taxi man '] = '200' 
print (jobOpenings) 

# if job is already stored you can just do this
jobOpenings['taxi man ']=  "500 "
print(jobOpenings)
