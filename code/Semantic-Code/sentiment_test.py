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

creepypasta = """It’s official: I’m an old man.

For the last couple years, I’ve comforted myself by saying I’m in my “early 70s,” but math is simple and unforgiving. Today is my 75th birthday, and God, the years do fly.

I’m not here for your well wishes; this is hardly a milestone I’m excited about. I’m glad to still be here, of course, but I find I have less and less to live for with every passing year. My bones ache, my kids live far away, and the other side of my bed has been empty for just over eight months now. In fact, once I cast my vote against that goddamned Trump this November, I may have nothing to live for at all.

So spare me your “happy birthdays” and your congratulations, if you please. I’m here because I have a story for you, and it’s one I’ve never told before. I used to think I kept it inside because it was silly, or maybe because nobody would believe it. I’ve found, though, that the older you grow, the more exhausting it becomes to lie to yourself. If I’m being perfectly honest, I’ve never told anybody this story because it scares me, almost to death.

But death seems friendlier than it used to, so listen close.

The year was 1950; the setting a small town in Maine. I was a boy of nine, rather small for my age, with only one friend in the world to speak of—and his family, seemingly on a whim, decided to move 2,000 miles away. It was shaping up to be the worst summer of my life.

My pop wasn’t around and my mom was a chore-whore—boy, was I proud of myself when I came up with that one—so I wasn’t apt to hang around the house. With some hesitation, I decided the public library was the place to be that summer. The library’s collection of books, particularly children’s books, was meager to say the least. But within the walls of that miserly structure, I would find no undone chores, no nagging mother (God rest her soul), and perhaps most importantly, no other children with whom I would be expected to associate. I was the only kid with a low enough social status to spend his precious days of freedom sulking amid the bookshelves, and that was just fine with me.

The first half of my summer was even more dreadful than I had imagined it would be. I would sleep in until 10, do my chores, and then ride my bike to the library (and by bike, I mean rusty log of shit attached to a pair of wheels). Once there, I would split my time between unintentionally annoying the elderly patrons and deliberately doing so. One pleasant lady actually interrupted my incessant tongue-clicking to hiss a “shut the fuck up!” at me—the first time I ever heard a grownup use The F Word. Big fuckin’ deal, I know, but in those days it was unheard of.

The dreary days turned to woeful weeks. I had actually begun praying for school to start again—until I discovered the basement. I could have sworn I’d roamed every inch of that library, but one day, in the far corner behind the foreign language collection I stumbled across a small wooden door I had never seen before. That was where it all began.

The door was windowless and made from oak that looked far older than the wall in which it rested. It had a knob of black metal that quite literally looked ancient—I wouldn’t have been surprised to learn it was crafted in the 17th century. Engraved on the knob was what appeared to be a single footprint. I had the sense that whatever lay beyond this door was forbidden to me, and therefore probably the most interesting thing I would encounter all summer. I quickly glanced around to make sure nobody was watching me, then turned the heavy knob, slipped behind the door, and shut it.

There was nothing; only darkness. I took a couple of steps and then stopped, unnerved by the totality of the shadow which surrounded me. I waved my hands in front of me in an attempt to find a wall or a shelf or anything to hold on to. What I actually found was far more subtle—a small string, dangling from above—but far more useful. I grabbed it firmly and pulled it down.

Back in the day, lots of lightbulbs were operated with strings, and this was one of them. My surroundings were instantly illuminated. I was standing on a small, dusty platform that looked as though it hadn’t seen life in quite some time. To my left was a crickety-ass spiral staircase, made of wood and appearing ready to collapse at any second. The bulb was the only source of light in the room, and it was feeble, so when I peered over the railing to see what lay below, the bottom of the staircase dissolved into the darkness.

I was beginning to feel scared. This place—wherever I was—seemed to have no business in a town library. It was as though I were in a completely different building. But no nine-year-old likes to let a mystery go unsolved. Looking back, I wish I could tell my prepubescent self to turn around, go back, do anything else besides descending that staircase. “You’ll be spared a lot of sleepless nights,” I’d say. But, of course, I didn’t know that then—and I may not have listened even if I had. So instead of turning back, I took a deep breath, gripped the railing, and glared resolutely forward as I began my descent.

The wood on the railing was dry and covered with splinters. I immediately let go, holding my hands out for balance as I carefully traversed the staircase. It was (or at least seemed) very long, and with only the dim glow from the string-bulb far above me, my heart pounded mercilessly in the darkness. Even kids can sense when something isn’t right, I think—they just don’t always give a shit.

By the time my feet reached the cement floor at the bottom, the light from the bulb above was very nearly a memory. But there was a new light source, and God, I’ll never forget it. Directly in front of me was a door, massive, and a deep shade of red. The light was coming from behind the door, and it shone out in thin lines from all four sides—a sinister, dimly glowing rectangle. For the second time, I took a deep breath and went through a door I shouldn’t have.

In contrast to the dank room I entered from, the room behind the door was blinding. When my eyes adjusted, what I saw nearly took my breath away.

It was a library. The most perfect library imaginable.

I gaped in wonder as I stepped, almost reverently, further into the room. It was beautiful. It was smaller than the library above, much smaller, but it seemed to be almost tailor-made for me. The shelves were packed with brightly colored titles, both armchairs in the middle of the room were exquisitely comfortable, and the smell—my God, the smell—was simply unbelievable. Sort of a mixture of citrus and pine. I simply can’t do it justice with words, so I’ll suffice it to say that I’ve never smelled anything better. Not in my 75 years.

What was this room? Why had I never heard of it before? Why was nobody else here? Those were the questions I should have been asking. But I was intoxicated. As I gazed around at all the books and basked in the smell of paradise, I could only form one thought: I will never be bored again.

In truth, boredom only hid from me for three years. It was on my 12th birthday, 63 years ago to this day, that everything changed.

Before that day, I visited my basement sanctuary as often as I could—usually several times a week. I never saw another soul down there, yet strangely remained free of suspicion. I never removed a book from that room, but instead would pick up a particular volume wherever I had stopped reading during my previous visit. I sat, always in the same deep purple armchair, and always leaving its twin barren and directly across from myself. That armchair was mine, the other was—well, I suppose I couldn’t have articulated it then much better than I can now. But it wasn’t mine, that’s for damn sure.

On my twelfth birthday, I arrived later than usual. My mom had invited a couple classmates and some cousins over to our house to celebrate, a gesture which I found more tedious than touching—really, I just wanted to spend my birthday sitting and reading and smelling paradise. Eventually, our guests went home, and I made it to the library about fifteen minutes before closing time. That didn’t matter; the workers never checked down there before they locked up. I was free to stay as late as I wished. This particular night, I was devouring the final chapters of an epic adventure; knights, swords, dragons, and the like. I didn’t smell it until I read the final words and closed the book.

The once exquisite aroma of that room had turned sour. I sat for a moment, unsettled. Objectively, I could recognize that the smell was actually the same as it had been before—that mixture of citrus and pine. I just perceived it differently, and I didn’t like it anymore. It was the nasal version of an optical illusion; you know, the one that looks like a young woman glancing backward, but all of a sudden you see that it’s really an old woman facing toward you? You can’t unsee that, and I couldn’t unsmell this. The spell was broken.

The odor also seemed, for the first time, to be coming from somewhere specific. With a fair amount of trepidation, I stalked around the room, sniffing the air like a crazed canine until I came to a shelf near the back. The shelf was perfectly normal, with the exception of one title—a large, leatherbound cover of solid faded maroon, with one striking black footprint at the top of the spine. This was the source of the smell. I opened the front cover, and saw one sentence scrawled neatly in blood-red ink atop the first page:

Rest your sorrows down, friend, and leave them where they lie.

I stared at this sentence, mesmerized, as I began to retreat to my chair. I turned a page. Blank. The smell became stronger. Another page, blank, and the smell grew stronger still. I stopped for a moment, suppressed a gag, and continued walking. Then, as I neared the armchairs, I turned one final page—and there, in the same sinister print, was the last thing I expected to see: my own name. I dropped the book. I began to sprint toward the door, but as I shifted my gaze forward, my heart leapt to my throat and I stopped in my tracks.

The empty chair wasn’t empty anymore.

An aged man in a suit sat before me, one leg crossed over the other, contemplating me with piercing gray eyes and a light smirk. This was all too much. I fell to my knees and expelled the contents of my stomach onto the carpet. I wiped my mouth, staring at my vomit, when I heard the man let out a chuckle.

I stared at him disbelievingly. “Who are you?” I asked, panic in my voice.

The man leapt to his feet, grabbed me gently by the shoulders, and helped me to my chair. He sat, once again, in his own. “I fear we got off to a bad start,” he said, glancing at the pile of sick on the carpet. “The smell . . . it does take some getting used to.”

“Who are you?” I repeated.

“Tonight, you will know hardship like you’ve never before known,” he said. “I come as a friend, offering you refuge from it, and from all other storms which lie ahead.”

I wanted nothing more than to leave at that moment, but I remained seated. I asked him what he was talking about.

“Your mother is dead, my boy. By her own hand, in her kitchen. The scene is gruesome, I must admit,” he said in sorrowful tones, but was there a playful glint in his eye? “Surely you wish to avoid this path. I can show you a safer one.”

My blood ran cold at the horrors this man spoke of, but I did not believe him. “What do you want with me?” I demanded, trying to sound braver than I felt. He laughed, an old, raspy yelp that seemed to shake him to his bones.

“Nothing but your friendship, dear boy,” he said. Then, sensing I found his answer inadequate, he expounded. “I want you to come on a journey with me. My work is noble and you will make a fine apprentice. And maybe, when I’m done”—he sighed tiredly, running his bony fingers through his thin white hair—“maybe then, my work can be yours.”

I stood up, shuffling toward the door but never breaking his gaze. “You’re crazy,” I told him. “My mom isn’t dead. She’s not.”

“See for yourself, if you must,” he said, gesturing toward the door. I threw him a contemptuous glare and bolted for the exit. As my hand closed around the knob, he said my name softly. In spite of myself, I turned around.

“Your road won’t be easy, friend. If it ever becomes too much for you, and I mean ever,” he said, pausing to sweep his hand over the room, “you know where to find me.”

I slammed the door behind me and took the decrepit stairs two at a time. I exited the library, clambered onto my bike, and high-tailed it home. The front door was wide open. I dismounted, leaving my bike in a heap on the ground, and approached the house cautiously. The old man was lying—he must have been. Still, tears began to sting my eyes. Heart pounding, I stepped inside and called for my mother. I heard no answer, so I turned into the kitchen.

To this day, I don’t know why she did it.

I’ve lived in that small town in Maine my entire life, although I’ve kept mostly clear of the public library. Once, in my late 20s, I summoned the courage to step inside. Life was good at that time, and my fear had begun to morph into idle curiosity. Where the door to my basement sanctuary once stood was only a blank wall. I asked the librarian what had become of that basement, though in my heart I knew the answer. There was no basement, she said. There had never been a basement. In fact, if she had her facts correctly, city zoning ordinances prohibited a basement in the area.

I’ve been haunted by that sickly-sweet smell, that poisonous blend of citrus and pine, ever since that long ago birthday. When I saw my mother in the kitchen that day, collapsed in a pool of her own blood, I smelled it. When a man claiming to be my father knocked on my college apartment door, begged me for money and beat me to within an inch of my life when I refused, I smelled it. When my wife miscarried our second child, I smelled it, and again when she miscarried our fourth. When our oldest son got behind the wheel of the family Buick completely shitfaced and got his girlfriend killed, I smelled it.

I began to smell it periodically as my wife became sick. She died late last year, and now, I’m alone for the first time in more than half a century. Now, I smell it every day, and it feels like an invitation.

A few months ago, I went back to the library and the small oak door with the ancient handle was there—right where it used to be. My evening walk has brought me past that library every day since, but I haven’t gone inside. Maybe tonight I will. I’m frightened to die, yes, but lately I’m even more frightened to keep living. The old man was right—my road hasn’t been easy, and I doubt it will get any easier.

Rest your sorrows down, friend, and leave them where they lie.

He promised relief. A refuge, he said. Was he right about that too? There’s only one way to find out. After all, I still know where to find him. """

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

