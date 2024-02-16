top = """<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="refresh" content="60">
    <link rel="stylesheet" type="text/css" href="style.css" />
    <title>{title}</title>
</head>
<body onload='autoplay();'>\n"""

person_open = '<div class="person">'

no_bd_open = '<h1>'
no_bd_close = '</h1>\n'

name = '<h1>{firstname} {lastname}</h1>\n'

birthdate = '<h2>Birthdate: {birthdate}</h2>\n'

image = '<img src="{source}">\n'

video = """<video id="video" loop autoplay muted>
  <source src="{source}" type="video/mp4">
</video>\n"""

person_close = '</div>'

bottom = """</body>
<script>
  function autoplay(){
    document.getElementById("video").play();
  }
</script>
</html>"""