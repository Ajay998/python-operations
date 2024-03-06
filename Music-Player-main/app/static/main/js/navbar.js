$(document).ready(function () {

    // Event delegation for dynamically loaded buttons
    $('.backnext').on('click', '#back-button', function () {
        window.history.back();
        console.log("hello")
    });

    $('.backnext').on('click', '#next-button', function () {
        window.history.forward();
    });

    function loadContent(url) {
        $.ajax({
            url: url,
            type: 'GET',
            success: function (data) {
                $('#content-container').html(data);
                // Add the state to the browser history
                window.history.pushState({ url: url }, '', url);
            },
            error: function () {
                console.error('Error loading content');
            }
        });
    }

    // Listen for popstate event (browser back/forward button clicked)
    window.addEventListener('popstate', function (event) {
        if (event.state && event.state.url) {
            loadContent(event.state.url);
        } else {
            // Handle the initial state (no state)
            loadContent(window.location.href);
        }
    });
});
