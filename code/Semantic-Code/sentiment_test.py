#################################
# author@ Daniel Laden          #
# email@ dthomasladen@gmail.com #
#################################

#This is a test file



#This function returns the sentiment values for the entered in text
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

    f.close()

    positivity_rating = 0
    emotions = {"fear" : 0,  "anger" : 0, "sadness" : 0, "joy" : 0, "disgust" : 0, "surprise" : 0, "trust" : 0, "anticipation" : 0}
    for word in example_sentence:
        if word in emotion_dictionary:
            #print(word + " : " + (str)(emotion_dictionary[word]))
            for emotion in emotions:
                emotions[emotion] = emotions[emotion] + emotion_dictionary[word][emotion]

            positivity_rating = positivity_rating + emotion_dictionary[word]["positive"] - emotion_dictionary[word]["negative"]


    top_emotion = "fear"
    for emotion in emotions:
        if(emotions[top_emotion]<emotions[emotion]):
            top_emotion = emotion


    if(positivity_rating>0):
        tone = "positive"
    elif(positivity_rating<0):
        tone = "negative"
    else:
        tone = "neutral"

    textural_emotion = tone + " " + top_emotion


    print(textural_emotion)

    return textural_emotion




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

planes = """i’m super big into DCS
it’s the most advanced flight sim on the market
It’s flight physics and handling are second to none. they have real pilots model everything, and you have a fully functioning cockpit and engine, so you actually acquire a technical understanding of how a plane operates
and you learn and learn as you study and it becomes very rewarding as you truly begin to understand why planes like the p51 are so legendary due to its characteristics
it’s beautiful ^^"""

