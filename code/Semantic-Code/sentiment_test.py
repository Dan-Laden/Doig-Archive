#################################
# author@ Daniel Laden          #
# email@ dthomasladen@gmail.com #
#################################

#This is a test file



def sentiment_analysis(example_sentence):
    f=open("NRC-Emotion-Lexicon-Wordlevel-v0.92.txt", 'r')
    active_word = " "
    emotion_dictionary = {}
    for line in f:
        words = line.split()
        empty_dict = {}
        if words[0] != active_word:
            active_word = words[0]
            emotion_dictionary[words[0]] = empty_dict

        emotion_dictionary[words[0]][words[1]] = (int)(words[2])

    example_sentence = example_sentence.split()

    positivity_rating = 0
    emotions = {"anger" : 0, "disgust" : 0, "fear" : 0, "joy" : 0, "sadness" : 0}
    for word in example_sentence:
        if word in emotion_dictionary:
            #print(word + " : " + (str)(emotion_dictionary[word]))
            for emotion in emotions:
                emotions[emotion] = emotions[emotion] + emotion_dictionary[word][emotion]

            positivity_rating = positivity_rating + emotion_dictionary[word]["positive"] - emotion_dictionary[word]["negative"]

    print(emotions)
    print("positive rating : "+(str)(positivity_rating))



wikipedia = """The domestic dog (Canis lupus familiaris when considered a subspecies of the gray wolf or Canis familiaris when considered a distinct species)[4] is a member of the genus Canis (canines), which forms part of the wolf-like canids,[5] and is the most widely abundant terrestrial carnivore.[6][7][8][9][10] The dog and the extant gray wolf are sister taxa[11][12][13] as modern wolves are not closely related to the wolves that were first domesticated,[12][13] which implies that the direct ancestor of the dog is extinct.[14] The dog was the first species to be domesticated[13][15] and has been selectively bred over millennia for various behaviors, sensory capabilities, and physical attributes.[16]

Their long association with humans has led dogs to be uniquely attuned to human behavior[17] and they are able to thrive on a starch-rich diet that would be inadequate for other canid species.[18] New research seems to show that dogs have mutations to equivalent genetic regions in humans where changes are known to trigger high sociability and somewhat reduced intelligence.[19][20] Dogs vary widely in shape, size and colors.[21] Dogs perform many roles for people, such as hunting, herding, pulling loads, protection, assisting police and military, companionship and, more recently, aiding handicapped individuals and therapeutic roles. This influence on human society has given them the sobriquet "man's best friend". """

blog = """Back in 2009, I got my first DSLR camera and started photographing my dachshund, Rocket, as a hobby. I created an Instagram account that exclusively featured him, and in 2017, I started this blog.

Over the years, photography has grown to be a daily activity we both look forward to. It feels like we’re just two great friends working on a project together. He loves to make me happy and when I encourage him, he joyfully lights up and wags his tail.

When shooting indoors, he goes to his “spot” as soon as he sees the camera. Whether I am photographing him with a product or wearing a cute bowtie, he is patient and listens to my every command. I keep the mood positive with lots of praise and treats.

Often, my passion for photography brings us on some great adventures together. Rocket and I have traveled all over the country to spectacular destinations. Photography encourages me to get out and see the world. To hike more, to explore more, to love nature more. It’s mentally and physically stimulating for both Rocket and I and in turn deepens our connection with each other."""

