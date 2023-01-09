top = """<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
</head>
<body onload="checkTime()">\n"""

name = '<h1>{firstname}, {lastname} ({gender})</h1>\n'

birthdate = '<h2>Birthdate: {birthdate}</h2>\n'

image = '<img src="{source}">\n'

video = """<video controls>
  <source src="{source}" type="video/mp4">
</video>\n"""

bottom = """</body>
<script>
  function checkTime(){
    const today = new Date();
    // reload page at 00:05
    if (today.getHours() == 0 && today.getMinutes() == 5){
      location.reload()
    }
    setTimeout(checkTime, 1000);
  }
</script>
</html>"""