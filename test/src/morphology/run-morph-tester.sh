#!/bin/bash
# test/src/morphology/run-morph-tester.sh.  Generated from run-morph-tester.sh.in by configure.

# This is a shell script that will take one test file
# and run it through the Apertium Quality morph-test.py tool, using Xerox
# or Hfst transducers to the extent found.
#
# It takes three arguments: the transducer type, the file to be tested
#                           and the text to precede each output line, e.g.
#                           test run number.
#
# The script is typically sourced by another shell script listed in the TESTS
# variable in the Makefile.am file. This other shell script identifies the fst
# and the test file to be used.
#
# This file must be processed by ./configure before being used.

# Wrong usage - short instruction:
if ! test $# -ge 2 ; then
    echo
    echo "Usage: $0 TRANSDUCERTYPE TESTFILE HALFTEST LEADTEXT"
    echo
    echo "were TRANSDUCERTYPE is the type of transducer targeted for testing,"
    echo "gt-norm, gt-desc, etc., and the optional TESTFILE is either a LexC"
    echo "file or a Yaml test data file, both containing test data."
    echo "HALFTEST is a string with one of the values 'ana', 'gen' or 'full',"
    echo "indicating that only the analyser, only the generator, or both are"
    echo "tested, respectively."
    echo "LEADTEXT is typically the number of the test in a test set loop."
    echo "LEADTEXT can contain spaces, it is effectively everything after the"
    echo "second argument."
    echo
    exit 77
fi

###### Variables: #######
transducer=$1
testfile=$2
halftest=$3
shift 3
leadtext="$@"

testfileshort=$(echo "$(basename \
	$(dirname $testfile))/$(basename $testfile)")

analyserfile=./../../../src/analyser-$transducer
generatorfile=./../../../src/generator-$transducer
pythonbin=/opt/local/bin/python3.2
runtests="$pythonbin /Users/rueter/main/gtcore/scripts/morph-test.py"

# Use autotools mechanisms to only run the configured fst types in the tests:
fsttype=
fsttype="$fsttype hfst"
fsttype="$fsttype xfst"

# Exit if both hfst and xerox have been shut off:
if [[ "$fsttype" == "" ]]; then
    echo "All transducer types have been shut off at configure time."
    echo "Nothing to test. SKIPPED."
    exit 77
fi

# Construct the correct argument for running either analysis, generation or both tests
if test "$halftest" == "ana"; then
    halftestoption="--surface"
elif test "$halftest" == "gen"; then
    halftestoption="--lexical"
else
    halftestoption=""
fi

function run_tests() {
	$runtests \
		--colour \
		--terse \
		--ignore-extra-analyses \
		--section $section \
	    --app $lookuptool \
	    --gen $generatorfile.$f \
	    --morph $analyserfile.$f \
	    $halftestoption \
	    $testfile
	# If the test failed, print instructions to rerun and get more details:
	if [[ $? -gt 0 ]]; then
	    let "Fail += 1"
	    echo "To rerun with more details, please triple-click, copy and paste the following:"
	    echo
	    echo "pushd $(pwd); $runtests -c -i -S $section --app $lookuptool --gen $generatorfile.$f --morph $analyserfile.$f $halftestoption $testfile; popd"
	    echo
	fi
}

###### Start testing: #######
transducer_found=0

# Loop over the transducer types first - we test both hfst and xfst if found:
for f in $fsttype; do
	if test $f == "xfst"; then
		lookuptool="/Users/rueter/bin/lookup"
		section="xerox"
	elif test $f == "hfst"; then
		lookuptool="/usr/local/bin/hfst-lookup"
		section="hfst"
	else
	    let "Fail += 1"
		echo "FAIL: Unknown fst type! FST=$f"
	    continue
	fi
	# Check whether the actual fst's exist, run the tests if true, FAIL if not:
	if test -f "$generatorfile.$f" -a -f "$analyserfile.$f"; then
		let "transducer_found += 1"
		printf "$leadtext $testfileshort + $(basename $analyserfile.$f) - "
		run_tests
	else
	    let "Fail += 1"
		echo "FAIL: Transducer not found! $(basename $analyserfile.$f)"
		echo "referenced by: $testfileshort"
	    continue
	fi
done
