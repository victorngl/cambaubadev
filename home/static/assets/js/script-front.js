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
//escopo
const pageHome = new Dom().el(".page_home")
const pageComunicadoSingle = new Dom().el("#page_comunicado-single")
const HomeAluno = new Dom().el(".page_aluno");

function escopo() {

    if (pageHome) { // ★ HOME  
        new Dom().bodyClass("body__home")
        if (HomeAluno) {
            new Dom().bodyClass("body__aluno")

        }

    } else if (pageComunicadoSingle) { // ★ Single COMUNICADO  
        new Dom().bodyClass("body__comunicado__single")
    }
}

escopo()