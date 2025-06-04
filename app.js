// Dados do escritório
const escritorioData = {
  "escritorio": {
    "nome": "RECANTO",
    "subtitulo": "ARQUITETURA CONTEMPORÂNEA",
    "arquitetos": ["Raul Hirsch", "Gabriel Thomé"],
    "formacao": "UFMG",
    "filosofia": "Acreditamos que a arquitetura tem o poder de preservar histórias e criar novas memórias"
  },
  "contato": {
    "instagram": "@RECANTO_ARQ",
    "whatsapp": "12 99646-2826",
    "email": "RECANTOMINEIROARQUITETURA@GMAIL.COM"
  },
  "servicos": [
    {
      "nome": "Estudo Preliminar",
      "descricao": "Esboços e Modelagens 3D",
      "preco": 900,
      "detalhes": "Ponto de partida para transformar ideias em realidade. Exploramos o potencial do terreno e criamos proposta inicial."
    },
    {
      "nome": "Anteprojeto", 
      "descricao": "Definição e Imagens Realistas",
      "preco": 1200,
      "detalhes": "Visão começa a ganhar contornos mais claros. Plantas detalhadas e renderizações tridimensionais."
    },
    {
      "nome": "Projeto Executivo",
      "descricao": "Desenhos Técnicos e Imagens para Execução", 
      "preco": 1250,
      "detalhes": "Plano técnico completo, pronto para ser materializado. Desenhos técnicos detalhados."
    },
    {
      "nome": "Detalhamento",
      "descricao": "Especificações para Construção e Aprovação",
      "preco": 1320,
      "detalhes": "Projeto ganha vida nos mínimos detalhes. Foco em áreas sensíveis como cozinhas e banheiros."
    }
  ],
  "pacotes": [
    {
      "nome": "Projeto Completo",
      "preco_original": 4670,
      "preco_desconto": 2690,
      "desconto": "45%",
      "inclui": ["Estudo Preliminar", "Anteprojeto", "Projeto Executivo", "Detalhamento"]
    },
    {
      "nome": "Projeto Rápido", 
      "preco_original": 2100,
      "preco_desconto": 980,
      "desconto": "53%",
      "inclui": ["Estudo Preliminar", "Anteprojeto"]
    }
  ],
  "metodologia": [
    {
      "etapa": 1,
      "nome": "Estudo Preliminar",
      "descricao": "Ponto de partida para transformar ideias em realidade"
    },
    {
      "etapa": 2, 
      "nome": "Anteprojeto",
      "descricao": "Momento em que a visão começa a ganhar contornos mais claros"
    },
    {
      "etapa": 3,
      "nome": "Projeto Executivo", 
      "descricao": "Sonho arquitetônico se transforma em plano técnico completo"
    },
    {
      "etapa": 4,
      "nome": "Detalhamento e Execução",
      "descricao": "Projeto ganha vida nos mínimos detalhes"
    },
    {
      "etapa": 5,
      "nome": "Consultoria",
      "descricao": "Acompanhamento profissional durante execução"
    },
    {
      "etapa": 6,
      "nome": "Consultoria para Airbnb", 
      "descricao": "Projetos específicos para hospedagem"
    }
  ],
  "projetos_placeholder": [
    {
      "id": 1,
      "titulo": "Residência Contemporânea",
      "descricao": "Projeto residencial com foco em integração com a natureza",
      "imagem": "/projetos/projeto1.jpg"
    },
    {
      "id": 2,
      "titulo": "Casa de Campo",
      "descricao": "Arquitetura que dialoga com o ambiente rural",
      "imagem": "/projetos/projeto2.jpg"  
    },
    {
      "id": 3,
      "titulo": "Loft Urbano",
      "descricao": "Espaço moderno no coração da cidade",
      "imagem": "/projetos/projeto3.jpg"
    },
    {
      "id": 4,
      "titulo": "Reforma Sustentável", 
      "descricao": "Revitalização com foco em sustentabilidade",
      "imagem": "/projetos/projeto4.jpg"
    },
    {
      "id": 5,
      "titulo": "Edifício Comercial",
      "descricao": "Arquitetura corporativa contemporânea", 
      "imagem": "/projetos/projeto5.jpg"
    },
    {
      "id": 6,
      "titulo": "Paisagismo Integrado",
      "descricao": "Jardins que conectam interior e exterior",
      "imagem": "/projetos/projeto6.jpg"
    }
  ]
};

// DOM Elements
let navToggle, navMenu, projetosGrid, metodologiaTimeline, contactForm, modal, modalBody, modalClose;

