document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.quantity-input').forEach(input => {
        input.addEventListener('change', function() {
            const itemId = this.dataset.itemId;
            const newQuantity = this.value;
            fetch(`/cart/update_quantity/${itemId}/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': getCookie('csrftoken'),
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({quantity: newQuantity})
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    console.log("Quantity updated");
                }
            });
        });
    });

    document.querySelectorAll('.remove-item-btn').forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            const confirmRemoval = confirm('Are you sure you want to remove this item?');
        if (confirmRemoval) {
            this.closest('form').submit();}
            const itemId = this.dataset.itemId;
            const itemName = this.dataset.itemName;
            fetch(`/cart/remove_item/${itemId}/`, {
                method: 'DELETE',
                headers: {
                    'X-CSRFToken': getCookie('csrftoken'),
                },
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    document.querySelector(`#cart-item-container-${itemId}`).remove();
                    displayMessage(`${itemName} has been removed successfully.`);
                }
            });
        });
    });
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=') ) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function displayMessage(message) {
    const toastContainer = document.getElementById('toastContainer');
    toastContainer.innerText = message;
    toastContainer.style.display = 'block';

    setTimeout(() => {
        toastContainer.style.display = 'none';
    }, 5000);
}