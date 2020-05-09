# HOMEWORK 04 

## Assignment: 
You are the new junior member of a data mining consulting firm.  Your newest client has come back with a new request.  They were very happy with what your consulting firm did with their previous request, and would now like to get more granular with the classification of the unknown animals.  They want you to build a classification system to help their field agents classify these new animals as amphibian, arthropod, bird, fish, insect, mammal, or reptile from the observational data they have collected.  
 
You may recall that the client feels their field agents can reliably collect the following observational data: presence of hair, presence of  feathers, if they lay eggs, if they nurse their young with milk, if they are airborne, if they are aquatic, if they are predatory, if they have teeth, if they have a backbone, if they breath air, if they are venomous, if they have fins, the number of legs they have, if they have a tail, if they are domesticated, if they are cat sized, and approximate gestation period. 
 
Your client, audience, can have technical skills that range from introductory (the field agents) to highly skilled (the clients in house scientists).  Keep this in mind when determining what to document and whether to use visualizations or not. 
 
The client has provided a training data set and a test data set of known animals to train your classification system with.  The tranimal-taxonomy-train.csv and the test data set animal-taxonomy-test.csv can be found in Canvas, the company document management system. 
 
Follow the corporate report template to format your work. 
 
 
## The Details: 
 
Create a model using Naive Bayes Classifiers that can classify the unknown animals into the 7 possible Classifications (bird, mammal, reptile... ). 
 
Create a model using ID3 that can classify the unknown animals into the 7 possible Classifications (bird, mammal, reptile... ). 
 
Evaluate the performance of both models using Confusion Matrices and Accuracy and Error rates.  Then select which of the two models should be presented to the client. 

 
## Summary of provided data: 
Number of Attributes: 18 (animal name, 15 Boolean attributes, 2 numerics) Classification (7 classes) 
 
Attribute Information: (name of attribute and type of value domain)    
1. animal name:      Unique for each instance    
2. hair Boolean    
3. feathers Boolean    
4. eggs Boolean    
5. milk Boolean    
6. airborne Boolean    
7. aquatic Boolean    
8. predator Boolean    
9. toothed Boolean   
10. backbone Boolean   
11. breathes Boolean   
12. venomous Boolean   
13. fins Boolean   
14. legs Numeric (set of values: {0,2,4,5,6,8})   
15. tail Boolean   
16. domestic Boolean   
17. catsize Boolean   
18. gestation Numeric (in days)   
19. type Label (amphibian, arthropod, bird, fish, insect, mammal, reptile) 
