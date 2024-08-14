// Function to open the modal
function openModal(modalId) {
    document.getElementById(modalId).style.display = 'block';
}

// Function to close the modal
function closeModal(modalId) {
    document.getElementById(modalId).style.display = 'none';
}

// Event listeners for opening modals
document.getElementById('loginBtn').addEventListener('click', function() {
    openModal('loginModal');
});

document.getElementById('registerBtn').addEventListener('click', function() {
    openModal('registerModal');
});

// Event listeners for closing modals
document.getElementById('closeLoginModal').addEventListener('click', function() {
    closeModal('loginModal');
});

document.getElementById('closeRegisterModal').addEventListener('click', function() {
    closeModal('registerModal');
});

// Close modal when clicking outside of it
window.onclick = function(event) {
    const loginModal = document.getElementById('loginModal');
    const registerModal = document.getElementById('registerModal');
    if (event.target == loginModal) {
        loginModal.style.display = 'none';
    }
    if (event.target == registerModal) {
        registerModal.style.display = 'none';
    }
}
