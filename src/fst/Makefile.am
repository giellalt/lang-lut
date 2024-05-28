## Process this file with automake to produce Makefile.in
## Copyright: Sámediggi/Divvun/UiT
## Licence: GPL v3+

# always build . last here, and tagsets have to be built after morphology
SUBDIRS = morphology filters phonetics syllabification orthography transcriptions tagsets . test

####### Automake targets: ########

# Define target variables first, before assigning to them:
GT_ANALYSERS=
GT_GENERATORS=
CUSTOM_FSTS=

#### Local modifications in *fst processing: ####
####
#### Copy the fallback targets, and rename them to the desired targets. Then:
#### Replace the 'cp' command (Xerox) / Prepend the hfst-invert command (Hfst -
#### remember to move the $<) with whatever you need to complete
#### the processing to get the final target transducer.
#### Remember to add the dependencies as well.
#### Also make sure that HFST and Xerox processing are the same.
####
#### If you add new transducers to be built, you need to add them to the
#### relevant variable, e.g.:
####
#### if CAN_HFST
#### GT_GENERATORS+=generator-oahpa-gt-norm.hfst
#### endif
####
#### NB!!!! The HFST targets should get a hyphen after 'analyser'/'generator'
#### respectively, to make the local targets minimally different from and
#### slightly more specific than the fallback targets. This is to avoid warnings
#### about duplicate targets. That is, the local targets should looke like:
####
#### analyser-%.hfst: analyser-%.tmp.hfst
#### generator-%.hfst: generator-%.tmp.hfst

##################################################################
#### BEGIN: Add local processing instructions BELOW this line ####
##################################################################

########################################################
#### Add language-specific transducer targets here: ####


.generated/analyser-gt-desc.%: .generated/analyser-gt-desc.tmp.% \
										filters/remove-letter-acute.%			   \
										filters/remove-letter-grave.%
		$(AM_V_XFST_TOOL)$(PRINTF) "read regex \
						 @\"$<\"										 \
						.o. @\"filters/remove-letter-acute.$*\" \
						.o. @\"filters/remove-letter-grave.$*\" \
						;\n\
				 $(INVERT_HFST)\
				 save stack $@\n\
				 quit\n" | $(XFST_TOOL)

# And also for the normative analyser (foma and hfst):
.generated/analyser-gt-norm.%: .generated/analyser-gt-norm.tmp.% \
										filters/remove-illegal-derivation-strings-flagbased.% \
										filters/insert-default-compounding-tags.% \
										filters/insert-default_left_compounding-tags.% \
										filters/block-illegal_compound-strings.%  \
										filters/split-CmpN-tags.% \
										filters/convert_to_flags-CmpNP-tags.% \
										filters/split-CmpNP-tags.% \
										filters/remove-letter-acute.%			   \
										filters/remove-letter-grave.%
		$(AM_V_XFST_TOOL)$(PRINTF) "read regex \
								@\"filters/block-illegal_compound-strings.$*\"			\
						.o. @\"filters/split-CmpN-tags.$*\"							\
						.o. @\"filters/insert-default_left_compounding-tags.$*\"	\
						.o. @\"filters/insert-default-compounding-tags.$*\"			\
						.o. @\"filters/remove-illegal-derivation-strings-flagbased.$*\" \
						.o. @\"filters/convert_to_flags-CmpNP-tags.$*\"			   \
						.o. @\"filters/split-CmpNP-tags.$*\"					   \
						.o. @\"$<\"												   \
						.o. @\"filters/remove-letter-acute.$*\"				   \
						.o. @\"filters/remove-letter-grave.$*\"				   \
						;\n\
				 twosided flag-diacritics\n\
				 $(INVERT_HFST)\
				 save stack $@\n\
				 quit\n" | $(XFST_TOOL)

# The operation 'twosided flag-diacritics" crashes Xerox badly, so we do with
# a simpler, less restrictive normative fst when building with Xerox:
.generated/analyser-gt-norm.xfst: .generated/analyser-gt-norm.tmp.xfst \
										filters/remove-illegal-derivation-strings.xfst	  \
										filters/remove-letter-acute.xfst			  \
										filters/remove-letter-grave.xfst
		$(AM_V_XFST)$(PRINTF) "read regex \
						 @\"filters/remove-illegal-derivation-strings.xfst\"	\
						.o. @\"$<\"												   \
						.o. @\"filters/remove-letter-acute.xfst\"			   \
						.o. @\"filters/remove-letter-grave.xfst\"			   \
						;\n\
				 save stack $@\n\
				 quit\n" | $(XFST) $(VERBOSITY)


