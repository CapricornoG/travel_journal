document.addEventListener('DOMContentLoaded', function () {
    // Function to open the modal
    function openModal(modalId) {
        document.getElementById(modalId).style.display = 'block';
    }

    // Function to close the modal
    function closeModal(modalId) {
        document.getElementById(modalId).style.display = 'none';
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
        if (event.target == loginModal) {
            loginModal.style.display = 'none';
        }
        if (event.target == registerModal) {
            registerModal.style.display = 'none';
        }
    };
});
