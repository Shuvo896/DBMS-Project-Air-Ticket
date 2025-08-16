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

// script.js
document.addEventListener('DOMContentLoaded', function() {
    const hamburger = document.querySelector('.hamburger');
    
    if (hamburger) {
        hamburger.addEventListener('click', function() {
            const navLeft = document.querySelector('.nav-left');
            const navRight = document.querySelector('.nav-right');
            
            navLeft.classList.toggle('active');
            navRight.classList.toggle('active');
        });
    }
});