# We need special treatment of the disamb fst going to further pmatch processing
# mainly due to the target pattern, thus listed here. The rule body and the
# dependencies should be the same as the regular disamb analysers below:
.generated/analyser-pmatchdisamb-gt-desc.hfst: .generated/analyser-pmatchdisamb-gt-desc.tmp.hfst \
								filters/remove-orig_lang-tags.hfst			   \
								filters/remove-letter-acute.hfst  \
								filters/remove-letter-grave.hfst
		$(AM_V_HXFST)$(PRINTF) "read regex \
				 @\"filters/remove-orig_lang-tags.hfst\"		   \
				.o. @\"$<\"											  \
				.o. @\"filters/remove-letter-acute.hfst\"			   \
				.o. @\"filters/remove-letter-grave.hfst\"			   \
				;\n\
		invert net\n\
		save stack $@\n\
		quit\n" | $(HFST_XFST) -p $(MORE_VERBOSITY)


# Special case for the disamb analyser, since it follows the same filename
# pattern as the raw fst:
.generated/analyser-disamb-gt-desc.%: .generated/analyser-disamb-gt-desc.tmp.%			 \
										filters/remove-orig_lang-tags.%				   \
										filters/remove-dialect-tags.%				   \
										filters/remove-homonymy-tags.%				   \
										filters/remove-letter-acute.%			   \
										filters/remove-letter-grave.%
		$(AM_V_XFST_TOOL)$(PRINTF) "read regex \
						 @\"filters/remove-orig_lang-tags.$*\"				  \
						.o. @\"filters/remove-dialect-tags.$*\"					 \
						.o. @\"filters/remove-homonymy-tags.$*\"				 \
						.o. @\"$<\"												 \
						.o. @\"filters/remove-letter-acute.$*\"				 \
						.o. @\"filters/remove-letter-grave.$*\"				 \
						;\n\
				 $(INVERT_HFST)\
				 save stack $@\n\
				 quit\n" | $(XFST_TOOL)

# We need to add processing of language-specific tags in the generator:
define giella_generators
.generated/generator-gt-%.$(1): .generated/generator-gt-%.tmp.$(1) \
										 filters/remove-letter-acute.$(1)			   \
										 filters/remove-letter-grave.$(1)
		$$(AM_V_XFST_TOOL)$$(PRINTF) "read regex \
						 @\"$$<\"												\
						.o. @\"filters/remove-letter-acute.$(1)\"			   \
						.o. @\"filters/remove-letter-grave.$(1)\"			   \
						;\n\
				 $$(INVERT_XFST)$$(INVERT_FOMA)\
				 save stack $$@\n\
				 quit\n" | $$(XFST_TOOL)
endef
$(foreach fst,hfst xfst foma,$(eval $(call giella_generators,$(fst))))

# Do NOT apply the accent removal filters to the normative
# dictionary generator:
.generated/generator-dict-gt-norm.%: .generated/generator-dict-gt-norm.tmp.%
		$(AM_V_XFST_TOOL)$(PRINTF) "read regex \
						 @\"$<\"										 \
						;\n\
				 $(INVERT_XFST)$(INVERT_FOMA)\
				 save stack $@\n\
				 quit\n" | $(XFST_TOOL)


### Split multichar letters early, to avoid repetitive code. Multichar ###
### letters must be split on both sides, and then the alphabet pruned, ###
### for hfst-tokenise to work without issues.						   ###
.generated/generator-raw-gt-desc.hfst: .generated/generator-raw-gt-desc.tmp.hfst \
										orthography/split-composed-chars.compose.hfst
		$(AM_V_XFST_TOOL)$(PRINTF) "read regex			  \
								@\"orthography/split-composed-chars.compose.hfst\".i \
						.o. @\"$<\"								  \
						.o. @\"orthography/split-composed-chars.compose.hfst\" \
						;\n\
				 save stack $@.tmp\n\
				 quit\n" | $(XFST_TOOL)
				 $(AM_V_HPRUNE)$(HFST_PRUNE_ALPHABET) -i $@.tmp -o $@
				 $(AM_V_at)rm -f $@.tmp

# Xfst and Foma version:
.generated/analyser-raw-gt-desc.%: .generated/analyser-raw-gt-desc.tmp.% \
										orthography/split-composed-chars.compose.%
		$(AM_V_XFST_TOOL)$(PRINTF) "read regex			  \
								@\"orthography/split-composed-chars.compose.$*\".i \
						.o. @\"$<\"								  \
						.o. @\"orthography/split-composed-chars.compose.$*\" \
						;\n\
				 save stack $@\n\
				 quit\n" | $(XFST_TOOL)

##################################################################
#### END: Add local processing instructions ABOVE this line ######
##################################################################

include $(top_srcdir)/../giella-core/am-shared/src-fst-dir-include.am
include $(top_srcdir)/../giella-core/am-shared/devtest-include.am
