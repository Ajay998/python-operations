$(document).ready(function () {
    function updateSuggestions(songs) {
        var suggestionsBox = $('#suggestions');
        suggestionsBox.empty();

        if (songs.length > 0) {
            songs.forEach(function (song) {
                var suggestionItem = $('<div class="suggestion-item"></div>');
                suggestionItem.html(`<span>${song.name} by ${song.artist}</span>
                                     <button class="add-to-playlist" data-song-id="${song.id}">Add to Playlist</button>`);
                suggestionsBox.append(suggestionItem);
            });
        } else {
            suggestionsBox.text('No matching songs found.');
        }

        suggestionsBox.show();
    }

    function clearSuggestions() {
        $('#suggestions').hide().empty();
    }

    $('#search-input').on('input', function () {
        var query = $(this).val();
        if (query.length > 0) {
            $.ajax({
                url: '/search_songs/',
                method: 'GET',
                data: { query: query },
                success: function (data) {
                    updateSuggestions(data.matching_songs);
                },
                error: function () {
                    // Handle error if needed
                }
            });
        } else {
            clearSuggestions();
        }
    });

    $(document).on('click', '.add-to-playlist', function() {
        var songId = $(this).data('song-id');

        $.ajax({
            url: `/add_to_playlist/${songId}/`,
            method: 'POST',
            headers: {
                'X-CSRFToken': $('input[name="csrfmiddlewaretoken"]').val(),
            },
            data: {},
            success: function (data) {
                if (data.success) {
                    $('#playlist-message').text('Song added to playlist successfully').show();
                } else {
                    $('#playlist-message').text('Error adding song to playlist').show();
                }
            },
            error: function () {
                $('#playlist-message').text('Error adding song to playlist').show();
            }
        });
    });

    $(document).on('click', function (e) {
        if (!$(e.target).closest('.search-box').length) {
            clearSuggestions();
        }
    });
});
