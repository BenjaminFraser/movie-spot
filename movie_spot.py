import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Movie Spot!</title>
    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.4.0/css/font-awesome.min.css">
    <link href='https://fonts.googleapis.com/css?family=Lobster' rel='stylesheet' type='text/css'>
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">

        body {
            padding-top: 0;
        }

        .no-margin {
            margin: 0;
        }

        .no-padding {
            padding: 0;
        }

        .smooth-orange {
            background-image: url('smooth_orange.jpg');
            color: #ffffff;
        }

        #main_header {
            padding: 10px 0 10px 0;
        }

        .custom-header-1 {
            color: white;
            font-weight: bold;
            font-family: 'Lobster', cursive;
        }

        #film_logo {
            height: 50px;
            width: 50px;
            padding: 5px;
            margin-left: 10px;
        }

        #main_page_body {
            background-color: #3b5998;
            width: 100%;
            padding-top: 70px;
            padding-bottom: 50px;
        }

        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
            color: #b2b2cc;
        }
        .movie-tile:hover {
            background-color: #00255c;
            cursor: pointer;
            color: white;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: #3b5998;
        }

        .lobster-text {
            font-family: 'Lobster', cursive;
        }

        .footer {
            position: relative;
            min-height: 120px;
            clear: both;
            padding: 30px 0 30px 0;
        }   
 
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>
    <!-- Main Page Content -->
    <div class="container no-margin">
      <div class="navbar navbar-fixed-top smooth-orange" role="navigation">
        <div class="container">

          <div class="navbar-header pull-left">
            <img src="film_reel.png" class="img-responsive pull-left" alt="Reel of film" id="film_logo"/>
          </div>
          <div class="navbar-header pull-right">
            <a class="navbar-brand custom-header-1" href="#">Welcome to MovieSpot!</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container" id="main_page_body">
      {movie_tiles}
    </div>
    <footer class="footer smooth-orange"> <!-- Thanks for visiting and social media links -->
      <div class="container">
        <div class="row"> 
            <div class="col-xs-6 pull-left">
                <p class="lobster-text">Thanks for visiting, be sure to share us on social media! <i class="fa fa-hand-peace-o"></i></p>
                <hr>
                <p>Ben Fraser - Udacity FSND Project 1 <span class="glyphicon glyphicon-user"></span></p>
            </div>
            

            <div class="col-xs-6 text-right">
                <ul class="list-inline">
                <li><a href="#" title="MovieSpot facebook" class="smooth-orange"><span class="fa fa-facebook-square fa-2x">&nbsp;</span></a> </li>
                <li><a href="#" title="MovieSpot twitter" class="smooth-orange"><span class="fa fa-twitter-square fa-2x">&nbsp;</span></a> </li>
                <li><a href="#" title="MovieSpot on youtube" class="smooth-orange"><span class="fa fa-youtube-square fa-2x">&nbsp;</span></a> </li>
                </ul>
            </div>
        </div>  
      </div>
   </footer>
  </body>
</html>
'''


# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" width="220" height="342">
    <h2>{movie_title}</h2>
    <p class="lead">{storyline}</p>
    <p>Directed by {director}</p>
</div>
'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            storyline=movie.storyline,
            director=movie.director,
            trailer_youtube_id=trailer_youtube_id
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
