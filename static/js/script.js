document.addEventListener('DOMContentLoaded', function () {
    const addToCartButtons = document.querySelectorAll('.cart-btn');

    addToCartButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            const message = this.getAttribute('data-message');
            const imageUrl = this.getAttribute('data-image-url');
            showToast(message, imageUrl);
        });
    });

    function showToast(message, imageUrl) {
        const toastHTML = `<div class="toast" role="alert" aria-live="assertive" aria-atomic="true" data-bs-delay="5000">
          <div class="toast-header">
            <img src="${imageUrl}" class="rounded me-2" alt="Product" style="width: 20px; height: 20px;">
            <strong class="me-auto">Added to Cart!</strong>
            <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
          </div>
          <div class="toast-body">
            ${message}
          </div>
        </div>`;

        const toastContainer = document.getElementById('toastContainer');
        toastContainer.innerHTML += toastHTML;

        var toastElList = [].slice.call(document.querySelectorAll('.toast'));
        var toastList = toastElList.map(function(toastEl) {
          return new bootstrap.Toast(toastEl).show();
        });
    }
});


function openTab(evt, tabName) {

    var i, tabcontent, tablinks;


    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }


    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }


    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " active";
}

document.getElementById("defaultOpen").click();

