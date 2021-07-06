


















* Sets for POS sub-categories





* Sets for Semantic tags





* Sets for Morphosyntactic properties






































































































































































* Sets for verbs


- V is all readings with a V tag in them, REAL-V should
be the ones without an N tag following the V.  
The REAL-V set thus awaits a fix to the preprocess V ... N bug.



* The set COPULAS is for predicative constructions







* NP sets defined according to their morphosyntactic features







* The PRE-NP-HEAD family of sets

These sets model noun phrases (NPs). The idea is to first define whatever can
occur in front of the head of the NP, and thereafter negate that with the
expression **WORD - premodifiers**.












The set **NOT-NPMOD** is used to find barriers between NPs.
Typical usage: ... (*1 N BARRIER NPT-NPMOD) ...
meaning: Scan to the first noun, ignoring anything that can be
part of the noun phrase of that noun (i.e., "scan to the next NP head")






* Miscellaneous sets





















* Border sets and their complements













* Syntactic sets




These were the set types.



## HABITIVE MAPPING


* **hab1** 


* **hab2** 

* **hab3** (<hab> @ADVL>) for hab-actor and hab-case; if leat to the right, and Nom to the right of leat. Lots of restrictions.



* **habNomLeft** 


* **hab4** 	



* **hab6** 

* **hab7** 

* **hab8** This is not HAB
* **hab5**  This is not HAB



* **habDain** (<hab> @ADVL>) for (Pron Dem Pl Loc) if leat followed by Nom to the right




* **habGen** (<hab> @<ADVL) hab for Gen; if Gen is located in the end of the sentence and Nom is sentence initial










































































* **spred<obj** (@SPRED<OBJ) for Acc; the object of an SPRPED. Not to be mistaken with OPRED. If SPRED is to the left, and copulas is to the left of it. Nom or Hab are found sentence initially.


* **Hab<spred** (@<SPRED) for Nom; if copulas, goallut or jápmit is FMAINV and habitive or human Loc is found to the left. OR: if Ill or @Pron< followed by HAB are found to the left.

* **Hab>Advlcase<spred** (<ext> @<SUBJ) for Nom; it allows adverbials with Ill/Loc/Com/Ess to be found inbetween HAB and <ext>.

* **Nom>Advlcase<spred** (<ext> @<SUBJ) for Nom; it allows adverbials with Ill/Loc/Com/Ess to be found inbetween Nom and <ext> @<SUBJ.

* **<spred** (<ext> @<SUBJ) for Nom; if copulas to the left, and some kind of adverb, N Loc, time related word or Po to the left of it. OR: if Ill or @Pron< to the left, followed by copulas and the before mentioned to the left of copulas. 

* **<spred** (<ext> @<SUBJ) for Nom, but not for Pers. To the left boahtit or heaŋgát as MAINV, and futher to the left is some kind of place related word, or time related word


* **<spredQst1** (<ext> @<SUBJ) for Nom in a typically question sentence; if A) Hab, some kind of place word, Po or Nom to the left, and Qst followed by copulas to the left. B) same as a, only the Qst-pcle is attached to copulas. C) Qst to the left, with copulas to its left, but not if two Nom:s are found somewhere to the right. D) copulas to the left, and BOS to the left. E) Loc or Ill to the left, and Loc or Hab to the left of this, Qst and copulas to the left. F) Num @>N to the left, Hab, some kind of place word, Po or Nom to the left, and Qst followed by copulas to the left. NOTE) for all these rules; human, Loc or Sem/Plc not allowed to the right.

* **<spredQst2** (@<SPRED) for Nom; in a typically question sentence; differs from <spredQst1 by not beeing as restricted to the right. Though you are not allowed to be Pers or human.

* **Nom<spredQst** (@<SPRED) for Nom; in a typically question sentence. Differs from <spredQst2 by letting Nom be found between SPRED and copulas



* **<spred** (@<SPRED) for A Nom or N Nom if; the subject Nom is on the same side of copulas as you: on the right side of copulas

* **<spredVeara** (@<SPRED) for veara + Nom; if genitive immediately to the right, and intransitive mainverb to the right of genitive

