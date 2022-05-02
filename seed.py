from app import db 
from models import Pet 

db.drop_all()
db.create_all()

woofly = Pet(name="Woofly",
             species="Dog",
             photo_url="https://media.istockphoto.com/photos/portrait-red-welsh-corgi-dog-outdoors-in-the-park-on-a-sunny-summer-picture-id1061822700?k=20&m=1061822700&s=612x612&w=0&h=MCzRF2xhYsIsXZSEGmsvBnVUg9zkrxr4GAkI_4-fAvk=",
             age=11,
             notes="Woofly is a sweet boy looking for a lovely home")

porchetta = Pet(name="Porchetta",
             species="Porcupine",
             photo_url="https://i.pinimg.com/originals/06/34/96/0634960a36a54be21b3c62619dbb19c3.jpg",
             age=1,
             notes="Snuggles with an attitude. Can be a prick(ly)")

hanky = Pet(name="Hanky",
             species="Dog",
             photo_url="https://i.ytimg.com/vi/5tV8NHkT7PM/maxresdefault.jpg",
             age=11,
             notes="Literally a puss in boots")

db.session.add_all([woofly, porchetta, hanky])
db.session.commit()