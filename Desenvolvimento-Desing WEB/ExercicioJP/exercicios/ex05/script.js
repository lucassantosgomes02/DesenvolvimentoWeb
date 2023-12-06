function exercicio5() {
    const distancia = Number(document.querySelector("#distancia").value)
    const volume = Number(document.querySelector("#volume").value)

    let consumoMedio = distancia/volume

    window.alert(`O consumo médio foi de ${consumoMedio} Km/L`)
}