creepypasta = """In the summer of 2013, I found myself driving home alone on highway 902 from a party. It was almost midnight, and needless to say it was pitch black. As was usual at night, I was on edge. I had the radio off, and could hear nothing but the muffle roar of tires on pavement and the dull hum of the engine. I stole a glance into the middle rear view mirror, and saw nothing but darkness through the back window.

I know that I looked backward and saw nothing. I’m sure of it. Just the seemingly endless blackness of the night. I remember it so clearly because not 10 seconds later a car passed me to the left. Headlights on. I had one of those sudden adrenaline rushes like when you think you see a person outside your bedroom window when it’s just a tree, or when you start awake at night with the feeling of falling. Ten seconds earlier, nothing had been behind me. Suddenly, a car. I drove the rest of the way home shivering and knowing something was off.

The next morning, I found two sets of scratches near the back of my van. One was on the left rear, one was on the right. The car was pretty old. They could have been there for months, but that was the first time that I distinctly remembered seeing them.

In hindsight, there are two possibilities for what happened that night. Possibility one. By some glitch in reality, or something paranormal, this other car had somehow appeared behind me within 10 seconds of me checking my mirror. Like some weird ghost crap or something. However, the second option is what makes my blood run cold whenever I consider it.

It didn’t even occur to me until months after the fact, but it makes me dread driving alone at night even more. Possibility two. The car was normal. It had approached me from the rear and passed me to my left. However, something large, and wide, and as black as the night had been clinging to the rear of my car, obscuring my view through the window and leaving deep scratches on the sides.

And I had inadvertently driven it home with me. """

cute_story = """About a year and a half ago I saw this girl across the room while I was at a debate tournament. Now god damn, was she cute as fuck, unfortunately she had a boyfriend at the time. I didn't ask for her number, I didn't go and talk to her. And I slightly regret it now. Flash forward to summer break of that year and I go off to debate camp, where surprise, I see that girl again. Things happen and she ends up being my debate partner for the rest of summer. So I got her number, I started texting her, and then camp ended.

I didn't flirt with her because I knew she was still dating someone, so I just kept it on the DL that I liked her. She eventually broke up with her boyfriend and I helped her out with that. I was there to talk to her every day and such. I started seeing her more and more as the year went on, I went over to her house for a christmas party with her family, I met them all, I got on good terms with her mom and dad. And eventually we just started seeing each other more often. She came to my birthday party, and she had her legs over mine while we were watching a movie.

After hanging out a few times, I asked her to go to a show with me (A live Welcome To Night Vale performance). And she was really excited and said yes right away! This was really awesome and I was feeling on top of the world. We get to the place and its a theater, and so we sit down and get comfortable and stuff like that.

Looking back on this, I kind of cringe but here it goes. I did the old "Yawn and then put your arm around her" trick and it actually worked. She pulled my arm around her and I held her hand. I rested my head on hers, and she rested her head on mine. I took her back home after having a really fun night of doing really cute stuff. I was really tired, and so was she. I looked into her beautiful hazel eyes, and before I left, I kissed her.
"""

medical_horror = """As a paramedic, responded to a call of "traffic accident, baby ejected ". We prepared for the worst we could imagine. Arrive in about 8 minutes, trooper on scene trying to clear the area of bystanders/ gawkers and preserve the scene. He had covered the "baby" with the yellow death-sheet troopers carry in their trunks. Lifted the sheet to check vitals/pronounce death, and it was not a baby, but the top half of the 19 year old girl that was driving the small pickup truck about 50 yards away. She was driving, and arguing with her 19 year old husband who was the passenger. They were doing about 55mph on a two lane road, and met an oncoming truck pulling a doublewide mobile home. She ran under the front corner of the mobile home, cutting her in half. Her bottom half remained in the drivers seat, while her unhurt husband watched as the truck the skidded another 50-60 yards, sideswiping a minivan, sending it into the ditch upside down. When the truck came to rest, her bottom half fell out onto the ground. We also found a trail of ribs from the cab to the bed, and down the pavement to the top half. It looked like a movie set. Her top and bottom looked unhurt, but from mid chest to about pelvis was strung along the road. The husband was absolutely freaking out about what he had just seen. He was babbling incoherently, running around swinging at people, just a mess. A witness who lived right in front of the scene started having chest pains, and had to be transported. We took the husband, and I called medical control and actually got orders to give him iv valuim, something paramedics normally can only give for grand-mal seizures. The driver of the big truck was fine, but was also very very distraught at what he had just witnessed. That was. 16 Years ago and I can still remember pulling up to that scene like it was yesterday. """