gummy_bears = """This is a cautionary tale and - unlike most of the other reviews on this product - this is a true story and its authenticity can be qualified by a small news item that appeared in the Toronto Star's local news section during the month of April in 2013, much to my chagrin.

I would consider myself a prudent man. Not given to bouts of outspokenness or craving attention, and certainly not one to rock the boat. On any given day I can be found reading a crime novel on a park bench in the middle of the city, soaking in the opulence of nature while nibbling on my tuna fish sandwiches and fending off the voracious gulls and squirrels that threaten to spoil my repose. This is me. Law-abiding and introspective. Which is why it came as a shock to me to find myself incarcerated because of the Devil's Confectionery, Satan's Sweetmeat, Lucifer's Lozenges - the horror that is known as 'Haribo Sugar Free Gummy Bears".

I'll set the scene: It was late winter / early spring in Toronto and the city had just been digging itself out from a late season snow-storm. I was heading to Pearson International Airport for a redeye flight to Amsterdam in order to give the Dutch arm of our company some training on the new software that had been installed (I'm deliberately being vague to prevent my place of work from being linked in any way to the incident that occurred). I had just finished packing, checked the time and found I was running late, my flight was at 7:10 PM and it was now almost 5:00 PM. Cursing softly, I ran out to the car and threw my bags in the trunk, hitting the gas a little harder than usual in my haste to make it to the Long Term Parking Lot as soon as possible. Luckily traffic was light on the 401 and I made it to the airport in record time, but knew that my chances of making the flight were still at risk if I didn't use my time wisely.

I hadn't eaten since lunch, and I was feeling a bit hungry, my stomach rumbling loudly in protestation, which caused me to look around at the other travellers rushing past me in the busy terminal, mortified that my bodily noises might be heard by others. I briskly checked my watch and decided that I had enough time to grab a quick snack before going through the baggage check and security, and would get something more substantial once I was checked through security. I spotted a vending machine nestled in a relatively low-traffic corner of the terminal and rushed over, already pulling out my credit-card and mentally assessing what I had a craving for so as to save time interacting with the machine. My eyes scanned the colourful array of confection quickly, coming to rest on a tantalizing, rainbow-coloured bag of gummy bears with the simple white and red logo "Haribo" emblazoned across the bag in what appeared to be a slightly tweaked Helvetica Rounded font.

Now I'd to pause here in the story for a moment to underscore the importance of making proper choices. I was hungry. When you're hungry, you should eat FOOD. FOOD is defined as "a nutritious substance that people consume to maintain life", this is what food is. These days, the definition of the word 'food' has been bastardized and the meaning has been broadened to include veritably any material that can be digested, or rather, chewed and swallowed without causing death or severe illness. "Haribo Sugar Free Gummy Bears" are NOT food. They aren't even from this planet. I imagine their origins being conceived in a boardroom in hell by a top team of Creative Pain Administers, with senior level Demons rubbing their hands together in ghoulish delight as Hell's Chief Chemist slowly lifts the veil on their new creation.

The point here being, I made a very, very, very poor choice. I pushed the button and the vending machine ejected the brightly coloured bag into my awaiting hands. I had always liked gummy bears - they were bright but rather innocuous, they weren't overly sweet so as to become cloying and - of course - each candy came in the visage of a rather happy, docile bear reminiscent of the picture one's mind's eye holds of all anthropomorphic bears from Yogi to Winnie.

The way I figured it, I was taking a bit of a holiday from life, so I could relax my fastidiously regimented daily schedule a little to allow for some frivolity. After all, I was going to be in Amsterdam come morning with 16 hours to kill before I had to be training the Dutch employees, maybe I would take a trip down to one of the Coffee Shops in the Red-Light District and really let my hair down! No, I wouldn't do that. I would see that area of the city from the bus as I went to the hotel where I would eat at the hotel restaurant and drink sparkling water. So I'd better enjoy the gummy bears, my one extravagance to commemorate my break from routine.

I joined the queue in the KLM line, which was mercifully short, most likely because all of the passengers for my flight had already been checked through as the flight was scheduled to depart in an hour. I checked my watch again, frowned, and absent-mindedly opened the bag of "Haribo Sugar Free Gummy Bears" and began to munch on them as the line slowly advanced. To be fair, they tasted fine - just like every other manufacturer's brand of the colourful candy, and they were sugar-free to boot. This is what made the whole incident that followed so baffling - if they had tasted 'off' or 'different' I most likely wouldn't have continued to shovel them into my mouth absent-mindedly while daydreaming about what I would order to eat from room-service in my hotel in Amsterdam.

As I gave the attendant my e-ticket and she weighed my bags, the first of the pains began in my stomach. I thought nothing of it at first, chalking it up to the fact that I needed something more substantial than gummy worms to tackle my hunger, but over the course of the next five-minutes the shooting pain began to come in more rapid succession. At this point, I had my boarding pass printed and rubbing my stomach a little, I proceeded to security. I briefly entertained the thought of trying to find a restroom before going through security, but at that point my discomfort was manageable and I didn't think it was get any worse, certainly not within the amount of time it would take to clear security.

I joined the line and started fishing for my passport to present to the agent checking tickets, I felt a thin sheen of sweat break out on my forehead and underarms, and my features flushed for a moment as a wave of heat washed over me. I didn't pay it much heed as going through security always caused me great anxiety and I chalked it up to pre-flight jitters. It was only as I stood face to face with the agent and handed her my passport and ticket that I had a glimpse of the agony that was about to begin. It felt like time rippled for a moment, as if my consciousness buckled so intense was the pain that fired through my bowels. I grimaced spastically and emitted a low moan, and felt myself take an involuntary step sideways. Stars shot though my head briefly and my vision blurred and then snapped back into focus. The agent was staring at me with slight consternation and asked me if I was alright. I pulled myself together, stood up straight and declared that I was fine, mortified that I had had a lapse of decorum not only in public but at the security clearance in an airport!

As I fumbled off my belt to go through the metal detector, the pain in my stomach increased and I practically had to sit on the floor to take my shoes off, terrified of what would happen if I bent at the middle to do it. It was becoming increasingly more evident to me that this wasn't just a stomach ache. No, this was something much worse. As a child I had had a bout of diarrhea after a trip to Mexico with my family, I remember the feeling of nausea that swept through me before my child self had surrendered to the gas pains and parked myself on the toilet for an hour, s***ting until I felt like I didn't have any bones left. And that was how I was feeling now, with several key differences - the pain was worse, the sense of an impending bowel movement was so formidable it gave me temporary amnesia, and it took all of my will-power, all of it, to clench my butt cheeks together to prevent my sphincter from exploding.

A sudden shock of pain racked my body, and I half wondered if I was going to give birth to a Tasmanian Devil. The crazy, fever-induced image of said cartoon animal chasing Bugs Bunny through the splashy, volcanic s***-kettle that was my stomach, caused me to illicit a short, maniacal bark of laughter as I approached the Metal detector, a wild, distant look in my eyes, sweat now beginning to poor off of my like a long-distance runner in Kenya. The security agent on the other side of the detector shot a quick glance over to her co-worker who narrowed his eyes and made a subtle movement towards his holster. My breathing became uneven as I entered the metal detector and I realized with alarm that I had taken off my socks without even registering it, and one of my shirt tails was untucked at the front. I held my breath, my eyes bulging dangerously from my head as the machine scanned me. As I shakily moved forward towards the agent for a pat down, my stomach began to illicit sounds that can only be described as otherworldly. It started off a sort-off bubbling sound heard from afar and grew in pitch and intensity at an alarming rate. My jaw dropped in shock as what I can only describe as the sound of an agonized wailing alley-cat in heat with a persistent Doppler effect added to it's voice emitted from some nether-region of my intestines. The officer's eyes widened in alarm, and she kept her eyes glued to my stomach as she thoroughly patted me down. As she reached my shins, I felt my innards suddenly expand, and plummet towards my rectum. With cat-like reflexes I squeezed my sphincter shut with what seemed like nano-seconds to spare, and I knew, I KNEW that if I didn't get the bathroom immediately I would s*** myself.

With a Herculean effort and all of the strength that I could muster, I forced my buttcheeks together knowing that one false move would open the floodgates. I began to walk like a duck, trying to remain as inconspicuous as possible, not even caring now what other people were seeing in front of them - a disheveled, barefoot 40-year-old business man, red-faced and bulgy-eyed, sweating profusely, shaking slightly and walking without bending his knees. With single-minded intensity I grabbed my carry-on, shoes and socks from out of the plastic tub that had passed the x-ray inspection, and without putting anything back on, I turned on my heels with the intention of finding the nearest restroom and slowly dying there one squirt at a time.

But that's not what happened.

I turned to go and found myself staring at three armed agents who stopped me and asked if I would follow them. "Why, what's the matter?" I stammered, wincing slightly as the act of speech seemed to strain the tenuous and extremely fragile truce I had negotiated between my bowels and the tempest that raged within. "I have to go the bathroom, RIGHT NOW" I pleaded. "Just follow us please", they said, leaving no room for argument. The other travellers clearing the security check stared with curiosity and revulsion at the spectacle unfolding before them, whispering amongst themselves and hurrying to pack up their belongings and get as far away from me as possible, no doubt assuming that the airport had nabbed some sort of domestic terrorist. If I hadn't been feverishly trying to hold back the eruption of Mount Vesuvius, I likely would have died of shame.

With each step I took towards the room that they ushered me into, I felt that my legs would give way. I marvelled at how strong the human will could be. Marvelled at what was essentially patching a hole in the Hoover Dam with bubblegum could actually be sustained indefinitely. Maybe I would make it through this ordeal after all. The room they brought me into was an examination room. I had pretty much stopped registering details of my environment as my consciousness closed off all but the absolutely necessary functions - breathing, ability to walk - but I snapped back to reality when I heard the snap of rubber. The slow dawning of realization poked through my agony and stoic resolve as I turned to face an agent dawning rubber gloves.

"Sir, we are going to perform a cavity search on you", a young fresh-faced agent stated in a firm but emotionless voice. His short-cropped, blond hair was immaculate and for a crazy moment I wondered if he was an actor and this was all some sort of elaborate practical joke done to amuse bored kids watching Youtube. He must have taken my tortured silence for resistance because he looked at me sharply and said "Lower your pants and underwear please, and face the desk". Panic started to grip me in it's icy grasp and the sudden adrenaline threatened to destroy my sphincters bulwarks and rend my anus in two. I inhaled sharply and with a pained gasp I doubled up my efforts to clench my cheeks together. "Sir, please", I begged deferring to this kid in an act of desperation, "I have to go to the bathroom. You can follow me into the stall if you need to but I had some bad "Haribo Sugar Free Gummy Bears" and now I feel like'", but they had stopped listening and smirked at each other, two of the other agents - a tall, dark-haired female and a shorter, balding fat man - looked away from me and I could see them shaking a little as they stifled their laughs. "Sir, face the wall, put your hands on the desk and spread your cheeks" the young agent stated, a lop-sided grin on his face. "But'", I began to protest, and then a fresh shock of pain forced me to stop and lean on the table for support as an ungodly howling rose from my stomach, something between the dying moans of a Wholly Mammoth, and the sound of bubble-wrap popping underwater. I exhaled shakily and my focus began to narrow, as I rallied for the final battle. Shaking uncontrollably and sweat literally raining down onto the tabletop in from of me, I turned to face the wall and heard a meek childlike voice, pleading from somewhere in the room. "Please", it said, and then again, "Please". From somewhere within me my mind recognized that this sound had issued from me, although my consciousness had now begun to separate from my body and I held my breath and prayed to God for strength.

"He probably has some heroin or something up there that opened up", the female guard said as a part of me that hadn't escaped into the ether yet acknowledged that she was behind me to my left, "probably high as a kite, LOOK at him", she said. The shorter guard agreed with a snort, off to my right.

"Spread your cheeks" the young agent said, his voice directly behind me and lower than the other two, "and bend over".

"Pleasegodpleasegodpleasegodpleasegod", I whispered in a desperate, maniacal mantra, not even aware of my surroundings anymore. I felt like I was lost in an opium fog with half-snatched images and sounds filtering through to create a nonsensical version of reality. Another volley of pain tore through me and I involuntarily leaned forward over the desk, my focus completely narrowed now to a spot on the wall two feet in front of me, a curious imperfection in the what seemed to be white-washed stone wall. It was a dark blotch about five millimetres long and shaped like a smiling bear, a yellow dancing bear. No, a green bear. No, red. It was all the colours of the rainbow. My god, it was beautiful.

It just took something as simple as a slight breeze to trigger Armegeddon. That's all. No trumpets, no fanfare, no fire raining from the heavens, no dogs and cats living together in harmony, no finger on the button, no prophet to predict it, no nothing. As I stared at the rainbow bear smiling and dancing in front of me, my mouth agape, drooling, eyes glazed and blood-shot, face coated with a sheen of sweat, I heard the softest sound, an exhalation from the young agent behind me, and then at the same instant the warm air of his breath feather across my butt cheeks. For just a moment, maybe less, maybe a split second, even a nanosecond, I felt the presence of God there with me in that room as neurons began to misfire at a blinding rate, nerve ending bristled and muscles twitched reflexively. I stood on the brink with one foot hovering over the edge, and then without taking a step, I found myself plummeting.

With a sound like an extra large plastic ketchup bottle being run over by a Mac truck, my sphincter released. The pressure of the blast pushed me hard into the desk and the legs of the desk screeched as they scraped across the floor. My body remained rigid for a moment and I experienced a relief that can only be described as orgasmic in it's purity. My eyes rolled back in my head and my tongue lolled out of my head like a half-retarded dog and I emitted a low, sustained groan that grew in pitch as the filthy torrent pushed its way out of my body. Tremors wracked my body and I must have looked like a fish out of water with an endless stream of s*** firing out of its ass. Other sounds and sensations started to filter in now as my consciousness began to materialize once more. The muffled scream of a dungeon filled with prisoners near death radiated from my stomach, the rushing sound of litres of liquid trying to escape through an aperture too small to accommodate it all at the same time, the omnipresent sound of chunky liquid spattering against a hard surface with great force, the high-pitched screaming of a woman's voice calling out to God, another voice sobbing uncontrollably imploring to "make it stop!!!" and my own ecstatic, monotone wail.

When my ordeal had eventually run its course, I was left panting for breath and wobbly legged, half-crying, half-laughing with relief, barely lucid and feeling as if I had birthed an elephant. My colon felt like someone had poured chile sauce all over it and then sent in a colony of fire ants to eat it. Through my sobs I heard the sound of dripping, like when the sprinklers are eventually turned off after an office fire, or after a thunderstorm when the willow that overhangs a pond continues to rain down long after the sky has stopped. From behind me, the sobbing continued and I heard someone trying to speak into a walkie-talkie but nonsensical words were all that the man could speak, which sounded like the ravings of a lunatic.

With great relief, I slowly pulled myself off the table, legs trembling, my stomach eliciting one last sound, a loud prolonged gas bubbling that eerily resembled a pig orgasm. I slowly turned my head to survey the devastation and in that instant, if I had had a pencil or some other sharp object, I probably would have gouged my eyes out in revulsion. And the smell. The smell was enough to drive a man insane. It was the stench of rotting potatoes mixed with sulphur and ammonia, cooked in a broth of chicken feces and left to age for two weeks in a yeasty stew at the bottom of a French outhouse. After half a whiff of this ghoulish brine, I immediately stopped breathing through my nose but the taste was to remain in the back of my throat for months to come.

The young agent had taken the brunt of the foul witch's brew, and at first I couldn't process what I was seeing. I thought somehow the young blond kid had been spirited away and replaced by a brown Golem, or a ATV rider that had spent the better part of a day driving through every mud puddle he could find after a torrential downpour. With some degree of compartmentalization I came to understand that for some unfathomable reason this kid hadn't moved - or hadn't been able to move - through the entire fecal deluge. He had weathered the entire assault head-on like some sort of hero from Greek Mythology. I had given this poor schmuck a one-man s*** bukkake that would make a Brazillian pornographer retch with disgust, and he was still in the same position he must have been from the moment of first impact. I tried to comprehend how he must be feeling, what he must be going through psychologically, but it became evident very quickly that he had become very broken. No doubt forced so deeply within himself once the firehose has been turned on that there was little to no hope of him ever coming back from it, certainly not without extensive psychotherapy or a lobotomy. I looked beyond his quivering, catatonic crouched form to see a perfect outline of him cutout on the white wall behind him, either side filled in with a dripping, opaque layer of alternately pulpy and runny fecal stew. I noticed two quivering masses at either extremes of the room and realized they were humanoid in form, although the caterwauling that was coming from these broken creatures was just blubbering gibberish. And this was the tableau that was burnt into my mind's eye for eternity.

Needless to say, I missed my flight.

In fact the next week is a blur. I have vague recollections of an army of Hazmat clad figures looming through the brown landscape of the soiled room, the slopping sounds of rubber boats squelching in puddles of fetid detritus, uncontrollable wailing and animal-like sounds issuing from the mouths of creatures that had been traumatized beyond their capacity for being put back together, the complete loss of sensation from my waist down as I was rolled through the room on a waterproof gurney, it's wheels struggling to surf on top of the s***-soaked floor. I spent a week or so in the hospital enclosed in a well ventilated, sealed room, with suited doctor coming in on the hour to monitor my vital signs as they tried to rehydrate my body. I had apparently expelled every available drop of water from my body that was possible to sustain life without for a short period of time. All of my clothes were incinerated in the hospital's crematorium, and the soiled bag of "Haribo Sugar Free Gummy Bears" was never recovered.

This is my story. It is inconceivable to think that this kind of product can be sold legally and be misrepresented as 'food'. I was lucky, I survived. But as for the families of the survivors, and the survivors themselves, they will forever live with the trauma of the events that took place at Pearson International Airport on that snowy day in April 2013."""

