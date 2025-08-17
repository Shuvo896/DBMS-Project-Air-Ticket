document.addEventListener('DOMContentLoaded', function() {
    // Confirm on booking
    document.querySelectorAll('.btn').forEach(function(button) {
        button.addEventListener('click', function(e) {
            if (this.textContent.includes('Book')) {
                if (!confirm('Do you want to book this flight?')) {
                    e.preventDefault();
                }
            }
        });
    });
});


document.addEventListener('DOMContentLoaded', function() {
    const hamburger = document.getElementById('hamburger');
    const navLeft = document.getElementById('navLeft');
    const navRight = document.getElementById('navRight');
    
    hamburger.addEventListener('click', function() {
        this.classList.toggle('active');
        navLeft.classList.toggle('active');
        navRight.classList.toggle('active');
        
        // Animate hamburger to X
        const spans = this.querySelectorAll('span');
        if (this.classList.contains('active')) {
            spans[0].style.transform = 'rotate(45deg) translate(5px, 5px)';
            spans[1].style.opacity = '0';
            spans[2].style.transform = 'rotate(-45deg) translate(5px, -5px)';
        } else {
            spans.forEach(span => {
                span.style.transform = '';
                span.style.opacity = '';
            });
        }
    });
    
    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
});