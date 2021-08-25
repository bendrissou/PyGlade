SUBJECT = target
CLASSPATH = ~/.m2/repository/org/json/json/20160810/json-20160810.jar:EarleyParser/target/classes

eval:
	echo "Evaluation of" $(SUBJECT)
	cd ../samples/handwritten && if [ -d $(SUBJECT) ]; then sudo rm -Rf $(SUBJECT); fi && mkdir $(SUBJECT)
	cd ../samples/synthesized && if [ -d $(SUBJECT) ]; then sudo rm -Rf $(SUBJECT); fi && mkdir $(SUBJECT)
	python3 sample_f.py $(SUBJECT)
	echo "Finished sampling."
	python3 eval_precision.py $(SUBJECT)
	cd ../EarleyJava && java -cp $(CLASSPATH) parser.App $(SUBJECT) 1 &
	cd ../EarleyJava && java -cp $(CLASSPATH) parser.App $(SUBJECT) 2 &
	cd ../EarleyJava && java -cp $(CLASSPATH) parser.App $(SUBJECT) 3 &
	cd ../EarleyJava && java -cp $(CLASSPATH) parser.App $(SUBJECT) 4 &
	cd ../EarleyJava && java -cp $(CLASSPATH) parser.App $(SUBJECT) 5 &
	cd ../EarleyJava && java -cp $(CLASSPATH) parser.App $(SUBJECT) 6 &
	cd ../EarleyJava && java -cp $(CLASSPATH) parser.App $(SUBJECT) 7 &
	cd ../EarleyJava && java -cp $(CLASSPATH) parser.App $(SUBJECT) 8 &
	cd ../EarleyJava && java -cp $(CLASSPATH) parser.App $(SUBJECT) 9 &
	cd ../EarleyJava && java -cp $(CLASSPATH) parser.App $(SUBJECT) 10
	echo "Finished eval for" $(SUBJECT)

eval-antlr:
	echo "Evaluation of" $(SUBJECT)
	#cd ../samples/handwritten && if [ -d $(SUBJECT) ]; then sudo rm -Rf $(SUBJECT); fi && mkdir $(SUBJECT)
	cd ../samples/synthesized && if [ -d $(SUBJECT) ]; then sudo rm -Rf $(SUBJECT); fi && mkdir $(SUBJECT)
	python3 sample_f.py $(SUBJECT)
	echo "Finished sampling."
	python3 eval_precision.py $(SUBJECT)
	cd ../EarleyJava && java -cp $(CLASSPATH) parser.App $(SUBJECT) 1 &
	cd ../EarleyJava && java -cp $(CLASSPATH) parser.App $(SUBJECT) 2 &
	cd ../EarleyJava && java -cp $(CLASSPATH) parser.App $(SUBJECT) 3 &
	cd ../EarleyJava && java -cp $(CLASSPATH) parser.App $(SUBJECT) 4 &
	cd ../EarleyJava && java -cp $(CLASSPATH) parser.App $(SUBJECT) 5 &
	cd ../EarleyJava && java -cp $(CLASSPATH) parser.App $(SUBJECT) 6 &
	cd ../EarleyJava && java -cp $(CLASSPATH) parser.App $(SUBJECT) 7 &
	cd ../EarleyJava && java -cp $(CLASSPATH) parser.App $(SUBJECT) 8 &
	cd ../EarleyJava && java -cp $(CLASSPATH) parser.App $(SUBJECT) 9 &
	cd ../EarleyJava && java -cp $(CLASSPATH) parser.App $(SUBJECT) 10
	echo "Finished eval for" $(SUBJECT)

eval-antlr-precision:
	echo "Evaluation of" $(SUBJECT)
	#cd ../samples/handwritten && if [ -d $(SUBJECT) ]; then sudo rm -Rf $(SUBJECT); fi && mkdir $(SUBJECT)
	cd ../samples/synthesized && if [ -d $(SUBJECT) ]; then sudo rm -Rf $(SUBJECT); fi && mkdir $(SUBJECT)
	python3 sample_f.py $(SUBJECT)
	echo "Finished sampling."
	python3 eval_precision.py $(SUBJECT)
	echo "Finished eval for" $(SUBJECT)

compile:
	echo "Compiling EarleyJava"
	cd ../EarleyJava && make compile
