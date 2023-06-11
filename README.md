# 2023 Brain Hack School Taiwan
***

### Brainhack Taiwan 2023 Project Progess  
##### THE Project
- [x] Using calculated syntactical surprisals from Ngram model as a predictor in ESL speech comprehension analysis

##### To-do list
- [x] `Done` Write the n-gram script 
- [x] 5/24 (三) 和TA開會  
      1. 介紹ngram計算過程  
      2. my scripts  
      3. 如何融合到TRF (how to interpret the TRF results)
- [ ] `lack word onset` Produce TRF
- [x] Present Project

##### Scripts TO-DO list
###### POS Trigram
- [ ] `not fully` Calculate the trigram count from tagged corpus(e.g. COCA) = the word frquency from the corpus  
- [x] POS tag the testing text files (=UCREL CLAWS_C7 tag)
- [x] Preprocess the tagged testing text files
- [x] Segment the testing txt files into trigram unit 
- [x] Calculate the probability(=surprisal) of the target POS (from the target word)
###### TRF Production
- [x] Preprocess the MEG data
- [x] Make the predictor pickle file from the surprisal of ngram (see ``POS Trigram`` part)
- [ ] `lack word onset` Produce the ngram TRF from the predictor
- [ ] `lack word onset` Analyze the ngram TRF (Statistics)

