function calcularDesconto()
{
    //window.alert("Calculando...");
    let qtdPacotes = document.querySelectorAll("input[name='pacotes']").length;
    console.log(qtdPacotes);
    
    let pacotes = document.querySelectorAll("input[name='pacotes']");
    console.log(pacotes);

    // i< pacote.length
    for (var i=0; i< qtdPacotes; i++)
    {
        console.log(pacotes[i].value);
    }
}