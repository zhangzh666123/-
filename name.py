BufferedWriter out = ;
try {
out = new BufferedWriter(new FileWriter(”filename”, true));
out.write(”aString”);
} catch (IOException e) {
// error processing code
} finally {
if (out != ) {
out.close;
}
}
