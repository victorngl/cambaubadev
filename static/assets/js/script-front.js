import Dom from './modules/constructors.js'; //selecionar elementos

const pageHome = new Dom().el(".page_home")
const pageComunicadoSingle = new Dom().el("#page_comunicado-single")

function escopo() {

    if (pageHome) { // ★ HOME  
        new Dom().bodyClass("body__home")

    } else if (pageComunicadoSingle) {// ★ Single COMUNICADO  
        new Dom().bodyClass("body__comunicado__single")
    }
}

escopo()