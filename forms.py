from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField


class NounForm(FlaskForm):
    Noun_word=StringField('ಪದ')  
    Genders=StringField('ಲಿಂಗ ') 
    Noun_categories=StringField('ನಾಮಪದದ ವರ್ಗ ') 
    submit=SubmitField('ಸೇರಿಸಿ')
    
class VerbForm(FlaskForm):
    Verb_word=StringField('ಪದ') 
    Present_tense=StringField('ವರ್ತಮಾನ ಕಾಲದ ವರ್ಗ ') 
    Future_tense=StringField('ಭವಿಷ್ಯತ್ಕಾಲದ ವರ್ಗ ')
    Past_tense=StringField('ಭೂತಕಾಲದ ವರ್ಗ')
    submit=SubmitField('ಸೇರಿಸಿ')   
    

    
class OtherForm(FlaskForm):
    Other_word=StringField('ಪದ') 
    Other_categories=StringField('ವರ್ಗ') 
    submit=SubmitField('ಸೇರಿಸಿ')