document.addEventListener('DOMContentLoaded', function() {
    // Общие функции для всех страниц
    
    // Плавная прокрутка для якорей
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
    
    // Анимация элементов при появлении в viewport
    const animateOnScroll = () => {
        const elements = document.querySelectorAll('.game-block, .screenshot-placeholder, .text-content');
        
        elements.forEach(element => {
            const elementPosition = element.getBoundingClientRect().top;
            const screenPosition = window.innerHeight / 1.2;
            
            if (elementPosition < screenPosition) {
                element.style.opacity = '1';
                element.style.transform = 'translateY(0)';
            }
        });
    };
    
    // Инициализация анимации
    window.addEventListener('scroll', animateOnScroll);
    animateOnScroll(); // Запустить при загрузке
    
    // Эффект параллакса для фона
    window.addEventListener('scroll', function() {
        const scrollPosition = window.pageYOffset;
        const background = document.querySelector('.background-blur');
        if (background) {
            background.style.transform = `translateY(${scrollPosition * 0.3}px)`;
        }
    });
});