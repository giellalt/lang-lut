
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
*  +Pass   -t-əb

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
*  +Err/Orth-no-q   missing glottal stop
*  +Err/Spellrelax 
*  +Use/-Spell  
* **+Use/TTS** – **only** retained in the HFST Text-To-Speech disambiguation tokeniser
* **+Use/-TTS** – **never** retained in the HFST Text-To-Speech disambiguation tokeniser

* +URL * For tagging URLs

Dialect tags:

* **+Dial/-NL** not North Lushootseed
* **+Dial/-SL** not South Lushootseed

The nominals are inflected in the following Case and Number
*  +Sg +Du +Pl +SP  
*  +Ess +Nom +Gen +Acc +Ill +Loc +Com +Com/Sh  

Possession is marked as follows:
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
* +Anew     * bə%<

Verb/Predicate tenses and aspect are:
*  +Fut  * future 
*  +Prs +Prt 
*  +Hab 	  * habitual ƛ̕u%<
*  +Irr     * Irrealis (future) ɬu%<
*  +RemPst  * remote past tu%<
* +Asp/Pfv  * perfective aspect ʔu%< , (Beck) punctual
* +Asp/Prog  * progressive aspect lə%<
* +Asp/Stat  * stative aspect ʔəs%< , (beck: as%<)
* +Asp/ProgStat  * progressive stative aspect lə%<ʔəs%<
* +Asp/Cont  * ləcu 

* +Dat 	   * verbal derivation -yid/šid

*  +LOC  * lack of control %>dxʷ
*  +Imprt  = %>ɬi

* +Surprise  * surprise %>əw̓ə
*  +Top  * topic marker 
*  +Now  * focus? %>axʷ  %>əxʷ
* +Qst          *   Question Particle: ʔu

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
* +CLB +PUNCT +LEFT +RIGHT +MIDDLE  

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
*  +Der/Dimin_12123  * diminutive pa-pasted ^Red12123
*  +Der/Dimin_1i123  * diminutive bi-bəlups; qi-qəlb 
*  +Der/Dimin_12q123  * diminutive 
*  +Der/Dimin_1iq123  * diminutive 
*  +Der/Dimin_1213  * diminutive pišpiš > pi-pšpiš;  sbádil:sbábdil
*  +Der/Dimin_1i13  * diminutive %^Red1i13 
*  +Der/Dimin_12q13  * diminutive
*  +Der/Dimin_1iq13  * diminutive

*  +Der/Dimin_121e3  * diminutive sbádil:sbábədil
*  +Der/Dimin_1i1e3  * diminutive
*  +Der/Dimin_12q1e3  * diminutive
*  +Der/Dimin_1iq1e3  * diminutive

*  +Der/Dimin_1i1i13  * diminutive with plural ^RedPL1i1i13

*  +Der/Distr	    * distributive
*  +Der/Distr_123123  * distributive

*  +Der/s  * Noun derivation
*  +Vnoun  * Deverbal Noun etc.

Reduplication in Lushootseed is associated with a three-letter reduplication segment.

reduplication type 1 envolves the first two letters of the three-letter reduplication segment
*  +Der/Red1_12123  * This is Red1, associated with Dimin pa-pasted
*  +Der/Red1_1i123  * This is Red1, associated with Dimin
*  +Der/Red1_12ʔ123  * This is Red1, associated with Dimin
*  +Der/Red1_1iʔ123  * This is Red1, associated with Dimin
*  +Der/Red1_1213  * This is Red1, associated with Dimin pišpiš > pi-pšpiš; pa-pstəd
*  +Der/Red1_1i13  * This is Red1, associated with Dimin
*  +Der/Red1_12ʔ13  * This is Red1, associated with Dimin
*  +Der/Red1_1iʔ13  * This is Red1, associated with Dimin
*  +Der/Red1_121ə3  * This is Red1, associated with Dimin
*  +Der/Red1_1i1ə3  * This is Red1, associated with Dimin
*  +Der/Red1_12ʔ1ə3  * This is Red1, associated with Dimin
*  +Der/Red1_1iʔ1ə3  * This is Red1, associated with Dimin

*  +Der/Red1_1i13_Distr_1212  * This is Red1, associated with Dimin ^RedPL1i1i13
reduplication type 2 involves the all three letters of the three-letter reduplication segment

* +Der/Red2_3L  * This is Red2 (Red2CVC=R2-123123), usually distributive, it is a reduplication where the first three letters are reduplicated as is pastəd > pas-pastəd

reduplication type 3 involves the last two letters of the three-letter reduplication segment

* +Der/Red3_12323  * This is Red3 this is random verbal
*  +Der/Red5_12323  * This is Red5 This is isolating, individuating cəliɬ:cədədiɬ 'he alone'

reduplication type 6 involves the all three letters of the three-letter reduplication segment with a double vowel

* +Der/Red6_122123  * This is Red6 
*  +Der/Red6_1aa1ə3  * This is Red6 sɬaaɬədəyʔ < sɬadəyʔ

* +Clt/Now  %>áxʷ %>əxʷ

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

* %{lØ%}    in slh stem-final l tends to be lost, but it is retained before Clt/Now

place holders
* %{pØ%}  
* %{p1%}  
* %{p2%}  
* %{p3%}  
* %{p4%}  
* %{p5%}  
* %{p6%}  
* %{p7%}  

And following triggers to control variation
*  {front} {back}  

