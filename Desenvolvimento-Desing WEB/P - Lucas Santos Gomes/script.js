elemento = document.getElementById("pesquisa");
let apikey="a8cf19d5139d6937352807eaf441360d";

x= document.getElementById("pesquisa")
x.addEventListener('click', async function()
{
    cidade = document.getElementById("cidade").value;
    const apiClimaURL = `https://api.openweathermap.org/data/2.5/weather?q=${cidade}&units=metric&appid=${apikey}&lang=pt_br`;
    let respostaClima = await fetch(apiClimaURL)
    document.getElementById('resultado')
})

elemento.addEventListener('click', async function () {
    document.getElementById('resultado').innerText = ""
    var valor = document.getElementById("cep").value
    if (valor == '')
        alert("Informe o CEP");
    else {
        var cep = valor.replace(/\D/g, '');
        var validacep = /^[0-9]{8}$/;

        if (validacep.test(cep)) {
            var api = `https://viacep.com.br/ws/${cep}/json/`;
            let resposta = await fetch(api);
            dados = await resposta.json();
            console.log(dados);
            if (dados.erro)
            document.getElementById('resultado').innerText = "CEP Não Existe";
         else
         {

             document.getElementById('cidade').value =  dados.localidade}
         }
        else
            if (!(resposta.ok))
                alert("cep inválido");
    }
}
)


