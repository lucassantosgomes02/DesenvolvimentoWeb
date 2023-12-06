const exercicio6 = () => {
    let horasTrabalhadas = Number(document.querySelector("#horasTrabalhadas").value)
    let valorHora = Number(document.querySelector("#valorHora").value)
    let qtdRefeicoes = Number(document.querySelector("#qtdRefeicoes").value)
    const valorRefeicao = 1.5
    let salario = 0

    if (horasTrabalhadas > 40) {
        salario = (horasTrabalhadas - 40)*3*valorHora + horasTrabalhadas * valorHora
    }
    else {
        salario = horasTrabalhadas * valorHora
    }

    resposta6 = `O valor do salário bruto é de R$${salario}.\nO valor descontado pelo total de refeições é de: R$${qtdRefeicoes * valorRefeicao}\nO salário líquido é de R$${salario - qtdRefeicoes * valorRefeicao}`

    document.querySelector("#resposta6").innerHTML = resposta
}