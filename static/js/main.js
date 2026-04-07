document.addEventListener('DOMContentLoaded', function() {
    initHeader();
    initMobileMenu();
    initTabs();
    initQuantitySelectors();
    initScrollAnimations();
});

function initHeader() {
    const header = document.getElementById('header');
    if (!header) return;
    
    let lastScroll = 0;
    
    window.addEventListener('scroll', () => {
        const currentScroll = window.pageYOffset;
        
        if (currentScroll > 100) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
        
        lastScroll = currentScroll;
    });
}

function initMobileMenu() {
    const menuBtn = document.getElementById('menu-btn');
    const nav = document.getElementById('nav');
    
    if (!menuBtn || !nav) return;
    
    menuBtn.addEventListener('click', () => {
        nav.classList.toggle('open');
        
        const icon = menuBtn.querySelector('svg');
        if (nav.classList.contains('open')) {
            icon.setAttribute('data-lucide', 'x');
        } else {
            icon.setAttribute('data-lucide', 'menu');
        }
        lucide.createIcons();
    });
    
    document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', () => {
            nav.classList.remove('open');
            const icon = menuBtn.querySelector('svg');
            icon.setAttribute('data-lucide', 'menu');
            lucide.createIcons();
        });
    });
}

function initTabs() {
    const tabBtns = document.querySelectorAll('.tab-btn');
    const tabContents = document.querySelectorAll('.tab-content');
    
    tabBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const target = btn.dataset.tab;
            
            tabBtns.forEach(b => b.classList.remove('active'));
            tabContents.forEach(c => c.classList.remove('active'));
            
            btn.classList.add('active');
            document.getElementById(target).classList.add('active');
        });
    });
}

function initQuantitySelectors() {
    const selectors = document.querySelectorAll('.quantity-controls');
    
    selectors.forEach(control => {
        const decreaseBtn = control.querySelector('.quantity-btn.decrease');
        const increaseBtn = control.querySelector('.quantity-btn.increase');
        const valueSpan = control.querySelector('.quantity-value');
        
        if (decreaseBtn && increaseBtn && valueSpan) {
            let value = parseInt(valueSpan.textContent);
            
            decreaseBtn.addEventListener('click', (e) => {
                e.preventDefault();
                if (value > 1) {
                    value--;
                    valueSpan.textContent = value;
                    updateHiddenInput(control, value);
                }
            });
            
            increaseBtn.addEventListener('click', (e) => {
                e.preventDefault();
                value++;
                valueSpan.textContent = value;
                updateHiddenInput(control, value);
            });
        }
    });
}

function updateHiddenInput(control, value) {
    const hiddenInput = control.querySelector('input[type="hidden"]');
    if (hiddenInput) {
        hiddenInput.value = value;
    }
}

function initScrollAnimations() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);
    
    document.querySelectorAll('.feature-card, .product-card, .value-card, .story-card').forEach(el => {
        observer.observe(el);
    });
}

function animateCartBadge() {
    const badge = document.querySelector('.cart-badge');
    if (badge) {
        badge.style.animation = 'none';
        badge.offsetHeight;
        badge.style.animation = 'bounce 0.3s ease';
    }
}

window.animateCartBadge = animateCartBadge;
