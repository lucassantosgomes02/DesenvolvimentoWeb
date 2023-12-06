function calculaSalario() {
    let salario = Number(document.querySelector("#salario").value)
    let porcentagemAumento = Number(document.querySelector("#porcentagemAumento").value)

    document.querySelector("#nSalario").innerHTML = `O novo salário do funcionário é: R$${salario + salario*porcentagemAumento/100}`
}