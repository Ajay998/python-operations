document.addEventListener("DOMContentLoaded", function() {
    let collapse = document.querySelector(".collapse");
    let maximize = document.querySelector(".maximize");
    let left = document.querySelector(".left");
    let right = document.querySelector(".right");
    let defaultOptionCollapse = false;
    let defaultOptionMaximize = false;
    const createPlaylistButton = document.querySelector('.createplaylist');

    saveSettings();

    collapse.addEventListener('click', function(){
        if (defaultOptionCollapse == false){
            left.style.width = "5%";
            right.style.width = "94%";
            localStorage.setItem("collapseSettings", true);
            localStorage.setItem("maximizeSettings", false);
            defaultOptionCollapse = true;
        }
        else {
            left.style.width = "35%";
            right.style.width = "75%";
            localStorage.setItem("collapseSettings", false);
            defaultOptionCollapse = false;
        }
    });

    maximize.addEventListener('click', function(){
        if (defaultOptionMaximize == false){
            left.style.width = "60%";
            right.style.width = "40%";
            localStorage.setItem("maximizeSettings", true);
            localStorage.setItem("collapseSettings", false);
            defaultOptionMaximize = true;
        }
        else {
            left.style.width = "25%";
            right.style.width = "75%";
            localStorage.setItem("maximizeSettings", false);
            defaultOptionMaximize = false;
        }
    });


    function saveSettings(){
        defaultOptionCollapse = localStorage.getItem("collapseSettings");
        defaultOptionMaximize = localStorage.getItem("maximizeSettings");
        if (defaultOptionCollapse=='true'){
            left.style.width = "5%";
            right.style.width = "94%";
        }
        if (defaultOptionMaximize=='true'){
            left.style.width = "60%";
            right.style.width = "40%";
        }
    }

    createPlaylistButton.addEventListener('click', function () {
        // Make an AJAX request to create a new playlist
        fetch('/create_playlist/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken'), // Ensure you include CSRF token
            },
            credentials: 'same-origin',
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // Redirect to the new playlist using the playlist slug
                window.location.href = '/playlist/' + data.playlist_slug + '/';
            } else {
                console.error(data.error);
            }
        })
        .catch(error => console.error('Error:', error));
    });

    $(document).ready(function () {
        // Handle playlist click event
        $(document).on('click', '.playlists', function () {
            var playlistSlug = $(this).data('slug');
            var url = '/playlist/' + playlistSlug + '/';
    
            // Load playlist details into the right container
            loadContent(url, '#dynamic-content');
        });
    
        function loadContent(url, target) {
            $.ajax({
                url: url,
                method: 'GET',
                success: function (data) {
                    $(target).html(data);
                },
                error: function () {
                    // Handle error if needed
                }
            });
        }
    });
    
    // Function to get CSRF token from cookies
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.startsWith(name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
