from InquirerPy import inquirer 
from InquirerPy import utils

name = inquirer.text(message="What's your name:").execute()

fav_lang = inquirer.select( message="What's your favourite programming language:", choices=["Go", "Python", "Rust", "JavaScript"], style=utils.get_style(style={"questionma rk": "#800000", "answer": "#008000"}, style_override=True)).execute()

confirm = inquirer.confirm (message="Confirm?").execute()