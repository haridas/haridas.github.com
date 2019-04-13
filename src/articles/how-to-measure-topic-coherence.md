Title: How to Measure Topic Coherence
Date: 2019-02-26 10:20
Category: data-science
Tags: LDA
Authors: Haridas N

Unsupervised topic modeling algorithms like LDA and NMF produces list of
vocabularies for each topic after the training. These vocabs help human
to assign the subject information of the topic model. So how we measure the
quality of these topic words ?, this problem has to be
addressed in unsupervised topic clustering algorithms like LDA / NMF to
understand models are improving or not.

It's always a challenge to qualitatively measure the goodness of the words
produced by each topic. Usually we take top 10 words ( It's recommended to keep
the top n word count up to 7+/-2 ie; 5 to 9 words appropriate for human to judge
and come up with a topic name using these words)

The methods discussed here are the standard coherence evaluation metrics, based
on Frequentest probabilistic evaluation, TF-IDF, Word2Vec and SVD based
methods, over the top-n words of each topic and the input corpus given into the
LDA model.

The probabilistic models generally measure the co-occurrence of the top-n topic
words in the actual input corpus and the coherence value will be good if the
co-occurrence measure from the top-n words will be higher. See more details of
each method and its conventions used.

>All unsupervised topic clustering algorithms have to address this point before
>going into production, ie; how much usable the topics produced by a given
>method, can human can interpret the meanings of topic and describe the topic
>using top N words ( eg N = 10 ).

