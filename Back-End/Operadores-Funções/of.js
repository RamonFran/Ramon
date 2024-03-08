let nota1 = 10;
let nota2 = 8 ;

//function
function media(n1, n2) {
    return(n1+n2)/2;
}

//ArrowFunction
let mediaArrow = (n1, n2) => (n1+n2)/2;

console.log("A média é " + mediaArrow(nota1, nota2));

//IMC
//---altura = 1.50
//---peso = 65

let imc = (a, p) => p/(a*a);

console.log("O IMC é " + imc(1.75, 70));