// Initialize app
document.addEventListener('DOMContentLoaded', function() {
  // Get DOM elements
  navToggle = document.getElementById('navToggle');
  navMenu = document.getElementById('navMenu');
  projetosGrid = document.getElementById('projetosGrid');
  metodologiaTimeline = document.getElementById('metodologiaTimeline');
  contactForm = document.getElementById('contactForm');
  modal = document.getElementById('projetoModal');
  modalBody = document.getElementById('modalBody');
  modalClose = document.querySelector('.modal__close');

  initNavigation();
  loadProjetos();
  loadMetodologia();
  initContactForm();
  initModal();
  initScrollAnimations();
  initSmoothScroll();
  initPackageButtons();
});

// Navigation functionality
function initNavigation() {
  if (!navToggle || !navMenu) return;

  // Mobile menu toggle
  navToggle.addEventListener('click', function() {
    navMenu.classList.toggle('active');
  });

  // Close menu when clicking on link
  navMenu.addEventListener('click', function(e) {
    if (e.target.classList.contains('nav__link')) {
      navMenu.classList.remove('active');
    }
  });

  // Active link highlighting on scroll
  window.addEventListener('scroll', updateActiveLink);
}

function updateActiveLink() {
  const sections = document.querySelectorAll('section[id]');
  const scrollY = window.pageYOffset;

  sections.forEach(section => {
    const sectionHeight = section.offsetHeight;
    const sectionTop = section.offsetTop - 100;
    const sectionId = section.getAttribute('id');
    const navLink = document.querySelector(`.nav__link[href="#${sectionId}"]`);

    if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
      document.querySelectorAll('.nav__link').forEach(link => link.classList.remove('active'));
      navLink?.classList.add('active');
    }
  });
}

// Load projects dynamically
function loadProjetos() {
  if (!projetosGrid) return;

  projetosGrid.innerHTML = '';
  
  escritorioData.projetos_placeholder.forEach(projeto => {
    const projetoCard = createProjetoCard(projeto);
    projetosGrid.appendChild(projetoCard);
  });
}

function createProjetoCard(projeto) {
  const card = document.createElement('div');
  card.className = 'card projeto-card fade-in-up';
  card.dataset.projetoId = projeto.id;
  
  card.innerHTML = `
    <div class="card__body">
      <div class="projeto__image">
        <span>Imagem do Projeto</span>
      </div>
      <h3 class="projeto__title">${projeto.titulo}</h3>
      <p class="projeto__desc">${projeto.descricao}</p>
      <button class="btn btn--outline projeto-details-btn" data-projeto-id="${projeto.id}">Ver Detalhes</button>
    </div>
  `;

  // Add click event listener to the button specifically
  const detailsButton = card.querySelector('.projeto-details-btn');
  detailsButton.addEventListener('click', function(e) {
    e.preventDefault();
    e.stopPropagation();
    openProjetoModal(projeto);
  });
  
  return card;
}

// Load methodology timeline
function loadMetodologia() {
  if (!metodologiaTimeline) return;

  metodologiaTimeline.innerHTML = '';
  
  escritorioData.metodologia.forEach(etapa => {
    const stepElement = createMetodologiaStep(etapa);
    metodologiaTimeline.appendChild(stepElement);
  });
}

function createMetodologiaStep(etapa) {
  const step = document.createElement('div');
  step.className = 'metodologia__step fade-in-up';
  
  step.innerHTML = `
    <div class="metodologia__number">${etapa.etapa}</div>
    <div class="metodologia__content">
      <h4>${etapa.nome}</h4>
      <p>${etapa.descricao}</p>
    </div>
  `;
  
  return step;
}

// Modal functionality
function initModal() {
  if (!modal || !modalClose) return;

  modalClose.addEventListener('click', closeModal);
  
  modal.addEventListener('click', function(e) {
    if (e.target === modal) {
      closeModal();
    }
  });

  // Close modal with Escape key
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape' && modal.style.display === 'block') {
      closeModal();
    }
  });
}

