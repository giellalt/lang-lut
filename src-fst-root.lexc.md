
# Lushootseed morphological analyser                      !
INTRODUCTION TO MORPHOLOGICAL ANALYSER OF LUSHOOTSEED LANGUAGE.

# Definitions for Multichar_Symbols

## Letters
b̓    
c̓    
č     
č̓    
dᶻ    
gʷ    
ǰ     

k̓    
kʷ    
k̓ʷ   

l̕    
ƛ̕    

m̓    
n̓    

p̓    

q̓    
qʷ    
q̓ʷ   

t̕    
w̓    
y̓    

x̌    
xʷ    
x̌ʷ   

y̓    

ə́    used in coding of dictionary
ə̀   used in coding of dictionary

## Analysis symbols
The morphological analyses of wordforms for the Lushootseed
language are presented in this system in terms of the following symbols.
(It is highly suggested to follow existing standards when adding new tags).

The parts-of-speech are:
*  +N +A +Adv +V                                 
*  +Pron +CS +CC +Adp +Po +Pr +Interj +Pcle +Num 

The parts of speech are further split up into:
*  +Prop +Pers +Dem +Interr +Refl +Recipr +Rel +Indef  
*  +Aux +Cop  

Types of adverbs also include
*  +Deg         this is degree
*  +Manner      with reference to type of adverb
*  +Parenthetic  parenthetic
*  +Qnt	      quantifier
*  +Spat	      spatial
*  +Temp	      temporal
*  +Tot	      total, universal quantifiers

The Usage extents are marked using following tags:
*  +Err/Orth  
*  +Use/-Spell  

Dialect tags:

* **+Dial/-NL** not north Lushootseed
* **+Dial/-SL** not south Lushootseed

The nominals are inflected in the following Case and Number
*  +Sg +Du +Pl  
*  +Ess +Nom +Gen +Acc +Ill +Loc +Com +Com/Sh  

The possessor indices are marked as such:
*  +PxSg1  first person singular
*  +PxSg2  second person singular
*  +PxSP3  third person singular or plural
*  +PxPl1  first person plural
*  +PxPl2  third person plural

The comparative forms are:
*  +Comp +Superl   

Numerals are classified under:
*  +Attr +Card  
*  +Ord  

Verb moods are:
*  +Ind +Pot +Cond +Imprt  

Verb tenses and aspect are:
*  +Fut  * future 
*  +Prs +Prt 
*  +RemPst  * remote past tu%<
* +Asp/Pfv  * perfective aspect ʔu%< , (Beck) punctual
* +Asp/Prog  * progressive aspect lə%<
* +Asp/Stat  * stative aspect ʔəs%< , (beck: as%<)
* +Asp/ProgStat  * progressive stative aspect lə%<ʔəs%<
* +Asp/Cont  * ləcu 

*  +LOC  * lack of control %>dxʷ
*  +Imprt  = %>ɬi

* +Surprise  * surprise %>əw̓ə
*  +Top  * topic marker 
*  +Now  * focus? %>əxʷ

Verb personal forms are:
*  +Sg1 +Sg2 +Sg3 +Du1 +Du2 +Du3 +Pl1 +Pl2 +Pl3  

## Direct Object conjugation
*  +OcSg1  = object conjugation first person singular
*  +OcSg2  = object conjugation second person singular
*  +OcSP3  = object conjugation third person singular or plural
*  +OcPl1  = object conjugation first person plural
*  +OcPl2  = object conjugation second person plural

Other verb forms are

*   +PrsPrc +PrfPrc +Sup +VGen +VAbess 

*  +ABBR +ACR  
* +Symbol = independent symbols in the text stream, like £, €, ©

Special symbols are classified with:
* +CLB +PUNCT +LEFT +RIGHT  

The verbs are syntactically split according to transitivity:
*  +TV +IV  

Special multiword units are analysed with:
*  +Multi  

Non-dictionary words can be recognised with:
*  +Guess  

Question and Focus particles:
*  +Qst +Foc  

Gender
* +Msc +Fem  

Semantics are classified with
*  +Sem/Mal +Sem/Fem +Sem/Sur  
*  +Sem/Plc    
*  +Sem/Org    
*  +Sem/Obj    
*  +Sem/Ani    
*  +Sem/Hum    
*  +Sem/Plant  
*  +Sem/Group  
*  +Sem/Time   
*  +Sem/Txt    
*  +Sem/Route  
*  +Sem/Measr  
*  +Sem/Wthr   
*  +Sem/Build  
*  +Sem/Edu    
*  +Sem/Veh    
*  +Sem/Clth   

Derivations are classified under the morphophonetic form of the suffix, the
source and target part-of-speech.
*  +V→N +V→V +V→A  
*  +Der/xxx  
*  +Der/Dimin  * diminutive
*  +Der/s  * Noun derivation
*  +Vnoun  * Deverbal Noun etc.

* +Clt  %>əxʷ

### Tags distinguishing different versions of the same lemma (before POS)
* +v1
* +v2
* +v3
* +v4
* +v5
* +v6
* +v7
* +v8
* +v9
* +v10
* +v11
* +v12
* +v13
* +v14
* +v15
* +v16
* +v17
* +v18
* +v19
* +v20
* +v21
* +v22
* +v23
* +v24

Note: These high +v... number are in use for one word only:

## Symbols that need to be escaped on the lower side (towards twolc):
* **»7**:  Literal »
* **«7**:  Literal «
```
 %[%>%]  - Literal >
 %[%<%]  - Literal <
```

* **%-**:  hyphen
* **%^√**:  commence root
* **%<**: prefix