medical_horror2 = """I was taking call one night, and woke up at two in the morning for a "general surgery" call. Pretty vague, but at the time, I lived in a town that had large populations of young military guys and avid meth users, so late-night emergencies were common.

Got to the hospital, where a few more details awaited me -- "Perirectal abscess." For the uninitiated, this means that somewhere in the immediate vicinity of the asshole, there was a pocket of pus that needed draining. Needless to say our entire crew was less than thrilled.

I went down to the Emergency Room to transport the patient, and the only thing the ER nurse said as she handed me the chart was "Have fun with this one." Amongst healthcare professionals, vague statements like that are a bad sign.

My patient was a 314lb Native American woman who barely fit on the stretcher I was transporting her on. She was rolling frantically side to side and moaning in pain, pulling at her clothes and muttering Hail Mary's. I could barely get her name out of her after a few minutes of questioning, so after I confirmed her identity and what we were working on, I figured it was best just to get her to the anesthesiologist so we could knock her out and get this circus started.

She continued her theatrics the entire ten-minute ride to the O.R., nearly falling off the surgical table as we were trying to put her under anesthetic. We see patients like this a lot, though, chronic drug abusers who don't handle pain well and who have used so many drugs that even increased levels of pain medication don't touch simply because of high tolerance levels.

It should be noted, tonight's surgical team was not exactly wet behind the ears. I'd been working in healthcare for several years already, mostly psych and medical settings. I've watched an 88-year-old man tear a 1"-diameter catheter balloon out of his penis while screaming "You'll never make me talk!". I've been attacked by an HIV-positive neo-Nazi. I've seen some shit. The other nurse had been in the OR as a trauma specialist for over ten years; the anesthesiologist had done residency at a Level 1 trauma center, or as we call them, "Knife and Gun Clubs". The surgeon was ex-Army, and averaged about eight words and two facial expressions a week. None of us expected what was about to happen next.

We got the lady off to sleep, put her into the stirrups, and I began washing off the rectal area. It was red and inflamed, a little bit of pus was seeping through, but it was all pretty standard. Her chart had noted that she'd been injecting IV drugs through her perineum, so this was obviously an infection from dirty needles or bad drugs, but overall, it didn't seem to warrant her repeated cries of "Oh Jesus, kill me now."

The surgeon steps up with a scalpel, sinks just the tip in, and at the exact same moment, the patient had a muscle twitch in her diaphragm, and just like that, all hell broke loose.

Unbeknownst to us, the infection had actually tunneled nearly a foot into her abdomen, creating a vast cavern full of pus, rotten tissue, and fecal matter that had seeped outside of her colon. This godforsaken mixture came rocketing out of that little incision like we were recreating the funeral scene from Jane Austen's "Mafia!".

We all wear waterproof gowns, face masks, gloves, hats, the works -- all of which were as helpful was rainboots against a firehose. The bed was in the middle of the room, an easy seven feet from the nearest wall, but by the time we were done, I was still finding bits of rotten flesh pasted against the back wall. As the surgeon continued to advance his blade, the torrent just continued. The patient kept seizing against the ventilator (not uncommon in surgery), and with every muscle contraction, she shot more of this brackish gray-brown fluid out onto the floor until, within minutes, it was seeping into the other nurse's shoes.

I was nearly twelve feet away, jaw dropped open within my surgical mask, watching the second nurse dry-heaving and the surgeon standing on tip-toes to keep this stuff from soaking his socks any further. The smell hit them first. "Oh god, I just threw up in my mask!" The other nurse was out, she tore off her mask and sprinted out of the room, shoulders still heaving. Then it hit me, mouth still wide open, not able to believe the volume of fluid this woman's body contained. It was like getting a great big bite of the despair and apathy that permeated this woman's life. I couldn't fucking breath, my lungs simply refused to pull anymore of that stuff in. The anesthesiologist went down next, an ex-NCAA D1 tailback, his six-foot-two frame shaking as he threw open the door to the OR suite in an attempt to get more air in, letting me glimpse the second nurse still throwing up in the sinks outside the door. Another geyser of pus splashed across the front of the surgeon. The YouTube clip of "David at the dentist" keeps playing in my head -- "Is this real life?"

In all operating rooms, everywhere in the world, regardless of socialized or privatized, secular or religious, big or small, there is one thing the same: Somewhere, there is a bottle of peppermint concentrate. Everyone in the department knows where it is, everyone knows what it is for, and everyone prays to their gods they never have to use it. In times like this, we rub it on the inside of our masks to keep the outside smells at bay long enough to finish the procedure and shower off.

I sprinted to the our central supply, ripping open the drawer where this vial of ambrosia was kept, and was greeted by -- an empty fucking box. The bottle had been emptied and not replaced. Somewhere out there was a godless bastard who had used the last of the peppermint oil, and not replaced a single fucking drop of it. To this day, if I figure out who it was, I'll kill them with my bare hands, but not before cramming their head up the colon of every last meth user I can find, just so we're even.

I darted back into the room with the next best thing I can find -- a vial of Mastisol, which is an adhesive rub we use sometimes for bandaging. It's not as good as peppermint, but considering that over one-third of the floor was now thoroughly coated in what could easily be mistaken for a combination of bovine after-birth and maple syrup, we were out of options.

I started rubbing as much of the Mastisol as I could get on the inside of my mask, just glad to be smelling anything except whatever slimy demon spawn we'd just cut out of this woman. The anesthesiologist grabbed the vial next, dowsing the front of his mask in it so he could stand next to his machines long enough to make sure this woman didn't die on the table. It wasn't until later that we realized that Mastisol can give you a mild high from huffing it like this, but in retrospect, that's probably what got us through.

By this time, the smell had permeated out of our OR suite, and down the forty-foot hallway to the front desk, where the other nurse still sat, eyes bloodshot and watery, clenching her stomach desperately. Our suite looked like the underground river of ooze from Ghostbusters II, except dirty. Oh so dirty.

I stepped back into the OR suite, not wanting to leave the surgeon by himself in case he genuinely needed help. It was like one of those overly-artistic representations of a zombie apocalypse you see on fan-forums. Here's this one guy, in blue surgical garb, standing nearly ankle deep in lumps of dead tissue, fecal matter, and several liters of syrupy infection. He was performing surgery in the swamps of Dagobah, except the swamps had just come out of this woman's ass and there was no Yoda. He and I didn't say a word for the next ten minutes as he scraped the inside of the abscess until all the dead tissue was out, the front of his gown a gruesome mixture of brown and red, his eyes squinted against the stinging vapors originating directly in front of him. I finished my required paperwork as quickly as I could, helped him stuff the recently-vacated opening full of gauze, taped this woman's buttocks closed to hold the dressing for as long as possible, woke her up, and immediately shipped off to the recovery ward.

Until then, I'd only heard of "alcohol showers." Turns out 70% isopropyl alcohol is about the only thing that can even touch a scent like that once its soaked into your skin. It takes four or five bottles to get really clean, but it's worth it. It's probably the only scenario I can honestly endorse drinking a little of it, too.

As we left the locker room, the surgeon and I looked at each other, and he said the only negative sentence I heard him utter in two and a half years of working together:

"That was bad."

The next morning the entire department (a fairly large floor within the hospital) still smelled. The housekeepers told me later that it took them nearly an hour to suction up all of the fluid and debris left behind. The OR suite itself was closed off and quarantined for two more days just to let the smell finally clear out."""

