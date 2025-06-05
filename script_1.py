# 2. Arquivo CSS principal
css_content = """/* Reset e configurações gerais */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Compagnon Medium', Georgia, serif;
}

:root {
    --bege: #FFF7F0;
    --marrom: #61452B;
}

html {
    scroll-behavior: smooth;
}

body {
    line-height: 1.6;
    color: var(--marrom);
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}

/* Header */
.header {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    background: var(--bege);
    z-index: 1000;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    height: 80px;
}

.header-content {
    display: flex;
    justify-content: space-between;
    align-items: center;
    height: 80px;
}

.logo-header img {
    width: 60px;
    height: 45px;
    object-fit: contain;
}

.nav-desktop {
    display: flex;
    gap: 30px;
}

.nav-link {
    text-decoration: none;
    color: var(--marrom);
    font-weight: 500;
    transition: opacity 0.3s;
    font-size: 1rem;
}

.nav-link:hover {
    opacity: 0.7;
}

.menu-toggle {
    display: none;
    flex-direction: column;
    background: none;
    border: none;
    cursor: pointer;
    gap: 4px;
}

.menu-toggle span {
    width: 25px;
    height: 3px;
    background: var(--marrom);
    transition: 0.3s;
}

.nav-mobile {
    display: none;
    flex-direction: column;
    background: var(--bege);
    padding: 20px;
    gap: 15px;
}

/* Seções */
.section {
    min-height: 100vh;
    display: flex;
    align-items: center;
    padding: 100px 0 80px;
}

.section-title {
    text-align: center;
    font-size: 3rem;
    margin-bottom: 60px;
    font-weight: 500;
}

/* Alternância de cores */
.section:nth-child(odd) {
    background-color: var(--bege);
    color: var(--marrom);
}

.section:nth-child(even) {
    background-color: var(--marrom);
    color: var(--bege);
}

/* HOME */
.section-home {
    text-align: center;
}

.home-content {
    max-width: 90%;
    margin: 0 auto;
}

.home-logo {
    margin-bottom: 40px;
}

.logo-principal {
    width: 100%;
    max-width: 1200px;
    height: auto;
}

.titulo-outline {
    font-size: 4rem;
    -webkit-text-stroke: 3px var(--marrom);
    -webkit-text-fill-color: transparent;
    color: transparent;
    margin-bottom: 20px;
    font-weight: 500;
}

.subtitulo {
    font-size: 1.5rem;
    margin-bottom: 40px;
    font-weight: 500;
}

.home-texto {
    font-size: 1.3rem;
    line-height: 1.8;
    text-align: justify;
    margin-bottom: 40px;
    max-width: 90%;
    margin-left: auto;
    margin-right: auto;
}

.btn-cta {
    background: var(--marrom);
    color: var(--bege);
    border: none;
    padding: 15px 30px;
    font-size: 1.1rem;
    border-radius: 25px;
    cursor: pointer;
    transition: all 0.3s;
    font-family: 'Compagnon Medium', Georgia, serif;
    font-weight: 500;
}

.btn-cta:hover {
    opacity: 0.8;
    transform: translateY(-2px);
}

/* SOBRE */
.sobre-content {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 60px;
    align-items: center;
}

.sobre-fotos {
    display: flex;
    gap: 30px;
    justify-content: center;
}

.foto-socio img {
    width: 300px;
    height: 400px;
    object-fit: cover;
    border-radius: 10px;
}

.sobre-texto p {
    font-size: 1.1rem;
    text-align: justify;
    margin-bottom: 20px;
    line-height: 1.8;
}

/* MÉTODO */
.metodo-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 60px;
    justify-items: center;
}

.metodo-item {
    text-align: center;
}

.metodo-circulo {
    width: 250px;
    height: 250px;
    border-radius: 50%;
    overflow: hidden;
    margin-bottom: 20px;
    border: 3px solid var(--marrom);
}

.metodo-circulo img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.metodo-nome {
    font-size: 1.2rem;
    font-weight: 500;
    color: var(--marrom);
}

/* PROJETOS */
.projetos-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: 40px;
}

.projeto-item {
    background: rgba(255, 247, 240, 0.1);
    border-radius: 10px;
    overflow: hidden;
    transition: transform 0.3s;
    cursor: pointer;
}

.projeto-item:hover {
    transform: translateY(-5px);
}

.projeto-item img {
    width: 100%;
    height: 250px;
    object-fit: cover;
}

.projeto-info {
    padding: 20px;
    text-align: center;
}

.projeto-info h3 {
    font-size: 1.3rem;
    margin-bottom: 15px;
    color: var(--bege);
}

.btn-detalhes {
    background: var(--bege);
    color: var(--marrom);
    border: none;
    padding: 10px 20px;
    border-radius: 20px;
    cursor: pointer;
    transition: all 0.3s;
    font-family: 'Compagnon Medium', Georgia, serif;
    font-weight: 500;
}

.btn-detalhes:hover {
    opacity: 0.8;
}

/* CONTATO */
.contato-content {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 60px;
}

.form-group {
    margin-bottom: 20px;
}

.form-group input,
.form-group textarea {
    width: 100%;
    padding: 15px;
    border: 2px solid var(--marrom);
    border-radius: 5px;
    font-family: 'Compagnon Medium', Georgia, serif;
    font-size: 1rem;
    background: transparent;
    color: var(--marrom);
}

.form-group input::placeholder,
.form-group textarea::placeholder {
    color: var(--marrom);
    opacity: 0.7;
}

.btn-enviar {
    background: var(--marrom);
    color: var(--bege);
    border: none;
    padding: 15px 30px;
    border-radius: 25px;
    cursor: pointer;
    font-family: 'Compagnon Medium', Georgia, serif;
    font-weight: 500;
    transition: all 0.3s;
}

.btn-enviar:hover {
    opacity: 0.8;
}

.info-item {
    margin-bottom: 30px;
}

.info-label {
    font-size: 1.2rem;
    font-weight: bold;
    margin-bottom: 5px;
    text-transform: uppercase;
}

.info-data {
    font-size: 1rem;
}

/* RODAPÉ */
.footer {
    background: var(--marrom);
    color: var(--bege);
    padding: 40px 0;
    text-align: center;
}

.footer-content {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 20px;
}

.footer-logo img {
    width: 40px;
    height: 30px;
    object-fit: contain;
}

.footer-text p {
    margin: 5px 0;
}

/* MODAL */
.modal {
    display: none;
    position: fixed;
    z-index: 2000;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0,0,0,0.8);
}

.modal-content {
    background-color: var(--bege);
    margin: 5% auto;
    padding: 20px;
    border-radius: 10px;
    width: 90%;
    max-width: 900px;
    max-height: 80vh;
    overflow-y: auto;
    position: relative;
}

.modal-close {
    position: absolute;
    top: 15px;
    right: 20px;
    font-size: 2rem;
    background: none;
    border: none;
    cursor: pointer;
    color: var(--marrom);
}

.modal-body h3 {
    text-align: center;
    margin-bottom: 30px;
    font-size: 2rem;
    color: var(--marrom);
}

.modal-images {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 15px;
    margin-bottom: 30px;
}

.modal-images img {
    width: 100%;
    height: 250px;
    object-fit: cover;
    border-radius: 10px;
}

.modal-avaliacao {
    text-align: center;
}

.estrelas {
    font-size: 2rem;
    color: #FFD700;
    margin-bottom: 20px;
}

.cliente-info h4 {
    font-size: 1.3rem;
    margin-bottom: 10px;
    color: var(--marrom);
}

.cliente-info p {
    font-size: 1.1rem;
    font-style: italic;
    color: var(--marrom);
    text-align: justify;
}

/* Responsividade */
@media (max-width: 768px) {
    .nav-desktop {
        display: none;
    }
    
    .menu-toggle {
        display: flex;
    }
    
    .nav-mobile.active {
        display: flex;
    }
    
    .section {
        padding: 120px 0 40px;
    }
    
    .titulo-outline {
        font-size: 2.5rem;
    }
    
    .home-texto {
        font-size: 1.1rem;
    }
    
    .sobre-content {
        grid-template-columns: 1fr;
        text-align: center;
    }
    
    .sobre-fotos {
        flex-direction: column;
        align-items: center;
    }
    
    .metodo-grid {
        grid-template-columns: 1fr;
    }
    
    .projetos-grid {
        grid-template-columns: 1fr;
    }
    
    .contato-content {
        grid-template-columns: 1fr;
    }
    
    .modal-images {
        grid-template-columns: 1fr;
    }
    
    .container {
        padding: 0 15px;
    }
    
    .home-content {
        max-width: 95%;
    }
}

@media (max-width: 480px) {
    .section-title {
        font-size: 2rem;
    }
    
    .titulo-outline {
        font-size: 2rem;
    }
    
    .foto-socio img {
        width: 250px;
        height: 333px;
    }
}"""

# Criar diretório CSS se não existir
import os
os.makedirs('css', exist_ok=True)

# Salvar o arquivo CSS
with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

print("✅ Arquivo CSS criado com sucesso!")