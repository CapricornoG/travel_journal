document.addEventListener('DOMContentLoaded', function () {
    // Function to open the modal
    function openModal(modalId) {
        const modal = document.getElementById(modalId);
        if (modal) {
            modal.style.display = 'block';
        }
    }

    // Function to close the modal
    function closeModal(modalId) {
        const modal = document.getElementById(modalId);
        if (modal) {
            modal.style.display = 'none';
        }
    }

    // Event listeners for opening modals
    const loginBtn = document.getElementById('loginBtn');
    const registerBtn = document.getElementById('registerBtn');

    if (loginBtn) {
        loginBtn.addEventListener('click', function () {
            openModal('loginModal');
        });
    }

    if (registerBtn) {
        registerBtn.addEventListener('click', function () {
            openModal('registerModal');
        });
    }

    // Event listeners for closing modals
    const closeLoginModal = document.getElementById('closeLoginModal');
    const closeRegisterModal = document.getElementById('closeRegisterModal');

    if (closeLoginModal) {
        closeLoginModal.addEventListener('click', function () {
            closeModal('loginModal');
        });
    }

    if (closeRegisterModal) {
        closeRegisterModal.addEventListener('click', function () {
            closeModal('registerModal');
        });
    }

    // Close modal when clicking outside of it
    window.onclick = function (event) {
        const loginModal = document.getElementById('loginModal');
        const registerModal = document.getElementById('registerModal');
        if (event.target === loginModal) {
            closeModal('loginModal');
        }
        if (event.target === registerModal) {
            closeModal('registerModal');
        }
    };

    // Scroll functionality for card row
    const scrollLeftBtn = document.querySelector('.scroll-left');
    const scrollRightBtn = document.querySelector('.scroll-right');
    const cardRow = document.querySelector('.card-row');

    if (scrollLeftBtn && cardRow) {
        scrollLeftBtn.addEventListener('click', function () {
            console.log('Scrolling left');
            cardRow.scrollBy({
                left: -300, // Adjust the value as needed for scrolling distance
                behavior: 'smooth'
            });
        });
    } else {
        console.warn('Scroll left button or card row not found.');
    }

    if (scrollRightBtn && cardRow) {
        scrollRightBtn.addEventListener('click', function () {
            console.log('Scrolling right');
            cardRow.scrollBy({
                left: 300, // Adjust the value as needed for scrolling distance
                behavior: 'smooth'
            });
        });
    } else {
        console.warn('Scroll right button or card row not found.');
    }
});
