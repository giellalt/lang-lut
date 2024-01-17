## Process this file with automake to produce Makefile.in
## Copyright: Sámediggi/Divvun/UiT
## Licence: GPL v3+

SUBDIRS = fst cg3

#################################################
#### Add language-specific build rules here: ####

# We need to add processing of language-specific tags in the analyser:
analyser-gt-desc.%: analyser-gt-desc.tmp.% \
					filters/remove-letter-acute.%              \
					filters/remove-letter-grave.%
	$(AM_V_XFST_TOOL)$(PRINTF) "read regex \
			 @\"$<\"                                         \
			.o. @\"filters/remove-letter-acute.$*\" \
			.o. @\"filters/remove-letter-grave.$*\" \
			;\n\
		 $(INVERT_HFST)\
		 save stack $@\n\
		 quit\n" | $(XFST_TOOL)

# And also for the normative analyser (foma and hfst):
analyser-gt-norm.%: analyser-gt-norm.tmp.% \
					filters/remove-illegal-derivation-strings-flagbased.% \
					filters/insert-default-compounding-tags.% \
					filters/insert-default_left_compounding-tags.% \
					filters/block-illegal_compound-strings.%  \
					filters/split-CmpN-tags.% \
					filters/convert_to_flags-CmpNP-tags.% \
					filters/split-CmpNP-tags.% \
					filters/remove-letter-acute.%              \
					filters/remove-letter-grave.%
	$(AM_V_XFST_TOOL)$(PRINTF) "read regex \
				@\"filters/block-illegal_compound-strings.$*\"          \
			.o. @\"filters/split-CmpN-tags.$*\"                         \
			.o. @\"filters/insert-default_left_compounding-tags.$*\"    \
			.o. @\"filters/insert-default-compounding-tags.$*\"         \
			.o. @\"filters/remove-illegal-derivation-strings-flagbased.$*\" \
			.o. @\"filters/convert_to_flags-CmpNP-tags.$*\"            \
			.o. @\"filters/split-CmpNP-tags.$*\"                       \
			.o. @\"$<\"                                                \
			.o. @\"filters/remove-letter-acute.$*\"                \
			.o. @\"filters/remove-letter-grave.$*\"                \
			;\n\
		 twosided flag-diacritics\n\
		 $(INVERT_HFST)\
		 save stack $@\n\
		 quit\n" | $(XFST_TOOL)

# The operation 'twosided flag-diacritics" crashes Xerox badly, so we do with
# a simpler, less restrictive normative fst when building with Xerox:
analyser-gt-norm.xfst: analyser-gt-norm.tmp.xfst \
					filters/remove-illegal-derivation-strings.xfst    \
					filters/remove-letter-acute.xfst              \
					filters/remove-letter-grave.xfst
	$(AM_V_XFST)$(PRINTF) "read regex \
			 @\"filters/remove-illegal-derivation-strings.xfst\"    \
			.o. @\"$<\"                                                \
			.o. @\"filters/remove-letter-acute.xfst\"              \
			.o. @\"filters/remove-letter-grave.xfst\"              \
			;\n\
		 save stack $@\n\
		 quit\n" | $(XFST) $(VERBOSITY)


# We need special treatment of the disamb fst going to further pmatch processing
# mainly due to the target pattern, thus listed here. The rule body and the
# dependencies should be the same as the regular disamb analysers below:
analyser-pmatchdisamb-gt-desc.hfst: analyser-pmatchdisamb-gt-desc.tmp.hfst \
				filters/remove-orig_lang-tags.hfst             \
				filters/remove-letter-acute.hfst  \
				filters/remove-letter-grave.hfst  
	$(AM_V_HXFST)$(PRINTF) "read regex \
		 @\"filters/remove-orig_lang-tags.hfst\"           \
		.o. @\"$<\"                                           \
		.o. @\"filters/remove-letter-acute.hfst\"              \
		.o. @\"filters/remove-letter-grave.hfst\"              \
		;\n\
	invert net\n\
	save stack $@\n\
	quit\n" | $(HFST_XFST) -p $(MORE_VERBOSITY)