lucid_dreams = """No, no, no
I still see your shadows in my room
Can't take back the love that I gave you
It's to the point where I love and I hate you
And I cannot change you so I must replace you (oh)
Easier said than done
I thought you were the one
Listening to my heart instead of my head
You found another one, but
I am the better one
I won't let you forget me
I still see your shadows in my room
Can't take back the love that I gave you
It's to the point where I love and I hate you
And I cannot change you so I must replace you (oh)
Easier said than done
I thought you were the one
Listening to my heart instead of my head
You found another one, but
I am the better one
I won't let you forget me
You left me falling and landing inside my grave
I know that you want me dead (cough)
I take prescriptions to make me feel a-okay
I know it's all in my head
I have these lucid dreams where I can't move a thing
Thinking of you in my bed
You were my everything
Thoughts of a wedding ring
Now I'm just better off dead (coughs)
I'll do it over again
I didn't want it to end
I watch it blow in the wind
I should've listened to my friends
Did this shit in the past
But I want it to last
You were made outta plastic (fake)
I was tangled up in your drastic ways
Who knew evil girls have the prettiest face
You gave me a heart that was full of mistakes
I gave you my heart and you made heart break
You made my heart break
You made my heart ache (I still see your shadows in my room)
You made my heart break
You made my heart ache (can't take back the love that I gave you)
You made my heart break (were made outta plastic fake)
You made my heart ache (I still see your shadows in my room)
You made my heart break again (I was tangled up your drastic ways)
(Who knew evil girls have the prettiest face?)
I still see your shadows in my room
Can't take back the love that I gave you
It's to the point where I love and I hate you
And I cannot change you so I must replace you (oh)
Easier said than done
I thought you were the one
Listening to my heart instead of my head
You found another one, but
I am the better one
I won't let you forget me
I still see your shadows in my room
Can't take back the love that I gave you
It's to the point where I love and I hate you
And I cannot change you so I must replace you (oh)
Easier said than done
I thought you were the one
Listening to my heart instead of my head
You found another one, but
I am the better one
I won't let you forget me
Did this shit in the past but I want it to last
You were made outta plastic (fake)
I was tangled up in your drastic ways
Who knew evil girls have the prettiest face?
Easier said than done
I thought you were
(Instead of my head, you found another)
I won't let you forget me"""

