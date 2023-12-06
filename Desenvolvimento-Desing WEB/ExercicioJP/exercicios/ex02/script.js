let exe2 = () => {
    let base = Number(document.querySelector("#base").value)
    let altura = Number(document.querySelector("#altura").value)

    document.querySelector("#resultado").value = `Área = ${base * altura / 2} cm²`
}