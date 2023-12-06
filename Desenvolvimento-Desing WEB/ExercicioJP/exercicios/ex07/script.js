function exe7() {
    rand = Math.floor(Math.random() * 100) + 1

    document.querySelector("#nRand").innerHTML = rand

    rand % 2 == 0 ? document.querySelector("#parImpar").innerHTML = "O número é par" : document.querySelector("#parImpar").innerHTML = "O número é impar"
    
    console.log(rand)
}