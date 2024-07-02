# Lushootseed language model documentation

All doc-comment documentation in one large file.

---

# src-cg3-disambiguator.cg3.md 


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

* * *

<small>This (part of) documentation was generated from [src/cg3/disambiguator.cg3](https://github.com/giellalt/lang-lut/blob/main/src/cg3/disambiguator.cg3)</small>

---

# src-cg3-functions.cg3.md 



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

<small>This (part of) documentation was generated from [src/cg3/functions.cg3](https://github.com/giellalt/lang-lut/blob/main/src/cg3/functions.cg3)</small>

---

# src-fst-morphology-affixes-adjectives.lexc.md 

Adjective inflection
The Lushootseed language adjectives are inflected in much the same way as nouns and verbs.

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/affixes/adjectives.lexc](https://github.com/giellalt/lang-lut/blob/main/src/fst/morphology/affixes/adjectives.lexc)</small>

---

# src-fst-morphology-affixes-adpositions.lexc.md 

Adpositions
The Lushootseed language adpositions

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/affixes/adpositions.lexc](https://github.com/giellalt/lang-lut/blob/main/src/fst/morphology/affixes/adpositions.lexc)</small>

---

# src-fst-morphology-affixes-adverbs.lexc.md 

Adverbs
The Lushootseed language adverbs

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/affixes/adverbs.lexc](https://github.com/giellalt/lang-lut/blob/main/src/fst/morphology/affixes/adverbs.lexc)</small>

---

# src-fst-morphology-affixes-nouns.lexc.md 

Noun inflection
The Lushootseed language nouns inflect in time person aspect.

qəlb+N+Pl: **rain showers**
* *{p5}{p4}{p3}{p2}{p1}qəlb^Red1i123*
* *00qi0qəlb0*

bəlups+N+Pl
* *{p5}{p4}{p3}{p2}{p1}bəlups^RedPL123123*
* *00bəlbəlups0*
* ★*{p5}{p4}{p3}{p2}{p1}bəlups^RedPL123123* (is not standard language)
* ★*00000bəlups0* (is not standard language)
k̓ʷəčədiʔ+N+Pl: __rabbit/jänis__
* *{p5}{p4}{p3}{p2}{p1}k̓ʷəčədiʔ^RedPL123123*
* *00k̓ʷəčk̓ʷəčədiʔ0*
* ★*k̓ʷəčədiʔ:* `k̓ʷəčədiʔ+N+Pl` (is not standard language)

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/affixes/nouns.lexc](https://github.com/giellalt/lang-lut/blob/main/src/fst/morphology/affixes/nouns.lexc)</small>

---

# src-fst-morphology-affixes-prefixes.lexc.md 

Prefixes
Prefixes in the Lushootseed language are bound to beginning of other words.

Beck, David 2018: Aspectual Affixation in Lushootseed: A minor reanalysis
ordering
Tense/mood | Poss.subj | nominalizers | Aspect | Stem | Object/voice | others
gʷə%<, ƛ̕u%<, tu%<, ɬu%<, bə%< | d%<, ad%< |s%<, dəxʷ%< | ʔu, ʔəs, lə, ləs, ləcu| X |%>s/%>bš, %>sut/%>ut, %>agʷəl, %>b |%>ləp, %>s, %>əxʷ

-1/-4?(lə=bə=ʔas-q̓ʷəl-il) proclitic Asp/Prog+:lə%<
@U.TAM-HAB.HAB@:@U.TAM-HAB.HAB@ƛ̕u%<  (+Hab)
@U.TAM-T.REM@:@U.TAM-T.REM@tu%<   (TM/Past+)
@U.TAM-HAB.IRR@:@U.TAM-HAB.IRR@ɬu%<  (+Fut)
@U.TAM-RE.RE@:@U.TAM-RE.RE@bə%<  (+Add)
-1 aspect
@U.TAM-A.PROG@:@U.TAM-A.PROG@lə%<  (non-circumscribed, progressive)
@U.TAM-A.STAT@:@U.TAM-A.STAT@ʔəs%<  (ongoing state: Asp/Stat)
@U.TAM-A.STAT@:@U.TAM-A.STAT@ʔas%<  (ongoing state: Asp/Stat)variant
@U.TAM-A.PROGSTAT@:@U.TAM-A.PROGSTAT@ləs%< (Asp/ProgStat)
@U.TAM-A.PFV@:@U.TAM-A.PFV@ʔu%<  (Asp/Pfv)
-1 Asp/Cont+:ləcu%< (?Asp/Prog+:lə%< + Asp/Pfv+:ʔu%<) Skagit
-1 Asp/Stat:ʔə{sØ}{dØ}xʷ%< (Asp/Stat+:ʔəs%< + dxʷ%<)

X
1 %>s/%>bš, %>sut/%>ut, %>agʷəl, %>b, +Inch:%>il
2 %>ləp, +Px3:%>s, %>əxʷ
lə<bə<ləcu<gʷaadgʷad

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/affixes/prefixes.lexc](https://github.com/giellalt/lang-lut/blob/main/src/fst/morphology/affixes/prefixes.lexc)</small>

---

# src-fst-morphology-affixes-pronouns.lexc.md 

Pronoun inflection
The Lushootseed language pronouns inflect in the same cases as regular
nouns, but with a colon (':') as separator.

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/affixes/pronouns.lexc](https://github.com/giellalt/lang-lut/blob/main/src/fst/morphology/affixes/pronouns.lexc)</small>

---

# src-fst-morphology-affixes-propernouns.lexc.md 

Proper noun inflection
The Lushootseed language proper nouns inflect in the same cases as regular
nouns, but with a colon (':') as separator.

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/affixes/propernouns.lexc](https://github.com/giellalt/lang-lut/blob/main/src/fst/morphology/affixes/propernouns.lexc)</small>

---

# src-fst-morphology-affixes-symbols.lexc.md 


# Symbol affixes

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/affixes/symbols.lexc](https://github.com/giellalt/lang-lut/blob/main/src/fst/morphology/affixes/symbols.lexc)</small>

---

# src-fst-morphology-affixes-verbs.lexc.md 

Verb inflection
The Lushootseed language verbs inflect in object persons.

bəčdub:bəčd
bəčdub:bəčd

kʷədad:kʷədad

kʷədad:kʷədad

q̓ʷuʔ "gather"
@U.TAM-A.PRF@

ʔəɬəd+V:ʔəɬəd

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/affixes/verbs.lexc](https://github.com/giellalt/lang-lut/blob/main/src/fst/morphology/affixes/verbs.lexc)</small>

---

# src-fst-morphology-phonology.twolc.md 

=================================== !
The Lushootseed morphophonological/twolc rules file !
=================================== !

The Lushootseed language is written in lower case only

This transformation, accent loss, will be moved to post dict. 2022-12-25

c U+0313

Lushootseed is written in IPA, there are no upper-case letters

place holders

* %^Red1i123:0  qəlb: qiqəlb **rain showers**
* %^Red1i13:0  2-segment to 3-segments with vowel change
* %^Red12q13:0 
* %^Red1213:0 
* %^Red1iq13:0  iʔ
* %^Red1iq123:0  iʔ biʔbədəʔs
* %^Red12123:0  papastəd
* %^RedPL1i1i13:0  2-segment to 3-segments with vowel change Plural
* %^Red12323:0  works with Red3 and Red5

* %^RedPL123123:0  3-segment reduplication 

* %^RedPL130130:0  ƛ̕xʷay: ƛ̕xʷaƛ̕xʷay 

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

C ə => C i C   %^Red1i13:
* *%{p5%}%{p4%}%{p3%}%{p2%}%{p1%}ʔəpus%^Red1i13*
* *00ʔi0ʔ0pus0*

C ə => C i C ə
Red 1 qəlb: qiqəlb %^Red1i123
* *%{p5%}%{p4%}%{p3%}%{p2%}%{p1%}qəlb%^Red1i123*
* *00qi0qəlb0*

**a:0 in inflection**

**ə:0 in inflection**
* *x̌əd»əd%>sid*
* *x̌əd000%>cid*
* *bəq̓əd^Pen^RmVOW^d2t>əb*
* *bəq̓0t000>əb*

sčətxʷəd+N+Der/Dimin+N+Pl __bear/karhu__
* *s%^√%{p5%}%{p4%}%{p3%}%{p2%}%{p1%}čətxʷəd%^RedPL1i1i13*
* *s%^√čiči0č0txʷəd0*

**i:0 in inflection**

**í:0 in inflection**

**ʔ:0 in preceding s**
ʔəɬəd+V+Prf+Der+Der/N+N+Sg+PxSg2: __eat/syödä__
* *ad<s<ʔu<ʔəɬəd*
* *ad<s<0u<ʔəɬəd*

**u:0 in preceding ƛ̕**

**%{pØ%}:a in reduplication**

**%{p2%}:ə in reduplication**
* *%{p5%}%{p4%}%{p3%}%{p2%}%{p1%}bəlups%^RedPL123123*
* *00bəlbəlups0*

**%{p2%}:u in reduplication**

**%{p2%}:í in reduplication**

**%{p2%}:i in reduplication**

* *{p5}{p4}{p3}{p2}{p1}x̌aʔx̌aʔ^Red1iq13*
* *00x̌iʔx̌0ʔx̌aʔ0*
qəlb+N+Pl: **rain showers**
* *{p5}{p4}{p3}{p2}{p1}qəlb^Red1i123*
* *00qi0qəlb0*
pišpiš+N+Pl: **cat/kissa**
* *{p5}{p4}{p3}{p2}{p1}pišpiš^RedPL123123*
* *00pišpišpiš0*

**%{p4%}:i in reduplication**

**%{p2%}:a in reduplication**

**%{p2%}:á in reduplication**

**%{pØ%}:0**

**%{p1%}:0**

**%{p2%}:0**

**%{p3%}:0**

**%{p4%}:0**

**%{p5%}:0**

* *ʔu%^√%{p5%}%{p4%}%{p3%}%{p2%}%{p1%}kʷədad%>s*
* *ʔu000000kʷəda0%>c*

**d:0 before s:c**
* *ʔu%^√%{p5%}%{p4%}%{p3%}%{p2%}%{p1%}kʷədad%>cid*
* *ʔu000000kʷəda0%>cid*

**d:t before ə b**
* *bəq̓əd^Pen^RmVOW^d2t>əb*
* *bəq̓0t000>əb*

**%{p1%}:Cx in reduplication**

**%{p3%}:Cx in reduplication**

**%{p5%}:Cx in reduplication**
sčətxʷəd+N+Der/Dimin+N+Pl bear
* *s%^√%{p5%}%{p4%}%{p3%}%{p2%}%{p1%}čətxʷəd%^RedPL1i1i13*
* *s%^√čičič0txʷəd0*

liquids

**%{p1%}:l̕ in reduplication**

**%{p1%}:y̓ in reduplication**

**%{p1%}:w̓ in reduplication**

**%{p1%}:ʔ in reduplication**

x̌aʔx̌aʔ+N+Der+Der/Dimin+N+Sg: **sacred/pyhä**
* *{p5}{p4}{p3}̌{p2}{p1}x̌aʔx̌aʔ^Red1iq123*
* *00x̌iqx̌aʔx̌aʔ0*

**%{p1%}:Cx in reduplication**
* *%{p5%}%{p4%}%{p3%}%{p2%}%{p1%}bəlups%^RedPL123123*
* *00bəlbəlups0*

**%{p1%}:Cx in reduplication**

**%{p1%}:Cx in reduplication**

**Cns:0 in reduplication 3 and 5**

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/phonology.twolc](https://github.com/giellalt/lang-lut/blob/main/src/fst/morphology/phonology.twolc)</small>

---

# src-fst-morphology-root.lexc.md 


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
* @U.NPrefix.sxw@ 
* @U.NPrefix.sexw@ 
* @U.NPrefix.xh@ 
* @R.NPrefix.ZERO@ 
* @R.NPrefix.c@ 
* @R.NPrefix.dexw@ 
* @R.NPrefix.dxw@ 
* @R.NPrefix.dxws@ 
* @R.NPrefix.je@ 
* @R.NPrefix.le@ 
* @R.NPrefix.s@ 
* @R.NPrefix.sxw@ 
* @R.NPrefix.sexw@ 
* @R.NPrefix.xh@ 
* @D.NPrefix@ 
* @C.NPrefix@ 

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

* @N.TAM-A@	  ʔu%<
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

* **LEXICON ENDLEX **

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/root.lexc](https://github.com/giellalt/lang-lut/blob/main/src/fst/morphology/root.lexc)</small>

---

# src-fst-morphology-stems-adjectives.lexc.md 

Adjectives
Adjectives in the Lushootseed language describe things.

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/adjectives.lexc](https://github.com/giellalt/lang-lut/blob/main/src/fst/morphology/stems/adjectives.lexc)</small>

---

# src-fst-morphology-stems-adpositions.lexc.md 

Adpositions
Adpositions in the LUSHOOTSEED language 

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/adpositions.lexc](https://github.com/giellalt/lang-lut/blob/main/src/fst/morphology/stems/adpositions.lexc)</small>

---

# src-fst-morphology-stems-adverbs.lexc.md 

Adverbs
Adverbs in the LUSHOOTSEED language 

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/adverbs.lexc](https://github.com/giellalt/lang-lut/blob/main/src/fst/morphology/stems/adverbs.lexc)</small>

---

# src-fst-morphology-stems-conjunctors.lexc.md 

Conjunctors
Conjunctors in the LUSHOOTSEED language 

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/conjunctors.lexc](https://github.com/giellalt/lang-lut/blob/main/src/fst/morphology/stems/conjunctors.lexc)</small>

---

# src-fst-morphology-stems-interjections.lexc.md 

Interjections
Interjections in the LUSHOOTSEED language 

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/interjections.lexc](https://github.com/giellalt/lang-lut/blob/main/src/fst/morphology/stems/interjections.lexc)</small>

---

# src-fst-morphology-stems-nouns.lexc.md 

Nouns
Nouns in LUSHOOTSEED language are things.

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/nouns.lexc](https://github.com/giellalt/lang-lut/blob/main/src/fst/morphology/stems/nouns.lexc)</small>

---

# src-fst-morphology-stems-nouns_newwords.lexc.md 

This is where new words are added as lexc entries before they are
added to the xml source files.
ɬaləp̓+N:ɬaləp̓ N_with_PL_RED2 "tongue" ;

ADD NOUNS BELOW

pupuhigʷəd # "March/april" ;
pədx̌ʷiwaac# "april/may" ;

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/nouns_newwords.lexc](https://github.com/giellalt/lang-lut/blob/main/src/fst/morphology/stems/nouns_newwords.lexc)</small>

---

# src-fst-morphology-stems-numerals.lexc.md 

Numerals
Numerals in the Lushootseed language are numbers.

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/numerals.lexc](https://github.com/giellalt/lang-lut/blob/main/src/fst/morphology/stems/numerals.lexc)</small>

---

# src-fst-morphology-stems-pronouns.lexc.md 

Pronouns
Pronouns in the Lushootseed language are references to things.

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/pronouns.lexc](https://github.com/giellalt/lang-lut/blob/main/src/fst/morphology/stems/pronouns.lexc)</small>

---

# src-fst-morphology-stems-propernouns.lexc.md 

Proper nouns
Proper nouns in LUSHOOTSEED language 

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/propernouns.lexc](https://github.com/giellalt/lang-lut/blob/main/src/fst/morphology/stems/propernouns.lexc)</small>

---

# src-fst-morphology-stems-verbs.lexc.md 

Verbs
Verbs in the Lushootseed language are actions.

* * *

<small>This (part of) documentation was generated from [src/fst/morphology/stems/verbs.lexc](https://github.com/giellalt/lang-lut/blob/main/src/fst/morphology/stems/verbs.lexc)</small>

---

# src-fst-phonetics-txt2ipa.xfscript.md 



retroflex plosive, voiceless			t`  ʈ	    0288, 648 (` = ASCII 096)
retroflex plosive, voiced			d`	ɖ		0256, 598
labiodental nasal					F 	ɱ		0271, 625
retroflex nasal						n` 	ɳ		0273, 627
palatal nasal						J 	ɲ		0272, 626
velar nasal							N 	ŋ		014B, 331
uvular nasal							N\	ɴ		0274, 628
	
bilabial trill						B\ 	ʙ		0299, 665
uvular trill							R\ 	ʀ		0280, 640
alveolar tap							4	ɾ		027E, 638
retroflex flap						r` 	ɽ		027D, 637
bilabial fricative, voiceless		p\ 	ɸ		0278, 632
bilabial fricative, voiced			B 	β		03B2, 946
dental fricative, voiceless			T 	θ		03B8, 952
dental fricative, voiced				D 	ð		00F0, 240
postalveolar fricative, voiceless	S	ʃ		0283, 643
postalveolar fricative, voiced		Z 	ʒ		0292, 658
retroflex fricative, voiceless		s` 	ʂ		0282, 642
retroflex fricative, voiced			z` 	ʐ		0290, 656
palatal fricative, voiceless			C 	ç		00E7, 231
palatal fricative, voiced			j\ 	ʝ		029D, 669
velar fricative, voiced	        	G 	ɣ		0263, 611
uvular fricative, voiceless			X	χ		03C7, 967
uvular fricative, voiced				R 	ʁ		0281, 641
pharyngeal fricative, voiceless		X\ 	ħ		0127, 295
pharyngeal fricative, voiced			?\ 	ʕ		0295, 661
glottal fricative, voiced			h\	ɦ		0266, 614

alveolar lateral fricative, vl.		K 
alveolar lateral fricative, vd.		K\

labiodental approximant				P (or v\) 
alveolar approximant					r\ 
retroflex approximant				r\` 
velar approximant					M\

retroflex lateral approximant		l` 
palatal lateral approximant			L 
velar lateral approximant			L\
Clicks

bilabial								O\	(O = capital letter) 
dental								|\
(post)alveolar						!\ 
palatoalveolar						=\ 
alveolar lateral						|\|\
Ejectives, implosives

ejective								_>	e.g. ejective p		p_>
implosive							_<	e.g. implosive b	b_<
Vowels

close back unrounded					M
close central unrounded 				1 
close central rounded				} 
lax i								I 
lax y								Y 
lax u								U

close-mid front rounded				2 
close-mid central unrounded			@\ 
close-mid central rounded			8 
close-mid back unrounded				7

schwa	ə							@

open-mid front unrounded				E 
open-mid front rounded				9
open-mid central unrounded			3 
open-mid central rounded				3\ 
open-mid back unrounded				V 
open-mid back rounded				O

ash (ae digraph)						{ 
open schwa (turned a)				6

open front rounded					& 
open back unrounded	        		A 
open back rounded					Q
Other symbols

voiceless labial-velar fricative		W 
voiced labial-palatal approx.		H 
voiceless epiglottal fricative		H\ 
voiced epiglottal fricative			<\ 
epiglottal plosive					>\

alveolo-palatal fricative, vl. 		s\ 
alveolo-palatal fricative, voiced	z\ 
alveolar lateral flap				l\ 
simultaneous S and x					x\ 
tie bar								_
Suprasegmentals

primary stress						" 
secondary stress						% 
long									: 
half-long							:\ 
extra-short							_X 
linking mark							-\
Tones and word accents

level extra high						_T 
level high							_H
level mid							_M 
level low							_L 
level extra low						_B
downstep								! 
upstep								^	(caret, circumflex)

contour, rising						 
contour, falling						_F 
contour, high rising					_H_T 
contour, low rising					_B_L 

contour, rising-falling				_R_F 
(NB Instead of being written as diacritics with _, all prosodic 
marks can alternatively be placed in a separate tier, set off 
by < >, as recommended for the next two symbols.)
global rise						<R> 
global fall						<F>
Diacritics						
									
voiceless						_0	(0 = figure), e.g. n_0
voiced							_v 
aspirated						_h 
more rounded						_O	(O = letter) 
less rounded						_c 
advanced							_+
retracted						_-
centralized						_" 
syllabic							=	(or _=) e.g. n= (or n_=) 
non-syllabic						_^ 
rhoticity						`
									
breathy voiced					_t 
creaky voiced					_k
linguolabial						_N 
labialized						_w 
palatalized						'	(or _j) e.g. t' (or t_j) 
velarized						_G 
pharyngealized					_?\
									
dental							_d 
apical							_a 
laminal							_m
nasalized						~	(or _~) e.g. A~ (or A_~) 
nasal release					_n
lateral release					_l 
no audible release				_}

velarized or pharyngealized		_e 
velarized l, alternatively		5 
raised							_r 
lowered							_o 
advanced tongue root				_A 
retracted tongue root			_q

* * *

<small>This (part of) documentation was generated from [src/fst/phonetics/txt2ipa.xfscript](https://github.com/giellalt/lang-lut/blob/main/src/fst/phonetics/txt2ipa.xfscript)</small>

---

# src-fst-transcriptions-transcriptor-abbrevs2text.lexc.md 



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

<small>This (part of) documentation was generated from [src/fst/transcriptions/transcriptor-abbrevs2text.lexc](https://github.com/giellalt/lang-lut/blob/main/src/fst/transcriptions/transcriptor-abbrevs2text.lexc)</small>

---

# src-fst-transcriptions-transcriptor-numbers-digit2text.lexc.md 



=================
Under the million
=================

Check this

* * *

<small>This (part of) documentation was generated from [src/fst/transcriptions/transcriptor-numbers-digit2text.lexc](https://github.com/giellalt/lang-lut/blob/main/src/fst/transcriptions/transcriptor-numbers-digit2text.lexc)</small>

---

# tools-grammarcheckers-grammarchecker.cg3.md 


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

<small>This (part of) documentation was generated from [tools/grammarcheckers/grammarchecker.cg3](https://github.com/giellalt/lang-lut/blob/main/tools/grammarcheckers/grammarchecker.cg3)</small>

---

# tools-tokenisers-tokeniser-disamb-gt-desc.pmscript.md 

# Tokeniser for lut

Usage:
```
$ make
$ echo "ja, ja" | hfst-tokenise --giella-cg tokeniser-disamb-gt-desc.pmhfst
$ echo "Juos gorreválggain lea (dárbbašlaš) deavdit gáibádusa boasttu olmmoš, man mielde lahtuid." | hfst-tokenise --giella-cg tokeniser-disamb-gt-desc.pmhfst
$ echo "(gáfe) 'ja' ja 3. ja? ц jaja ukjend \"ukjend\"" | hfst-tokenise --giella-cg tokeniser-disamb-gt-desc.pmhfst
$ echo "márffibiillagáffe" | hfst-tokenise --giella-cg tokeniser-disamb-gt-desc.pmhfst
```

Pmatch documentation:
<https://github.com/hfst/hfst/wiki/HfstPmatch>

Characters which have analyses in the lexicon, but can appear without spaces
before/after, that is, with no context conditions, and adjacent to words:
* Punct contains ASCII punctuation marks
* The symbol after m-dash is soft-hyphen `U+00AD`
* The symbol following {•} is byte-order-mark / zero-width no-break space
`U+FEFF`.

Whitespace contains ASCII white space and
the List contains some unicode white space characters
* En Quad U+2000 to Zero-Width Joiner U+200d'
* Narrow No-Break Space U+202F
* Medium Mathematical Space U+205F
* Word joiner U+2060

Apart from what's in our morphology, there are
1. unknown word-like forms, and
2. unmatched strings
We want to give 1) a match, but let 2) be treated specially by
`hfst-tokenise -a`
Unknowns are made of:
* lower-case ASCII
* upper-case ASCII
* select extended latin symbols
* lut specific symbols
ASCII digits
* select symbols
* Combining diacritics as individual symbols,
* various symbols from Private area (probably Microsoft),
so far:
* U+F0B7 for "x in box"

## Unknown handling
Unknowns are tagged ?? and treated specially with `hfst-tokenise`
hfst-tokenise --giella-cg will treat such empty analyses as unknowns, and
remove empty analyses from other readings. Empty readings are also
legal in CG, they get a default baseform equal to the wordform, but
no tag to check, so it's safer to let hfst-tokenise handle them.

Finally we mark as a token any sequence making up a:
* known word in context
* unknown (OOV) token in context
* sequence of word and punctuation
* URL in context

* * *

<small>This (part of) documentation was generated from [tools/tokenisers/tokeniser-disamb-gt-desc.pmscript](https://github.com/giellalt/lang-lut/blob/main/tools/tokenisers/tokeniser-disamb-gt-desc.pmscript)</small>

---

# tools-tokenisers-tokeniser-gramcheck-gt-desc.pmscript.md 

# Grammar checker tokenisation for lut

Requires a recent version of HFST (3.10.0 / git revision>=3aecdbc)
Then just:
```
$ make
$ echo "ja, ja" | hfst-tokenise --giella-cg tokeniser-disamb-gt-desc.pmhfst
```

More usage examples:
```
$ echo "Juos gorreválggain lea (dárbbašlaš) deavdit gáibádusa boasttu olmmoš, man mielde lahtuid." | hfst-tokenise --giella-cg tokeniser-disamb-gt-desc.pmhfst
$ echo "(gáfe) 'ja' ja 3. ja? ц jaja ukjend \"ukjend\"" | hfst-tokenise --giella-cg tokeniser-disamb-gt-desc.pmhfst
$ echo "márffibiillagáffe" | hfst-tokenise --giella-cg tokeniser-disamb-gt-desc.pmhfst
```

Pmatch documentation:
<https://github.com/hfst/hfst/wiki/HfstPmatch>

Characters which have analyses in the lexicon, but can appear without spaces
before/after, that is, with no context conditions, and adjacent to words:
* Punct contains ASCII punctuation marks
* The symbol after m-dash is soft-hyphen `U+00AD`
* The symbol following {•} is byte-order-mark / zero-width no-break space
`U+FEFF`.

Whitespace contains ASCII white space and
the List contains some unicode white space characters
* En Quad U+2000 to Zero-Width Joiner U+200d'
* Narrow No-Break Space U+202F
* Medium Mathematical Space U+205F
* Word joiner U+2060

Apart from what's in our morphology, there are
1) unknown word-like forms, and
2) unmatched strings
We want to give 1) a match, but let 2) be treated specially by hfst-tokenise -a
* select extended latin symbols
* select symbols
* various symbols from Private area (probably Microsoft),
so far:
* U+F0B7 for "x in box"

TODO: Could use something like this, but built-in's don't include šžđčŋ:

Simply give an empty reading when something is unknown:
hfst-tokenise --giella-cg will treat such empty analyses as unknowns, and
remove empty analyses from other readings. Empty readings are also
legal in CG, they get a default baseform equal to the wordform, but
no tag to check, so it's safer to let hfst-tokenise handle them.

Finally we mark as a token any sequence making up a:
* known word in context
* unknown (OOV) token in context
* sequence of word and punctuation
* URL in context

* * *

<small>This (part of) documentation was generated from [tools/tokenisers/tokeniser-gramcheck-gt-desc.pmscript](https://github.com/giellalt/lang-lut/blob/main/tools/tokenisers/tokeniser-gramcheck-gt-desc.pmscript)</small>

---

# tools-tokenisers-tokeniser-tts-cggt-desc.pmscript.md 

# TTS tokenisation for smj

Requires a recent version of HFST (3.10.0 / git revision>=3aecdbc)
Then just:
```sh
make
echo "ja, ja" \
| hfst-tokenise --giella-cg tokeniser-disamb-gt-desc.pmhfst
```

More usage examples:
```sh
echo "Juos gorreválggain lea (dárbbašlaš) deavdit gáibádusa \
boasttu olmmoš, man mielde lahtuid." \
| hfst-tokenise --giella-cg tokeniser-disamb-gt-desc.pmhfst
echo "(gáfe) 'ja' ja 3. ja? ц jaja ukjend \"ukjend\"" \
| hfst-tokenise --giella-cg tokeniser-disamb-gt-desc.pmhfst
echo "márffibiillagáffe" \
| hfst-tokenise --giella-cg tokeniser-disamb-gt-desc.pmhfst
```

Pmatch documentation:
<https://kitwiki.csc.fi/twiki/bin/view/KitWiki/HfstPmatch>

Characters which have analyses in the lexicon, but can appear without spaces
before/after, that is, with no context conditions, and adjacent to words:
* Punct contains ASCII punctuation marks
* The symbol after m-dash is soft-hyphen `U+00AD`
* The symbol following {•} is byte-order-mark / zero-width no-break space
`U+FEFF`.

Whitespace contains ASCII white space and
the List contains some unicode white space characters
* En Quad U+2000 to Zero-Width Joiner U+200d'
* Narrow No-Break Space U+202F
* Medium Mathematical Space U+205F
* Word joiner U+2060

Apart from what's in our morphology, there are
1) unknown word-like forms, and
2) unmatched strings
We want to give 1) a match, but let 2) be treated specially by hfst-tokenise -a
* select extended latin symbols
* select symbols
* various symbols from Private area (probably Microsoft),
so far:
* U+F0B7 for "x in box"

TODO: Could use something like this, but built-in's don't include šžđčŋ:

Simply give an empty reading when something is unknown:
hfst-tokenise --giella-cg will treat such empty analyses as unknowns, and
remove empty analyses from other readings. Empty readings are also
legal in CG, they get a default baseform equal to the wordform, but
no tag to check, so it's safer to let hfst-tokenise handle them.

Needs hfst-tokenise to output things differently depending on the tag they get

* * *

<small>This (part of) documentation was generated from [tools/tokenisers/tokeniser-tts-cggt-desc.pmscript](https://github.com/giellalt/lang-lut/blob/main/tools/tokenisers/tokeniser-tts-cggt-desc.pmscript)</small>
