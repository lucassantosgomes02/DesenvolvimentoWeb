let exe4 = () => {
    const anoNascimento = document.querySelector("#dataNascimento").value
    const dataAtual = new Date()
    const anoAtual = dataAtual.getFullYear()
    const mesAtual = dataAtual.getMonth()
    const diaAtual = dataAtual.getDay()
    const horaAtual = dataAtual.getHours()
    const minutosAtuais = dataAtual.getMinutes()

    const idadeAnos =  anoAtual - anoNascimento
    const idadeMeses = idadeAnos * 12 + mesAtual
    const idadeDias = Math.floor(idadeAnos * 365.25 + (mesAtual - 2) * 30.5 + 28 + diaAtual)
    const idadeHoras = idadeDias * 24 + horaAtual
    const idadeMinutos = idadeHoras * 60 + minutosAtuais
    const idadeSemanas = Math.floor(idadeDias / 7)
    const idade2050 = 2050 - anoNascimento

    const mensagem = `A idade aproximada é: \n${idadeAnos} anos, ou ${idadeMeses} meses, ou ${idadeSemanas} semanas, \nou ${idadeDias} dias, ou ${idadeHoras} horas, ou ${idadeMinutos} minutos. \nIdade aproximada em 2050: ${idade2050} anos`
    window.alert(`Mensagem exibida no console: \n${mensagem}`)
    console.log (mensagem)
}