from .models import Category, Invention
from django.apps import apps

def load_default_data():
  Invention.objects.all().delete()
  Category.objects.all().delete()

  # Load categories
  c1 = Category.objects.create(name="Process")
  c2 = Category.objects.create(name="Machine")
  c3 = Category.objects.create(name="Manufacture")
  c4 = Category.objects.create(name="Composition of Matter")
  c5 = Category.objects.create(name="Improvement")

  Invention.objects.create(
      name="Telephone",
      inventor="Alexander Graham Bell",
      year=1876,
      description="A device for transmitting sound over long distances by connecting telephones or microphones with electrical wires.",
      background="Bell's work on the telephone, which was motivated by his mother's gradual deafness, began while he was a teacher of the deaf.",
      outcome="The telephone revolutionized communication, making it possible for people to talk to each other over long distances.  It also disallows us from escaping our significant others.",
      category=c1
  )

  Invention.objects.create(
      name="Light Bulb",
      inventor="Thomas Edison",
      year=1879,
      description="A device that produces light by passing an electric current through a thin filament, causing it to glow.",
      background="Edison's work on the light bulb was part of his larger efforts to develop a practical electric lighting system.",
      outcome="The light bulb transformed the way people lived and worked, providing reliable indoor lighting for homes and businesses. It also takes away any excuses from getting our IT112 homwork done.",
      category=c5
  )
  Invention.objects.create(
      name="Penicillin",
      inventor="Alexander Fleming",
      year=1928,
      description="An antibiotic produced naturally by certain blue molds, and now usually prepared synthetically, that kills bacteria.",
      background="Fleming accidentally stumbled upon the mold Penicillium notatum, which produced a substance that killed bacteria.",
      outcome="This chance discovery revolutionized medicine by providing an effective treatment for bacterial infections and saving countless lives. Without Penicillin, we wouldn't have a punchline to the joke: 'what do you give a man who has everything?'",
      category=c4
  )

  Invention.objects.create(
      name="Gun Powder",
      inventor="Unknown",
      year=900,
      description="Gunpowder is a mixture of saltpeter, sulfur, and charcoal.",
      background="Initially used in fireworks, it later became a critical component in firearms, cannons, and explosives, transforming warfare and shaping world history.",
      outcome="Provides the chemical foundation for projectile weapons from guns for hunting to cannons used in modern warfare. Without gun powder, we would not be able to binge watch Duck Dynasty.",
      category=c4
  )
  Invention.objects.create(
      name="Airplane",
      inventor="Orville & Wilbur Wright",
      year=1903,
      description="An airplane is a fixed-wing heavier than air craft, and uses a propeller or a high-velocity jet for aerial travel.",
      background="In 1903, the Wright brothers flew for 12 seconds over a distance of 120 feet at Kitty Hawk, North Carolina. This achievement marked the beginning of modern aviation and transformed transportation and global connectivity",
      outcome="Airplanes allow humans to travel overnight what would have taken months to travel.  They have increased the reach of humanity both for good and bad, as both bombs and aid can be dropped from the same plane. Without airplanes, we would not have the opportunity to be kicked in the back for several hours by a small child.",
      category=c2
  )

  Invention.objects.create(
      name="Printing Press",
      inventor="Johannes Gutenberg",
      year=1440,
      description="A printing press is a machine by which text and images are transferred from movable type to paper or other media by means of ink.",
      background="The printing press revolutionized the spread of knowledge by making the mass production of books and other printed materials possible. Gutenberg's invention democratized access to information, accelerated the spread of ideas and sparked the renaissance.",
      outcome="This innovation significantly increased literacy rates, facilitated the spread of knowledge, and laid the foundation for the modern publishing,  and particularly the self-help, comic book anime industries.",
      category=c3
  )

  Invention.objects.create(
      name="Steam Engine",
      inventor="Thomas Newcomen",
      year=1712,
      description="A heat engine that performs mechanical work using the pressure of steam to push a piston or pistons.",
      background="The steam engine, played a pivotal role in the Industrial Revolution. Steam engines powered factories, locomotives, and ships, driving unprecedented economic growth and urbanization.",
      outcome="Besides still being used for transportation of heavy loads by land in locomotives, it also informs fashion as it has driven the Steam Punk movement.",
      category=c2
  )

  Invention.objects.create(
      name="Internet",
      inventor="Bob Kahn & Vint Cerf + others",
      year=1969,
      description="The Internet (meaning, between networks) provides global connectivity between billions of computers and other electronic devices via electrical and also light guided digital transmissions.",
      background="Kahn & Cerf came up with the Transmission Control Protocol and Internet Protocol (TCP/IP), which is the standard for how information is shared between different networks. Tim Berners-Lee came up with the HTTP protocol and the WWW became available in 1993.",
      outcome="The internet's widespread adoption enables instant access to vast amounts of knowledge, communication across continents, and the rise of digital economies.  It also causes us to look at our mobile phones constantly.",
      category=c2
  )

  Invention.objects.create(
      name="The Computer",
      inventor="Charles Babbage",
      year=1837,
      description="A device for storing and processing data, typically in binary form, according to instructions given to it in a variable program.",
      background="Charles Babbage, an English mechanical engineer and polymath, originated the concept of a programmable computer when he created his difference engine around 1837. The first electronic computer, the ENIAC was created in 1946.",
      outcome="Computers provide mathematical, educational and employment services in a digital format. Computers allow us to perform complex mathematical operations in order to calculations to enable physical and electrical engineering.   Computers also allow us to buy things that land on our porch before we can stop ourselves from making an ill advised purchase.",
      category=c2
  )


  print('Default data loaded successfully.')
