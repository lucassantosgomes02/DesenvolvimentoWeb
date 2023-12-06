function exe3() {
    let nota1 = Number(document.querySelector("#nota1").value)
    let nota2 = Number(document.querySelector("#nota2").value)

    document.querySelector("#resultado").innerHTML = `O calculo da média ponderada é de ${nota1 * 0.3 + nota2 * 0.7} pontos`
}