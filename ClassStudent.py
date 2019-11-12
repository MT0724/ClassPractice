class Student(object):
	def __init__(self,name,score):
		self.__name=name
		self.__score=score
	def show(self):
		print(self.__name)
		print(self.__score)
def main():
	a=Student('Jane',100)
	#print(a.__name)  
	#当类Student的成员变量变成私有的，即__name,__score,此处不能访问，必须通过show()函数
	a.show()

main()
