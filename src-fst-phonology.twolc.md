=================================== !
The Lushootseed morphophonological/twolc rules file !
=================================== !

The Lushootseed language is written in lower case only

This transformation, accent loss, will be moved to post dict. 2022-12-25

c U+0313

Lushootseed is written in IPA, there are no upper-case letters

place holders

* %^Red1CV2CiCV:0  qəlb: qiqəlb **rain showers**
* %^Red1CV1toCV2C:0  2-segment to 3-segments with vowel change 
* %^Red1CV1toCV2CPL:0  2-segment to 3-segments with vowel change Plural
* %^Red12323:0  works with Red3 and Red5

* %^Red2CVC:0  3-segment reduplication 

* %^Pen:0  this combines with subsequent RmVow or perhaps RmCns
* %^RmVOW:0  this removes previous vowel or with Pen the penultimate vowel
* %^d2t:0  this devoices d to t specifically

## Symbols that need to be escaped on the lower side (towards twolc):
* **»7**:  Literal »
* **«7**:  Literal «
```
 %[%>%]  - Literal >
 %[%<%]  - Literal <
```
* **%^√:0**: at commence of root

* **%-**:  hyphen

Reduplications are worked with on the basis of the Lushootseed Dictionary by Dawn Bates, Thom Hess and Vi Hilbert. Seattle & London. 1994:xvii

Red1
C V1 => C V1 C V1 
* *s%^√%{p5%}%{p4%}%{p3%}%{p2%}%{p1%}tubš*
* *s000tu0tubš*
* *ʔiɬ%^√%{p5%}%{p4%}%{p3%}%{p2%}%{p1%}t̕isu*
* *ʔiɬ000t̕i0t̕isu*

C V1 => C V1 C ə  
* *s%^√%{p5%}%{p4%}%{p3%}%{p2%}%{p1%}tuləkʷ*
* *s000tu0tələkʷ*
* *%{p5%}%{p4%}%{p3%}%{p2%}%{p1%}yubil*
* *00yu0yəbil*
* *%{p5%}%{p4%}%{p3%}%{p2%}%{p1%}ɬaɬil*
* *00ɬa0ɬəlil*
* *%{p5%}%{p4%}%{p3%}%{p2%}%{p1%}k̓ʷid*
* *00k̓ʷi0k̓ʷəd*

C V1 => C V1 C   
* *%{p5%}%{p4%}%{p3%}%{p2%}%{p1%}pastəd*
* *00pa0p0stəd*
* *s%^√%{p5%}%{p4%}%{p3%}%{p2%}%{p1%}x̌ʷiƛ̕əyʔ*
* *s000x̌ʷi0x̌ʷ0ƛ̕əyʔ*

C ə => C i C   %^Red1CV1toCV2C:
* *%{p5%}%{p4%}%{p3%}%{p2%}%{p1%}ʔəpus%^Red1CV1toCV2C*
* *00ʔi0ʔ0pus0*

C ə => C i C ə
Red 1 qəlb: qiqəlb %^Red1CV2CiCV
* *%{p5%}%{p4%}%{p3%}%{p2%}%{p1%}qəlb%^Red1CV2CiCV*
* *00qi0qəlb0*

**ə:0 in inflection**
* *x̌əd»əd%>sid*
* *x̌əd000%>cid*
* *bəq̓əd^Pen^RmVOW^d2t>əb*
* *bəq̓0t000>əb*

sčətxʷəd+N+Der/Dimin+N+Distr+Nom bear
* *s%^√%{p5%}%{p4%}%{p3%}%{p2%}%{p1%}čətxʷəd%^Red1CV1toCV2CPL*
* *s%^√čiči0č0txʷəd0*

**i:0 in inflection**

**í:0 in inflection**

**ʔ:0 in preceding s**
ʔəɬəd+V+Prf+Der+Der/N+N+Sg+Nom+PxSg2: __eat/syödä__
* *ad<s<ʔu<ʔəɬəd*
* *ad<s<0u<ʔəɬəd*

**u:0 in preceding ƛ̕**

**%{p2%}:ə in reduplication**
* *%{p5%}%{p4%}%{p3%}%{p2%}%{p1%}bəlups%^Red2CVC*
* *00bəlbəlups0*

**%{p2%}:u in reduplication**

**%{p2%}:i in reduplication**
qəlb+N+Distr+Nom: **rain showers**
* *%{p5%}%{p4%}%{p3%}%{p2%}%{p1%}qəlb%^Red1CV2CiCV*
* *00qi0qəlb0*
pišpiš+N+Distr+Nom: **cat/kissa**
* *%{p5%}%{p4%}%{p3%}%{p2%}%{p1%}pišpiš%^Red2CVC*
* *00pišpišpiš0*

**%{p4%}:i in reduplication**

**%{p2%}:a in reduplication**

**%{p1%}:0**

**%{p2%}:0**

**%{p3%}:0**

**%{p4%}:0**

**%{p5%}:0**

* *ʔu%^√%{p3%}%{p2%}%{p1%}kʷədad%>s*
* *ʔu0000kʷəda0%>c*

**d:0 before s:c**
* *ʔu%^√%{p3%}%{p2%}%{p1%}kʷədad%>cid*
* *ʔu0000kʷəda0%>cid*

**d:t before ə b**
* *bəq̓əd^Pen^RmVOW^d2t>əb*
* *bəq̓0t000>əb*

**%{p1%}:Cx in reduplication**

**%{p3%}:Cx in reduplication**

**%{p5%}:Cx in reduplication**
sčətxʷəd+N+Der/Dimin+N+Distr+Nom bear
* *s%^√%{p5%}%{p4%}%{p3%}%{p2%}%{p1%}čətxʷəd%^Red1CV1toCV2CPL*
* *s%^√čičič0txʷəd0*

liquids

**%{p1%}:l̕ in reduplication**

**%{p1%}:y̓ in reduplication**

**%{p1%}:w̓ in reduplication**

**%{p1%}:ʔ in reduplication**

**%{p1%}:Cx in reduplication**
* *%{p5%}%{p4%}%{p3%}%{p2%}%{p1%}bəlups%^Red2CVC*
* *00bəlbəlups0*

**%{p1%}:Cx in reduplication**

**%{p1%}:Cx in reduplication**

**Cns:0 in reduplication 3 and 5**

* * *

<small>This (part of) documentation was generated from [src/fst/phonology.twolc](https://github.com/giellalt/lang-lut/blob/main/src/fst/phonology.twolc)</small>

---