function openProjetoModal(projeto) {
  if (!modal || !modalBody) return;

  modalBody.innerHTML = `
    <div class="projeto-modal">
      <div class="projeto-modal__image">
        <div class="placeholder-image">
          <span>Imagem: ${projeto.titulo}</span>
        </div>
      </div>
      <div class="projeto-modal__content">
        <h2>${projeto.titulo}</h2>
        <p>${projeto.descricao}</p>
        <p>Este projeto representa nossa filosofia de criar espaços que emocionam e transformam vidas. Cada detalhe foi pensado para proporcionar a melhor experiência aos usuários, integrando funcionalidade e beleza.</p>
        <div class="projeto-modal__actions">
          <button class="btn btn--primary" onclick="contactarSobreProjeto('${projeto.titulo}')">
            Solicitar Orçamento
          </button>
          <button class="btn btn--outline" onclick="closeModal()">
            Fechar
          </button>
        </div>
      </div>
    </div>
  `;

  modal.style.display = 'block';
  document.body.style.overflow = 'hidden';
}

function closeModal() {
  if (!modal) return;
  
  modal.style.display = 'none';
  document.body.style.overflow = 'auto';
}

function contactarSobreProjeto(projetoTitulo) {
  closeModal();
  
  // Scroll to contact section
  const contatoSection = document.getElementById('contato');
  if (contatoSection) {
    contatoSection.scrollIntoView({ behavior: 'smooth' });
    
    // Pre-fill form with project info
    setTimeout(() => {
      const mensagemField = document.getElementById('mensagem');
      if (mensagemField) {
        mensagemField.value = `Olá! Gostaria de solicitar um orçamento para um projeto similar ao "${projetoTitulo}". `;
        mensagemField.focus();
      }
    }, 1000);
  }
}

// Package button functionality
function initPackageButtons() {
  // Wait for DOM to be ready and then attach event listeners
  setTimeout(() => {
    const packageButtons = document.querySelectorAll('.pacotes .btn');
    packageButtons.forEach(button => {
      button.addEventListener('click', function(e) {
        e.preventDefault();
        const packageCard = this.closest('.card');
        const packageName = packageCard.querySelector('h4').textContent;
        contactarSobrePacote(packageName);
      });
    });
  }, 100);
}

function contactarSobrePacote(packageName) {
  // Scroll to contact section
  const contatoSection = document.getElementById('contato');
  if (contatoSection) {
    contatoSection.scrollIntoView({ behavior: 'smooth' });
    
    // Pre-fill form with package info
    setTimeout(() => {
      const nomeField = document.getElementById('nome');
      const emailField = document.getElementById('email');
      const projetoField = document.getElementById('projeto');
      const mensagemField = document.getElementById('mensagem');
      
      if (projetoField) {
        projetoField.value = 'residencial';
      }
      
      if (mensagemField) {
        mensagemField.value = `Olá! Tenho interesse no pacote "${packageName}". Gostaria de mais informações e solicitar um orçamento. `;
        mensagemField.focus();
      }
    }, 1000);
  }
}

// Contact form functionality
function initContactForm() {
  if (!contactForm) return;

  contactForm.addEventListener('submit', function(e) {
    e.preventDefault();
    handleFormSubmission();
  });
}

function handleFormSubmission() {
  // Get form values
  const nome = document.getElementById('nome').value.trim();
  const email = document.getElementById('email').value.trim();
  const telefone = document.getElementById('telefone').value.trim();
  const projeto = document.getElementById('projeto').value;
  const mensagem = document.getElementById('mensagem').value.trim();
  
  // Basic validation
  if (!nome || !email || !mensagem) {
    showNotification('Por favor, preencha todos os campos obrigatórios.', 'error');
    return;
  }

  // Email validation
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(email)) {
    showNotification('Por favor, insira um email válido.', 'error');
    return;
  }

  // Simulate form submission
  const submitButton = contactForm.querySelector('button[type="submit"]');
  const originalText = submitButton.textContent;
  
  submitButton.textContent = 'Enviando...';
  submitButton.disabled = true;
  submitButton.classList.add('loading');

  // Simulate API call
  setTimeout(() => {
    // Create WhatsApp message
    const whatsappMessage = createWhatsAppMessage(nome, email, telefone, projeto, mensagem);
    
    // Open WhatsApp
    window.open(`https://wa.me/5512996462826?text=${encodeURIComponent(whatsappMessage)}`, '_blank');
    
    // Reset form
    contactForm.reset();
    
    // Reset button
    submitButton.textContent = originalText;
    submitButton.disabled = false;
    submitButton.classList.remove('loading');
    
    showNotification('Redirecionando para WhatsApp...', 'success');
  }, 1000);
}

function createWhatsAppMessage(nome, email, telefone, projeto, mensagem) {
  return `Olá! Sou ${nome} e gostaria de solicitar um orçamento.

📧 Email: ${email}
📱 Telefone: ${telefone || 'Não informado'}
🏠 Tipo de Projeto: ${projeto || 'Não especificado'}

💬 Mensagem:
${mensagem}

Aguardo retorno!`;
}

