
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

from database_setup import SportCategory, Base, SportItem

engine = create_engine('sqlite:///catalogapp.db')
engine.text_factory = str
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Category for Soccer
sportcategory1 = SportCategory(name="Soccer")

session.add(sportcategory1)
session.commit()

sportItem1 = SportItem(name = "Shin Guard", description = "A shin guard or shin pad is a piece of equipment worn on the front of a players shin to protect them from injury. These are commonly used in sports including association football, baseball, ice hockey, field hockey, lacrosse, rugby, cricket, and other sports. This is due to either being required by the rules of the sport or worn voluntarily by the participants for protective measures.",
                     time = datetime.utcnow(), sport_category = sportcategory1)

session.add(sportItem1)
session.commit()

sportItem2 = SportItem(name = "Soccer Ball", description = "A football, soccer ball, or association football ball is the ball used in the sport of association football. The name of the ball varies according to whether the sport is called football, soccer, or association football. The ball's spherical shape, as well as its size, weight, and material composition, are specified by Law 2 of the Laws of the Game maintained by the International Football Association Board. Additional, more stringent, standards are specified by FIFA and subordinate governing bodies for the balls used in the competitions they sanction.",
                     time = datetime.utcnow(), sport_category = sportcategory1)

session.add(sportItem2)
session.commit()

sportItem3 = SportItem(name = "Cleats", description = "Football boots, called cleats or soccer shoes in North America, are an item of footwear worn when playing football. Those designed for grass pitches have studs on the outsole to aid grip. From simple and humble beginnings football boots have come a long way and today find themselves subject to much research, development, sponsorship and marketing at the heart of a multi-national global industry. Modern boots are not truly boots in that they do not cover the ankle.",
                     time = datetime.utcnow(), sport_category = sportcategory1)

session.add(sportItem3)
session.commit()

# Category for Basketball
sportcategory2 = SportCategory(name="Basketball")

session.add(sportcategory2)
session.commit()

sportItem1 = SportItem(name = "Ball", description = "A basketball is a spherical inflated ball used in a game of basketball. Basketballs typically range in size from very small promotional items only a few inches in diameter to extra large balls nearly a foot in diameter used in training exercises to increase the skill of players. The standard size of a basketball in the NBA is 9.5 to 9.85 inches (24.1 to 25.0 cm) in diameter.",
                     time = datetime.utcnow(), sport_category = sportcategory2)

session.add(sportItem1)
session.commit()

sportItem2 = SportItem(name = "Backboard", description = "A backboard is a piece of basketball equipment. It is a raised vertical board with a basket attached. It is made of a flat, rigid piece of material, often Plexiglas. It is usually rectangular as used in NBA, NCAA and international basketball. But many backboards may be oval or a fan-shape, particularly in non-professional games.",
                     time = datetime.utcnow(), sport_category = sportcategory2)

session.add(sportItem2)
session.commit()

# Category for Baseball
sportcategory1 = SportCategory(name="Baseball")

session.add(sportcategory1)
session.commit()

sportItem1 = SportItem(name = "Ball", description = "A baseball is a ball used in the sport of the same name, baseball. The ball features a rubber or cork center, wrapped in yarn, and covered, in the words of the Official Baseball Rules with two strips of white horsehide or cowhide, tightly stitched together.",
                     time = datetime.utcnow(), sport_category = sportcategory1)

session.add(sportItem1)
session.commit()

sportItem2 = SportItem(name = "Bat", description = "A baseball bat is a smooth wooden or metal club used in the sport of baseball to hit the ball after it is thrown by the pitcher. By regulation it may be no more than 2.75 inches in diameter at the thickest part and no more than 42 inches (1,100 mm) long. Although historically bats approaching 3 pounds (1.4 kg) were swung,[1] today bats of 33 ounces (0.94 kg) are common, topping out at 34 ounces (0.96 kg) to 36 ounces (1.0 kg).",
                     time = datetime.utcnow(), sport_category = sportcategory1)

session.add(sportItem2)
session.commit()


sportItem3 = SportItem(name = "Cap", description = "A baseball cap is a type of soft cap with a rounded crown and a stiff peak projecting in front. The front of the cap typically contains designs or logos of sports teams (namely baseball teams, or names of relevant companies, when used as a commercial marketing technique). The back of the cap may be fitted to the wearer's head size or it may have a plastic, Velcro, or elastic adjuster so that it can be quickly adjusted to fit different wearers. The baseball cap is a part of the traditional baseball uniform worn by players, with the brim pointing forward to shield the eyes from the sun. The cap is often seen in everyday casual wear.",
                     time = datetime.utcnow(), sport_category = sportcategory1)