TIFU_story = """Obligatory this happened four years ago or so. I was 13 at the time—17 now. My best friend at the time had a hamster named Indiana Jones. Yes. Indiana Jones. The first day she had purchased Indie when we were around 10 or so, she picked him up out of his cage to pet and hold the little guy in his hand. Indie jumped out of her palm and fell about three or four feet onto the ground, giving himself a limp from there on out. While the original Indiana Jones didn’t have a limp—or was a hamster—we took Indie on many, many adventures.

We would build obstacle courses outside and have Indie navigate them in his hamster ball. Construct massive tube mazes with treats hidden throughout them. Watch little Indie run on his hamster wheel. And on and on. The fun with Indie seemed like it would never end.

One fateful day, my friend announced that Indie was probably going to die soon. I was bummed. I guess when he fell and hurt his leg, he suffered some internal damage that would soon end his life. When the day of Indie’s death came and passed, my friend had put his body in a little cardboard box that we we’re going to take with us on a camping trip with a group of friends and a friend’s mom.

We planned to go on a 3-day trip where we could hangout, do some exploring, and have some fun. We didn’t want the trip to only be full of sadness and sorrow. At least that’s how I would have viewed it.

We were out in the middle of nowhere in the midwest. So it was dark. Dark is an understatement. It was pitch black actually. Our first night out when we set-up camp my friend's mom had freeze dried pre-marinated meat in a ziplock bag to make a stew with.

She asked me to grab it from the back of her jeep. She said it should be in a little cardboard box. I grab the box, pull the ziplock bag out, and dump the contents into our pot sitting on top of the burning camping stove in the middle of our campsite.

After everything had been cooking for awhile, her mom grabs some bowls and begins to use a ladle and pour the stew into bowls for us.

It tastes weird. Really weird.

My friend’s mom comments that there are no bits of meat in her bowl, and we all look down and realize there isn’t any in any of ours. That’s odd. I was the one who put it in there.

Confused, I grab a flashlight and approach the pot. As I look down, right in the middle of the stew, I see the disgustingly dead and grossly cooked body of Indiana Jones. I scream and instinctively kick the pot and stove over, and then watch to my dismay as the contents of the pot spill all over the ground and the lit camping stove begins to ignite my friend’s sleeping bag on fire."""