Morphophonology
To represent phonologic variations in word forms we use the following
symbols in the lexicon files:
*  {aä} {oö} {uü}  

place holders
* %{p1%}  
* %{p2%}  
* %{p3%}  
* %{p4%}  
* %{p5%}  
* %{p6%}  
* %{p7%}  

And following triggers to control variation
*  {front} {back}  
* %^Red1CV2CiCV  qəlb: qiqəlb *rain showers*
* %^Red1CV1toCV2C  2-segment to 3-segments with vowel change
* %^Red1CV1toCV2CPL  2-segment to 3-segments with vowel change Plural
* %^Red2CVC  3-segment preposed reduplication CVC-to-CVCCVC bəlups:bəlbəlups 

## Flag diacritics
We have manually optimised the structure of our lexicon using following
flag diacritics to restrict morhpological combinatorics - only allow compounds
with verbs if the verb is further derived into a noun again:

|   @P.NeedNoun.ON@     | (Dis)allow compounds with verbs unless nominalised
|   @D.NeedNoun.ON@     | (Dis)allow compounds with verbs unless nominalised
|   @C.NeedNoun@        | (Dis)allow compounds with verbs unless nominalised

For languages that allow compounding, the following flag diacritics are needed
to control position-based compounding restrictions for nominals. Their use is
handled automatically if combined with +CmpN/xxx tags. If not used, they will
do no harm.

|   @P.CmpFrst.FALSE@  | Require that words tagged as such only appear first
|   @D.CmpPref.TRUE@   | Block such words from entering ENDLEX
|   @P.CmpPref.FALSE@  | Block these words from making further compounds
|   @D.CmpLast.TRUE@   | Block such words from entering R
|   @D.CmpNone.TRUE@   | Combines with the next tag to prohibit compounding
|   @U.CmpNone.FALSE@  | Combines with the prev tag to prohibit compounding
|   @P.CmpOnly.TRUE@   | Sets a flag to indicate that the word has passed R
|   @D.CmpOnly.FALSE@  | Disallow words coming directly from root.

Use the following flag diacritics to control downcasing of derived proper
nouns (e.g. Finnish Pariisi -> pariisilainen). See e.g. North Sámi for how to use
these flags. There exists a ready-made regex that will do the actual down-casing
given the proper use of these flags.

|   @U.Cap.Obl@         | Allowing downcasing of derived names: deatnulasj.
|   @U.Cap.Opt@         | Allowing downcasing of derived names: deatnulasj.

###  NOUNS

* @U.PossPx.SP3@  
* @U.PossPx.Sg1@  
* @U.PossPx.Sg2@  
* @U.PossPx.Sg3@  
* @U.PossPx.Pl1@  
* @U.PossPx.Pl2@  
* @U.PossPx.Pl3@  

* @R.PossPx.Sg1@  
* @R.PossPx.Sg2@  
* @D.PossPx@	    
* @C.PossPx@	    

### VERBS
* @U.TAM-SUBJ.SUBJ@  gʷə%<
* @R.TAM-SUBJ.SUBJ@  gʷə%<
* @D.TAM-SUBJ@  gʷə%<

* @U.TAM-HAB.IRR@	  ɬu%< also FUT
* @R.TAM-HAB.IRR@	  ɬu%< also FUT
* @U.TAM-HAB.HAB@	  ƛ̕u%<
* @R.TAM-HAB.HAB@	  ƛ̕u%<
* @D.TAM-HAB@	  ƛ̕u%<

* @U.TAM-RE.RE@   bə
* @R.TAM-RE.RE@   bə Anew, re-
* @D.TAM-RE.RE@   bə

* @U.NMZ.V2N@   s%^√
* @R.NMZ.V2N@   s%^√
* @U.NMZ.V2A@   dəxʷ
* @R.NMZ.V2A@   dəxʷ
* @D.NMZ@       s%^√ dəxʷ

* @U.TAM-T.REM@	  tu%<
* @R.TAM-T.REM@	  tu%<
* @D.TAM-T@	  tu%<

* @D.TAM-A@	  ʔu%<
* @U.TAM-A.PFV@	  ʔu%<
* @R.TAM-A.PFV@	  ʔu%<
* @U.TAM-A.CONT@	  ləcu%<
* @R.TAM-A.CONT@	  ləcu%<
* @U.TAM-A.PROGSTAT@  ləs%<
* @R.TAM-A.PROGSTAT@  ləs%<
* @U.TAM-A.PROG@	  progressive lə%<
* @R.TAM-A.PROG@	  progressive lə%<
* @U.TAM-A.STAT@  ʔəs%<
* @R.TAM-A.STAT@  ʔəs%<
* @U.TAM.NO@  
* @R.TAM.NO@  

* @U.OBJ.1@	  
* @U.OBJ.2@	  

* @D.OBJ.1@	  
* @D.OBJ.2@	  

* @R.TAM@		  
* @D.TAM@		  
* @C.TAM@		  

* **LEXICON Root ** Root lexicon
The word forms in LUSHOOTSEED language start from the lexeme roots of basic
word classes, or optionally from prefixes:

* 0   Verbs   ;	    
* 0   Adjectives  ;   
* 0   Adpositions  ;  
* 0   Adverbs  ;	    
* 0   Conjunctors  ;	    
* 0   Interjections  ;	    
* 0   Pronouns    ;   
* 0   Propernouns    ;   
* 0   Numerals    ;   
* 0   Prefixes    ;   

* **LEXICON K ** Clitic lexicon

* * *

<small>This (part of) documentation was generated from [src/fst/root.lexc](https://github.com/giellalt/lang-lut/blob/main/src/fst/root.lexc)</small>

---

