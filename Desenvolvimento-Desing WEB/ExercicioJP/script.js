function carrega(exercicio){
    const iframe = document.getElementsByTagName('iframe')[0]

    iframe.src=`./exercicios/${exercicio}/index.html`
   
}


