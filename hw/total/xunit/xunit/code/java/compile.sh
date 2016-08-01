#compile the source file
javac unitTest.java #just change the java file
#compile the ObjScheme file
javac javaschema.java
javac testSchema.java
#generate coverage report(using jacoco)
sh coverage.sh
#get the detail of codestyle
java -jar /usr/share/java/checkstyle-7.0-all.jar -c /google_checks.xml arithTest.java > codestyle #Just change the java file. If more than one, add all to this single command.