* **leftCop<spred** (@<SPRED) for Nom; if copulas is the main verb to the left, and there is no Ess found to the left of cop (note that Loc is allowed between target and cop). OR: if you are Coll or Sem/Group with copulas to your left. 

* **<spredLocEXPERIMENT** (@<SPRED) for material Loc; if you are to the right of copulas, and the Nom to the left of copulas is not a hab-actor


* **NumTime** (@<SPRED) for A Nom

* **<spredSg** (@<SPRED) for Sg Nom	

* **<spredPg** (@<SPRED) for Pl Nom	

* **<spred** (@<SPRED) for Nom; if copulas to the left, and Nom or sentence boundary to the left of copulas. First one to the right is EOS.

* **<spred** (@<SPRED) for N Ess

* **spredEss>** (@SPRED>) for N Ess; if copulas to the right of you, and if an NP with nom-case first one to your left.

* **HABSpredSg>** (@SPRED>) for Nom; if habitive first one to the left, followed by copulas.

* **GalleSpred>** (@SPRED>) for Num Nom; if sentence initial

* **spredSgMII>** (@SPRED>)

* **r492>** (@SPRED>) for Interr Gen; consisting only of negations. You are not allowed to be MII. You are not allowed to have an adjective or noun to yor right. You are not allowed to have a verb to your right; the exception beeing an aux.



* **AdjSpredSg>** (@SPRED>) for A Sg Nom; if copulas to the right, but not if A or @<SPRED are found to the right of copulas

* **SpredSg>Hab** (@SPRED>) for Nom; if you are sentence initial, copulas is located to the right, and there is a habitive to the right of copulas



* **Spred>SubjInf** (@SPRED>) for Nom; if copulas to the right, and the subject of copulas is an Inf to the right

* **spredCoord** (@<SPRED) coordination for Nom; only if there already is a SPRED to the left of CNP. Not if there is some kind of comparison involved.






* **subj>Sgnr1** (@SUBJ>) for Nom Sg, including Indef Nom if; VFIN + Sg3 or Pl3 to the right (VFIN not allowed to the left) 

* **subj>Du** (@SUBJ>) for dual nominatives, including Coll Nom. VFIN + Du3 to the right. 
* **subj>Pl** (@SUBJ>) for plural nominatives, including Coll and Sem/Group. VFIN + Pl3 to the right.

* **subj>Pl** (@SUBJ>) for plural nominatives


* **subj>Sgnr2** (@SUBJ>) for Nom Sg; if VFIN + Sg3 to the right.

* **<subjSg** (@<SUBJ) for Nom Sg; if VFIN Sg3 or Du2 to the left (no HAB allowed to the left).




















* **f<advl** (@-F<ADVL) for infinite adverbials

* **f<advl** (@-F<ADVL) for infinite adverbials



* **s-boundary=advl>** (@ADVL>) for ADVL that resemble s-booundaries. Mainverb to the right.




* **-fobj>** (@-FOBJ>) for Acc 

* **-fobj>** (@-FOBJ>) for Acc




* **advl>mainV** (@ADVL>) if; finite mainverb not found to the left, but the finite mainverb is found to the right.


* **<advl** (@<ADVL) if; finite mainverb found to the left. Not if a comma is found immediately to the left and a finite mainverb is located somewhere to the right of this comma.




* **<advlPoPr** (@<ADVL) if mainverb to the left.
* **advlPoPr>** (@<ADVL) if mainverb to the right.



* **advlEss>** (@<ADVL) for weather and time Ess, if FMAINV to the left.






* **advl>inbetween** (@ADVL>) for Adv; if inbetween two sentenceboundaries where no mainverb is present.

* **comma<advlEOS** (@<ADVL) if; comma found to the left and the finite mainverb to the left of comma. To the right is the end of the sentence.



* **advlBOS>** (@ADVL>) if; you are N Ill and found sentnece initially. First one to your right is a clause.


* **<advlPoEOS** (@<ADVL) for Po; if you are found at the very end of a sentence. A mainverb is needed to the right though.



* **cleanupILL<advl** (@<ADVL) for N Ill if; there are no boundarysymbols to your left, if you arent already @N< OR @APP-N<, and no mainverb is to yor left.











