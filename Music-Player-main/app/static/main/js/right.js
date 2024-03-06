document.addEventListener("DOMContentLoaded", function() {
    let rightnavmenu = document.querySelector(".signloginmenu");
    let signlogin = document.querySelector(".signlogin");
    let defaultMenu = false;
    let songIndex=1;
    const musicItems = document.querySelectorAll('.musicitem');

    signlogin.addEventListener("click", function (event) {
        event.stopPropagation();

        if (defaultMenu == false) {
            rightnavmenu.style.display = "block";
            defaultMenu = true;
        } else {
            rightnavmenu.style.display = "none";
            defaultMenu = false;
        }
    });

    document.body.addEventListener("click", function () {
        if (defaultMenu == true) {
            rightnavmenu.style.display = "none";
            defaultMenu = false;
        }
    });
});

$(document).ready(function () {
    // Load initial content

    

    // Handle button click event
    $('button.uploadBtn').click(function (e) {
        e.preventDefault();
        loadContent('upload', '#dynamic-content');
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
