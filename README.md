The Lushootseed (Southern Puget Sound Salish) morphology and tools
==========================================

[![Maturity](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fgiellalt%2Flang-lut%2Fgh-pages%2Fmaturity.json)](https://giellalt.github.io/MaturityClassification.html)
![Lemma count](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fgiellalt%2Flang-lut%2Fgh-pages%2Flemmacount.json)
[![GitHub issues](https://img.shields.io/github/issues-raw/giellalt/lang-lut)](https://github.com/giellalt/lang-lut/issues)
[![License](https://img.shields.io/github/license/giellalt/lang-lut)](https://github.com/giellalt/lang-lut/blob/main/LICENSE)
[![Doc Build Status](https://github.com/giellalt/lang-lut/workflows/Docs/badge.svg)](https://github.com/giellalt/lang-lut/actions)
[![CI/CD Build Status](https://divvun-tc.giellalt.org/api/github/v1/repository/giellalt/lang-lut/main/badge.svg)](https://divvun-tc.giellalt.org/api/github/v1/repository/giellalt/lang-lut/main/latest)

Download nightly / CI/CD installation packages for testing (contains the core zhfst file(s)):

[![Windows](https://img.shields.io/badge/download%40latest-Windows--bhfst-brightgreen)](https://pahkat.uit.no/main/download/speller-lut?platform=windows&channel=nightly)
[![MacOS](https://img.shields.io/badge/download%40latest-macOS--bhfst-brightgreen)](https://pahkat.uit.no/main/download/speller-lut?platform=macos&channel=nightly)
[![Mobile](https://img.shields.io/badge/download%40latest-mobile--bhfst-brightgreen)](https://pahkat.uit.no/main/download/speller-lut?platform=mobile&channel=nightly)

__NB!!__ Note that the nightly / CI/CD installation packages are not tested for language quality, and might contain regressions and errors.

This repository contains finite state source files for the Lushootseed language,
for building morphological analysers, proofing tools
and dictionaries. The data and implementation are licenced under GNU GPL
licence, also detailed in the
[LICENSE](https://github.com/giellalt/lang-lut/blob/main/LICENSE). The
authors named in the AUTHORS file are available to grant other licencing
choices.

Install proofing tools and [keyboards](https://github.com/giellalt/keyboard-lut)
for the Lushootseed language by using the [Divvun Installer](http://divvun.no)
(some languages are only available via the nightly channel).

Download and test speller files
-------------------------------

The speller files downloadable at the top of this page (the `*.bhfst` files) can
be used with [divvunspell](https://github.com/divvun/divvunspell), to test their
performance. These files are the exact same ones as installed on users' computers
and mobile phones. Desktop and mobile speller files differ from each other in the
error model and should be tested separately — thus also two different downloads.

Documentation
-------------

Documentation can be found at:

- [Language specific documentation](https://giellalt.github.io/lang-lut/)
- [General documentation](https://giellalt.github.io/)

Core dependencies
-----------------

In order to compile and use Lushootseed language morphology and
dictionaries, you need:

- an FST compiler: [HFST](https://github.com/hfst/hfst), [Foma](https://github.com/mhulden/foma) or [Xerox Xfst](https://web.stanford.edu/~laurik/fsmbook/home.html)
- [VislCG3](https://visl.sdu.dk/svn/visl/tools/vislcg3/trunk) Constraint Grammar tools

To install VislCG3 and HFST, just copy/paste this into your Terminal on **macOS**:

```
curl https://apertium.projectjj.com/osx/install-nightly.sh | sudo bash
```

or terminal on **Ubuntu, Debian or Windows Subsystem for Linux**:

```
wget https://apertium.projectjj.com/apt/install-nightly.sh -O - | sudo bash
sudo apt-get install cg3 hfst
```

or terminal on **RedHat, Fedora, CentOS or Windows Subsystem for Linux**:

```
wget https://apertium.projectjj.com/rpm/install-nightly.sh -O - | sudo bash
sudo dnf install cg3 hfst
```

Alternatively, the Apertium wiki has good instructions on how to [install the dependencies for Mac
OS X](https://wiki.apertium.org/wiki/Apertium_on_Mac_OS_X) and how to [install
the dependencies on
linux](https://wiki.apertium.org/wiki/Installation_of_grammar_libraries)

Further details and dependencies are described on the GiellaLT [Getting Started](https://giellalt.uit.no/infra/GettingStarted.html) pages.

Downloading
-----------

Using Git:
```
git clone https://github.com/giellalt/lang-lut
```

Using Subversion:
```
svn checkout https://github.com/giellalt/lang-lut.git/trunk lang-lut
```

Building and installation
-------------------------

[INSTALL](https://github.com/giellalt/lang-lut/blob/main/INSTALL)
describes the GNU build system in detail, but for most users it is the usual:

```sh
./autogen.sh # This will automatically clone or check out other GiellaLT dependencies
./configure
make
(as root) make install
```

Citing
------

<!-- Add language specific citation stuff here and to the CITATION.cff -->

> Rueter, J., Hämäläinen, M., & Alnajjar, K. (2023). Modelling the Reduplicating Lushootseed Morphology with an FST and LSTM. In M. Mager, A. Ebrahimi, & A. Oncevay, et al. (Eds.), Proceedings of the Workshop on Natural Language Processing for Indigenous Languages of the Americas (AmericasNLP) (pp. 40-46). The Association for Computational Linguistics. https://doi.org/10.18653/v1/2023.americasnlp-1.6

````bibtex
@inproceedings{f61050ee279c40a18cf138859332d422,
title = "Modelling the Reduplicating Lushootseed Morphology with an FST and LSTM",
abstract = "In this paper, we present an FST based approach for conducting morphological analysis, lemmatization and generation of Lushootseed words. Furthermore, we use the FST to generate training data for an LSTM based neural model and train this model to do morphological analysis. The neural model reaches a 71.9% accuracy on the test data. Furthermore, we discuss reduplication types in the Lushootseed language forms. The approach involves the use of both attested instances of reduplication and bare stems for applying a variety of reduplications to, as it is unclear just how much variation can be attributed to the individual speakers and authors of the source materials. That is, there may be areal factors that can be aligned with certain types of reduplication and their frequencies.",
keywords = "6121 Languages, 113 Computer and information sciences",
author = "Jack Rueter and Mika H{\"a}m{\"a}l{\"a}inen and Khalid Alnajjar",
year = "2023",
month = jul,
doi = "10.18653/v1/2023.americasnlp-1.6",
language = "English",
pages = "40--46",
editor = "Mager, {Manuel } and Ebrahimi, {Abteen } and {Oncevay, et al.}, {Arturo }",
booktitle = "Proceedings of the Workshop on Natural Language Processing for Indigenous Languages of the Americas (AmericasNLP)",
publisher = "The Association for Computational Linguistics",
address = "United States",
note = "Workshop on Natural Language Processing for indigenous Languages of the Americas ; Conference date: 14-06-2023 Through 14-06-2023",
url = "https://turing.iimas.unam.mx/americasnlp/2023_workshop.html",
```


If you use language data from more than one GiellaLT language, consider citing
[our LREC 2022 article on whole
infra](https://aclanthology.org/2022.lrec-1.125/):

> Linda Wiechetek, Katri Hiovain-Asikainen, Inga Lill Sigga Mikkelsen,
  Sjur Moshagen, Flammie Pirinen, Trond Trosterud, and Børre Gaup. 2022.
  *Unmasking the Myth of Effortless Big Data - Making an Open Source
  Multi-lingual Infrastructure and Building Language Resources from Scratch*.
  In Proceedings of the Thirteenth Language Resources and Evaluation Conference,
  pages 1167–1177, Marseille, France. European Language Resources Association.

If you use bibtex, following is as it is on ACL anthology:

```bibtex
@inproceedings{wiechetek-etal-2022-unmasking,
    title = "Unmasking the Myth of Effortless Big Data - Making an Open Source
    Multi-lingual Infrastructure and Building Language Resources from Scratch",
    author = "Wiechetek, Linda  and
      Hiovain-Asikainen, Katri  and
      Mikkelsen, Inga Lill Sigga  and
      Moshagen, Sjur  and
      Pirinen, Flammie  and
      Trosterud, Trond  and
      Gaup, B{\o}rre",
    booktitle = "Proceedings of the Thirteenth Language Resources and Evaluation
    Conference",
    month = jun,
    year = "2022",
    address = "Marseille, France",
    publisher = "European Language Resources Association",
    url = "https://aclanthology.org/2022.lrec-1.125",
    pages = "1167--1177"
}
```