session.add(sportItem3)
session.commit()

sportItem4 = SportItem(name = "Glove", description = "A baseball glove or mitt is a large leather glove worn by baseball players of the defending team which assist players in catching and fielding balls hit by a batter or thrown by a teammate.",
                     time = datetime.utcnow(), sport_category = sportcategory1)

session.add(sportItem4)
session.commit()

# Category for Hockey
sportcategory2 = SportCategory(name="Hockey")

session.add(sportcategory2)
session.commit()

sportItem1 = SportItem(name = "Ice Skate", description = "Ice skates are boots with blades attached to the bottom, used to propel the bearer across a sheet of ice while ice skating.",
                     time = datetime.utcnow(), sport_category = sportcategory2)

session.add(sportItem1)
session.commit()

sportItem2 = SportItem(name = "Hockey Stick", description = "A hockey stick is a piece of equipment used in field hockey, ice hockey , roller hockey or underwater hockey to move the ball or puck.",
                     time = datetime.utcnow(), sport_category = sportcategory2)

session.add(sportItem2)
session.commit()


sportItem3 = SportItem(name = "Hockey Puck", description = "A hockey puck is a disk made of vulcanized rubber serves the same functions in various games as a ball does in ball games. The best-known use of pucks is in ice hockey, a major international sport.",
                     time = datetime.utcnow(), sport_category = sportcategory2)

session.add(sportItem3)
session.commit()

sportItem4 = SportItem(name = "Hockey Helmet", description = "A hockey helmet is worn by players of ice hockey and inline hockey to help protect the head from potential injury when hit by the puck, sticks, skates, boards, other players, or the ice.",
                     time = datetime.utcnow(), sport_category = sportcategory2)

session.add(sportItem4)
session.commit()


# Category for American Football
sportcategory2 = SportCategory(name="American Football")

session.add(sportcategory2)
session.commit()

sportItem1 = SportItem(name = "Football Helmet", description = "The football helmet is a piece of protective equipment used mainly in American football and Canadian football. It consists of a hard plastic shell with thick padding on the inside, a face mask made of one or more plastic-coated metal bars, and a chinstrap. Each position has a different type of face mask to balance protection and visibility, and some players add polycarbonate visors to their helmets, which are used to protect their eyes from glare and impacts. Helmets are a requirement at all levels of organized football, except for non-tackle variations such as flag football. Although they are protective, players can and do still suffer head injuries such as concussions.",
                     time = datetime.utcnow(), sport_category = sportcategory2)

session.add(sportItem1)
session.commit()

sportItem2 = SportItem(name = "Eyeshield", description = "An eyeshield is a piece of football equipment. It is a visor that attaches to the helmet of a player to protect the eyes. It leaves the mouth exposed and covers the eyes and nose. Only clear eyeshields are allowed in high school football. On the college level, a tinted eyeshield may be used if the player has eye problems. The NFL requires a waiver by the trainer and a doctor to wear tinted or reflective visors.",
                     time = datetime.utcnow(), sport_category = sportcategory1)

session.add(sportItem2)
session.commit()


sportItem3 = SportItem(name = "Shoulder Pads", description = "Shoulder pads are a piece of protective equipment used in many contact sports such as American football, Canadian football, lacrosse and hockey. Most modern shoulder pads consist of a shock absorbing foam material with a hard plastic outer covering. The pieces are usually secured by rivets or strings that the user can tie to adjust the size. Allegedly Pop Warner first had his players wear them.",
                     time = datetime.utcnow(), sport_category = sportcategory2)

session.add(sportItem3)
session.commit()

sportItem4 = SportItem(name = "Mouthguard", description = "A mouthguard is a protective device for the mouth that covers the teeth and gums to prevent and reduce injury to the teeth, arches, lips and gums. A mouthguard is most often used to prevent injury in contact sports, as a treatment for bruxism or TMD, or as part of certain dental procedures, such as tooth bleaching. Depending on application, it may also be called a mouth protector, mouth piece, gumshield, gumguard, nightguard, occlusal splint, bite splint, or bite plane.",
                     time = datetime.utcnow(), sport_category = sportcategory2)

session.add(sportItem4)
session.commit()




print "added sport items!"
