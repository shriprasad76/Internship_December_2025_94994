const s1 = {} 
s1.name = "Anil" 
s1.age = 35 
console.log(`type of(s1) - ${typeof (s1)}`)
console.log(s1)

const s2 = {}
s2.name = "Mukesh"
s2.age = 40
s2.mobile = "9876543210"
console.log(s2)

const s3 = {}
s3["first name"] = "Ramesh"
s3.last_name = "Ambani"
console.log(s3)

const s4 = {}
s4["name"] = "Suresh"
s4["age"] = 45
console.log(s4)

const s5 = {
    "name": "Ram",
    "age": 50,
    "canVote": true,
    skills: ["C", "CPP", "Java"]
}

s5.mobile = "8976543210"
s5["email Id"] = "ram@gmail.com"
s5.canVote = false
console.log(s5)

const s1 = new Object() 
s1.name = "Anil"
s1.age = 35
s1["last name"] = "Ambani"
console.log(`type of(s1) - ${typeof (s1)}`)
console.log(s1)



function Student(name, age) {
    this.name = name
    this.age = age
}

const s1 = new Student()
console.log(typeof (s1))
console.log(s1)

const s2 = new Student("Anil", 35)
console.log(s2)

const s3 = new Student("Mukesh", 30)
s3.mobile = "9876543210"
s3["email id"] = 'mukesh@gmail.com'
console.log(s3)

const arr1 = [] 
console.log(typeof (arr))
console.log(arr)

const arr2 = [10, 20]
console.log(arr2)

const arr3 = new Array()
arr3.push(10)
arr3.push(20)
arr3.push(30)
arr3.push(40)

arr3.pop()
console.log(arr3.length)
console.log(arr3)

const arr = [10, 20, 30, 40, 50, 60]
for (let i = 0; i < arr.length; i++)
    console.log(`element - ${arr[i]}`)

for (const element of arr)
    console.log(`element - ${element}`)

const arr7 = [10, 22.33, 33.44, 40, 50]
console.log(arr7)

const arr5 = ["Anil", "Mukesh", "Ramesh", "Suresh"]
console.log(arr5)

const arr6 = [function (n1, n2) { return n1 + n2 }, function (n1, n2) { return n1 - n2 }]
console.log(arr6)
console.log(arr6[0])
console.log(arr6[0](10, 20))

const arr4 = [{ name: "Anil", age: 30 }, { name: "Mukesh", age: 35 }, { name: "Ramesh", age: 40 }]
arr4[1].mobile = "9876543210"
arr4[1]["email  id"] = "mukesh@gmail.com"
console.log(arr4)

const arr8 = [10, 20, 30, 40, 50, 60]
console.log(arr8)
console.log(arr8[2])
console.log(arr8.at(2))

console.log(arr8[-5])
console.log(arr8.at(-5))

arr1.splice(2, 3)
console.log(arr1)

