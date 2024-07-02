#create

##car={"name":"ford",
##     "model":"mustang",
##     "year":2020,
##     "year":2024,
##     "active":True
##     }
##print(type(car))
#access by key name

##print(car)

##my_car=dict(name="bmw",model="b20",color="black")
##
##print(type(my_car))


#access the dict

##car={"name":"ford",
##     "model":"mustang",
##     "year":2024,
##     "active":True
##     }
##print(car["model"])
##print(car.get("name"))
##
##print(car.keys())
##print(car.values())
##
##car["year"]=2025
##
##print(car)
##
##car["color"]="black"
##print(car)


##print(car.items())
##
##if "hjags" in car:
##    print("yes")


##car.update({"color":"brown"})
##print(car)

##car.pop("active")
##print(car)

car={"name":"ford",
     "model":"mustang",
     "year":2024,
     "active":True
     }
for i,j in car.items():
    print(i,j)







