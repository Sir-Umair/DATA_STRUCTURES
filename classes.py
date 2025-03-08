class person :
    name="UMAIR"
    status="STUDENT"
    def info(self):
        print(f"{self.name}is a {self.status}")
a=person() 
b=person()
a.name="ali"
a.status="BUISNESS"
b.name="ABRAR"
b.status="ceo"
a.info() 
b.info()