Based on this [paper](https://svn.aksw.org/papers/2015/WSDM_Topic_Evaluation/public.pdf) - coherence evaluation can be structured into
4 stages,

1. Segmentation of word subsets
2. Probability Estimation
3. Confirmation Measure
4. Aggregation

### 1. Segmentation of word subsets

In this stage we split the top-n words into pairs, we can do this in multiple
ways to support the Boolean document counting or sliding window based counting
discussed in next sections.

### 2. Probability Estimation methods
<div>
$$

 \begin{array}{l}
 \mathcal{P}_{bd} \ \ \ \ \ \ \ \ \ \ =\ \ \ Boolean\ document\ estimation,\
 count\ only\ onces\ in\ a\ given\ document.\\
 \mathcal{P}_{bp} \ \ \ \ \ \ \ \ \ \ =\ \ Boolean\ paragraph\ estimation,\
 counts\ the\ occurrences\ on\ every\ paragraph.\\
 \mathcal{P}_{bs} \ \ \ \ \ \ \ \ \ \ =\ \ Boolean\ sentence\ estimation,\
 counts\ on\ occurrences\ on\ every\ sentences\ wise.\\
 \mathcal{P}_{sw} \ \ \ \ \ \ \ \ \ =\ \ Sliding\ window\ estimation,\ here\ a\
 window\ of\ size\ N\ has\ been\ used\ to\ move\\
 \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ over\ the\ document\ and\ each\
 window\ is\ considered\ a\ virtual\ document,\ and\\
 \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ do\ \mathcal{P}_{bd} \ counts\
 on\ each\ windows.\\
 \\
 \ P( w_{j} ,\ w_{i}) =\ \ \ \ \#documents\ ( w_{j} ,\ w_{i}) \ co-occures\ /\
 \#\ total\ number\ of\ documents.\\
 \ P( w_{j}) \ \ \ \ \ \ =\ \ \ \ \ \#documents\ w_{j} \ occures\ /\ \#\ total\
 number\ of\ documents\\
 \\
 The\ denominators\ /\ normalization\ term\ of\ the\ joint\ and\ marginal\
 probability\ can\ be\ different\\
 based\ on\ the\ method\ used\ for\ estimate\ the\ same.\ Above\ one\ is\ used\
 if\ \mathcal{P}_{bd} \ is\ the\ estimation\ used.\\
 \\
 For\ other\ estimation\ types\ like\ \mathcal{P}_{np} \ we\ use\ \#\ total\
 number\ of\ paragraph\ as\ the\ normalisation\ term.
 \end{array}

$$
</div>

### 3. Confirmation Measures 

In this phase the actual scoring function is defined, which make uses any of
the segmentation or probabilistic measuring methods described above. Lets see
some of the widely used coherence measuring methods.


##### 3.1 UMass

UMass is the simplest method of all mentioned bellow and compute time is least among
all others.


<div>
$$
 \begin{array}{l}
C_{UMass} \ =\dfrac{1}{^{N} C_{2}} \ \sum ^{N}_{j=2} \ \sum ^{j\ -1}_{i=1} \ log\left(\dfrac{P( w_{j} ,\ w_{i}) \ +\ \epsilon }{P( w_{i})}\right)\\
\\
N=\ \#Top\ words\ from\ a\ Topic.\ eg;\ N=10\\
\\
Here\ the\ P( w_{j} ,\ w_{i}) \ co-occurrence\ is\ calculated\ by\ using\ \ \mathcal{P}_{bd} \ \ method\ mentioned\ above.\ \\
\ \ 
\end{array}
$$
</div>

##### 3.2 UCI

Slightly improved version of UMass, and applying the sliding window based probabilistic
measure.

<div>
$$
 \begin{array}{l}
C_{UCI} \ =\dfrac{1}{^{N} C_{2}} \ \sum ^{N}_{j=2} \ \sum ^{j\ -1}_{i=1} \ log\left(\dfrac{P( w_{j} ,\ w_{i}) \ +\ \epsilon }{P( w_{i}) \ P( w_{j})}\right)\\
\\
N=\ \#Top\ words\ from\ a\ Topic.\ eg;\ N=10\\
\\
Here\ the\ co-occurrence\ is\ calculated\ by\ applying\ the\ sliding\ window\ over\ the\\
text\ document.
\end{array}
$$
</div>


##### 3.3 NPMI - Normalized Point-wise Mutual Information

Measuring the co-occurrence of words as the name suggest. This one is improved version
of PMI, by applying a added normalisation to PMI.

<div>
$$

 \begin{array}{l}
 N=\ \#Top\ words\ from\ a\ Topic.\ eg;\ N=10\\
 \\
 C_{NPMI} \ =\ \dfrac{1}{^{N} C_{2}} \ \sum ^{N}_{j=2} \ \sum ^{j\
 -1}_{i=1}\left( \ \dfrac{\left(\dfrac{log\ ( P( w_{j} ,w_{i})) \ +\ \epsilon
 }{P( w_{j}) \ P( w_{i})}\right)}{-\ log( P( w_{j} ,\ w_{i})) \ +\ \epsilon
 }\right)\\
 \\
 P( w_{j} ,\ w_{i}) \ =\ Frequency\ of\ these\ two\ tokens\ co-occurrence\ on\
 the\ input\ datasets.\ \\
 \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ Here\ we\ apply\ \mathcal{P}_{sw}
 \ method.
 \end{array}
$$
</div>


Outside this 4 stage framework, there are multiple coherence measures available,
we can fit those measures along with above mentioned coherence measuring
framework; even though some parts aren't relevant in some cases. Few of those
measures are listed bellow,

#### 3.4 Word2Vec based similarity score
Here we are making use of the semantic meanings of each words on word2vec vector 
space and finding the cosine similarity between two word vectors.

<div>
$$
\displaystyle \dfrac{1}{^{N} C_{2}} \ \sum ^{N}_{j=2} \ \sum ^{j\ -1}_{i=1} \ similarity( wvi,\ wvj)
$$
</div>

#### 3.5 TF-IDF based improvement for UMass method

Here instead of measuring co-occurrence of two words across the documents, measure
its relevance using tf-idf calculation.

<div>
$$
 \begin{array}{l}
c( t,\ W_{t}) \ -\ Topic\ t\ is\ characterized\ by\ its\ set\ of\ top\ W_{t} \ words.\\
\\
c_{tf-idf}( t,\ W_{t}) \ =\ \sum _{w_{1} ,w_{2} \ \in \ W_{t}} log\ \left(\dfrac{\sum _{d:\ w_{1} ,w_{w} \ \in \ d}( tf-idf( w_{1} ,\ d) \ \times \ tf-idf( w_{2} ,\ d) \ +\ \epsilon )}{\sum _{d:\ w_{1} \ \in \ d} tf-idf( w_{1} ,\ d)}\right)\\
Where;\\
\\
a) \ tf-idf( w_{1} ,\ d) \ =\ tf( w,\ d) \ \times \ idf( w) \ \\
\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ =\ \dfrac{1}{2} \ \dfrac{f( w,\ d)}{max\ _{w^{*} \ \in \ d} \ f\left( \ w^{*} ,\ d\right)} \ \ \times \ log\ (\dfrac{|D|}{|\{d\ \in \ D:\ w\ \in \ d\} |}\\
b) \ f( w,\ d) \ =\ Frequency\ of\ word\ w\ in\ document\ d.\\
c) \ max\ _{w^{*} \ \in \ d} \ f\left( \ w^{*} ,\ d\right) \ =\ Normalise\ it\ with\ max\ frequency\ of\ word\ on\ that\ same\ document.\\
d) \ w^{*} \ \ \neq \ \ w
\end{array}
$$
</div>


