all: compile
	$(MAKE) javaparser

compile:
	cd EarleyParser; mvn clean compile

myfile=EarleyParser/myfile.json
#grammar=EarleyParser/jsongrammar_ascii.json
grammar=EarleyParser/grep-java.json
#grammar=EarleyParser/grammar.json
#grammar=EarleyParser/expr.json
debug=-m pudb
pythonparser:
	python3 src/Parser.py $(grammar) $(myfile)

cp=~/.m2/repository/org/json/json/20160810/json-20160810.jar:EarleyParser/target/classes

# needs atleast this much to parse the full json tarball
javaopts=-Xmx8192m

javaparser:
	java -cp $(cp) parser.App $(grammar) $(myfile)
