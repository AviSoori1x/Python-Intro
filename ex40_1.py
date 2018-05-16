#create class, pass along object into it
class Song(object):
    #initialize self, pass self, lyrics to it
    def __init__(self,lyrics):
        #Assign lyrics to self.lyrics
        self.lyrics = lyrics
    #function that takes lyrics from above and prints line by line
    def sing_me_a_song(self):
        #prints each line item, one after the other
        for line in self.lyrics:
            print(line)
#Instantiate five song objects
happy_bday = Song(["Happy Birthday to you", "I don't want to get sued", "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family", "With pockets full of shells"])

Johny_B_Good = Song(["There used to live a boy named","Johny B. Good"])

Party_up= Song(["Ya'll go make me lose my mind","Up in here, Up in here"])

I_like_to = Song(["I like to move it move it","Physically fit, physically quite fit"])

#Call the sing_me_a_song() function of those objects
happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
Johny_B_Good.sing_me_a_song()
Party_up.sing_me_a_song()
I_like_to.sing_me_a_song()
