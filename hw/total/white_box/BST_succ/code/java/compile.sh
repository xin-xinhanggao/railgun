#compile the source file
#javac unitTest.java #just change the java file
#generate coverage report(using jacoco)
sh coverage.sh
#compile the ObjScheme file
#cp coverage/classes/* .
#javac javaschema.java
#javac testSchema.java
#get the detail of codestyle
java -jar /usr/share/java/checkstyle-7.0-all.jar -c /google_checks.xml SucceedTest.java > codestyle #Just change the java file. If more than one, add all to this single command.
