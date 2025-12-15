console.log("Hello from External JS")
let n1 = 10
const n2 = 20

n1 = 100 

n1 = true
n1 = "Sunbeam"

console.log('n1 - ' + n1)
console.log('n2 - ' + n2)
 n1;

console.log(`n1 - ${n1}, typeof(n1) - ${typeof (n1)}`)

n1 = 10
console.log(`n1 - ${n1}, typeof(n1) - ${typeof (n1)}`) 
n1 = 10.22
console.log(`n1 - ${n1}, typeof(n1) - ${typeof (n1)}`)

n1 = true
console.log(`n1 - ${n1}, typeof(n1) - ${typeof (n1)}`)

n1 = 'sunbeam'
console.log(`n1 - ${n1}, typeof(n1) - ${typeof (n1)}`)

n1 = null
console.log(`n1 - ${n1}, typeof(n1) - ${typeof (n1)}`)

function f1() {
    console.log('Inside f1()')
}

function f2(n1, n2) {
    console.log('Inside f2()')
    console.log(`n1 - ${n1} , typeof(n1) - ${typeof (n1)}`)
    console.log(`n2 - ${n2} , typeof(n2) - ${typeof (n2)}`)

}

f1()
f2(10, 20)
f2(10, true)
f2(null, 'sunbeam')
f2(false)
f2()

function f1() {
    console.log('Inside f1()')
}

function f1(n1, n2) {
    console.log('Inside f1(n1,n2)')
}

f1(10, 20) 
f1() 

function f1(n1 = 1, n2 = 2, n3 = 3) {
    console.log('Inside f1()')
    console.log(`n1 - ${n1}, n2 - ${n2},  n3 - ${n3}`)
}

f1(10, 20, 30)
f1(10, 20)
f1(10)
f1()
f1(11, 22, 33, 44, 55)

function f1(n1 = 1, n2 = 2, n3 = 3) {
    console.log('Inside f1()')
    console.log(`n1 - ${n1}, n2 - ${n2},  n3 - ${n3}`)
}

f1(10, 20, 30)
f1(10, 20)
f1(10)
f1()
f1(11, 22, 33, 44, 55)

function f1() {
    console.log("f1 returns")
  
    return null
}

const res = f1()
console.log(`result - ${res} , typeof(result) - ${typeof (res)}`)

function add(n1, n2) {
    console.log(`Addition - ${n1 + n2}`)
}

const myadd = add

add(10, 20)
myadd(11, 22)
console.log(`typeof(myadd) - ${typeof (myadd)}`)
console.log(`myadd - ${myadd}`)

const myadd = function (n1, n2) {
    console.log(`Addition - ${n1 + n2}`)
}

myadd(11, 22)
console.log(`typeof(myadd) - ${typeof (myadd)}`)
console.log(`myadd - ${myadd}`)


const myadd = (n1, n2) => {
    console.log(`Addition - ${n1 + n2}`)
}

myadd(11, 22)
console.log(`typeof(myadd) - ${typeof (myadd)}`)
console.log(`myadd - ${myadd}`)

function add(n1, n2) {
    return n1 + n2
}

function sub(n1, n2) {
    return n1 - n2
}

function mul(n1, n2) {
    return n1 * n2
}

function div(n1, n2) {
    return n1 / n2
}

const res1 = add(20, 10)
console.log(`Result - ${res1}`)

const res2 = sub(20, 10)
console.log(`Result - ${res2}`)

const res3 = mul(20, 10)
console.log(`Result - ${res3}`)

const res4 = div(20, 10)
console.log(`Result - ${res4}`)


function arithmeticExecuter(fn) {
    const res1 = fn(20, 10)
    console.log(`Result in Executer - ${res1}`)
}

arithmeticExecuter((n1, n2) => n1 + n2)
arithmeticExecuter((n1, n2) => n1 - n2)
arithmeticExecuter((n1, n2) => n1 * n2)
arithmeticExecuter((n1, n2) => n1 / n2)