# Special case for the disamb analyser, since it follows the same filename
# pattern as the raw fst:
analyser-disamb-gt-desc.%: analyser-disamb-gt-desc.tmp.%           \
					filters/remove-orig_lang-tags.%                \
					filters/remove-dialect-tags.%                  \
					filters/remove-homonymy-tags.%                 \
					filters/remove-letter-acute.%              \
					filters/remove-letter-grave.%              
	$(AM_V_XFST_TOOL)$(PRINTF) "read regex \
			 @\"filters/remove-orig_lang-tags.$*\"                \
			.o. @\"filters/remove-dialect-tags.$*\"                  \
			.o. @\"filters/remove-homonymy-tags.$*\"                 \
			.o. @\"$<\"                                              \
			.o. @\"filters/remove-letter-acute.$*\"              \
			.o. @\"filters/remove-letter-grave.$*\"              \
			;\n\
		 $(INVERT_HFST)\
		 save stack $@\n\
		 quit\n" | $(XFST_TOOL)

# We need to add processing of language-specific tags in the generator:
define giella_generators
generator-gt-%.$(1): generator-gt-%.tmp.$(1) \
					 filters/remove-letter-acute.$(1)              \
					 filters/remove-letter-grave.$(1)
	$$(AM_V_XFST_TOOL)$$(PRINTF) "read regex \
			 @\"$$<\"                                               \
			.o. @\"filters/remove-letter-acute.$(1)\"              \
			.o. @\"filters/remove-letter-grave.$(1)\"              \
			;\n\
		 $$(INVERT_XFST)$$(INVERT_FOMA)\
		 save stack $$@\n\
		 quit\n" | $$(XFST_TOOL)
endef
$(foreach fst,hfst xfst foma,$(eval $(call giella_generators,$(fst))))

# Do NOT apply the accent removal filters to the normative
# dictionary generator:
generator-dict-gt-norm.%: generator-dict-gt-norm.tmp.% 
	$(AM_V_XFST_TOOL)$(PRINTF) "read regex \
			 @\"$<\"                                         \
			;\n\
		 $(INVERT_XFST)$(INVERT_FOMA)\
		 save stack $@\n\
		 quit\n" | $(XFST_TOOL)


### Split multichar letters early, to avoid repetitive code. Multichar ###
### letters must be split on both sides, and then the alphabet pruned, ###
### for hfst-tokenise to work without issues.                          ###
generator-raw-gt-desc.hfst: generator-raw-gt-desc.tmp.hfst \
					orthography/split-composed-chars.compose.hfst
	$(AM_V_XFST_TOOL)$(PRINTF) "read regex            \
				@\"orthography/split-composed-chars.compose.hfst\".i \
			.o. @\"$<\"                               \
			.o. @\"orthography/split-composed-chars.compose.hfst\" \
			;\n\
		 save stack $@.tmp\n\
		 quit\n" | $(XFST_TOOL)
		 $(AM_V_HPRUNE)$(HFST_PRUNE_ALPHABET) -i $@.tmp -o $@
		 $(AM_V_at)rm -f $@.tmp

# Xfst and Foma version:
analyser-raw-gt-desc.%: analyser-raw-gt-desc.tmp.% \
					orthography/split-composed-chars.compose.%
	$(AM_V_XFST_TOOL)$(PRINTF) "read regex            \
				@\"orthography/split-composed-chars.compose.$*\".i \
			.o. @\"$<\"                               \
			.o. @\"orthography/split-composed-chars.compose.$*\" \
			;\n\
		 save stack $@\n\
		 quit\n" | $(XFST_TOOL)

##################################################################
#### END: Add local processing instructions ABOVE this line ######
##################################################################

include $(top_srcdir)/../giella-core/am-shared/src-dir-include.am
