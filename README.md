# Birthday Calendar
Display current birthdays. Possible output methods are a html site inside a browser window or a video.
The html page displays the name and optionally a picture and/or a video. The second output method prints out the names
to the screen and plays the video on loop in the background. 

## How to use
Get the executable for your system from the latest [release](https://github.com/philipp-schuetz/birthday-calendar/releases/latest).
If you don't want to use the executable, you can run the program with python. 
```bash
pip install -r requirements.txt
python src/main.py
```
Input your birthdays using a `.csv` or `.json` file ([more info](#input)).
Videos need to be in the .mp4 format and images in `.png`, `.jpg` or `.jpeg` format. The video's sound is muted on playback. 
Put all files you want to use with the program in the same directory as the executable.
To change the output method or further customize your experience, edit `config.json` ([more info](#configuration)). The file is created on first start.
If you use `video` as the output method, you can quit the program by pressing `q` during video playback.

## Input
There are two input methods to choose from, `.csv` and `.json`. The input file using `.json` is more readable but a lot 
longer than the file using `.csv`. The fields for `firstname`, `lastname`, `gender` and `birthdate` are required. The 
fields for `image` and `video` are optional. Here are examples for both input methods:
```json
[
  {
    "firstname": "Abraham",
    "lastname": "Abel",
    "gender": "m",
    "birthdate": "2000-01-11",
    "image": "example.png",
    "video": "example.mp4"
  },
  {
    "firstname": "Beate",
    "lastname": "Bommel",
    "gender": "f",
    "birthdate": "2001-01-12"
  }
]
```
```csv
Abraham,Abel,m,2000-01-11,example.png,example.mp4,
Beate,Bommel,f,2001-01-12,example.mp4,
Conrad,Cicero,n,2002-02-13,example.jpg,
Diether,Dathe,n,2003-03-14,
Ellie,Ecker,f,2004-02-02,
```

## Configuration
The default config generated on first start.
```json
{
  "input_file": "input.json",
  "output_method": "html",
  "lastname_only": false,
  "address_terms": {
    "m": "Mr.",
    "f": "Ms.",
    "n": "Mx."
  },
  "default": {
    "image": "example.png",
    "video": "example.mp4"
  },
  "video_output": {
    "text_start_pos": [20, 20],
    "text_color": [255, 255, 255],
    "font_scale": 1.0,
    "text_spacing_y": 25,
    "text_thickness": 2
  },
  "output_time": {
    "start": "00:00",
    "end": "23:59"
  }
}
```
### Input file
Use either a `.csv` or `.json` file as an input.
```json
"input_file": "input.json"
```
### Output method
Choose between `html` and `video` as the output method.
```json
"output_method": "html"
```
### Lastname only mode
If `lastname_only` is set to `true`, only the last name of each person will be displayed.
`address_terms` then defined the terms used to address the person.
```json
"lastname_only": false,
"address_terms": {
  "m": "Mr.",
  "f": "Ms.",
  "n": "Mx."
}
```
### Default image and video
If no image or video is found for a person, the default image and video will be used.
```json
"default": {
  "image": "example.png",
  "video": "example.mp4"
}
```
### Video output
This section is used for customizing the `video` output method.
`text_start_pos` defines the xy position of the first line of text.
`text_color` defines the color of the text in RGB.
`font_scale` defines the size of the font.
`text_spacing_y` defines the vertical spacing between the lines of text.
`text_thickness` defines the thickness of the letters.
```json
"video_output": {
  "text_start_pos": [20, 20],
  "text_color": [255, 255, 255],
  "font_scale": 1.0,
  "text_spacing_y": 25,
  "text_thickness": 2
}
```

### Output time
`start` and `end` define the time range in which the output is displayed.
```json
"output_time": {
  "start": "00:00",
  "end": "23:59"
}
```

## License
Licensed under the [GPL-3.0](https://github.com/philipp-schuetz/birthday-calendar/blob/main/LICENSE) license.