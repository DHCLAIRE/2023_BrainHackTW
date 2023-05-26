# 2023 Brain Hack School Taiwan
***
### Brainhack Taiwan 2023 Project Progess
##### THE Project
- [x] Using calculated syntactical surprisals from Ngram model as a predictor in ESL speech comprehension analysis

##### To-do list
- [ ] Write the n-gram script ``Ongoing``
- [x] 5/24 (三) 和TA開會  
      1. 介紹ngram計算過程  
      2. my scripts  
      3. 如何融合到TRF (how to interpret the TRF results)
- [ ] Produce TRF
- [ ] Present Project

##### Scripts TO-DO list
###### POS Trigram
- [ ] Calculate the trigram count from tagged corpus(e.g. COCA) = the word frquency from the corpus
- [x] POS tag the testing text files (=UCREL CLAWS_C7 tag)
- [ ] Preprocess the tagged testing text files
- [ ] Segment the testing txt files into trigram unit 
- [ ] Calculate the probability(=surprisal) of the target POS (from the target word)
###### TRF Production
- [ ] Preprocess the MEG data
- [x] Make the predictor pickle file from the surprisal of ngram (see ``POS Trigram`` part)
- [ ] Produce the ngram TRF from the predictor
- [ ] Analyze the ngram TRF (Statistics)


##### THE web of my github.io
- [ ] Brainhack progress??