* %^Red1i123  qəlb: qiqəlb *rain showers*
* %^Red1i13  2-segment to 3-segments with vowel change sčətxʷəd:sčičtxʷəd Der/Red1_1i13
* %^Red12q13  
* %^Red1213 
* %^Red1iq13  iʔ
* %^Red1iq123  iʔ   biʔbədəʔs
* %^Red12123  papastəd
* %^RedPL1i1i13  2-segment to 3-segments with vowel change Distr sčətxʷəd:sčičičtxʷəd Der/Red1_1i13_Distr_1212 
* %^RedPL123123  3-segment preposed reduplication CVC-to-CVCCVC bəlups:bəlbəlups 
* %^Red12323  should work for Red3 and Red5
* %^RedPL130130  ƛ̕xʷay: ƛ̕xʷaƛ̕xʷay 

* %^Pen  this combines with subsequent RmVow or perhaps RmCns
* %^RmVOW  this removes previous vowel or with Pen the penultimate vowel
* %^d2t  this devoices d to t specifically

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

### SPELLRELAX

###  NOUNS

* @U.PossPx.ZERO@ 
* @U.PossPx.SP3@  
* @U.PossPx.Sg1@  
* @U.PossPx.Sg2@  
* @U.PossPx.Sg3@  
* @U.PossPx.Pl1@  
* @U.PossPx.Pl2@  
* @U.PossPx.Pl3@  

* @R.PossPx.Sg1@  
* @R.PossPx.Sg2@  
* @R.PossPx@	    
* @D.PossPx@	    
* @C.PossPx@	    

* @U.NPrefix.ZERO@ 
* @U.NPrefix.c@ 
* @U.NPrefix.dexw@ 
* @U.NPrefix.dxw@ 
* @U.NPrefix.dxws@ 
* @U.NPrefix.je@ 
* @U.NPrefix.le@ 
* @U.NPrefix.s@ 
* @U.NPrefix.sexw@ 
* @U.NPrefix.sxw@ 
* @U.NPrefix.tsi@ 
* @U.NPrefix.xh@ 
* @U.NPrefix.xhw@ 
* @U.NPrefix.xw@ 

* @R.NPrefix.ZERO@ 
* @R.NPrefix.c@ 
* @R.NPrefix.dexw@ 
* @R.NPrefix.dxw@ 
* @R.NPrefix.dxws@ 
* @R.NPrefix.je@ 
* @R.NPrefix.le@ 
* @R.NPrefix.s@ 
* @R.NPrefix.sexw@ 
* @R.NPrefix.sxw@ 
* @R.NPrefix.tsi@ 
* @R.NPrefix.xh@ 
* @R.NPrefix.xhw@ 
* @R.NPrefix.xw@ 
* @D.NPrefix@ 
* @C.NPrefix@ 

### VERBS
* @U.TAM-SUBJ.ZERO@  
* @U.TAM-SUBJ.SUBJ@  gʷə%<
* @R.TAM-SUBJ.SUBJ@  gʷə%<

* @U.TAM-HAB.ZERO@  
* @U.TAM-HAB.IRR@	  ɬu%< also FUT
* @R.TAM-HAB.IRR@	  ɬu%< also FUT
* @U.TAM-HAB.HAB@	  ƛ̕u%<
* @R.TAM-HAB.HAB@	  ƛ̕u%<

* @U.TAM-RE.ZERO@   
* @U.TAM-RE.RE@   bə Anew, re-
* @R.TAM-RE.RE@   bə

* @U.NMZ.ZERO@  
* @U.NMZ.V2N@   s%^√
* @R.NMZ.V2N@   s%^√
* @U.NMZ.V2A@   dəxʷ
* @R.NMZ.V2A@   dəxʷ

* @U.TAM-T.ZERO@	  
* @U.TAM-T.REM@	  tu%<
* @R.TAM-T.REM@	  tu%<

* @U.TAM-A.ZERO@	  none of these
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
* @U.TAM.NO@  What is this? 2025-07-18
* @R.TAM.NO@  

* @U.OBJ.ZERO@     
* @U.OBJ.1@        
* @U.OBJ.2@        
* @U.OBJ.3@        

* @U.OBJ.SG1@	  
* @U.OBJ.SG2@	  
* @U.OBJ.PL1@	  
* @U.OBJ.PL2@	  
* @U.OBJ.SP3@	  
* @U.OBJ.ZERO@	  

* @D.OBJ.SG1@	  
* @D.OBJ.SG2@	  
* @D.OBJ.PL1@	  
* @D.OBJ.PL2@	  
* @D.OBJ.SP3@	  
* @D.OBJ@	  

* @R.TAM@		  
* @D.TAM@		  
* @C.TAM@		  

* **LEXICON Root ** Root lexicon
The word forms in LUSHOOTSEED language start from the lexeme roots of basic
word classes, or optionally from prefixes:

*    Adpositions  ;  
*    Adverbs  ;	    
*    Conjunctors  ;	    
*    Interjections  ;	    
*    Pronouns    ;   
*    Numerals    ;   
*    Prefixes    ;    Feeds Adjectives, Nouns, Propernouns, Verbs

* **LEXICON K ** Clitic lexicon

* **LEXICON ENDLEX **

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/root.lexc](https://github.com/giellalt/lang-lut/blob/main/src/fst/morphology/root.lexc)</small>
