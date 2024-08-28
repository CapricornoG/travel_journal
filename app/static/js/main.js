document.addEventListener('DOMContentLoaded', function () {
    // Function to show the Bootstrap modal
    function showModal(modalId) {
        $(`#${modalId}`).modal('show');
    }

    // Function to hide the Bootstrap modal
    function hideModal(modalId) {
        $(`#${modalId}`).modal('hide');
    }

    // Event listeners for opening modals
    const loginBtn = document.getElementById('loginBtn');
    const registerBtn = document.getElementById('registerBtn');

    if (loginBtn) {
        loginBtn.addEventListener('click', function () {
            showModal('loginModal');
        });
    }

    if (registerBtn) {
        registerBtn.addEventListener('click', function () {
            showModal('registerModal');
        });
    }

    // Close modal when clicking outside of it is handled by Bootstrap by default

    // Scroll functionality for card row
    const scrollLeftBtn = document.querySelector('.scroll-left');
    const scrollRightBtn = document.querySelector('.scroll-right');
    const cardRow = document.querySelector('.card-row');

    if (scrollLeftBtn && cardRow) {
        scrollLeftBtn.addEventListener('click', function () {
            cardRow.scrollBy({
                left: -300, // Adjust the value as needed for scrolling distance
                behavior: 'smooth'
            });
        });
    }

    if (scrollRightBtn && cardRow) {
        scrollRightBtn.addEventListener('click', function () {
            cardRow.scrollBy({
                left: 300, // Adjust the value as needed for scrolling distance
                behavior: 'smooth'
            });
        });
    }

    // Toggle content visibility for 'Read more' functionality
    document.querySelectorAll('.toggle-content').forEach(button => {
        button.addEventListener('click', () => {
            const cardContent = button.closest('.card-content');
            const shortContent = cardContent.querySelector('.short-content');
            const fullContent = cardContent.querySelector('.full-content');

            if (fullContent && shortContent) {
                fullContent.classList.toggle('d-none'); // Show/hide full content
                shortContent.classList.toggle('d-none'); // Show/hide short content
                button.classList.toggle('active'); // Toggle button active state
                button.innerHTML = fullContent.classList.contains('d-none') 
                    ? '<i class="fas fa-chevron-down"></i> Read more' 
                    : '<i class="fas fa-chevron-up"></i> Read less';
            }
        });
    });
});
