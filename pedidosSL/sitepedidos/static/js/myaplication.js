
function funcao_valor_total___() {
    var num1 = document.querySelector(".valorItem").value;
    var num2 = document.querySelector(".quantidadeItens").value;
    //var num1 = 2.98;

    //var num3 = document.getElementById(num1).value.replace('.', ',');
    //var num1 = parseFloat(num3) *100;


    //document.write(num1);
    //document.write(Number.parseFloat(num1));

    var vl_total_itens = num1 * num2;

    //document.write(Number.isNaN(vl_total_itens));
        //-- COM R$
    //var vl_total_itens = vl_total_itens.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' });

        //-- SEM R$
    var vl_total_itens = vl_total_itens.toLocaleString('pt-br', {minimumFractionDigits: 2});

    //document.querySelector(".resultado").innerHTML = vl_total_itens;

    campoTotal.value = vl_total_itens;
    campoTotal2.value = vl_total_itens;

}

function funcao_valor_total() {
    var varTotal = (document.getElementById("campoValorUnitario").value *
                    document.getElementById("campoQuantidade").value)

    document.getElementById("campoTotal").value = varTotal

    document.getElementById("campoTotal2").value =
               document.getElementById("campoTotal").value

}

function validaEmail() {
    if (!document.CadUsuarioForm.email.value.includes("@")){
        alert("E-mail invalido!");

    }
}

function avisoFazerLogin() {
     alert("Para comprar, Faça o LOGIN ou cadastre-se!");
}

function avisoSemItemNoCarrinho() {
    alert("Atenção! Nao há item no carrinho!");

}

function avisoSemEnderecoEntrega(){
    alert("Atenção! Cadastre um endereço de entrega!");
}

function botaoMaisUm(){
    var _varTotal =0
    var maisUm = document.getElementById("campoQuantidade").value
    var maisUm =  parseFloat(maisUm) + 1
    document.getElementById("campoQuantidade").value = maisUm

    var _varTotal = (document.getElementById("campoValorUnitario").value *
                    document.getElementById("campoQuantidade").value)



    //var _varTotal = document.getElementById("campoValorUnitario").value
    //alert(_varTotal)


    document.getElementById("campoTotal").value = _varTotal

    document.getElementById("campoTotal2").value = _varTotal


}

function botaoMenosUm(){
    var menosUm = document.getElementById("campoQuantidade").value;
    var menosUm =  menosUm - 1;
    document.getElementById("campoQuantidade").value = menosUm;

    var varTotal = (document.getElementById("campoValorUnitario").value *
                    document.getElementById("campoQuantidade").value);

    if (menosUm < 1) {
        var menosUm = 1;
        var varTotal = document.getElementById("campoValorUnitario").value;
        document.getElementById("campoTotal").value = varTotal;
       // document.getElementById("campoTotal2").value = varTotal;
        document.getElementById("campoQuantidade").value = menosUm;
        alert("Quantidade não pode ser ZERO!");

    } else {
        document.getElementById("campoTotal").value = varTotal

        document.getElementById("campoTotal2").value = varTotal

    }

}

function alteraVirgula(){
    document.getElementById("latitudeEnt").value = 
            document.getElementById("latitudeEnt").value.replace(",", ".")
    document.getElementById("longitudeEnt").value = 
            document.getElementById("longitudeEnt").value.replace(",", ".")
  
}









