#################################
# author@ Daniel Laden          #
# email@ dthomasladen@gmail.com #
#################################

#This is a test file

f=open("NRC-Emotion-Lexicon-Wordlevel-v0.92.txt", 'r')

example_sentence = "A angry dog was very hateful about the sneezing man"

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
        print(word + " : " + (str)(emotion_dictionary[word]))
        for emotion in emotions:
            emotions[emotion] = emotions[emotion] + emotion_dictionary[word][emotion]

        positivity_rating = positivity_rating + emotion_dictionary[word]["positive"] + emotion_dictionary[word]["negative"]


print(emotions)
print("positive rating : "+(str)(positivity_rating))