function showNotification(message, type = 'info') {
  // Remove existing notifications
  const existingNotifications = document.querySelectorAll('.notification');
  existingNotifications.forEach(notification => notification.remove());

  // Create notification element
  const notification = document.createElement('div');
  notification.className = `notification notification--${type}`;
  notification.innerHTML = `
    <div class="notification__content">
      <span>${message}</span>
      <button class="notification__close">&times;</button>
    </div>
  `;

  // Add styles
  notification.style.cssText = `
    position: fixed;
    top: 20px;
    right: 20px;
    z-index: 3000;
    background: var(--color-surface);
    border: 1px solid var(--color-border);
    border-radius: var(--radius-base);
    padding: var(--space-16);
    box-shadow: var(--shadow-lg);
    max-width: 400px;
    animation: slideInRight 0.3s ease-out;
  `;

  if (type === 'success') {
    notification.style.borderColor = 'var(--color-success)';
    notification.style.backgroundColor = 'rgba(33, 128, 141, 0.1)';
  } else if (type === 'error') {
    notification.style.borderColor = 'var(--color-error)';
    notification.style.backgroundColor = 'rgba(192, 21, 47, 0.1)';
  }

  document.body.appendChild(notification);

  // Close button functionality
  const closeBtn = notification.querySelector('.notification__close');
  closeBtn.addEventListener('click', () => {
    notification.remove();
  });

  // Auto remove after 5 seconds
  setTimeout(() => {
    if (notification.parentNode) {
      notification.remove();
    }
  }, 5000);
}

// Smooth scroll functionality
function initSmoothScroll() {
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      e.preventDefault();
      const target = document.querySelector(this.getAttribute('href'));
      
      if (target) {
        const headerHeight = document.querySelector('.header').offsetHeight;
        const targetPosition = target.offsetTop - headerHeight;
        
        window.scrollTo({
          top: targetPosition,
          behavior: 'smooth'
        });
      }
    });
  });
}

// Scroll animations
function initScrollAnimations() {
  const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('fade-in-up');
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  // Observe elements for animation
  const animatedElements = document.querySelectorAll('.card, .metodologia__step, .hero__content, .section__header');
  animatedElements.forEach(el => {
    observer.observe(el);
  });
}

// Header scroll effect
window.addEventListener('scroll', function() {
  const header = document.querySelector('.header');
  if (header) {
    if (window.scrollY > 100) {
      header.style.background = 'rgba(255, 255, 255, 0.98)';
      header.style.boxShadow = '0 2px 20px rgba(0, 0, 0, 0.1)';
    } else {
      header.style.background = 'rgba(255, 255, 255, 0.95)';
      header.style.boxShadow = 'none';
    }
  }
});

// Add CSS animations dynamically
const style = document.createElement('style');
style.textContent = `
  @keyframes slideInRight {
    from {
      transform: translateX(100%);
      opacity: 0;
    }
    to {
      transform: translateX(0);
      opacity: 1;
    }
  }

  .notification__content {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: var(--space-12);
  }

  .notification__close {
    background: none;
    border: none;
    font-size: 18px;
    cursor: pointer;
    color: var(--color-text-secondary);
    padding: 0;
    width: 20px;
    height: 20px;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .notification__close:hover {
    color: var(--color-text);
  }

  .projeto-modal {
    display: grid;
    gap: var(--space-24);
  }

  .projeto-modal__image .placeholder-image {
    height: 250px;
    margin-bottom: var(--space-16);
  }

  .projeto-modal__content h2 {
    color: var(--color-primary-dark);
    margin-bottom: var(--space-16);
  }

  .projeto-modal__content p {
    margin-bottom: var(--space-16);
    line-height: var(--line-height-normal);
  }

  .projeto-modal__actions {
    display: flex;
    gap: var(--space-12);
    margin-top: var(--space-24);
  }

  .nav__link.active {
    color: var(--color-primary-yellow);
  }

  .nav__link.active::after {
    width: 100%;
  }

  @media (min-width: 768px) {
    .projeto-modal {
      grid-template-columns: 1fr 1fr;
      align-items: start;
    }

    .projeto-modal__actions {
      flex-direction: column;
    }
  }
`;

document.head.appendChild(style);

// Make functions globally available for onclick handlers
window.closeModal = closeModal;
window.contactarSobreProjeto = contactarSobreProjeto;