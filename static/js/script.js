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