billy = """That's my word! Get up in they face!
Talk your shit! Let your nuts drag!
Nigga, these niggas just runnin' out they fuckin' mouth, man
Follow protocol Blood, get in they fuckin' chest!
(Scum Gang!)
We the fuckin' M.O.B., nigga
These niggas bleed different
We don't bleed nigga
We make niggas bleed, Blood!
TR3YWAY!
These niggas say they heard of me, I ain't heard of you
Get the fuck up out my fucking face, 'fore I murder you
Bitch niggas always jacking Blood, but I know they fu
Whole squad full of fucking killers, I'm a killer too
Sending shots, shots, shots, shots, shots nigga
Everybody get pop, pop, popped nigga
The thing go rrrah, rrrah, rrrah, rrrah, rrrah nigga
We send shots, shots, shots, shots, shots nigga
It's always 6ix9ine this and 6ix9ine that
Niggas on my dick and on my yack
These niggas lookin' for me you could hit my jack
I done dropped my address, y'all know where 6ix9ine at
I don't flock, yeah
Nine to his back like Ibaka
Baka, not nice, with the fuckin' choppa
Pop 'em, scope on the nigga, who shot ya?
Dropped him, somebody call a fucking doctor!
Dick up in the pussy, bet that shit get gushy gushy
She want the whole gang bussin' all in her pussy
I want the drip, drip while I get my dick licked
Lil' sick bitch, lickin' on my dick tip
She a freak ho, fuck her, she on beast mode
Arch your back, put your hands on your knees ho
I'm on beast mode, shoot you through your peep-hole
Said he want smoke, I don't really see it though
These niggas say they heard of me, I ain't heard of you
Get the fuck up out my fucking face, 'fore I murder you
Bitch niggas always jacking Blood, but I know they fu
Whole squad full of fucking killers, I'm a killer too
Sending shots, shots, shots, shots, shots nigga
Everybody get pop, pop, popped nigga
The thing go rrrah, rrrah, rrrah, rrrah, rrrah nigga
We send shots, shots, shots, shots, shots nigga"""

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
print("\nGummy Bears")
sentiment_analysis(gummy_bears)
print("\nLucid Dreams")
sentiment_analysis(lucid_dreams)
print("\nBilly")
sentiment_analysis(billy)
