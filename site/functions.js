function onloadFunc(){
    console.log("Usuário: meuUsuario\nSenha: 123");
    let path = window.location.pathname;
    let page = path.split("/").pop();
    if (page == "autorizado.html"){
        const frame = document.getElementById('frame_id');
        const file = document.getElementById('file_id');
        const reader = new FileReader();

        reader.addEventListener("load", function () {
            frame.style.backgroundImage = `url(${ reader.result })`;
            }, false);

        file.addEventListener('change',function() {
            const image = this.files[0];
            if(image) reader.readAsDataURL(image);
            }, false)
    }
}

function login(){ //isso é apenas um exemplo, nunca realize este tipo de verificações desta forma.
    if ((document.getElementById("login_id").value == "meuUsuario") && (document.getElementById("senha_id").value == "123")){
        console.log("logado");
        location = ("./autorizado.html");
    } else{
        alert("Login ou senha incorretos!");
    }
}

function logout(){
    location = ("./index.html");
}