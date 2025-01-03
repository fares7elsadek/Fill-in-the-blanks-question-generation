from app.Model import *
import json

text = """HTML (HyperText Markup Language) serves as the structural backbone of web content, defining elements through tags such as <div>, <p>, and <header>.
HTML5, the latest iteration, introduced semantic elements like <article> and <aside>, APIs for offline storage, and multimedia support through <audio>
and <video> tags. CSS (Cascading Style Sheets) manages the presentation layer, allowing precise control over typography, spacing, and layouts. CSS3
extended its capabilities with pseudo-classes, media queries for responsive design, and advanced features like Flexbox, Grid, and keyframe-based
animations. JavaScript (JS), a versatile programming language, enables interactivity by manipulating the DOM (Document Object Model), handling events,
and incorporating asynchronous operations via promises and async/await. Bootstrap, a powerful CSS and JS framework, streamlines web development with a
mobile-first grid system, customizable components like modals and carousels, and extensive utility classes, fostering rapid, responsive design."""


app = FillInTheBlankModel(text)
output = app.get_fill_in_the_blanks()

print(json.dumps(output,indent=4))