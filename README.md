# DeepPhilaOD
Predicting Opioid epidemic progression from EMS radio audio

## Inspiration

Philadelphia is one of many locations in the US that is affected by economic inequity.  By July 2018, nearly 3 million low-income Pensylvania residents were enrolled in Medicaid/ CHIP.  Community poverty has been shown to be a risk factor of drug addiction to which the opioid epidemic is linked.  

## What it does

This project models the opioid epidemic progression and predicts its progression through analysis of EMS radio audio, such as on police channels using Broadcastity, to identify incidents of opioid-related calls along with other attributes like location and time.  The proposed predictive model DeepPhilaOD is a deep convolutional neural network that generates predictions of overdoses for certain zip codes.  Prelimary training and testing has resulted in 99.99% accuracy, but only 5 zip code areas were analyzed. 

## How we built it

The deep learning portion of this is based on the pre-trained model called Inceptionv3 by Google.  This pre-trained model has network weights from training on about 1.2 million images, validation on 50,000 images and testing on 100,000 images.  Because this base network is very deep, a considerable number of layers (dense, dropout, convolution, maxpooling,etc) were added for the implementation of transfer learning in Keras.  Although the data is self-generated,the preliminary results indicate a high accuracy.

## Challenges we ran into
First, data.  It was difficult to get examples of police and EMS raw audio files.  Later in the workflow, ideally, the transfer learning model would be trained on data that was used to generate the annual summary figures on Philadelphia's Department of Health, Health Information Portal.

Another significant issue is that there were only 5 zip code regions considered in the training, testing, and evaluation.  It is fairly common to see 47 zip code regions on zip code maps, but there is a total of 87 total zip codes in Philadelphia.  The small number of regions targeted for generating predictions may have been a factor contributing to an artificial inflation of the testing result (nearly all at 100%).

## Accomplishments that we're proud of
We're all first time hackers and first time using API and image-related deep learning!

## What we learned
Lots!

## What's next for DeepPhilaOD?
Although the skeleton of DeepPhilaOD has taken shape, the workflow has yet to be automated.  Future works include filtering the audio transcripts with an embedding network, such as the pre-trained word2vec, to determine whether the indicence is opioid overdose-realated, whether each new dialouge is a new incident, and so on.  Another augmention could be developed for scraping additional attributes from other EMS data that would ideally improve the model's reliability and prediction.

[1] https://www.healthinsurance.org/pennsylvania-medicaid/ <br>
[2] https://www.drugabuse.gov/publications/drugs-brains-behavior-science-addiction/drug-misuse-addiction