#### 3.6 TBuckets

>"we aim at measuring the quality of a single topic and propose a novel approach - TBuckets,
>which groups a topic’s words into thematic groups (which we call buckets).
>The intuition is that if a single large bucket is obtained from a topic, the topic carries a single coherent theme"

Refer [paper](http://www.aclweb.org/anthology/E17-2070)

<div>
$$
 \begin{array}{l}
A\ =\ U{\textstyle \sum V^{T} \ \ \ ;\ SVD\ of\ the\ Matrix\ A}\\
\\
\\
A=\ N\ \times \ D\\
\\
Where:\ N\ \rightarrow \ top\ N\ words\ from\ topic\\
\ \ \ \ \ \ \ \ \ \ \ \ \ \ D\ \rightarrow \ Dimention\ of\ word\ embeddings.\\
\ \ \ \ \ \ \ \ \ \ \ \ \ \ A\ \rightarrow \ Word2Vec\ vectors\ for\ top\ N\ words\ of\ a\ topic.\\
\\
\sum \ \rightarrow \ Captures\ the\ different\ theme\ on\ same\ cluster\ with\ top\ N\ words.\\
\ \ \ \ \ \ \ \ \ \ \ \ \ These\ are\ the\ Buckets\ in\ TBucket\ algorithm.\\
\\
Eg;\ If\ we\ take\ top\ 10\ words\ from\ a\ topic,\ we\ can\ bucket\ them\ under\ major\ categories\ like\\
\ \ \ \ \ \ T_{1} \ =\ \{\ aircraft( 5) ,\ footwear\ ( \ 3) ,\ beverage( 2) \ \} \ \ \\
\ \ \ \ \ \ Higher\ the\ size\ of\ the\ bucket\ compared\ to\ others,\ model\ done\ better\ on\ topic\ identification.\\
\\
To\ allocate\ the\ word\ vectors\ under\ these\ buckets\ ( \ eigenvectors\ ) ,\ instead\ of\ naive\ assignment,\\
use\ Interger\ Linear\ Programming\ or\ Linear\ optimization\ to\ get\ better\ allocation\ and\ reduce\ the\\
fragmentation.
\end{array}
$$
</div>

### 4. Aggregation strategies

All the coherence measures discussed till now mainly deals with per topic level,
to aggregate the measure for the entire model we need to aggregate all the topic 
level scores in to one. Common method applied here is arithmetic mean of topic level
coherence score. Or other type of statistical summary like std or median etc.



<hr/>

### Jaccard Similarity Measure for Model

All the above mentioned measuring mechanisms discuss about coherence of
individual topic and then we are applying standard aggregation over these scores
via simple arithmetic mean. Is there any measure the quality of all the topics
or relationships between them ?

The Jaccard Similarity between topics helps to understand how the topics are
dependent each other. If the similarity is higher means topics are very
dependent each other, otherwise topics are discussing about similar domain ( eg;
automobile ). The key thing to care is, there is know good setting for this
value, it's purely set based on the business requirement and nature of the data.

<div>
$$
 \begin{array}{l}
K\ =\ \#Topics\\
\\
MPJ_{m,\ k} \ =\ \dfrac{1}{^{K} C_{2}} \ \sum ^{K}_{j=2} \ \sum ^{j\ -1}_{i=1} \ \left( \ \dfrac{TD_{i} \ \cap \ TD_{j}}{TD_{i} \ \cup \ TD_{j}}\right)
\end{array}

$$
</div>


Thank you, That's all for now. Hope these heuristics helped you to understand your models well.



    NOTE: This blog entry was orginally published at https://labs.imaginea.com/post/how-to-measure-topic-coherence/
    Location, and republished here with permission.


## References

###### 1. https://svn.aksw.org/papers/2015/WSDM_Topic_Evaluation/public.pdf

###### 2. TBuckets paper http://www.aclweb.org/anthology/E17-2070

###### 3. http://www.cs.loyola.edu/~binkley/papers/icpc14-lda.pdf

###### 4. Gensim Implementation - https://radimrehurek.com/gensim/models/coherencemodel.html 

###### 5. Math equations are built using this site - https://www.mathcha.io/editor/w6PBH0GSWNtDpir3