weed_story = """Guys my naive mother used my CANNABUTTER to make dinner with. Apparently we were out of real butter and she used mine because she though it was "vegan butter". My entire family just eat chicken made with high quality cannabutter. I have around 45 mins before it kicks in.WHAT DO I DO GUYS?

Edit -Sorry about the typo in the title I was in a hurry.

Edit 2-Guys I know I can just come clean and tell them. I will if it gets to the point where they are freaking out or something. I'm trying very hard to avoid them ever having to know.

Edit 3-No guys I'm not going to record it and embarrass my family for karma.

Edit 4-I think they are starting to feel it. Still haven't told them anything. I think I am in denial about this whole thing.

Edit 5-My mother just asked me if there was anything wrong with my vegan butter. I decided to tell her it was really old, so they will all just think they have food poisoning or something.

Edit 6-I think my sister is asleep .My father is in some kind of trance with a giant smile on his face. He doesn't seem to be freaking out. My mother on the other hand,is going ape shit and wants to go the hospital. My uncle keeps on trying to talk her out of it, ( because no one can drive so we would have to pay for an ambulance).

Edit 7-Wtf guys my uncle is barely affected and laughs his ass off every time he looks at me. I think he knows.

Edit 8-BIG UPDATE.Ok so my uncle definitely knows. He noticed what it was when he ate it,but he didn't say anything about it for whatever fucking reason intill after everyone ate it. He approached my dad about it,Who said he had no idea but that my mom used my "vegan butter". So my uncle told him what was up,so that is why my father has not been freaking out.My father is slightly more liberal about drugs then I thought,apparently he smoked in high school but still didn't recognize the taste. He is the type who likes Ronald Regan and Donald Trump so I'm kinda surprised. My father keeps trying to get pissed and scold at me,but the weed is preventing him from being mad for more then 30 seconds. My sister has locked herself in her room since after dinner so I assume/hope she is just sleeping. My mother on the other hand (Who 100% has never done any drugs, including alcohol/coffee/cigs) has been freaking out pretty bad.She has been having a intense existential crisis. I can get into more details about that later. She is greening out at this point and just threw up. I'm hoping that she puked some of the THC out. But it could have already absorbed into her body idk. My uncle has been doing a pretty great job at talking her down and convincing her to ride it out (She still thinks it is food poisoning)Some of you guys don't understand that my mother CAN NOT KNOW SHE TOOK WEED .It would make the situation 100x worse. I will keep you guys updated if anything interesting happens.

Edit 9-Just to make to clear everything up

1.my sister has been in her room the entire time since after dinner this isn't strange for her so I think she is sleeping

2.My dad knows because my uncle told him.

3.My uncle knows because he is a fucking pothead

4.Mother is feeling better,She is just laying down on her bed at this point. She had some kind of epiphany about how boring her life is and how she wish she never gave up on doing art work etc etc. She got sick for awhile but appears better now.

5.AND FOR THE 1000TH TIME MY MOTHER CAN NOT KNOW SHE TOOK WEED.ME,MY UNCLE,AND MY DAD ALL DECIDED THAT IS AN AWFUL IDEA.SHE HAS NO IDEA WHAT WEED IS.ALL SHE KNOWS ABOUT IT IS FROM REEFER MADNESS ERA SHIT.IT WILL DEFIANTLY FREAK HER OUT WAY WAY WORSE IF SHE KNEW. """


print("Wikipedia")
sentiment_analysis(wikipedia)
print("\nBlog")
sentiment_analysis(blog)
print("\nCreepypasta")
sentiment_analysis(creepypasta)
print("\nCute Story")
sentiment_analysis(cute_story)
print("\nMedical Horror Story")
sentiment_analysis(medical_horror)
print("\nWeed Story")
sentiment_analysis(weed_story)
