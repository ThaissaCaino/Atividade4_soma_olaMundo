// Adicionando a mensagem "Olá Mundo"
document.addEventListener("DOMContentLoaded", function() {
    // Encontrar o último elemento h2
    let todosH2 = document.querySelectorAll("h2");
    let ultimoH2 = todosH2[todosH2.length - 1];

    // Criar a mensagem "Olá Mundo"
    let mensagem = "Olá Mundo";
    let mensagemElement = document.createElement("p");
    mensagemElement.textContent = mensagem;

    // Inserir a mensagem após o último h2
    if (ultimoH2) {
        ultimoH2.parentNode.insertBefore(mensagemElement, ultimoH2.nextSibling);
    }
});