* **<opredAAcc** (@<OPRED) for A Acc; if an other accusative to the left, and a transtive verb to the left of it. OR: if a transitive verb to the left, and an accusative to the left of it.


### sma object









* **<advlEss** (@<ADVL) for ESS-ADVL if; FMAINV to the left
* **<spredEss** (@<SPRED) for N Ess if; FMAINV to the left is intransitive or bargat





## SUBJ MAPPING - leftovers

## OBJ MAPPING - leftovers


## HNOUN MAPPING
















* * *
<small>This (part of) documentation was generated from [../src/cg3/functions.cg3](http://github.com/giellalt/lang-lut/blob/main/../src/cg3/functions.cg3)</small>
S O U T H   S Á M I   D I S A M B I G U A T O R          




# Delimiters 




## Tags and sets 

* BOS/EOS


* Tags declared as single-membered LISTs 





















* Semantic tags

Sem/Ani
Sem/Fem
Sem/Mal
Sem/Obj
Sem/Org
Sem/Plc
Sem/Sur
Sem/Time
Sem/Hum
Sem/Date
Sem/Year
Sem/Group
Sem/Route
Sem/Build
Sem/Place
Sem/Food

* Syntactic tags

@CNP
@CVP
@+FAUXV
@+FMAINV
@-FAUXV
@-FMAINV
MAINV



* More sets















* Noun sets

















* Verb sets































* BOUNDARY SETS


























# Disambiguation #


## @NO CODE@

Rule for adding Sem/Date as a tag to readings which looks like dates


## @NO CODE@

## Cycle 0

Removing non-lexicalised forms when lexicalised 







Remove Num, ACR, ...







Possessive suffix



Short Pronouns


Proper nouns



Trivialia















Verbs







Imperative



## CC- and CS-Mapping



## CNP mapping

Mapping CNP to CC and CS.






## CVP Mapping

Mapping @CVP to all CS












## PrfPrc

Select PrfPrc if DerNomAct


## Person

leah Prs Sg2 = Pl3



Select Inf If Infv







## Span sentences



### Nomen

REmove Px if not family


Remove Prop Attr if not 1 Prop 










### Verb or Noun







## CC and CS or Adv















## Adj or Adv



## Grammatisk ord eller N eller A









## N or V









Ger or Der/NomAct


Adj or Indef


Num




Rel or Interr




Po or Pr



Adv or Po/Pr


Illative or genetive



Com



Accusative or illative

Indef or Adv

special lemmas







Adverb context prefers Adv


Verb person vs. Inf -- moved here in order to have the pronouns disambiguated first.






# Proper nouns

Rule set taken from sme



Substituting Prop tags 



























adverbs modifying another adverb
Adv modifying a pronoun or noun









* * *
<small>This (part of) documentation was generated from [../src/cg3/disambiguator.cg3](http://github.com/giellalt/lang-lut/blob/main/../src/cg3/disambiguator.cg3)</small>
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
 * +Asp/Prf  * perfective aspect ʔu%< , (Beck) punctual
 * +Asp/Prog  * progressive aspect lə%<
 * +Asp/Stat  * stative aspect ʔəs%< , (beck: as%<)

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
 * %^Red2CVC2CVCCVC  3-segment reduplication

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
 * @U.TAM.PRF@	  
 * @R.TAM.PRF@	  
 * @U.TAM.FUT@	  
 * @R.TAM.FUT@	  
 * @U.TAM.COND@  
 * @R.TAM.COND@  
 * @U.TAM.PROG@	  progressive
 * @R.TAM.PROG@	  progressive
 * @U.TAM.REM@	  
 * @R.TAM.REM@	  
 * @U.TAM.STAT@  
 * @R.TAM.STAT@  
 * @U.TAM.NO@  
 * @R.TAM.NO@  

 * @U.TAM@		  
 * @R.TAM@		  

 * @U.OBJ.1@	  
 * @U.OBJ.2@	  

 * @D.OBJ.1@	  
 * @D.OBJ.2@	  

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
 * 0   Numerals    ;   
 * 0   Prefixes    ;   



 * **LEXICON K ** Clitic lexicon

* * *
<small>This (part of) documentation was generated from [../src/fst/root.lexc](http://github.com/giellalt/lang-lut/blob/main/../src/fst/root.lexc)</small>Proper noun inflection
The Lushootseed language proper nouns inflect in the same cases as regular
nouns, but with a colon (':') as separator.



* * *
<small>This (part of) documentation was generated from [../src/fst/affixes/propernouns.lexc](http://github.com/giellalt/lang-lut/blob/main/../src/fst/affixes/propernouns.lexc)</small>Pronoun inflection
The Lushootseed language pronouns inflect in the same cases as regular
nouns, but with a colon (':') as separator.











* * *
<small>This (part of) documentation was generated from [../src/fst/affixes/pronouns.lexc](http://github.com/giellalt/lang-lut/blob/main/../src/fst/affixes/pronouns.lexc)</small>Prefixes
Prefixes in the Lushootseed language are bound to beginning of other words.






* * *
<small>This (part of) documentation was generated from [../src/fst/affixes/prefixes.lexc](http://github.com/giellalt/lang-lut/blob/main/../src/fst/affixes/prefixes.lexc)</small>Noun inflection
The Lushootseed language nouns inflect in time person aspect.









qəlb+N+Pl+Nom: **rain showers**
* *%{p5%}%{p4%}%{p3%}%{p2%}%{p1%}qəlb%^Red1CV2CiCV*
* *00qi0qəlb0*
bəlups+N+Pl+Nom
* *%{p5%}%{p4%}%{p3%}%{p2%}%{p1%}bəlups%^Red2CVC2CVCCVC*
* *00bəlbəlups0*
* ★*%{p5%}%{p4%}%{p3%}%{p2%}%{p1%}bəlups%^Red2CVC2CVCCVC* (is not standard language)
* ★*00000bəlups0* (is not standard language)
* *k̓ʷəčk̓ʷəčədiʔ:* `k̓ʷəčədiʔ+N+Pl+Nom`
* ★*k̓ʷəčədiʔ:* `k̓ʷəčədiʔ+N+Pl+Nom` (is not standard language)








* * *
<small>This (part of) documentation was generated from [../src/fst/affixes/nouns.lexc](http://github.com/giellalt/lang-lut/blob/main/../src/fst/affixes/nouns.lexc)</small>
# Symbol affixes





* * *
<small>This (part of) documentation was generated from [../src/fst/affixes/symbols.lexc](http://github.com/giellalt/lang-lut/blob/main/../src/fst/affixes/symbols.lexc)</small>Adjective inflection
The Lushootseed language adjectives compare.







* * *
<small>This (part of) documentation was generated from [../src/fst/affixes/adjectives.lexc](http://github.com/giellalt/lang-lut/blob/main/../src/fst/affixes/adjectives.lexc)</small>Adpositions
The Lushootseed language adpositions





* * *
<small>This (part of) documentation was generated from [../src/fst/affixes/adpositions.lexc](http://github.com/giellalt/lang-lut/blob/main/../src/fst/affixes/adpositions.lexc)</small>Verb inflection
The Lushootseed language verbs inflect in object persons.




bəčdub:bəčd

kʷədad:kʷədad

kʷədad:kʷədad



















* * *
<small>This (part of) documentation was generated from [../src/fst/affixes/verbs.lexc](http://github.com/giellalt/lang-lut/blob/main/../src/fst/affixes/verbs.lexc)</small>Adverbs
The Lushootseed language adverbs











* * *
<small>This (part of) documentation was generated from [../src/fst/affixes/adverbs.lexc](http://github.com/giellalt/lang-lut/blob/main/../src/fst/affixes/adverbs.lexc)</small>Proper nouns
Proper nouns in LUSHOOTSEED language 



* * *
<small>This (part of) documentation was generated from [../src/fst/stems/propernouns.lexc](http://github.com/giellalt/lang-lut/blob/main/../src/fst/stems/propernouns.lexc)</small>Pronouns
Pronouns in the Lushootseed language are references to things.






* * *
<small>This (part of) documentation was generated from [../src/fst/stems/pronouns.lexc](http://github.com/giellalt/lang-lut/blob/main/../src/fst/stems/pronouns.lexc)</small>Conjunctors
Conjunctors in the LUSHOOTSEED language 



* * *
<small>This (part of) documentation was generated from [../src/fst/stems/conjunctors.lexc](http://github.com/giellalt/lang-lut/blob/main/../src/fst/stems/conjunctors.lexc)</small>Nouns
Nouns in LUSHOOTSEED language are things.


* * *
<small>This (part of) documentation was generated from [../src/fst/stems/nouns.lexc](http://github.com/giellalt/lang-lut/blob/main/../src/fst/stems/nouns.lexc)</small>Interjections
Interjections in the LUSHOOTSEED language 




* * *
<small>This (part of) documentation was generated from [../src/fst/stems/interjections.lexc](http://github.com/giellalt/lang-lut/blob/main/../src/fst/stems/interjections.lexc)</small>Adjectives
Adjectives in the Lushootseed language describe things.



* * *
<small>This (part of) documentation was generated from [../src/fst/stems/adjectives.lexc](http://github.com/giellalt/lang-lut/blob/main/../src/fst/stems/adjectives.lexc)</small>Adpositions
Adpositions in the LUSHOOTSEED language 



* * *
<small>This (part of) documentation was generated from [../src/fst/stems/adpositions.lexc](http://github.com/giellalt/lang-lut/blob/main/../src/fst/stems/adpositions.lexc)</small>Verbs
Verbs in the Lushootseed language are actions.








* * *
<small>This (part of) documentation was generated from [../src/fst/stems/verbs.lexc](http://github.com/giellalt/lang-lut/blob/main/../src/fst/stems/verbs.lexc)</small>Adverbs
Adverbs in the LUSHOOTSEED language 











* * *
<small>This (part of) documentation was generated from [../src/fst/stems/adverbs.lexc](http://github.com/giellalt/lang-lut/blob/main/../src/fst/stems/adverbs.lexc)</small>Numerals
Numerals in the Lushootseed language are numbers.


* * *
<small>This (part of) documentation was generated from [../src/fst/stems/numerals.lexc](http://github.com/giellalt/lang-lut/blob/main/../src/fst/stems/numerals.lexc)</small>This is where new words are added as lexc entries before they are
added to the xml source files.
ɬaləp̓+N:ɬaləp̓ N_with-PL_RED2 "tongue" ;


ADD NOUNS BELOW


pupuhigʷəd # "March/april" ;
pədx̌ʷiwaac# "april/may" ;




* * *
<small>This (part of) documentation was generated from [../src/fst/stems/nouns_newwords.lexc](http://github.com/giellalt/lang-lut/blob/main/../src/fst/stems/nouns_newwords.lexc)</small>=================================== !
The Lushootseed morphophonological/twolc rules file !
=================================== !



The Lushootseed language is written in lower case only

This transformation, accent loss, will be moved to post dict.



c U+0313










Lushootseed is written in IPA, there are no upper-case letters












place holders

 * %^Red1CV2CiCV:0  qəlb: qiqəlb **rain showers**
 * %^Red1CV1toCV2C:0  2-segment to 3-segments with vowel change 
 * %^Red1CV1toCV2CPL:0  2-segment to 3-segments with vowel change Plural

 * %^Red2CVC2CVCCVC:0  3-segment reduplication 






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

Red 1 qəlb: qiqəlb %^Red1CV2CiCV



**ə:0 in inflection**
* *x̌əd»əd%>sid*
* *x̌əd000%>cid*
sčətxʷəd+N+Der/Dimin+N+Pl+Nom bear
* *s%^√%{p5%}%{p4%}%{p3%}%{p2%}%{p1%}čətxʷəd%^Red1CV1toCV2CPL*
* *s%^√čiči0č0txʷəd0*

**ʔ:0 in preceding s**
ʔəɫəd+V+Prf+Der+Der/N+N+Sg+Nom+PxSg2: __eat/syödä__
* *ad<s<ʔu<ʔəɫəd*
* *ad<s<0u<ʔəɫəd*




**%{p2%}:ə in reduplication**
* *%{p5%}%{p4%}%{p3%}%{p2%}%{p1%}bəlups%^Red2CVC2CVCCVC*
* *00bəlbəlups0*


**%{p2%}:u in reduplication**


**%{p2%}:i in reduplication**
qəlb+N+Pl+Nom: **rain showers**
* *%{p5%}%{p4%}%{p3%}%{p2%}%{p1%}qəlb%^Red1CV2CiCV*
* *00qi0qəlb0*
pišpiš+N+Pl+Nom: **cat/kissa**
* *%{p5%}%{p4%}%{p3%}%{p2%}%{p1%}pišpiš%^Red2CVC2CVCCVC*
* *00pišpišpiš0*

**%{p4%}:i in reduplication**


**%{p2%}:a in reduplication**

**%{p1%}:0**

**%{p2%}:0**


**%{p3%}:0**

**%{p4%}:0**

**%{p5%}:0**


### CONSONANTS
**s:c after d:0**

* *ʔu%^√%{p3%}%{p2%}%{p1%}kʷədad%>s*
* *ʔu0000kʷəda0%>c*

**d:0 before s:c**
* *ʔu%^√%{p3%}%{p2%}%{p1%}kʷədad%>s*
* *ʔu0000kʷəda0%>c*
* *ʔu%^√%{p3%}%{p2%}%{p1%}kʷədad%>cid*
* *ʔu0000kʷəda0%>cid*


**%{p1%}:Cx in reduplication**

**%{p3%}:Cx in reduplication**

**%{p5%}:Cx in reduplication**
sčətxʷəd+N+Der/Dimin+N+Pl+Nom bear
* *s%^√%{p5%}%{p4%}%{p3%}%{p2%}%{p1%}čətxʷəd%^Red1CV1toCV2CPL*
* *s%^√čičič0txʷəd0*

liquids

**%{p1%}:l̕ in reduplication**

**%{p1%}:y̓ in reduplication**



**%{p1%}:w̓ in reduplication**

**%{p1%}:ʔ in reduplication**

**%{p1%}:Cx in reduplication**
* *%{p5%}%{p4%}%{p3%}%{p2%}%{p1%}bəlups%^Red2CVC2CVCCVC*
* *00bəlbəlups0*

**%{p1%}:Cx in reduplication**

**%{p1%}:Cx in reduplication**





* * *
<small>This (part of) documentation was generated from [../src/fst/phonology.twolc](http://github.com/giellalt/lang-lut/blob/main/../src/fst/phonology.twolc)</small>












Check this


Check this









Check this


Check this


















* * *
<small>This (part of) documentation was generated from [../src/transcriptions/transcriptor-numbers-digit2text.lexc](http://github.com/giellalt/lang-lut/blob/main/../src/transcriptions/transcriptor-numbers-digit2text.lexc)</small>


We describe here how abbreviations are in Lushootseed are read out, e.g.
for text-to-speech systems.

For example:

 * s.:syntynyt # ;  
 * os.:omaa% sukua # ;  
 * v.:vuosi # ;  
 * v.:vuonna # ;  
 * esim.:esimerkki # ; 
 * esim.:esimerkiksi # ; 


* * *
<small>This (part of) documentation was generated from [../src/transcriptions/transcriptor-abbrevs2text.lexc](http://github.com/giellalt/lang-lut/blob/main/../src/transcriptions/transcriptor-abbrevs2text.lexc)</small>
[ L A N G U A G E ]  G R A M M A R   C H E C K E R









# DELIMITERS


# TAGS AND SETS



## Tags


This section lists all the tags inherited from the fst, and used as tags
in the syntactic analysis. The next section, **Sets**, contains sets defined
on the basis of the tags listed here, those set names are not visible in the output.




### Beginning and end of sentence
BOS
EOS



### Parts of speech tags

N
A
Adv
V
Pron
CS
CC
CC-CS
Po
Pr
Pcle
Num
Interj
ABBR
ACR
CLB
LEFT
RIGHT
WEB
QMARK
PPUNCT
PUNCT

COMMA
¶



### Tags for POS sub-categories

Pers
Dem
Interr
Indef
Recipr
Refl
Rel
Coll
NomAg
Prop
Allegro
Arab
Romertall


### Tags for morphosyntactic properties

Nom
Acc
Gen
Ill
Loc
Com
Ess
Ess
Sg
Du
Pl
Cmp/SplitR
Cmp/SgNom Cmp/SgGen
Cmp/SgGen
PxSg1
PxSg2
PxSg3
PxDu1
PxDu2
PxDu3
PxPl1
PxPl2
PxPl3
Px

Comp
Superl
Attr
Ord
Qst
IV
TV
Prt
Prs
Ind
Pot
Cond
Imprt
ImprtII
Sg1
Sg2
Sg3
Du1
Du2
Du3
Pl1
Pl2
Pl3
Inf
ConNeg
Neg
PrfPrc
VGen
PrsPrc
Ger
Sup
Actio
VAbess



Err/Orth



### Semantic tags

Sem/Act
Sem/Ani
Sem/Atr
Sem/Body
Sem/Clth
Sem/Domain
Sem/Feat-phys
Sem/Fem
Sem/Group
Sem/Lang
Sem/Mal
Sem/Measr
Sem/Money
Sem/Obj
Sem/Obj-el
Sem/Org
Sem/Perc-emo
Sem/Plc
Sem/Sign
Sem/State-sick
Sem/Sur
Sem/Time
Sem/Txt

HUMAN

HAB-ACTOR
HAB-ACTOR-NOT-HUMAN


PROP-ATTR
PROP-SUR



TIME-N-SET


###  Syntactic tags

@+FAUXV
@+FMAINV
@-FAUXV
@-FMAINV
@-FSUBJ>
@-F<OBJ
@-FOBJ>
@-FSPRED<OBJ
@-F<ADVL
@-FADVL>
@-F<SPRED
@-F<OPRED
@-FSPRED>
@-FOPRED>
@>ADVL
@ADVL<
@<ADVL
@ADVL>
@ADVL
@HAB>
@<HAB
@>N
@Interj
@N<
@>A
@P<
@>P
@HNOUN
@INTERJ
@>Num
@Pron<
@>Pron
@Num<
@OBJ
@<OBJ
@OBJ>
@OPRED
@<OPRED
@OPRED>
@PCLE
@COMP-CS<
@SPRED
@<SPRED
@SPRED>
@SUBJ
@<SUBJ
@SUBJ>
SUBJ
SPRED
OPRED
@PPRED
@APP
@APP-N<
@APP-Pron<
@APP>Pron
@APP-Num<
@APP-ADVL<
@VOC
@CVP
@CNP
OBJ
<OBJ
OBJ>
<OBJ-OTHERS
OBJ>-OTHERS
SYN-V
@X





## Sets containing sets of lists and tags

This part of the file lists a large number of sets based partly upon the tags defined above, and
partly upon lexemes drawn from the lexicon.
See the sourcefile itself to inspect the sets, what follows here is an overview of the set types.



### Sets for Single-word sets

INITIAL


### Sets for word or not

WORD
REAL-WORD
REAL-WORD-NOT-ABBR
NOT-COMMA


### Case sets

ADLVCASE

CASE-AGREEMENT
CASE

NOT-NOM
NOT-GEN
NOT-ACC

### Verb sets


NOT-V

### Sets for finiteness and mood

REAL-NEG

MOOD-V

NOT-PRFPRC


### Sets for person

SG1-V
SG2-V
SG3-V
DU1-V
DU2-V
DU3-V
PL1-V
PL2-V
PL3-V





### Pronoun sets

















### Adjectival sets and their complements




### Adverbial sets and their complements




### Sets of elements with common syntactic behaviour


### NP sets defined according to their morphosyntactic features








### The PRE-NP-HEAD family of sets

These sets model noun phrases (NPs). The idea is to first define whatever can
occur in front of the head of the NP, and thereafter negate that with the
expression **WORD - premodifiers**.





















### Border sets and their complements











### Grammarchecker sets








* * *
<small>This (part of) documentation was generated from [../tools/grammarcheckers/grammarchecker.cg3](http://github.com/giellalt/lang-lut/blob/main/../tools/grammarcheckers/grammarchecker.cg3)</small>