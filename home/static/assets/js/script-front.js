function Dom(seletor) {
    //retorna lista de Elementos
    const items = document.querySelectorAll(seletor);
    this.elements = items;

    //retorna elemento
    this.el = function (seletor) {
        return document.querySelector(seletor)
    };

    //add classe no elemento
    this.add = function (classe) {
        this.el().classList.add(classe)
    };

    this.has = function (classe) {
        return this.el().classList.contains(classe)
    };
    //add classe no body
    this.bodyClass = function (classe) {
        document.body.classList.add(classe)
    };

    //classe toggle  body
    this.bodyToggle = function (classe) {
        document.body.classList.toggle(classe)
    };
    this.bodyRemove = function (classe) {
        document.body.classList.remove(classe)
    };

    //add class NodeList
    this.addClassAll = function (classe) {
        items.forEach((i) => {
            i.classList.add(classe)
        })
    };

    //class toggle item
    this.toggle = function (classe) {
        this.el().classList.toggle(classe)
    };

    //remove class item
    this.remove = function (classe) {
        this.el().classList.remove(classe)
    };


    // this.event = function (evento, funcao) {
    //     this.element().addEventListener(evento, funcao)
    // }

}


function calendarioFechado() {
    const media = window.matchMedia('(min-width: 992px)').matches
    const botaoShowCalendar = document.querySelector(".show__calendar")
    const calendar = document.querySelector(".calendar")
    calendar.classList.add("fechado")

    botaoShowCalendar.addEventListener("click", function () {
        calendar.classList.toggle("fechado")
    })
}

//escopo
const pageHome = new Dom().el(".page_home")
const HomeAluno = new Dom().el(".page_aluno");
const pageTurma = new Dom().el(".page_turma-single");
const pageAtividadesSingle = new Dom().el(".single__atividades");


const pageComunicadoSingle = new Dom().el("#page_comunicado-single")

function escopo() {

    if (pageHome) { // ★ HOME  
        new Dom().bodyClass("body__home")
        calendarioFechado()

        if (HomeAluno)
            new Dom().bodyClass("body__aluno")


    } else if (pageComunicadoSingle) { // ★ Single COMUNICADO  
        new Dom().bodyClass("body__comunicado__single")
    } else if (pageTurma) { // ★ Page turma  
        new Dom().bodyClass("body__turma-single")
        calendarioFechado()
    } else if (pageAtividadesSingle) {
        new Dom().bodyClass("body__atividades-single")

    }
}

escopo()