<!DOCTYPE html>
<html lang="en">

<head>
	<title>WAV to MP3 Converter</title>
	<meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="Thomas Delaney">
	{% load staticfiles %}
	<link rel='stylesheet' href="{% static 'css/bootstrap.min.css' %}" type="text/css">
    <link href="{% static 'css/narrow-jumbotron.css' %}" rel="stylesheet" type="text/css">
</head>

<div class="container">
      <div class="header clearfix">
        <nav>
          <ul class="nav nav-pills float-right">
            <li class="nav-item">
              <a class="nav-link active" href="#">Home <span class="sr-only">(current)</span></a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">About</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Contact</a>
            </li>
          </ul>
        </nav>
        <h3 class="text-muted">Quick Converter</h3>
      </div>

      <div class="jumbotron">
        <h1 class="display-3">WAV to MP3 Converter</h1>
        <p class="lead">Convert any WAV to a MP3 File</p>
        <p>
			<form action="upload_file" method="POST" enctype="multipart/form-data">
			{% csrf_token %}
				<input type="file" name="wavFile" >
				<input class="btn btn-lg btn" type="submit" style="cursor: pointer" value="Convert">
			</form>
		</p>
      </div>

      <div class="row marketing">
        <div class="col-lg-6">
          <h4>Subheading</h4>
          <p>Donec id elit non mi porta gravida at eget metus. Maecenas faucibus mollis interdum.</p>

          <h4>Subheading</h4>
          <p>Morbi leo risus, porta ac consectetur ac, vestibulum at eros. Cras mattis consectetur purus sit amet fermentum.</p>

          <h4>Subheading</h4>
          <p>Maecenas sed diam eget risus varius blandit sit amet non magna.</p>
        </div>

        <div class="col-lg-6">
          <h4>Subheading</h4>
          <p>Donec id elit non mi porta gravida at eget metus. Maecenas faucibus mollis interdum.</p>

          <h4>Subheading</h4>
          <p>Morbi leo risus, porta ac consectetur ac, vestibulum at eros. Cras mattis consectetur purus sit amet fermentum.</p>

          <h4>Subheading</h4>
          <p>Maecenas sed diam eget risus varius blandit sit amet non magna.</p>
        </div>
      </div>
	  
	  <!-- footer would go here -->
	  
    </div> <!-- /container -->
  </body>		
</html>
