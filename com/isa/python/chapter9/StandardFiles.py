## File is a general interface like InputStream/OutputStream of Java.
# And there are standard files like: stdin, stdout and stderr located in module sys which must be imported
import sys

sys.stdout.write("Enter a text to be echoed:\n")  # This is also buffered
sys.stderr.write("No errors at start!\n")
text = sys.stdin.readline()  # This is buffered
print text
sys.stderr.write("No errors in the end!")  # stderr is not buffered, it directly outputs. Hence it can output before the buffered standard files