disney_story = """I have one moment that stands out above all the rest. I was waiting for someone to ask me this question. It's the reason I left a good job as a VIP Tourguide and moved to the Character Department.

I was working City Hall one day when two guests came in with two little girls. One was in a wheel chair and the other one looked like she had just seen death. Both were cut and bruised and the one in the wheelchair had her arm in a cast. The two women were actually nurses from a hospital and were asking for a refund on the girl's tickets, something we avoided doing at all costs. When I asked why they told me the story. The two girls were with their mom and dad at Epcot and on the way home they got into a horrible car accident. The mother was beheaded right in front of them. The father eventually died too but the two girls didn't know that yet. They were from overseas and had no money and no contact information for anyone they knew. They were bringing the tickets back to get the girls some much needed money to help get them back home. My heart absolutely sunk. If you had seen these girls you'd know why. They were truly traumatized. I refunded their tickets and got permission to be their private tour guide for the rest of the day (which they were not expecting). I walked them to the VIP viewing area for the parade which was as far as I could walk them in the costume we used to wear at City Hall. I had to leave them there while I put on my VIP costume. On the way down I pulled out every kid joke I could think of. I was a REALLY good tour guide (I helped write part of it) and I knew how to make kids smile. Nothing worked. These girls were too far gone for that. I left them at the bridge to go change, walked backstage and bawled my eyes out. I just had never seen something so horrible. I was truly affected and it was a terrible feeling of powerlessness not being able to fix the situation. When I came back I brought them to get ice-cream, take them on rides and stuff but they never smiled, not once. The nurses were loving it and were trying to get them into it but it just wasn't working. We went back to the bridge to watch the parade. It was there that I honestly saw true magic. Real magic, not bullshit. I had called the parade department to let them know what was going on and set up a private meet and greet after the parade. As the parade was coming around Liberty Square I told the girls that I had called Mickey and told him all about them. I told them that Mickey asked to meet them after the parade.

The little girl in the wheelchair smiled.

"Really?" she asked. My heart skipped. "Yes, really! He told me to tell you to look out for him in the parade and to follow the float back to City Hall."

The other girl smiled.

"You mean right now?" she asked.

It had worked. They were talking. Not laughing, but talking. It was the first time I had heard them speak. Every single parade performer came up to them on the bridge and told them to look out for Mickey. Every one of them told them that. When Mickey's float came up Mickey (who was attached to a pole at the top of the float) managed to turn her body sideways, look down at the girls and point towards Main Street. That was all it took. The girls were excited now. They had forgotten about death. They were lost in a magical world and I couldn't believe I was watching it unfold in front of my eyes. We followed that float all the way back to City Hall, singing "Mickey Mania" the whole way. Back then, City Hall used to have a VIP lounge behind the desk that was for privacy during difficult situations or to host celebrities. I took them in and showed them the book where all of the autographs were. They were eating it up.

The girl who was Mickey that day got down off her float and without even taking her head off walked up to me backstage and said "Let's go." I walked in with Mickey behind me so I got to see the exact moment the girls met their new friend. They got shy but Mikey was in control now. Those girls met the REAL Mickey Mouse that day. Every single parade character stayed dressed to meet those girls. One by one they'd come in and play a bit then leave. We were in that lounge for over an hour. Mickey stayed in costume the entire time (which is hard to do after a parade). When Mickey finally said goodbye I had two excited girls on my hands that couldn't stop smiling. They talked and talked and talked. We had a wonderful day after that but what I remember most is when we walked by the rose garden, the older one said "Oh, my mommy loves roses! I mean..." and she stopped. I held out my hand and walked her to the gate, picked her up and put her on the other side and said "Pick one!" She looked happy as she picked out her favorite rose. She didn't say anything more and she didn't need to. I said goodbye to the wonderful nurses and the wonderful girls then walked backstage behind the train station. This time I didn't cry. It felt so good to be a part of that. I realized that as much as I liked helping guests at City Hall, the true magic of Disney was in the character department. I auditioned, transferred and never looked back. Thanks for letting me relive this. It was a special day for me."""

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
print("\nPost on Planes")
sentiment_analysis(planes)
print("\nMedical Horror Story 2")
sentiment_analysis(medical_horror2)
print("\nTIFU Story")
sentiment_analysis(TIFU_story)
print("\nDisney Story")
sentiment_analysis(disney_story)
